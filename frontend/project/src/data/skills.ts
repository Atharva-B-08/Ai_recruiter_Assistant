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
      { name: 'RESTAPIs', level: 'Advanced' },
      { name: 'JWT', level: 'Intermediate' },
      { name: 'Spring Security', level: 'Intermediate' },
      { name: 'Node.js', level: 'Intermediate' },
      { name: 'FastAPI', level: 'Intermediate' },
      { name: 'Hibernate', level: 'Intermediate' },
      { name: 'Microservices', level: 'Intermediate' },
      {name : 'Express.js', level: 'Familiar'}
    ],
  },
  {
    category: 'Frontend',
    icon: 'Layout',
    skills: [
      { name: 'React', level: 'Advanced' },
      { name: 'JavaScript', level: 'Advanced' },
      { name: 'Tailwind CSS', level: 'Advanced' },
      { name: 'TypeScript', level: 'Intermediate' },
      { name: 'ShadCN UI', level: 'Intermediate' },
    ],
  },
  {
    category: 'Database',
    icon: 'Database',
    skills: [
      { name: 'MySQL', level: 'Advanced' },
      { name: 'PostgreSQL', level: 'Intermediate' },
      { name: 'MongoDB', level: 'Familiar' },
    ],
  },
  {
    category: 'AI / ML',
    icon: 'BrainCircuit',
    skills: [
      { name: 'Python', level: 'Intermediate' },
      { name: 'LLM APIs (Anthropic, Groq, Gemini)', level: 'Intermediate' },
      { name: 'FastAPI', level: 'Intermediate' },
      { name: 'Jupyter Notebook', level: 'Intermediate' },
      { name: 'NumPy', level: 'Intermediate' },
      { name: 'Pandas', level: 'Intermediate' },
      { name: 'RAG', level: 'Intermediate' },
      { name: 'OpenCV', level: 'Familiar' },
      { name: 'TensorFlow / Keras', level: 'Familiar' },
      { name: 'PyTorch', level: 'Familiar' },
      { name: 'Streamlit', level: 'Familiar' },
      { name: 'Vector Databases (Qdrant)', level: 'Familiar' },
    ],
  },
  {
    category: 'Tools & Platforms',
    icon: 'Wrench',
    skills: [
      { name: 'Git', level: 'Advanced' },
      { name: 'GitHub', level: 'Advanced' },
      { name: 'VS Code', level: 'Advanced' },
      { name: 'Postman', level: 'Advanced' },
      { name: 'Docker', level: 'Intermediate' },
      {name: 'linux', level: 'Intermediate'},
      { name: 'Jira', level: 'Familiar' },
    ],
  },
];

export default skillCategories;
