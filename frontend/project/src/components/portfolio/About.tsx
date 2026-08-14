import { ArrowLeft, MapPin, Code2 } from 'lucide-react';
import { profile } from '@/data/profile';

interface AboutProps {
  onBack: () => void;
}

export function About({ onBack }: AboutProps) {
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

        <div className="animate-fade-in-up">
          {/* Avatar + name */}
          <div className="flex items-center gap-4">
            <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-gradient-to-br from-accent/20 to-accent/5 border border-accent/20 text-2xl font-bold text-accent">
              AB
            </div>
            <div>
              <h1 className="text-xl font-semibold text-gray-100">{profile.name}</h1>
              <p className="text-sm text-gray-400">{profile.role}</p>
            </div>
          </div>

          {/* Meta */}
          <div className="mt-4 flex flex-wrap gap-3 text-sm text-gray-500">
            <span className="flex items-center gap-1.5">
              <MapPin size={14} />
              {profile.location}
            </span>
            <span className="flex items-center gap-1.5">
              <Code2 size={14} />
              Available for opportunities
            </span>
          </div>

          {/* Summary */}
          <p className="mt-6 leading-relaxed text-gray-300">{profile.summary}</p>

          {/* Highlights */}
          <h2 className="mb-3 mt-8 text-sm font-medium uppercase tracking-wider text-gray-500">
            Highlights
          </h2>
          <ul className="space-y-2">
            {profile.highlights.map((h, i) => (
              <li
                key={i}
                className="flex items-start gap-2.5 rounded-lg border border-border bg-bg-surface px-3.5 py-2.5 text-sm text-gray-300"
              >
                <span className="mt-1 h-1.5 w-1.5 shrink-0 rounded-full bg-accent" />
                {h}
              </li>
            ))}
          </ul>

          {/* Focus areas */}
          <h2 className="mb-3 mt-8 text-sm font-medium uppercase tracking-wider text-gray-500">
            Focus Areas
          </h2>
          <div className="flex flex-wrap gap-2">
            {profile.focus.map((f) => (
              <span
                key={f}
                className="rounded-lg border border-border bg-bg-surface px-3 py-1.5 text-sm text-gray-300"
              >
                {f}
              </span>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default About;
