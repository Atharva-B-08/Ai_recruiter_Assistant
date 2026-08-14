import { memo } from 'react';
import { MarkdownRenderer } from './MarkdownRenderer';
import type { ChatMessage } from '@/services/chatApi';

interface ChatMessageItemProps {
  message: ChatMessage;
  isStreaming?: boolean;
}

function ChatMessageItemBase({ message, isStreaming }: ChatMessageItemProps) {
  const isUser = message.role === 'user';

  if (isUser) {
    return (
      <div className="flex justify-end animate-fade-in-up">
        <div className="max-w-[85%] rounded-2xl rounded-br-md bg-accent/10 border border-accent/20 px-4 py-2.5 text-[0.95rem] leading-relaxed text-gray-100 whitespace-pre-wrap">
          {message.content}
        </div>
      </div>
    );
  }

  return (
    <div className="flex gap-3 animate-fade-in-up">
      <div className="mt-0.5 flex h-7 w-7 shrink-0 items-center justify-center rounded-lg bg-accent/15 border border-accent/25">
        <span className="text-xs font-semibold text-accent">AI</span>
      </div>
      <div className="min-w-0 flex-1 pt-0.5">
        {message.error ? (
          <div className="rounded-lg border border-error/30 bg-error/5 px-3 py-2 text-sm text-error">
            {message.content}
          </div>
        ) : (
          <div className="text-[0.95rem] text-gray-200">
            <MarkdownRenderer content={message.content} />
            {isStreaming && (
              <span className="ml-0.5 inline-block h-4 w-1.5 translate-y-0.5 animate-blink bg-accent" />
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export const ChatMessageItem = memo(ChatMessageItemBase);
export default ChatMessageItem;
