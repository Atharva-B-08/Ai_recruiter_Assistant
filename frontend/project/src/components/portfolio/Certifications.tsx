import { ArrowLeft, ScrollText, Award } from 'lucide-react';
import { certifications } from '@/data/certifications';

interface CertificationsProps {
  onBack: () => void;
}

export function Certifications({ onBack }: CertificationsProps) {
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

        <h1 className="mb-1 text-xl font-semibold text-gray-100">Certifications</h1>
        <p className="mb-6 text-sm text-gray-500">Professional certifications and credentials.</p>

        {certifications.length === 0 ? (
          <div className="flex flex-col items-center justify-center rounded-xl border border-dashed border-border bg-bg-surface py-16 text-center">
            <div className="mb-3 flex h-12 w-12 items-center justify-center rounded-xl bg-bg-elevated border border-border">
              <ScrollText size={24} className="text-gray-600" />
            </div>
            <p className="text-sm text-gray-500">No certifications listed yet.</p>
            <p className="mt-1 text-2xs text-gray-600">
              Check back soon for updates.
            </p>
          </div>
        ) : (
          <div className="space-y-3">
            {certifications.map((cert, i) => (
              <div
                key={i}
                className="flex items-center gap-3 rounded-xl border border-border bg-bg-surface px-4 py-3.5 animate-fade-in-up"
              >
                <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-bg-elevated border border-border">
                  <Award size={18} className="text-accent" />
                </div>
                <div className="min-w-0 flex-1">
                  <h2 className="text-sm font-semibold text-gray-100">{cert.name}</h2>
                  <p className="text-xs text-gray-500">
                    {cert.issuer && <span>{cert.issuer}</span>}
                    {cert.issuer && cert.date && <span> · </span>}
                    {cert.date && <span>{cert.date}</span>}
                  </p>
                </div>
                {cert.link && (
                  <a
                    href={cert.link}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-xs text-accent hover:underline"
                  >
                    View →
                  </a>
                )}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default Certifications;
