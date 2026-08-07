'use client';

import React from 'react';
import Link from 'next/link';
import { ArrowRight, BookOpen, Clock, Sparkles, CheckCircle2 } from 'lucide-react';
import { Problem } from '@/lib/types';

interface ContinueCardProps {
  problem: Problem;
  isCompleted?: boolean;
}

export const ContinueCard: React.FC<ContinueCardProps> = ({ problem, isCompleted }) => {
  return (
    <div className="relative overflow-hidden rounded-2xl border border-emerald-500/20 bg-gradient-to-br from-slate-900 via-slate-900 to-emerald-950/30 p-6 shadow-xl">
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div className="space-y-2 max-w-xl">
          <div className="flex items-center gap-2 text-xs font-semibold text-emerald-400 uppercase tracking-wider">
            <Sparkles className="h-4 w-4" />
            <span>Continue Learning</span>
          </div>

          <h2 className="text-xl font-bold text-slate-100 flex items-center gap-2">
            <span>#{String(problem.number).padStart(3, '0')}</span>
            <span>{problem.title}</span>
          </h2>

          <p className="text-xs text-slate-400 line-clamp-2 leading-relaxed">
            {problem.summary || `Master the ${problem.pattern} pattern in Phase ${problem.phaseNumber}: ${problem.phaseTitle}.`}
          </p>

          <div className="flex flex-wrap items-center gap-2 pt-1">
            <span className="text-xs font-semibold px-2.5 py-0.5 rounded-md bg-slate-800 text-slate-300 border border-slate-700">
              Phase {problem.phaseNumber}: {problem.phaseTitle}
            </span>
            <span className="text-xs font-semibold px-2.5 py-0.5 rounded-md bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
              {problem.pattern}
            </span>
            <span className="text-xs text-slate-400 flex items-center gap-1 font-medium">
              <Clock className="h-3.5 w-3.5" />
              {problem.readingTimeMinutes} min read
            </span>
          </div>
        </div>

        <Link
          href={`/problems/${problem.slug}`}
          className="px-5 py-3 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-400 text-slate-950 font-bold flex items-center gap-2 hover:scale-105 transition-all shadow-lg shadow-emerald-500/20 shrink-0 text-sm"
        >
          <span>{isCompleted ? 'Review Solution' : 'Resume Problem'}</span>
          <ArrowRight className="h-4 w-4" />
        </Link>
      </div>
    </div>
  );
};
