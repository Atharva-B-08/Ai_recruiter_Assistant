export interface EducationItem {
  institution: string;
  degree: string;
  field: string;
  period: string;
  description?: string;
  percentage?: number;
}

export const education: EducationItem[] = [
  {
    institution: 'Atharva College of Engineering',
    degree: 'Bachelor of Technology',
    field: 'Computer Engineering',
    period: '2023 — 2026',
    description:
      'Completed my Bachelor of Technology in Computer Engineering (CGPA: 8.18) from Atharva College of Engineering with a strong focus on software development, algorithms, and data structures. Gained hands-on experience in various programming languages and technologies through coursework and projects. Actively participated in coding competitions and hackathons, enhancing problem-solving skills and teamwork. Developed a solid foundation in computer science principles, preparing for a successful career in the tech industry.',
    percentage: 72.31
  },
  {
    institution: 'Ramniranjan Jhunjhunwala College',
    degree: 'Higher Secondary Education',
    field: 'Science (Physics, Chemistry, Mathematics)',
    period: '2021 — 2022',
    description:
      "Completed my Higher Secondary Education in Science (Physics, Chemistry, Mathematics) from Ramniranjan Jhunjhunwala College with a strong academic record. Developed a solid understanding of scientific principles and analytical thinking. Actively engaged in extracurricular activities, including science fairs and competitions, fostering creativity and problem-solving skills. This educational foundation has prepared me for further studies in engineering and technology.",
    percentage: 73.33
  }, 
  {
    institution: 'Saraswati vidya Niketan',
    degree: 'Secondary Education',
    field: 'General Education',
    period: '2010 — 2020',
    description:
      "Completed my Secondary Education from Saraswati vidya Niketan with a focus on general education. Developed essential skills in communication, critical thinking, and teamwork. Actively participated in school events and activities, fostering personal growth and leadership abilities. This educational experience has provided a strong foundation for future academic and professional pursuits.",
    percentage: 88.20
  }
];

export default education;
