import {
  User,
  Zap,
  FolderGit2,
  GraduationCap,
  Trophy,
  ScrollText,
  Github,
  Linkedin,
  Mail,
  FileText,
  Plus,
  PanelLeftClose,
  PanelLeftOpen,
  Bot,
  MessageSquare,
} from 'lucide-react';
import { profile } from '@/data/profile';

export type ViewKey =
  | 'chat'
  | 'about'
  | 'skills'
  | 'projects'
  | 'education'
  | 'achievements'
  | 'certifications';

interface SidebarProps {
  activeView: ViewKey;
  onViewChange: (view: ViewKey) => void;
  onNewChat: () => void;
  collapsed: boolean;
  onToggleCollapse: () => void;
  mobileOpen: boolean;
  onCloseMobile: () => void;
}

const portfolioNav: { key: ViewKey; label: string; icon: typeof User }[] = [
  { key: 'about', label: 'About Me', icon: User },
  { key: 'skills', label: 'Skills', icon: Zap },
  { key: 'projects', label: 'Projects', icon: FolderGit2 },
  { key: 'education', label: 'Education', icon: GraduationCap },
  { key: 'achievements', label: 'Achievements', icon: Trophy },
  { key: 'certifications', label: 'Certifications', icon: ScrollText },
];

const connectLinks = [
  { label: 'GitHub', icon: Github, href: profile.socials.github },
  { label: 'LinkedIn', icon: Linkedin, href: profile.socials.linkedin },
  { label: 'Email', icon: Mail, href: profile.socials.email },
  { label: 'Resume', icon: FileText, href: profile.socials.resume },
];

export function Sidebar({
  activeView,
  onViewChange,
  onNewChat,
  collapsed,
  onToggleCollapse,
  mobileOpen,
  onCloseMobile,
}: SidebarProps) {
  return (
    <>
      {/* Mobile overlay */}
      {mobileOpen && (
        <div
          className="fixed inset-0 z-30 bg-black/60 backdrop-blur-sm md:hidden"
          onClick={onCloseMobile}
        />
      )}

      <aside
        className={`
          fixed left-0 top-0 z-40 flex h-full flex-col border-r border-border bg-bg-surface
          transition-all duration-300 ease-in-out
          ${collapsed ? 'w-[60px]' : 'w-[260px]'}
          ${mobileOpen ? 'translate-x-0' : '-translate-x-full'}
          md:relative md:translate-x-0
        `}
      >
        {/* Header */}
        <div className="flex items-center gap-2 border-b border-border-subtle px-3 py-3.5">
          <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-accent/15 border border-accent/25">
            <Bot size={18} className="text-accent" />
          </div>
          {!collapsed && (
            <div className="min-w-0 flex-1 animate-fade-in">
              <h1 className="truncate text-sm font-semibold text-gray-100">Atharva AI</h1>
              <p className="truncate text-2xs text-gray-500">AI-powered developer portfolio</p>
            </div>
          )}
          <button
            onClick={onToggleCollapse}
            className="hidden rounded-md p-1.5 text-gray-500 transition-colors hover:bg-bg-hover hover:text-gray-300 md:block"
            aria-label={collapsed ? 'Expand sidebar' : 'Collapse sidebar'}
          >
            {collapsed ? <PanelLeftOpen size={16} /> : <PanelLeftClose size={16} />}
          </button>
        </div>

        {/* New Chat */}
        <div className="px-2 py-2">
          <button
            onClick={() => {
              onNewChat();
              onViewChange('chat');
            }}
            className={`flex w-full items-center gap-2 rounded-lg border border-border bg-bg-elevated px-3 py-2 text-sm text-gray-200 transition-colors hover:border-accent/30 hover:bg-bg-hover ${
              collapsed ? 'justify-center' : ''
            }`}
            title="New Chat"
          >
            <Plus size={16} className="shrink-0 text-accent" />
            {!collapsed && <span className="animate-fade-in">New Chat</span>}
          </button>
        </div>

        {/* Scrollable nav */}
        <nav className="flex-1 overflow-y-auto scrollbar-thin px-2 pb-2">
          {/* Portfolio section */}
          <div className="mb-1 mt-2">
            {!collapsed && (
              <p className="px-2 pb-1 text-2xs font-medium uppercase tracking-wider text-gray-600 animate-fade-in">
                Portfolio
              </p>
            )}
            <div className="space-y-0.5">
              {portfolioNav.map((item) => {
                const Icon = item.icon;
                const active = activeView === item.key;
                return (
                  <button
                    key={item.key}
                    onClick={() => onViewChange(item.key)}
                    title={collapsed ? item.label : undefined}
                    className={`flex w-full items-center gap-2.5 rounded-lg px-2.5 py-2 text-sm transition-colors ${
                      collapsed ? 'justify-center' : ''
                    } ${
                      active
                        ? 'bg-accent/10 text-accent'
                        : 'text-gray-400 hover:bg-bg-hover hover:text-gray-200'
                    }`}
                  >
                    <Icon size={16} className="shrink-0" />
                    {!collapsed && <span className="animate-fade-in">{item.label}</span>}
                  </button>
                );
              })}
            </div>
          </div>

          {/* Connect section */}
          <div className="mb-1 mt-4">
            {!collapsed && (
              <p className="px-2 pb-1 text-2xs font-medium uppercase tracking-wider text-gray-600 animate-fade-in">
                Connect
              </p>
            )}
            <div className="space-y-0.5">
              {connectLinks.map((link) => {
                const Icon = link.icon;
                return (
                  <a
                    key={link.label}
                    href={link.href}
                    target="_blank"
                    rel="noopener noreferrer"
                    title={collapsed ? link.label : undefined}
                    className={`flex w-full items-center gap-2.5 rounded-lg px-2.5 py-2 text-sm text-gray-400 transition-colors hover:bg-bg-hover hover:text-gray-200 ${
                      collapsed ? 'justify-center' : ''
                    }`}
                  >
                    <Icon size={16} className="shrink-0" />
                    {!collapsed && <span className="animate-fade-in">{link.label}</span>}
                  </a>
                );
              })}
            </div>
          </div>
        </nav>

        {/* Footer — AI Assistant status */}
        <div className="border-t border-border-subtle px-2 py-3">
          <div
            className={`flex items-center gap-2.5 rounded-lg px-2.5 py-2 ${
              collapsed ? 'justify-center' : ''
            }`}
          >
            <div className="relative shrink-0">
              <div className="flex h-7 w-7 items-center justify-center rounded-lg bg-bg-elevated border border-border">
                <MessageSquare size={14} className="text-gray-400" />
              </div>
              <span className="absolute -bottom-0.5 -right-0.5 h-2.5 w-2.5 rounded-full border-2 border-bg-surface bg-accent animate-pulse-soft" />
            </div>
            {!collapsed && (
              <div className="min-w-0 animate-fade-in">
                <p className="text-xs font-medium text-gray-200">AI Assistant</p>
                <p className="text-2xs text-accent/80">Online</p>
              </div>
            )}
          </div>
        </div>
      </aside>
    </>
  );
}

export default Sidebar;
