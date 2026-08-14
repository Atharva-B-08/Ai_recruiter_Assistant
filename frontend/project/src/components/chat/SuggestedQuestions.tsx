import { Sparkles } from 'lucide-react';

interface SuggestedQuestionsProps {
  onSelect: (question: string) => void;
}

const suggestions = [
  { icon: '💼', text: 'Tell me about FinTrack' },
  { icon: '⚡', text: "What are Atharva's strongest skills?" },
  { icon: '🚀', text: 'Tell me about his projects' },
  { icon: '🛠️', text: 'What technologies does he use?' },
  { icon: '⚙️', text: 'Explain his backend experience' },
  { icon: '🏆', text: "Tell me about his DSA achievements" },
];

export function SuggestedQuestions({ onSelect }: SuggestedQuestionsProps) {
  return (
    <div className="mx-auto w-full max-w-2xl">
      <div className="mb-3 flex items-center gap-2 text-2xs font-medium uppercase tracking-wider text-gray-600">
        <Sparkles size={12} />
        Suggested questions
      </div>
      <div className="grid grid-cols-1 gap-2 sm:grid-cols-2">
        {suggestions.map((s) => (
          <button
            key={s.text}
            onClick={() => onSelect(s.text)}
            className="group flex items-center gap-3 rounded-xl border border-border bg-bg-surface px-4 py-3 text-left text-sm text-gray-300 transition-all hover:border-accent/30 hover:bg-bg-hover hover:text-gray-100"
          >
            <span className="text-base">{s.icon}</span>
            <span className="flex-1">{s.text}</span>
          </button>
        ))}
      </div>
    </div>
  );
}

export default SuggestedQuestions;
