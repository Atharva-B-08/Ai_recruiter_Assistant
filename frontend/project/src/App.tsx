import { useState, useRef, useCallback } from 'react';
import Sidebar, { type ViewKey } from '@/components/layout/Sidebar';
import MobileHeader from '@/components/layout/MobileHeader';
import ChatWindow from '@/components/chat/ChatWindow';
import ChatInput from '@/components/chat/ChatInput';
import WelcomeScreen from '@/components/chat/WelcomeScreen';
import About from '@/components/portfolio/About';
import Skills from '@/components/portfolio/Skills';
import Projects from '@/components/portfolio/Projects';
import EducationPanel from '@/components/portfolio/Education';
import Achievements from '@/components/portfolio/Achievements';
import Certifications from '@/components/portfolio/Certifications';
import { streamChat, type ChatMessage } from '@/services/chatApi';

function App() {
  const [activeView, setActiveView] = useState<ViewKey>('chat');
  const [sidebarCollapsed, setSidebarCollapsed] = useState(false);
  const [mobileSidebarOpen, setMobileSidebarOpen] = useState(false);

  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [conversationId, setConversationId] = useState<string | null>(null);
  const [inputValue, setInputValue] = useState('');
  const [isGenerating, setIsGenerating] = useState(false);

  const abortControllerRef = useRef<AbortController | null>(null);

  const handleNewChat = useCallback(() => {
    if (abortControllerRef.current) {
      abortControllerRef.current.abort();
    }
    setMessages([]);
    setConversationId(null);
    setInputValue('');
    setIsGenerating(false);
  }, []);

  const handleViewChange = useCallback((view: ViewKey) => {
    setActiveView(view);
    setMobileSidebarOpen(false);
  }, []);

  const handleSubmit = useCallback(
    (question?: string) => {
      const q = (question ?? inputValue).trim();
      if (!q || isGenerating) return;

      // Add user message
      const userMessage: ChatMessage = { role: 'user', content: q };
      const assistantPlaceholder: ChatMessage = { role: 'assistant', content: '' };

      setMessages((prev) => [...prev, userMessage, assistantPlaceholder]);
      setInputValue('');
      setIsGenerating(true);

      const controller = new AbortController();
      abortControllerRef.current = controller;

      streamChat(
        q,
        conversationId,
        {
          onConversationId: (id) => setConversationId(id),
          onChunk: (content) => {
            setMessages((prev) => {
              const updated = [...prev];
              const last = updated[updated.length - 1];
              if (last && last.role === 'assistant') {
                updated[updated.length - 1] = {
                  ...last,
                  content: last.content + content,
                };
              }
              return updated;
            });
          },
          onDone: () => {
            setIsGenerating(false);
            abortControllerRef.current = null;
          },
          onError: (error) => {
            setMessages((prev) => {
              const updated = [...prev];
              const last = updated[updated.length - 1];
              if (last && last.role === 'assistant') {
                updated[updated.length - 1] = {
                  ...last,
                  content: error.message,
                  error: true,
                };
              }
              return updated;
            });
            setIsGenerating(false);
            abortControllerRef.current = null;
          },
        },
        controller.signal,
      );
    },
    [inputValue, isGenerating, conversationId],
  );

  const handleStop = useCallback(() => {
    if (abortControllerRef.current) {
      abortControllerRef.current.abort();
    }
    setIsGenerating(false);
  }, []);

  const handleSuggestionSelect = useCallback(
    (question: string) => {
      handleSubmit(question);
    },
    [handleSubmit],
  );

  const renderMainContent = () => {
    switch (activeView) {
      case 'about':
        return <About onBack={() => handleViewChange('chat')} />;
      case 'skills':
        return <Skills onBack={() => handleViewChange('chat')} />;
      case 'projects':
        return <Projects onBack={() => handleViewChange('chat')} />;
      case 'education':
        return <EducationPanel onBack={() => handleViewChange('chat')} />;
      case 'achievements':
        return <Achievements onBack={() => handleViewChange('chat')} />;
      case 'certifications':
        return <Certifications onBack={() => handleViewChange('chat')} />;
      default:
        return (
          <div className="flex h-full flex-col">
            {messages.length === 0 ? (
              <div className="flex-1 overflow-y-auto scrollbar-thin">
                <WelcomeScreen onSuggestionSelect={handleSuggestionSelect} />
              </div>
            ) : (
              <ChatWindow messages={messages} isGenerating={isGenerating} />
            )}
            <ChatInput
              value={inputValue}
              onChange={setInputValue}
              onSubmit={() => handleSubmit()}
              onStop={handleStop}
              isGenerating={isGenerating}
            />
          </div>
        );
    }
  };

  return (
    <div className="flex h-screen overflow-hidden bg-bg-base text-gray-200">
      <Sidebar
        activeView={activeView}
        onViewChange={handleViewChange}
        onNewChat={handleNewChat}
        collapsed={sidebarCollapsed}
        onToggleCollapse={() => setSidebarCollapsed((v) => !v)}
        mobileOpen={mobileSidebarOpen}
        onCloseMobile={() => setMobileSidebarOpen(false)}
      />

      <div className="flex min-w-0 flex-1 flex-col">
        <MobileHeader
          onOpenSidebar={() => setMobileSidebarOpen(true)}
          onNewChat={handleNewChat}
        />
        <main className="min-h-0 flex-1">{renderMainContent()}</main>
      </div>
    </div>
  );
}

export default App;
