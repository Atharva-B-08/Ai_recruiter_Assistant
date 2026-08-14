import { ArrowLeft, Trophy, Code2, Award, FileText, Star } from 'lucide-react';
import { achievements, type Achievement } from '@/data/achievements';

const categoryConfig: Record<
  Achievement['category'],
  { icon: typeof Trophy; color: string }
> = {
  DSA: { icon: Code2, color: 'text-accent' },
  LeetCode: { icon: Star, color: 'text-warning' },
  Certification: { icon: Award, color: 'text-info' },
  Research: { icon: FileText, color: 'text-purple-400' },
  Other: { icon: Trophy, color: 'text-gray-400' },
};

interface AchievementsProps {
  onBack: () => void;
}

export function Achievements({ onBack }: AchievementsProps) {
  return (
    <div className="flex h-full flex-col overflow-y-auto scrollbar-thin">
      <div className="mx-auto w-full max-w-3xl px-4 py-6">
        <button
          onClick={onBack}
          className="mb-6 flex items-center gap-2 text-sm text-gray-400 transition-colors hover:text-accent"
        >
          <ArrowLeft size={16} />
          Back to AI Chat
        </button>

        <h1 className="mb-1 text-xl font-semibold text-gray-100">Achievements</h1>
        <p className="mb-6 text-sm text-gray-500">
          DSA accomplishments, competitive programming, and verified achievements.
        </p>

        <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
          {achievements.map((item, i) => {
            const config = categoryConfig[item.category];
            const Icon = config.icon;
            return (
              <div
                key={i}
                className="rounded-xl border border-border bg-bg-surface px-4 py-3.5 animate-fade-in-up"
              >
                <div className="flex items-start gap-3">
                  <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-bg-elevated border border-border">
                    <Icon size={18} className={config.color} />
                  </div>
                  <div className="min-w-0 flex-1">
                    <div className="flex items-center gap-2">
                      <h2 className="text-sm font-semibold text-gray-100">{item.title}</h2>
                      <span className="text-2xs text-gray-600">{item.category}</span>
                    </div>
                    <p className="mt-1 text-sm leading-relaxed text-gray-400">
                      {item.description}
                    </p>
                    {item.link && (
                      <a
                        href={item.link}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="mt-2 inline-block text-xs text-accent hover:underline"
                      >
                        View details →
                      </a>
                    )}
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

export default Achievements;
