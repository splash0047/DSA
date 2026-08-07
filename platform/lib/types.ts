export type Difficulty = 'Easy' | 'Medium' | 'Hard';

export interface Problem {
  id: string; // e.g. "001-two-sum"
  number: number; // e.g. 1
  title: string; // e.g. "Two Sum"
  slug: string; // e.g. "001-two-sum"
  phaseFolder: string; // e.g. "Phase 00 Programming Foundation"
  problemFolder: string; // e.g. "001 Two Sum"
  phaseNumber: number; // e.g. 0
  phaseTitle: string; // e.g. "Programming Foundation"
  difficulty: Difficulty;
  platform: string; // e.g. "LeetCode"
  platformProblemNumber: string; // e.g. "#1"
  url: string;
  pattern: string; // e.g. "Two Pointers", "DFS Grid Sink", etc.
  readingTimeMinutes: number;
  questionMd: string;
  bruteForceMd: string;
  optimalMd: string;
  explanationMd: string;
  bruteCode: string;
  optimalCode: string;
  summary: string;
  timeComplexity: string;
  spaceComplexity: string;
  similarProblems: Array<{ title: string; url: string }>;
  revisionNotes: string;
}

export interface Phase {
  id: string;
  number: number;
  title: string;
  folderName: string;
  problemCount: number;
  problems: Problem[];
}

export interface UserProgress {
  completedIds: string[];
  bookmarkedIds: string[];
  revisionIds: string[];
  notes: Record<string, string>;
  streak: number;
  lastActiveDate: string;
  ratings: Record<string, 'easy' | 'good' | 'hard'>;
  recentlyViewed: string[];
}

export interface StatsOverview {
  totalProblems: number;
  completedProblems: number;
  easyCount: number;
  easyCompleted: number;
  mediumCount: number;
  mediumCompleted: number;
  hardCount: number;
  hardCompleted: number;
  streak: number;
  phaseProgress: Array<{
    phaseNumber: number;
    phaseTitle: string;
    total: number;
    completed: number;
    percentage: number;
  }>;
  patternMastery: Array<{
    pattern: string;
    total: number;
    completed: number;
  }>;
}
