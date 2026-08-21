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
      'FinTrack is a personal finance management application that helps users track their income, expenses, and savings. It provides an intuitive interface for managing budgets, visualizing spending patterns, and setting financial goals. Users can categorize transactions, generate reports, and gain insights into their financial health. The application also supports recurring transactions and allows users to upload receipts for easy record-keeping.',
    technologies: [
      'Java',
      'Spring Boot',
      'Spring Security',
      'JWT',
      'Hibernate',
      'Microservices',
      'FastAPI',
      'React',
      'Tailwind CSS',
      'ShadCN UI',
      'PostgreSQL',
      'MongoDB',
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
    github: 'https://github.com/Atharva-B-08/fintrack-app',
    featured: true,
  },
  {
    name: 'SignMate',
    tagline: 'Real-Time Sign Language Recognition',
    description:
      'SignMate is a gesture recognition system that translates sign language hand gestures into text in real time. Built using a CNN-based deep learning model, it captures live video input, processes hand landmarks, and classifies gestures with high accuracy, helping bridge communication gaps for the hearing and speech impaired community.',
    technologies: [
      'Python',
      'TensorFlow',
      'Keras',
      'OpenCV',
      'CNN',
      'NumPy',
    ],
    features: [
      'Real-time gesture detection',
      'CNN-based image classification',
      'Live webcam input processing',
      'Hand landmark tracking',
      'Text output for recognized signs',
    ],
    featured: false,
  },
  {
    name: 'Smart Contact Manager',
    tagline: 'Secure Contact Management System',
    description:
      'Smart Contact Manager is a secure web application for storing and organizing personal and professional contacts. It features robust authentication with Spring Security, role-based access control, and OTP-based password recovery, giving users a safe and reliable way to manage their contact data.',
    technologies: [
      'Java',
      'Spring Boot',
      'Spring Security',
      'RBAC',
      'MySQL',
    ],
    features: [
      'Secure authentication & authorization',
      'Role-based access control',
      'OTP-based password recovery',
      'Add, edit, delete contacts',
      'Search and filter contacts',
    ],
    github: 'https://github.com/Atharva-B-08/Smart-Contact-Manager',
    featured: false,
  },
];

export default projects;
