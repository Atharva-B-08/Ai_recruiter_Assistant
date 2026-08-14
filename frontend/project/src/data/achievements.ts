export interface Achievement {
  title: string;
  category: 'DSA' | 'LeetCode' | 'Certification' | 'Research' | 'Other';
  description: string;
  date?: string;
  link?: string;
}

export const achievements: Achievement[] = [
  {
    title: 'Competitive Programming',
    category: 'DSA',
    description:
      'Strong foundation in data structures and algorithms with consistent practice across competitive programming platforms.',
  },
  {
    title: 'LeetCode Problem Solving',
    category: 'LeetCode',
    description:
      'Solved a wide range of problems spanning arrays, graphs, dynamic programming, trees, and system design fundamentals.',
  },
];

export default achievements;
