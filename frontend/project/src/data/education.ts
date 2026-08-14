export interface EducationItem {
  institution: string;
  degree: string;
  field: string;
  period: string;
  description?: string;
}

export const education: EducationItem[] = [
  {
    institution: 'University',
    degree: 'Bachelor of Technology',
    field: 'Computer Science & Engineering',
    period: '2021 — 2025',
    description:
      'Coursework in data structures, algorithms, operating systems, database management, and software engineering.',
  },
];

export default education;
