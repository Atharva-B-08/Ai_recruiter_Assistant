export interface Certification {
  name: string;
  issuer?: string;
  date?: string;
  link?: string;
}

export const certifications: Certification[] = [];

export default certifications;
