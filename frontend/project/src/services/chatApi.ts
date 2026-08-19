export interface ChatMessage {
  role: 'user' | 'assistant';
  content: string;
  error?: boolean;
}

export interface StreamError {
  type: 'rate_limit' | 'general';
  message: string;
}

export interface StreamCallbacks {
  onConversationId: (id: string) => void;
  onChunk: (content: string) => void;
  onDone: () => void;
  onError: (error: StreamError) => void;
  onThinking?: (content: string) => void;
}

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

function parseSSEStream(
  reader: ReadableStreamDefaultReader<Uint8Array>,
  callbacks: StreamCallbacks,
) {
  const decoder = new TextDecoder();
  let buffer = '';

  const processBuffer = () => {
    const lines = buffer.split('\n');
    // Keep the last (possibly incomplete) line in the buffer
    buffer = lines.pop() ?? '';

    let currentEvent = '';
    for (const line of lines) {
      if (line.startsWith('event:')) {
        currentEvent = line.slice(6).trim();
      } else if (line.startsWith('data:')) {
        const data = line.slice(5).trim();
        if (!data) continue;

        try {
          const parsed = JSON.parse(data);
          switch (currentEvent) {
            case 'conversation':
              if (parsed.conversation_id) {
                callbacks.onConversationId(parsed.conversation_id);
              }
              break;
            case 'thinking':
              if (parsed.content) {
                callbacks.onThinking?.(parsed.content);
              }
              break;
            case 'chunk':
              if (parsed.content) {
                callbacks.onChunk(parsed.content);
              }
              break;
            case 'done':
              callbacks.onDone();
              break;
            case 'error':
              callbacks.onError({
                type: parsed.type ?? 'general',
                message: parsed.message ?? 'An error occurred.',
              });
              break;
          }
        } catch {
          // Non-JSON data line, ignore
        }
        currentEvent = '';
      } else if (line.trim() === '') {
        // Event boundary — reset
        currentEvent = '';
      }
    }
  };

  const read = async (): Promise<void> => {
    const { done, value } = await reader.read();
    if (done) {
      // Process any remaining buffered content
      if (buffer.trim()) {
        processBuffer();
      }
      return;
    }
    buffer += decoder.decode(value, { stream: true });
    processBuffer();
    return read();
  };

  return read();
}

export async function streamChat(
  question: string,
  conversationId: string | null,
  callbacks: StreamCallbacks,
  signal?: AbortSignal,
): Promise<void> {
  const url = `${API_BASE_URL}/chat/stream`;

  const body: Record<string, string> = { question };
  if (conversationId) {
    body.conversation_id = conversationId;
  }

  let response: Response;
  try {
    response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Accept: 'text/event-stream',
      },
      body: JSON.stringify(body),
      signal,
    });
    console.log('Response:', response.status, response);
  } catch (err) {
    if ((err as Error).name === 'AbortError') {
      callbacks.onDone();
      return;
    }
    callbacks.onError({
      type: 'general',
      message:
        'Could not reach the AI service. Please check your connection and try again.',
    });
    return;
  }

  if (!response.ok || !response.body) {
    let message = `Request failed with status ${response.status}.`;
    try {
      const errData = await response.json();
      if (errData?.message) message = errData.message;
    } catch {
      // ignore parse failure
    }
    callbacks.onError({ type: 'general', message });
    return;
  }

  const reader = response.body.getReader();
  try {
    await parseSSEStream(reader, callbacks);
  } catch (err) {
    if ((err as Error).name === 'AbortError') {
      callbacks.onDone();
      return;
    }
    callbacks.onError({
      type: 'general',
      message: 'The connection was interrupted. Please try again.',
    });
  }
}

export default { streamChat };
