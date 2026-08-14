import { useEffect, useRef } from 'react';
import ChatMessageItem from './ChatMessage';
import type { ChatMessage } from '@/services/chatApi';

interface ChatWindowProps {
  messages: ChatMessage[];
  isGenerating: boolean;
}

export function ChatWindow({ messages, isGenerating }: ChatWindowProps) {
  const endRef = useRef<HTMLDivElement>(null);
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const el = endRef.current;
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'end' });
    }
  }, [messages, isGenerating]);

  return (
    <div
      ref={containerRef}
      className="flex-1 overflow-y-auto scrollbar-thin"
    >
      <div className="mx-auto max-w-3xl space-y-6 px-4 py-6">
        {messages.map((msg, idx) => {
          const isLast = idx === messages.length - 1;
          const isStreaming = isGenerating && isLast && msg.role === 'assistant';
          return (
            <ChatMessageItem
              key={idx}
              message={msg}
              isStreaming={isStreaming}
            />
          );
        })}
        <div ref={endRef} className="h-1" />
      </div>
    </div>
  );
}

export default ChatWindow;
