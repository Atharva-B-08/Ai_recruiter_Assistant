import { Bot } from 'lucide-react';
import SuggestedQuestions from './SuggestedQuestions';

interface WelcomeScreenProps {
  onSuggestionSelect: (question: string) => void;
}

export function WelcomeScreen({ onSuggestionSelect }: WelcomeScreenProps) {
  return (
    <div className="flex h-full flex-col items-center justify-center px-4 py-8">
      <div className="mb-6 flex h-16 w-16 items-center justify-center rounded-2xl bg-accent/10 border border-accent/20 animate-fade-in">
        <Bot size={32} className="text-accent" />
      </div>
      <h1 className="mb-2 text-2xl font-semibold text-gray-100 animate-fade-in-up">
        Hi, I'm Atharva's AI
      </h1>
      <p className="mb-8 max-w-md text-center text-[0.95rem] leading-relaxed text-gray-400 animate-fade-in-up">
        I can tell you about Atharva's projects, skills, education, achievements
        and technical journey.
      </p>
      <div className="w-full max-w-2xl animate-fade-in-up">
        <SuggestedQuestions onSelect={onSuggestionSelect} />
      </div>
    </div>
  );
}

export default WelcomeScreen;
