'use client';

import React from 'react';
import Link from 'next/link';
import { 
  CheckCircle2, 
  Circle, 
  Bookmark, 
  RotateCcw, 
  Clock, 
  ExternalLink, 
  ArrowUpRight,
  Code2
} from 'lucide-react';
import { Problem, UserProgress } from '@/lib/types';

interface ProblemTableProps {
  problems: Problem[];
  progress: UserProgress;
  viewMode: 'table' | 'grid';
  onToggleComplete: (id: string) => void;
  onToggleBookmark: (id: string) => void;
  onToggleRevision: (id: string) => void;
}

export const ProblemTable: React.FC<ProblemTableProps> = ({
  problems,
  progress,
  viewMode,
  onToggleComplete,
  onToggleBookmark,
  onToggleRevision,
}) => {
  const getDifficultyBadge = (diff: string) => {
    switch (diff) {
      case 'Easy':
        return 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20';
      case 'Medium':
        return 'bg-amber-500/10 text-amber-400 border-amber-500/20';
      case 'Hard':
        return 'bg-rose-500/10 text-rose-400 border-rose-500/20';
      default:
        return 'bg-slate-800 text-slate-400 border-slate-700';
    }
  };

  if (problems.length === 0) {
    return (
      <div className="p-12 text-center border border-slate-800 rounded-2xl bg-slate-900/40 space-y-3">
        <Code2 className="h-10 w-10 text-slate-600 mx-auto" />
        <h3 className="text-base font-bold text-slate-200">No matching problems</h3>
        <p className="text-xs text-slate-500">Try adjusting your filters or search query.</p>
      </div>
    );
  }

  if (viewMode === 'grid') {
    return (
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {problems.map((problem) => {
          const isCompleted = progress.completedIds.includes(problem.id);
          const isBookmarked = progress.bookmarkedIds.includes(problem.id);
          const isRevision = progress.revisionIds.includes(problem.id);

          return (
            <div
              key={problem.id}
              className="glass-card rounded-2xl p-5 border border-slate-800 flex flex-col justify-between space-y-4 hover:border-slate-700 transition-all"
            >
              <div>
                <div className="flex items-center justify-between gap-2">
                  <span className="font-mono text-xs text-slate-500 font-bold">
                    #{String(problem.number).padStart(3, '0')}
                  </span>
                  <div className="flex items-center gap-1.5">
                    <span className={`text-[10px] px-2 py-0.5 rounded border font-semibold ${getDifficultyBadge(problem.difficulty)}`}>
                      {problem.difficulty}
                    </span>
                    <button
                      onClick={() => onToggleBookmark(problem.id)}
                      className="p-1 text-slate-500 hover:text-amber-400 transition-colors"
                      title={isBookmarked ? 'Remove bookmark' : 'Bookmark problem'}
                    >
                      <Bookmark className={`h-4 w-4 ${isBookmarked ? 'text-amber-400 fill-amber-400' : ''}`} />
                    </button>
                  </div>
                </div>

                <Link href={`/problems/${problem.slug}`} className="block mt-2 group">
                  <h3 className="text-base font-bold text-slate-100 group-hover:text-emerald-300 transition-colors line-clamp-1">
                    {problem.title}
                  </h3>
                </Link>

                <div className="flex flex-wrap items-center gap-1.5 mt-2">
                  <span className="text-[10px] px-2 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700 font-medium">
                    {problem.pattern}
                  </span>
                  <span className="text-[10px] text-slate-400 flex items-center gap-1">
                    <Clock className="h-3 w-3" />
                    {problem.readingTimeMinutes}m
                  </span>
                </div>
              </div>

              <div className="pt-3 border-t border-slate-800/60 flex items-center justify-between text-xs">
                <span className="text-slate-400 text-[11px] font-medium truncate max-w-[150px]">
                  Phase {problem.phaseNumber}: {problem.phaseTitle}
                </span>

                <div className="flex items-center gap-2">
                  <button
                    onClick={() => onToggleRevision(problem.id)}
                    className={`p-1.5 rounded-lg border transition-colors ${
                      isRevision 
                        ? 'bg-purple-500/10 text-purple-400 border-purple-500/30' 
                        : 'bg-slate-900 border-slate-800 text-slate-500 hover:text-purple-400'
                    }`}
                    title="Toggle revision mark"
                  >
                    <RotateCcw className="h-3.5 w-3.5" />
                  </button>

                  <button
                    onClick={() => onToggleComplete(problem.id)}
                    className={`p-1.5 rounded-lg border transition-colors flex items-center gap-1 font-semibold text-[11px] ${
                      isCompleted 
                        ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30' 
                        : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-slate-200'
                    }`}
                  >
                    {isCompleted ? (
                      <>
                        <CheckCircle2 className="h-3.5 w-3.5 text-emerald-400" />
                        <span>Solved</span>
                      </>
                    ) : (
                      <>
                        <Circle className="h-3.5 w-3.5" />
                        <span>Solve</span>
                      </>
                    )}
                  </button>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    );
  }

  // Table View
  return (
    <div className="overflow-hidden rounded-2xl border border-slate-800 bg-slate-900/60 backdrop-blur-md shadow-xl">
      <div className="overflow-x-auto">
        <table className="w-full text-left text-xs">
          <thead className="bg-slate-950/80 text-slate-400 font-semibold border-b border-slate-800 uppercase tracking-wider text-[10px]">
            <tr>
              <th className="py-3 px-4 w-12 text-center">Status</th>
              <th className="py-3 px-4 w-16">#</th>
              <th className="py-3 px-4">Title</th>
              <th className="py-3 px-4">Phase</th>
              <th className="py-3 px-4">Pattern</th>
              <th className="py-3 px-4 w-24">Difficulty</th>
              <th className="py-3 px-4 w-28 text-right">Actions</th>
            </tr>
          </thead>

          <tbody className="divide-y divide-slate-800/60 text-slate-300">
            {problems.map((problem) => {
              const isCompleted = progress.completedIds.includes(problem.id);
              const isBookmarked = progress.bookmarkedIds.includes(problem.id);
              const isRevision = progress.revisionIds.includes(problem.id);

              return (
                <tr key={problem.id} className="hover:bg-slate-800/40 transition-colors group">
                  {/* Status Checkbox */}
                  <td className="py-3 px-4 text-center">
                    <button
                      onClick={() => onToggleComplete(problem.id)}
                      className="text-slate-500 hover:text-emerald-400 transition-colors"
                      title={isCompleted ? 'Mark unsolved' : 'Mark solved'}
                    >
                      {isCompleted ? (
                        <CheckCircle2 className="h-4 w-4 text-emerald-400 fill-emerald-500/20" />
                      ) : (
                        <Circle className="h-4 w-4 text-slate-600 hover:text-slate-400" />
                      )}
                    </button>
                  </td>

                  {/* Problem Number */}
                  <td className="py-3 px-4 font-mono text-slate-500 font-bold">
                    #{String(problem.number).padStart(3, '0')}
                  </td>

                  {/* Problem Title & Link */}
                  <td className="py-3 px-4 font-bold text-slate-100">
                    <Link
                      href={`/problems/${problem.slug}`}
                      className="hover:text-emerald-300 transition-colors flex items-center gap-2"
                    >
                      <span>{problem.title}</span>
                      {problem.url && (
                        <ArrowUpRight className="h-3 w-3 text-slate-600 group-hover:text-emerald-400" />
                      )}
                    </Link>
                  </td>

                  {/* Phase Title */}
                  <td className="py-3 px-4 text-slate-400 font-medium">
                    Phase {problem.phaseNumber}: {problem.phaseTitle}
                  </td>

                  {/* Pattern Badge */}
                  <td className="py-3 px-4">
                    <span className="px-2 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700 font-medium text-[10px]">
                      {problem.pattern}
                    </span>
                  </td>

                  {/* Difficulty */}
                  <td className="py-3 px-4">
                    <span className={`px-2 py-0.5 rounded border font-semibold text-[10px] ${getDifficultyBadge(problem.difficulty)}`}>
                      {problem.difficulty}
                    </span>
                  </td>

                  {/* Actions (Bookmark & Revision) */}
                  <td className="py-3 px-4 text-right">
                    <div className="flex items-center justify-end gap-1">
                      <button
                        onClick={() => onToggleRevision(problem.id)}
                        className={`p-1.5 rounded-lg border transition-colors ${
                          isRevision 
                            ? 'bg-purple-500/10 text-purple-400 border-purple-500/30' 
                            : 'text-slate-500 hover:text-purple-400 border-transparent hover:border-slate-700'
                        }`}
                        title="Mark for Spaced Revision"
                      >
                        <RotateCcw className="h-3.5 w-3.5" />
                      </button>

                      <button
                        onClick={() => onToggleBookmark(problem.id)}
                        className={`p-1.5 rounded-lg border transition-colors ${
                          isBookmarked 
                            ? 'bg-amber-500/10 text-amber-400 border-amber-500/30' 
                            : 'text-slate-500 hover:text-amber-400 border-transparent hover:border-slate-700'
                        }`}
                        title="Bookmark"
                      >
                        <Bookmark className={`h-3.5 w-3.5 ${isBookmarked ? 'fill-amber-400' : ''}`} />
                      </button>
                    </div>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
};
