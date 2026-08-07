'use client';

import React, { useState, useEffect } from 'react';
import { Phase, Problem, UserProgress, StatsOverview } from '@/lib/types';
import { getStoredProgress, toggleCompleted, toggleBookmarked } from '@/lib/storage';
import { Header } from '@/components/layout/header';
import { CommandPalette } from '@/components/layout/command-palette';
import { HeroStats } from '@/components/dashboard/hero-stats';
import { ContinueCard } from '@/components/dashboard/continue-card';
import { PhaseCard } from '@/components/dashboard/phase-card';
import { ProblemTable } from '@/components/problems/problem-table';
import { Sparkles, Trophy, BookOpen, Clock, Flame, ChevronRight, CheckCircle2 } from 'lucide-react';
import Link from 'next/link';

interface DashboardClientProps {
  initialPhases: Phase[];
  initialProblems: Problem[];
}

export const DashboardClient: React.FC<DashboardClientProps> = ({
  initialPhases,
  initialProblems,
}) => {
  const [progress, setProgress] = useState<UserProgress>({
    completedIds: [],
    bookmarkedIds: [],
    revisionIds: [],
    notes: {},
    streak: 1,
    lastActiveDate: new Date().toISOString().split('T')[0],
    ratings: {},
    recentlyViewed: [],
  });

  const [isCommandPaletteOpen, setIsCommandPaletteOpen] = useState(false);

  useEffect(() => {
    setProgress(getStoredProgress());
  }, []);

  const handleToggleComplete = (problemId: string) => {
    const updated = toggleCompleted(problemId);
    setProgress(updated);
  };

  const handleToggleBookmark = (problemId: string) => {
    const updated = toggleBookmarked(problemId);
    setProgress(updated);
  };

  // Find Continue Learning Problem (last recently viewed OR first unsolved problem)
  const continueProblem = React.useMemo(() => {
    if (progress.recentlyViewed && progress.recentlyViewed.length > 0) {
      const found = initialProblems.find(p => p.id === progress.recentlyViewed[0]);
      if (found) return found;
    }
    const firstUnsolved = initialProblems.find(p => !progress.completedIds.includes(p.id));
    return firstUnsolved || initialProblems[0];
  }, [progress.recentlyViewed, progress.completedIds, initialProblems]);

  // Compute Overall Stats Overview
  const stats: StatsOverview = React.useMemo(() => {
    const totalProblems = initialProblems.length;
    const completedProblems = progress.completedIds.length;

    const easyCount = initialProblems.filter(p => p.difficulty === 'Easy').length;
    const easyCompleted = initialProblems.filter(p => p.difficulty === 'Easy' && progress.completedIds.includes(p.id)).length;

    const mediumCount = initialProblems.filter(p => p.difficulty === 'Medium').length;
    const mediumCompleted = initialProblems.filter(p => p.difficulty === 'Medium' && progress.completedIds.includes(p.id)).length;

    const hardCount = initialProblems.filter(p => p.difficulty === 'Hard').length;
    const hardCompleted = initialProblems.filter(p => p.difficulty === 'Hard' && progress.completedIds.includes(p.id)).length;

    const phaseProgress = initialPhases.map(phase => {
      const total = phase.problems.length;
      const completed = phase.problems.filter(p => progress.completedIds.includes(p.id)).length;
      return {
        phaseNumber: phase.number,
        phaseTitle: phase.title,
        total,
        completed,
        percentage: Math.round((completed / (total || 1)) * 100),
      };
    });

    return {
      totalProblems,
      completedProblems,
      easyCount,
      easyCompleted,
      mediumCount,
      mediumCompleted,
      hardCount,
      hardCompleted,
      streak: progress.streak || 1,
      phaseProgress,
      patternMastery: [],
    };
  }, [initialProblems, initialPhases, progress.completedIds, progress.streak]);

  // Recently Viewed Problems List
  const recentProblems = React.useMemo(() => {
    if (!progress.recentlyViewed) return [];
    return progress.recentlyViewed
      .map(id => initialProblems.find(p => p.id === id))
      .filter(Boolean) as Problem[];
  }, [progress.recentlyViewed, initialProblems]);

  return (
    <div className="min-h-screen flex flex-col">
      <Header progress={progress} onOpenCommandPalette={() => setIsCommandPaletteOpen(true)} />

      <CommandPalette 
        isOpen={isCommandPaletteOpen} 
        onClose={() => setIsCommandPaletteOpen(false)} 
        problems={initialProblems} 
      />

      <div className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 py-8 space-y-10">
        {/* Hero Section */}
        <HeroStats stats={stats} />

        {/* Continue Learning Recommendation */}
        {continueProblem && (
          <ContinueCard 
            problem={continueProblem} 
            isCompleted={progress.completedIds.includes(continueProblem.id)} 
          />
        )}

        {/* Recently Viewed Bar */}
        {recentProblems.length > 0 && (
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <h2 className="text-sm font-bold text-slate-300 uppercase tracking-wider flex items-center gap-2">
                <Clock className="h-4 w-4 text-emerald-400" />
                Recently Viewed
              </h2>
            </div>
            <div className="flex gap-3 overflow-x-auto pb-2 scrollbar-none">
              {recentProblems.map((prob) => (
                <Link
                  key={prob.id}
                  href={`/problems/${prob.slug}`}
                  className="glass-card rounded-xl p-3 border border-slate-800 shrink-0 w-64 hover:border-slate-700 transition-all flex flex-col justify-between"
                >
                  <div>
                    <div className="flex items-center justify-between text-[10px] text-slate-500 font-mono">
                      <span>#{String(prob.number).padStart(3, '0')}</span>
                      <span className={
                        prob.difficulty === 'Easy' ? 'text-emerald-400' :
                        prob.difficulty === 'Medium' ? 'text-amber-400' : 'text-rose-400'
                      }>
                        {prob.difficulty}
                      </span>
                    </div>
                    <h4 className="text-xs font-bold text-slate-200 mt-1 line-clamp-1">
                      {prob.title}
                    </h4>
                  </div>
                  <div className="text-[10px] text-slate-400 mt-2 font-medium truncate">
                    {prob.pattern}
                  </div>
                </Link>
              ))}
            </div>
          </div>
        )}

        {/* Phases Mastery Grid */}
        <div className="space-y-4">
          <div className="flex items-center justify-between">
            <h2 className="text-lg font-bold text-slate-100 flex items-center gap-2">
              <BookOpen className="h-5 w-5 text-emerald-400" />
              <span>Phase Curriculum & Mastery</span>
            </h2>
            <Link 
              href="/problems" 
              className="text-xs font-bold text-emerald-400 hover:text-emerald-300 flex items-center gap-1"
            >
              <span>View All 154 Problems</span>
              <ChevronRight className="h-4 w-4" />
            </Link>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {initialPhases.map((phase) => (
              <PhaseCard key={phase.id} phase={phase} progress={progress} />
            ))}
          </div>
        </div>

        {/* Quick Problem Table Preview */}
        <div className="space-y-4 pt-4 border-t border-slate-800/80">
          <div className="flex items-center justify-between">
            <h2 className="text-lg font-bold text-slate-100 flex items-center gap-2">
              <Trophy className="h-5 w-5 text-emerald-400" />
              <span>Featured Problems</span>
            </h2>
            <Link 
              href="/problems" 
              className="text-xs font-semibold text-slate-400 hover:text-slate-200"
            >
              Filter & Search All →
            </Link>
          </div>

          <ProblemTable
            problems={initialProblems.slice(0, 10)}
            progress={progress}
            viewMode="table"
            onToggleComplete={handleToggleComplete}
            onToggleBookmark={handleToggleBookmark}
            onToggleRevision={() => {}}
          />
        </div>
      </div>
    </div>
  );
};
