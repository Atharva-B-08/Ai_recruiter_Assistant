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
      'Strong foundation in data structures and algorithms with consistent practice across competitive programming platforms. Participated in various coding competitions, achieving top ranks and honing problem-solving skills.',
  },
  {
    title: 'LeetCode Problem Solving',
    category: 'LeetCode',
    description:
      'Solved a wide range of problems spanning arrays, graphs, dynamic programming, trees, and system design fundamentals. Solved over 900 problems on LeetCode, achieving a high ranking in the global leaderboard. I have also participated in several LeetCode contests, gets a Knight rank in LeetCode contests.',
  },
];

export default achievements;
