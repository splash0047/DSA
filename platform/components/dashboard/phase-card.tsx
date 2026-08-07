'use client';

import React from 'react';
import Link from 'next/link';
import { ChevronRight, Folder, CheckCircle2, Layers } from 'lucide-react';
import { Phase, UserProgress } from '@/lib/types';

interface PhaseCardProps {
  phase: Phase;
  progress: UserProgress;
}

export const PhaseCard: React.FC<PhaseCardProps> = ({ phase, progress }) => {
  const completedCount = phase.problems.filter(p => progress.completedIds.includes(p.id)).length;
  const percent = Math.round((completedCount / phase.problems.length) * 100) || 0;

  return (
    <Link
      href={`/problems?phase=${phase.number}`}
      className="group glass-card rounded-2xl p-5 border border-slate-800 hover:border-emerald-500/40 transition-all flex flex-col justify-between"
    >
      <div>
        <div className="flex items-center justify-between">
          <div className="h-8 w-8 rounded-xl bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 flex items-center justify-center font-bold text-xs">
            P{String(phase.number).padStart(2, '0')}
          </div>
          <span className="text-xs font-mono text-slate-500 font-semibold">
            {phase.problemCount} Problems
          </span>
        </div>

        <h3 className="text-base font-bold text-slate-100 mt-3 group-hover:text-emerald-300 transition-colors">
          {phase.title}
        </h3>

        <div className="flex items-center justify-between text-xs text-slate-400 mt-2">
          <span>Progress</span>
          <span className="font-semibold text-slate-200">{completedCount} / {phase.problemCount} ({percent}%)</span>
        </div>

        {/* Progress Bar */}
        <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden mt-2">
          <div 
            className="bg-gradient-to-r from-emerald-500 to-teal-400 h-full rounded-full transition-all duration-500"
            style={{ width: `${percent}%` }}
          />
        </div>
      </div>

      <div className="flex items-center justify-between text-xs font-semibold text-emerald-400 mt-4 pt-3 border-t border-slate-800/60">
        <span>Explore Phase</span>
        <ChevronRight className="h-4 w-4 group-hover:translate-x-1 transition-transform" />
      </div>
    </Link>
  );
};
