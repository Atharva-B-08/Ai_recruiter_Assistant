export interface Skill {
  name: string;
  level: 'Advanced' | 'Intermediate' | 'Familiar';
}

export interface SkillCategory {
  category: string;
  icon: string;
  skills: Skill[];
}

export const skillCategories: SkillCategory[] = [
  {
    category: 'Backend',
    icon: 'Server',
    skills: [
      { name: 'Java', level: 'Advanced' },
      { name: 'Spring Boot', level: 'Advanced' },
      { name: 'Spring Security', level: 'Intermediate' },
      { name: 'JWT', level: 'Intermediate' },
      { name: 'Hibernate', level: 'Intermediate' },
      { name: 'JPA', level: 'Intermediate' },
    ],
  },
  {
    category: 'Frontend',
    icon: 'Layout',
    skills: [
      { name: 'React', level: 'Advanced' },
      { name: 'JavaScript', level: 'Advanced' },
      { name: 'TypeScript', level: 'Intermediate' },
      { name: 'Tailwind CSS', level: 'Advanced' },
      { name: 'ShadCN UI', level: 'Intermediate' },
    ],
  },
  {
    category: 'Database',
    icon: 'Database',
    skills: [
      { name: 'PostgreSQL', level: 'Intermediate' },
      { name: 'MySQL', level: 'Intermediate' },
      { name: 'MongoDB', level: 'Familiar' },
    ],
  },
  {
    category: 'AI / ML',
    icon: 'BrainCircuit',
    skills: [
      { name: 'Python', level: 'Intermediate' },
      { name: 'TensorFlow', level: 'Familiar' },
      { name: 'PyTorch', level: 'Familiar' },
      { name: 'scikit-learn', level: 'Familiar' },
    ],
  },
  {
    category: 'Tools',
    icon: 'Wrench',
    skills: [
      { name: 'Git', level: 'Advanced' },
      { name: 'GitHub', level: 'Advanced' },
      { name: 'Docker', level: 'Familiar' },
      { name: 'Postman', level: 'Intermediate' },
    ],
  },
];

export default skillCategories;
