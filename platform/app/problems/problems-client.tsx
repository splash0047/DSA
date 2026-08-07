'use client';

import React, { useState, useEffect, useMemo } from 'react';
import { useSearchParams } from 'next/navigation';
import { Phase, Problem, UserProgress } from '@/lib/types';
import { 
  getStoredProgress, 
  toggleCompleted, 
  toggleBookmarked, 
  toggleRevision 
} from '@/lib/storage';
import { Header } from '@/components/layout/header';
import { Sidebar } from '@/components/layout/sidebar';
import { CommandPalette } from '@/components/layout/command-palette';
import { ProblemFilters } from '@/components/problems/problem-filters';
import { ProblemTable } from '@/components/problems/problem-table';
import { BookOpen } from 'lucide-react';

interface ProblemsClientProps {
  initialPhases: Phase[];
  initialProblems: Problem[];
}

export const ProblemsClient: React.FC<ProblemsClientProps> = ({
  initialPhases,
  initialProblems,
}) => {
  const searchParams = useSearchParams();
  const phaseParam = searchParams.get('phase');

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

  // Filters State
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedPhase, setSelectedPhase] = useState(phaseParam || 'all');
  const [selectedDifficulty, setSelectedDifficulty] = useState('all');
  const [selectedStatus, setSelectedStatus] = useState('all');
  const [viewMode, setViewMode] = useState<'table' | 'grid'>('table');

  useEffect(() => {
    setProgress(getStoredProgress());
  }, []);

  useEffect(() => {
    if (phaseParam) {
      setSelectedPhase(phaseParam);
    }
  }, [phaseParam]);

  const handleToggleComplete = (problemId: string) => {
    const updated = toggleCompleted(problemId);
    setProgress(updated);
  };

  const handleToggleBookmark = (problemId: string) => {
    const updated = toggleBookmarked(problemId);
    setProgress(updated);
  };

  const handleToggleRevision = (problemId: string) => {
    const updated = toggleRevision(problemId);
    setProgress(updated);
  };

  // Filter Problems Logic
  const filteredProblems = useMemo(() => {
    return initialProblems.filter(problem => {
      // Search query filter
      if (searchQuery.trim()) {
        const q = searchQuery.toLowerCase();
        const matchesTitle = problem.title.toLowerCase().includes(q);
        const matchesPattern = problem.pattern.toLowerCase().includes(q);
        const matchesNum = String(problem.number).includes(q);
        const matchesPhase = problem.phaseTitle.toLowerCase().includes(q);
        if (!matchesTitle && !matchesPattern && !matchesNum && !matchesPhase) {
          return false;
        }
      }

      // Phase filter
      if (selectedPhase !== 'all') {
        if (String(problem.phaseNumber) !== selectedPhase) {
          return false;
        }
      }

      // Difficulty filter
      if (selectedDifficulty !== 'all') {
        if (problem.difficulty !== selectedDifficulty) {
          return false;
        }
      }

      // Status filter
      if (selectedStatus !== 'all') {
        const isComp = progress.completedIds.includes(problem.id);
        const isBook = progress.bookmarkedIds.includes(problem.id);
        const isRev = progress.revisionIds.includes(problem.id);

        if (selectedStatus === 'completed' && !isComp) return false;
        if (selectedStatus === 'unsolved' && isComp) return false;
        if (selectedStatus === 'bookmarked' && !isBook) return false;
        if (selectedStatus === 'revision' && !isRev) return false;
      }

      return true;
    });
  }, [
    initialProblems,
    searchQuery,
    selectedPhase,
    selectedDifficulty,
    selectedStatus,
    progress.completedIds,
    progress.bookmarkedIds,
    progress.revisionIds,
  ]);

  return (
    <div className="min-h-screen flex flex-col">
      <Header progress={progress} onOpenCommandPalette={() => setIsCommandPaletteOpen(true)} />

      <CommandPalette
        isOpen={isCommandPaletteOpen}
        onClose={() => setIsCommandPaletteOpen(false)}
        problems={initialProblems}
      />

      <div className="flex-1 flex">
        {/* Collapsible Sidebar */}
        <div className="hidden lg:block">
          <Sidebar 
            phases={initialPhases} 
            progress={progress} 
            onToggleComplete={handleToggleComplete} 
          />
        </div>

        {/* Main Content Area */}
        <div className="flex-1 p-4 sm:p-6 md:p-8 space-y-6 max-w-7xl mx-auto w-full">
          {/* Header Bar */}
          <div className="flex items-center justify-between border-b border-slate-800 pb-4">
            <div>
              <h1 className="text-2xl font-black text-slate-100 flex items-center gap-2.5">
                <BookOpen className="h-6 w-6 text-emerald-400" />
                <span>Problem Directory</span>
              </h1>
              <p className="text-xs text-slate-400 mt-1">
                Showing {filteredProblems.length} of {initialProblems.length} DSA problems across 11 curriculum phases
              </p>
            </div>
          </div>

          {/* Filter Bar */}
          <ProblemFilters
            searchQuery={searchQuery}
            onSearchChange={setSearchQuery}
            selectedPhase={selectedPhase}
            onPhaseChange={setSelectedPhase}
            selectedDifficulty={selectedDifficulty}
            onDifficultyChange={setSelectedDifficulty}
            selectedStatus={selectedStatus}
            onStatusChange={setSelectedStatus}
            viewMode={viewMode}
            onViewModeChange={setViewMode}
            phases={initialPhases}
          />

          {/* Problem List (Table or Grid) */}
          <ProblemTable
            problems={filteredProblems}
            progress={progress}
            viewMode={viewMode}
            onToggleComplete={handleToggleComplete}
            onToggleBookmark={handleToggleBookmark}
            onToggleRevision={handleToggleRevision}
          />
        </div>
      </div>
    </div>
  );
};
