export interface Certification {
  name: string;
  issuer?: string;
  date?: string;
  link?: string;
}

export const certifications: Certification[] = [
  {
    name: "Introduction to SQL",
    issuer: "Great learning",
    date: "2024-05-15",
  },
  {
    name: "Deep Learning Onramp",
    issuer: "Mathworks",
    date: "2025-07-06",
  },
  {
    name: "Machine Learning Onramp",
    issuer: "Mathworks",
    date: "2025-07-06",
  },
  {
    name: "MATLAB Onramp",
    issuer: "Mathworks",
    date: "2025-07-02",
  }

];

export default certifications;
