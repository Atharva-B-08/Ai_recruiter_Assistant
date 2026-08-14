import { ArrowLeft, Github, ExternalLink, Star, Check } from 'lucide-react';
import { projects } from '@/data/projects';

interface ProjectsProps {
  onBack: () => void;
}

export function Projects({ onBack }: ProjectsProps) {
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

        <h1 className="mb-1 text-xl font-semibold text-gray-100">Projects</h1>
        <p className="mb-6 text-sm text-gray-500">Featured work and technical projects.</p>

        <div className="space-y-6">
          {projects.map((project) => (
            <div
              key={project.name}
              className="overflow-hidden rounded-2xl border border-border bg-bg-surface animate-fade-in-up"
            >
              {/* Header */}
              <div className="border-b border-border-subtle px-5 py-4">
                <div className="flex items-start justify-between gap-3">
                  <div>
                    <div className="flex items-center gap-2">
                      {project.featured && (
                        <span className="flex items-center gap-1 rounded-full bg-accent/10 border border-accent/20 px-2 py-0.5 text-2xs font-medium text-accent">
                          <Star size={10} className="fill-accent" />
                          Featured
                        </span>
                      )}
                    </div>
                    <h2 className="mt-1.5 text-lg font-semibold text-gray-100">{project.name}</h2>
                    <p className="text-sm text-gray-400">{project.tagline}</p>
                  </div>
                </div>
              </div>

              {/* Body */}
              <div className="space-y-5 px-5 py-4">
                <p className="text-sm leading-relaxed text-gray-300">{project.description}</p>

                {/* Features */}
                <div>
                  <h3 className="mb-2.5 text-2xs font-medium uppercase tracking-wider text-gray-500">
                    Features
                  </h3>
                  <div className="grid grid-cols-1 gap-2 sm:grid-cols-2">
                    {project.features.map((feature) => (
                      <div
                        key={feature}
                        className="flex items-center gap-2 text-sm text-gray-300"
                      >
                        <Check size={14} className="shrink-0 text-accent" />
                        {feature}
                      </div>
                    ))}
                  </div>
                </div>

                {/* Technologies */}
                <div>
                  <h3 className="mb-2.5 text-2xs font-medium uppercase tracking-wider text-gray-500">
                    Technologies
                  </h3>
                  <div className="flex flex-wrap gap-1.5">
                    {project.technologies.map((tech) => (
                      <span
                        key={tech}
                        className="rounded-md border border-border bg-bg-elevated px-2.5 py-1 text-xs text-gray-300"
                      >
                        {tech}
                      </span>
                    ))}
                  </div>
                </div>

                {/* Links */}
                <div className="flex gap-3 pt-1">
                  {project.github && (
                    <a
                      href={project.github}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="flex items-center gap-1.5 rounded-lg border border-border bg-bg-elevated px-3 py-1.5 text-sm text-gray-300 transition-colors hover:border-accent/30 hover:text-accent"
                    >
                      <Github size={14} />
                      GitHub
                    </a>
                  )}
                  {project.demo && (
                    <a
                      href={project.demo}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="flex items-center gap-1.5 rounded-lg border border-border bg-bg-elevated px-3 py-1.5 text-sm text-gray-300 transition-colors hover:border-accent/30 hover:text-accent"
                    >
                      <ExternalLink size={14} />
                      Live Demo
                    </a>
                  )}
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Projects;
