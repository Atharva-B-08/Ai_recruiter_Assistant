export interface Project {
  name: string;
  tagline: string;
  description: string;
  technologies: string[];
  features: string[];
  github?: string;
  demo?: string;
  featured?: boolean;
}

export const projects: Project[] = [
  {
    name: 'FinTrack',
    tagline: 'Personal Finance Manager',
    description:
      'A full-featured personal finance management application for tracking budgets, transactions, and financial analytics. Built with a secure Spring Boot backend and a modern React frontend.',
    technologies: [
      'Java',
      'Spring Boot',
      'Spring Security',
      'JWT',
      'React',
      'Tailwind CSS',
      'ShadCN UI',
      'PostgreSQL',
      'Supabase',
      'Inngest',
    ],
    features: [
      'Budget management',
      'Transaction history',
      'Analytics dashboard',
      'Recurring transactions',
      'Receipt upload and auto-fill',
      'Multiple accounts',
    ],
    github: 'https://github.com/',
    featured: true,
  },
];

export default projects;
