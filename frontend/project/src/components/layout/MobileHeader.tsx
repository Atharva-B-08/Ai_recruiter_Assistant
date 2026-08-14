import { Menu, Bot, Plus } from 'lucide-react';

interface MobileHeaderProps {
  onOpenSidebar: () => void;
  onNewChat: () => void;
}

export function MobileHeader({ onOpenSidebar, onNewChat }: MobileHeaderProps) {
  return (
    <header className="flex items-center justify-between border-b border-border bg-bg-surface px-3 py-2.5 md:hidden">
      <button
        onClick={onOpenSidebar}
        className="rounded-lg p-2 text-gray-400 transition-colors hover:bg-bg-hover hover:text-gray-200"
        aria-label="Open menu"
      >
        <Menu size={20} />
      </button>
      <div className="flex items-center gap-2">
        <div className="flex h-7 w-7 items-center justify-center rounded-lg bg-accent/15 border border-accent/25">
          <Bot size={16} className="text-accent" />
        </div>
        <span className="text-sm font-semibold text-gray-100">Atharva AI</span>
      </div>
      <button
        onClick={onNewChat}
        className="rounded-lg p-2 text-gray-400 transition-colors hover:bg-bg-hover hover:text-gray-200"
        aria-label="New chat"
      >
        <Plus size={20} />
      </button>
    </header>
  );
}

export default MobileHeader;
