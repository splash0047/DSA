'use client';

import React, { useState, useEffect } from 'react';
import Link from 'next/link';
import { Network, Sparkles, ChevronRight, CheckCircle2, BookOpen, Zap } from 'lucide-react';
import { Phase, Problem, UserProgress } from '@/lib/types';
import { getStoredProgress } from '@/lib/storage';
import { Header } from '@/components/layout/header';
import { CommandPalette } from '@/components/layout/command-palette';

interface PatternsClientProps {
  initialPhases: Phase[];
  initialProblems: Problem[];
}

export const PatternsClient: React.FC<PatternsClientProps> = ({
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

  // Group problems by pattern name
  const patternGroups = React.useMemo(() => {
    const map: Record<string, Problem[]> = {};
    initialProblems.forEach(p => {
      const pattern = p.pattern || 'General Technique';
      if (!map[pattern]) map[pattern] = [];
      map[pattern].push(p);
    });

    return Object.entries(map)
      .map(([patternName, probs]) => ({
        pattern: patternName,
        problems: probs,
        total: probs.length,
        completed: probs.filter(p => progress.completedIds.includes(p.id)).length,
      }))
      .sort((a, b) => b.total - a.total);
  }, [initialProblems, progress.completedIds]);

  return (
    <div className="min-h-screen flex flex-col">
      <Header progress={progress} onOpenCommandPalette={() => setIsCommandPaletteOpen(true)} />

      <CommandPalette
        isOpen={isCommandPaletteOpen}
        onClose={() => setIsCommandPaletteOpen(false)}
        problems={initialProblems}
      />

      <div className="flex-1 max-w-7xl mx-auto w-full px-4 sm:px-6 py-8 space-y-8">
        {/* Header */}
        <div className="border-b border-slate-800 pb-4">
          <h1 className="text-2xl font-extrabold text-slate-100 flex items-center gap-2.5">
            <Network className="h-6 w-6 text-cyan-400" />
            <span>DSA Pattern Knowledge Graph</span>
          </h1>
          <p className="text-xs text-slate-400 mt-1">
            Master the underlying algorithmic templates and reusable techniques across all 154 problems
          </p>
        </div>

        {/* Pattern Cards Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {patternGroups.map((group) => {
            const percent = Math.round((group.completed / (group.total || 1)) * 100) || 0;
            return (
              <div
                key={group.pattern}
                className="glass-card rounded-2xl p-5 border border-slate-800 flex flex-col justify-between space-y-4 hover:border-cyan-500/40 transition-all"
              >
                <div>
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-bold text-cyan-400 bg-cyan-500/10 px-2.5 py-1 rounded-lg border border-cyan-500/20">
                      {group.total} Problems
                    </span>
                    <span className="text-xs text-slate-400 font-semibold">
                      {group.completed}/{group.total} ({percent}%)
                    </span>
                  </div>

                  <h3 className="text-base font-bold text-slate-100 mt-3">
                    {group.pattern}
                  </h3>

                  {/* Progress Bar */}
                  <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden mt-3">
                    <div 
                      className="bg-gradient-to-r from-cyan-500 to-emerald-400 h-full rounded-full transition-all duration-500"
                      style={{ width: `${percent}%` }}
                    />
                  </div>

                  {/* Sample Problems Preview */}
                  <div className="mt-3 space-y-1">
                    <span className="text-[10px] uppercase font-bold text-slate-500 tracking-wider">
                      Featured In:
                    </span>
                    <ul className="text-xs text-slate-300 space-y-1">
                      {group.problems.slice(0, 3).map(p => (
                        <li key={p.id} className="truncate flex items-center gap-1.5">
                          <span className="text-slate-500 text-[10px] font-mono">#{String(p.number).padStart(3, '0')}</span>
                          <span className="truncate">{p.title}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>

                <Link
                  href={`/problems?search=${encodeURIComponent(group.pattern)}`}
                  className="flex items-center justify-between text-xs font-bold text-cyan-400 pt-3 border-t border-slate-800/60 hover:text-cyan-300"
                >
                  <span>Practice {group.pattern} Problems</span>
                  <ChevronRight className="h-4 w-4" />
                </Link>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
