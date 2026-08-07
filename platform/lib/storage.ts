import { UserProgress } from './types';

const STORAGE_KEY = 'dsa_learning_platform_progress';

const defaultProgress: UserProgress = {
  completedIds: [],
  bookmarkedIds: [],
  revisionIds: [],
  notes: {},
  streak: 1,
  lastActiveDate: new Date().toISOString().split('T')[0],
  ratings: {},
  recentlyViewed: [],
};

export function getStoredProgress(): UserProgress {
  if (typeof window === 'undefined') return defaultProgress;
  try {
    const item = localStorage.getItem(STORAGE_KEY);
    if (!item) return defaultProgress;
    return JSON.parse(item);
  } catch {
    return defaultProgress;
  }
}

export function saveStoredProgress(progress: UserProgress): void {
  if (typeof window === 'undefined') return;
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
  } catch (e) {
    console.error('Failed to save progress to localStorage', e);
  }
}

export function toggleCompleted(problemId: string): UserProgress {
  const current = getStoredProgress();
  const exists = current.completedIds.includes(problemId);
  
  const updatedCompleted = exists
    ? current.completedIds.filter(id => id !== problemId)
    : [...current.completedIds, problemId];
    
  const updated: UserProgress = {
    ...current,
    completedIds: updatedCompleted,
    lastActiveDate: new Date().toISOString().split('T')[0],
  };
  
  saveStoredProgress(updated);
  return updated;
}

export function toggleBookmarked(problemId: string): UserProgress {
  const current = getStoredProgress();
  const exists = current.bookmarkedIds.includes(problemId);
  
  const updatedBookmarked = exists
    ? current.bookmarkedIds.filter(id => id !== problemId)
    : [...current.bookmarkedIds, problemId];
    
  const updated: UserProgress = {
    ...current,
    bookmarkedIds: updatedBookmarked,
  };
  
  saveStoredProgress(updated);
  return updated;
}

export function toggleRevision(problemId: string): UserProgress {
  const current = getStoredProgress();
  const exists = current.revisionIds.includes(problemId);
  
  const updatedRevision = exists
    ? current.revisionIds.filter(id => id !== problemId)
    : [...current.revisionIds, problemId];
    
  const updated: UserProgress = {
    ...current,
    revisionIds: updatedRevision,
  };
  
  saveStoredProgress(updated);
  return updated;
}

export function saveUserNote(problemId: string, noteContent: string): UserProgress {
  const current = getStoredProgress();
  const updated: UserProgress = {
    ...current,
    notes: {
      ...current.notes,
      [problemId]: noteContent,
    },
  };
  
  saveStoredProgress(updated);
  return updated;
}

export function addRecentlyViewed(problemId: string): UserProgress {
  const current = getStoredProgress();
  const filtered = (current.recentlyViewed || []).filter(id => id !== problemId);
  const updated: UserProgress = {
    ...current,
    recentlyViewed: [problemId, ...filtered].slice(0, 10),
  };
  saveStoredProgress(updated);
  return updated;
}

export function setRating(problemId: string, rating: 'easy' | 'good' | 'hard'): UserProgress {
  const current = getStoredProgress();
  const updated: UserProgress = {
    ...current,
    ratings: {
      ...current.ratings,
      [problemId]: rating,
    },
  };
  saveStoredProgress(updated);
  return updated;
}
