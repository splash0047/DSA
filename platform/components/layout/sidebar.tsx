'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { 
  ChevronDown, 
  ChevronRight, 
  CheckCircle2, 
  Circle, 
  Search, 
  BookOpen,
  Sparkles,
  FolderOpen,
  Bookmark
} from 'lucide-react';
import { Phase, Problem, UserProgress } from '@/lib/types';
import { motion, AnimatePresence } from 'framer-motion';

interface SidebarProps {
  phases: Phase[];
  progress: UserProgress;
  onToggleComplete?: (problemId: string) => void;
}

export const Sidebar: React.FC<SidebarProps> = ({ phases, progress, onToggleComplete }) => {
  const pathname = usePathname();
  const [filterQuery, setFilterQuery] = useState('');
  const [expandedPhases, setExpandedPhases] = useState<Record<string, boolean>>(() => {
    // Default expand Phase 0 or active phase
    const initial: Record<string, boolean> = {};
    phases.forEach((p, idx) => {
      initial[p.id] = idx === 0;
    });
    return initial;
  });

  const togglePhase = (phaseId: string) => {
    setExpandedPhases(prev => ({
      ...prev,
      [phaseId]: !prev[phaseId]
    }));
  };

  const getDifficultyColor = (diff: string) => {
    switch (diff) {
      case 'Easy': return 'text-emerald-400 border-emerald-500/20 bg-emerald-500/10';
      case 'Medium': return 'text-amber-400 border-amber-500/20 bg-amber-500/10';
      case 'Hard': return 'text-rose-400 border-rose-500/20 bg-rose-500/10';
      default: return 'text-slate-400 border-slate-700 bg-slate-800';
    }
  };

  return (
    <aside className="w-80 shrink-0 h-[calc(100vh-4rem)] sticky top-16 border-r border-slate-800/80 bg-slate-950/60 backdrop-blur-xl flex flex-col">
      {/* Sidebar Search Filter */}
      <div className="p-3.5 border-b border-slate-800/60">
        <div className="relative">
          <Search className="absolute left-3 top-2.5 h-4 w-4 text-slate-500" />
          <input
            type="text"
            placeholder="Quick filter problems..."
            value={filterQuery}
            onChange={(e) => setFilterQuery(e.target.value)}
            className="w-full bg-slate-900/80 border border-slate-800 rounded-xl pl-9 pr-3 py-1.5 text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:border-emerald-500/50 focus:ring-1 focus:ring-emerald-500/50 transition-all"
          />
        </div>
      </div>

      {/* Collapsible Phases Navigation List */}
      <div className="flex-1 overflow-y-auto p-3 space-y-2">
        {phases.map((phase) => {
          const isExpanded = expandedPhases[phase.id] || filterQuery.trim().length > 0;
          
          // Filter problems inside phase if query present
          const matchingProblems = phase.problems.filter(p => 
            p.title.toLowerCase().includes(filterQuery.toLowerCase()) ||
            p.pattern.toLowerCase().includes(filterQuery.toLowerCase()) ||
            String(p.number).includes(filterQuery)
          );

          if (filterQuery.trim() && matchingProblems.length === 0) {
            return null; // Hide empty phase on search
          }

          const completedCount = phase.problems.filter(p => progress.completedIds.includes(p.id)).length;
          const percent = Math.round((completedCount / phase.problems.length) * 100) || 0;

          return (
            <div key={phase.id} className="rounded-xl border border-slate-800/60 bg-slate-900/40 overflow-hidden">
              {/* Phase Header */}
              <button
                onClick={() => togglePhase(phase.id)}
                className="w-full flex items-center justify-between p-3 text-left hover:bg-slate-800/40 transition-colors"
              >
                <div className="flex items-center gap-2.5 min-w-0">
                  <div className="h-6 w-6 rounded-lg bg-emerald-500/10 text-emerald-400 flex items-center justify-center text-xs font-bold shrink-0 border border-emerald-500/20">
                    P{phase.number}
                  </div>
                  <div className="truncate">
                    <h3 className="text-xs font-bold text-slate-200 truncate">
                      {phase.title}
                    </h3>
                    <p className="text-[10px] text-slate-500">
                      {completedCount}/{phase.problems.length} solved ({percent}%)
                    </p>
                  </div>
                </div>

                <div className="flex items-center gap-2 shrink-0">
                  <div className="w-12 bg-slate-800 h-1.5 rounded-full overflow-hidden">
                    <div 
                      className="bg-gradient-to-r from-emerald-500 to-teal-400 h-full transition-all duration-300"
                      style={{ width: `${percent}%` }}
                    />
                  </div>
                  {isExpanded ? (
                    <ChevronDown className="h-4 w-4 text-slate-400" />
                  ) : (
                    <ChevronRight className="h-4 w-4 text-slate-400" />
                  )}
                </div>
              </button>

              {/* Collapsible Problems Sub-list */}
              <AnimatePresence initial={false}>
                {isExpanded && (
                  <motion.div
                    initial={{ height: 0, opacity: 0 }}
                    animate={{ height: 'auto', opacity: 1 }}
                    exit={{ height: 0, opacity: 0 }}
                    transition={{ duration: 0.2 }}
                    className="border-t border-slate-800/40 divide-y divide-slate-800/30"
                  >
                    {(filterQuery.trim() ? matchingProblems : phase.problems).map((problem) => {
                      const isActive = pathname === `/problems/${problem.slug}`;
                      const isCompleted = progress.completedIds.includes(problem.id);
                      const isBookmarked = progress.bookmarkedIds.includes(problem.id);

                      return (
                        <div
                          key={problem.id}
                          className={`group flex items-center justify-between px-3 py-2 text-xs transition-colors ${
                            isActive 
                              ? 'bg-emerald-500/10 text-emerald-300 font-medium border-l-2 border-emerald-400' 
                              : 'text-slate-300 hover:bg-slate-800/50 hover:text-slate-100'
                          }`}
                        >
                          <Link 
                            href={`/problems/${problem.slug}`}
                            className="flex items-center gap-2.5 min-w-0 flex-1 py-0.5"
                          >
                            <span className="text-[10px] font-mono text-slate-500 shrink-0 w-7">
                              #{String(problem.number).padStart(3, '0')}
                            </span>

                            <span className="truncate flex-1">
                              {problem.title}
                            </span>

                            {isBookmarked && (
                              <Bookmark className="h-3 w-3 text-amber-400 fill-amber-400 shrink-0" />
                            )}

                            <span className={`text-[9px] px-1.5 py-0.5 rounded border shrink-0 font-medium ${getDifficultyColor(problem.difficulty)}`}>
                              {problem.difficulty}
                            </span>
                          </Link>

                          {/* Completion Toggle */}
                          <button
                            onClick={() => onToggleComplete && onToggleComplete(problem.id)}
                            className="ml-2 p-1 text-slate-500 hover:text-emerald-400 transition-colors shrink-0"
                            title={isCompleted ? 'Mark incomplete' : 'Mark complete'}
                          >
                            {isCompleted ? (
                              <CheckCircle2 className="h-4 w-4 text-emerald-400 fill-emerald-500/20" />
                            ) : (
                              <Circle className="h-4 w-4 text-slate-600 hover:text-slate-400" />
                            )}
                          </button>
                        </div>
                      );
                    })}
                  </motion.div>
                )}
              </AnimatePresence>
            </div>
          );
        })}
      </div>
    </aside>
  );
};
