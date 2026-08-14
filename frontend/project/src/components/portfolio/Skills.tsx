import { ArrowLeft, Server, Layout, Database, BrainCircuit, Wrench } from 'lucide-react';
import { skillCategories, type Skill } from '@/data/skills';

const iconMap: Record<string, typeof Server> = {
  Server,
  Layout,
  Database,
  BrainCircuit,
  Wrench,
};

const levelStyles: Record<Skill['level'], string> = {
  Advanced: 'text-accent border-accent/30 bg-accent/5',
  Intermediate: 'text-info border-info/30 bg-info/5',
  Familiar: 'text-gray-400 border-border bg-bg-surface',
};

interface SkillsProps {
  onBack: () => void;
}

export function Skills({ onBack }: SkillsProps) {
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

        <h1 className="mb-1 text-xl font-semibold text-gray-100">Skills</h1>
        <p className="mb-6 text-sm text-gray-500">Technologies and tools Atharva works with.</p>

        <div className="space-y-6">
          {skillCategories.map((cat) => {
            const Icon = iconMap[cat.icon] ?? Server;
            return (
              <div key={cat.category} className="animate-fade-in-up">
                <div className="mb-3 flex items-center gap-2">
                  <Icon size={16} className="text-accent" />
                  <h2 className="text-sm font-medium text-gray-200">{cat.category}</h2>
                </div>
                <div className="flex flex-wrap gap-2">
                  {cat.skills.map((skill) => (
                    <span
                      key={skill.name}
                      className={`flex items-center gap-2 rounded-lg border px-3 py-1.5 text-sm ${levelStyles[skill.level]}`}
                    >
                      {skill.name}
                      <span className="text-2xs opacity-70">{skill.level}</span>
                    </span>
                  ))}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

export default Skills;
