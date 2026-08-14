import { ArrowLeft, GraduationCap } from 'lucide-react';
import { education } from '@/data/education';

interface EducationPanelProps {
  onBack: () => void;
}

export function EducationPanel({ onBack }: EducationPanelProps) {
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

        <h1 className="mb-1 text-xl font-semibold text-gray-100">Education</h1>
        <p className="mb-6 text-sm text-gray-500">Academic background and qualifications.</p>

        <div className="relative space-y-4">
          {/* Timeline line */}
          <div className="absolute left-[15px] top-2 bottom-2 w-px bg-border" />

          {education.map((edu, i) => (
            <div key={i} className="relative flex gap-4 animate-fade-in-up">
              <div className="relative z-10 mt-0.5 flex h-8 w-8 shrink-0 items-center justify-center rounded-full border border-accent/30 bg-bg-surface">
                <GraduationCap size={16} className="text-accent" />
              </div>
              <div className="flex-1 rounded-xl border border-border bg-bg-surface px-4 py-3.5">
                <div className="flex flex-wrap items-start justify-between gap-2">
                  <div>
                    <h2 className="text-sm font-semibold text-gray-100">{edu.institution}</h2>
                    <p className="text-sm text-gray-400">
                      {edu.degree} — {edu.field}
                    </p>
                  </div>
                  <span className="rounded-md border border-border bg-bg-elevated px-2.5 py-1 text-2xs text-gray-400">
                    {edu.period}
                  </span>
                </div>
                {edu.description && (
                  <p className="mt-2 text-sm leading-relaxed text-gray-400">{edu.description}</p>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default EducationPanel;
