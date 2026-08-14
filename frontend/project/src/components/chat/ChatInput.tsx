import { ArrowUp, Square } from 'lucide-react';
import { useRef, useEffect } from 'react';

interface ChatInputProps {
  value: string;
  onChange: (value: string) => void;
  onSubmit: () => void;
  onStop: () => void;
  isGenerating: boolean;
  disabled?: boolean;
}

export function ChatInput({
  value,
  onChange,
  onSubmit,
  onStop,
  isGenerating,
  disabled,
}: ChatInputProps) {
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    const el = textareaRef.current;
    if (!el) return;
    el.style.height = 'auto';
    el.style.height = `${Math.min(el.scrollHeight, 200)}px`;
  }, [value]);

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      if (!isGenerating && value.trim()) onSubmit();
    }
  };

  return (
    <div className="px-4 pb-3 pt-2">
      <div className="mx-auto max-w-3xl">
        <div className="relative flex items-end rounded-2xl border border-border bg-bg-input shadow-lg shadow-black/20 transition-colors focus-within:border-accent/40">
          <textarea
            ref={textareaRef}
            value={value}
            onChange={(e) => onChange(e.target.value)}
            onKeyDown={handleKeyDown}
            disabled={disabled}
            placeholder="Ask Atharva's AI anything..."
            rows={1}
            className="flex-1 resize-none bg-transparent px-4 py-3.5 pr-12 text-[0.95rem] text-gray-100 placeholder:text-gray-500 focus:outline-none scrollbar-thin disabled:opacity-50"
          />
          <div className="absolute bottom-2.5 right-2.5">
            {isGenerating ? (
              <button
                onClick={onStop}
                className="flex h-8 w-8 items-center justify-center rounded-lg bg-bg-hover text-gray-300 transition-colors hover:bg-border-strong hover:text-white"
                aria-label="Stop generating"
              >
                <Square size={14} className="fill-current" />
              </button>
            ) : (
              <button
                onClick={onSubmit}
                disabled={!value.trim() || disabled}
                className="flex h-8 w-8 items-center justify-center rounded-lg bg-accent text-white transition-all hover:bg-accent-hover disabled:cursor-not-allowed disabled:bg-bg-hover disabled:text-gray-600"
                aria-label="Send message"
              >
                <ArrowUp size={16} strokeWidth={2.5} />
              </button>
            )}
          </div>
        </div>
        <p className="mt-2 text-center text-2xs text-gray-600">
          Atharva's AI answers using information from his portfolio.
        </p>
      </div>
    </div>
  );
}

export default ChatInput;
