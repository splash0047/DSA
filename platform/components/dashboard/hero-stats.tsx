'use client';

import React from 'react';
import { CheckCircle2, Flame, Trophy, Zap, Target, BookOpen } from 'lucide-react';
import { StatsOverview } from '@/lib/types';
import { motion } from 'framer-motion';

interface HeroStatsProps {
  stats: StatsOverview;
}

export const HeroStats: React.FC<HeroStatsProps> = ({ stats }) => {
  const percentTotal = Math.round((stats.completedProblems / stats.totalProblems) * 100) || 0;

  return (
    <div className="space-y-6">
      {/* Hero Welcome Banner */}
      <div className="relative overflow-hidden rounded-3xl border border-slate-800 bg-gradient-to-r from-slate-900 via-slate-900/90 to-emerald-950/40 p-6 sm:p-8 shadow-2xl">
        <div className="absolute top-0 right-0 -mt-8 -mr-8 w-64 h-64 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none" />
        <div className="absolute bottom-0 right-1/4 -mb-8 w-48 h-48 bg-teal-500/10 rounded-full blur-2xl pointer-events-none" />

        <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
          <div className="space-y-2 max-w-2xl">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs font-bold">
              <Zap className="h-3.5 w-3.5" />
              <span>Full Master Sheet — 154 Problems Across 11 Phases</span>
            </div>
            
            <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-slate-100">
              Welcome back to your <span className="bg-gradient-to-r from-emerald-400 via-teal-300 to-cyan-400 bg-clip-text text-transparent">DSA Vault</span>
            </h1>

            <p className="text-sm text-slate-400 leading-relaxed">
              Master Data Structures & Algorithms with structured patterns, C++17 optimal solutions, visual dry runs, and active recall revision.
            </p>
          </div>

          {/* Quick Streak Card */}
          <div className="flex items-center gap-4 bg-slate-950/80 border border-slate-800/80 p-4 rounded-2xl shrink-0 backdrop-blur-md">
            <div className="h-12 w-12 rounded-xl bg-amber-500/10 border border-amber-500/20 text-amber-400 flex items-center justify-center font-bold">
              <Flame className="h-6 w-6 fill-amber-400 text-amber-500" />
            </div>
            <div>
              <div className="text-2xl font-black text-slate-100">{stats.streak} Days</div>
              <div className="text-xs text-slate-400 font-medium">Active Study Streak</div>
            </div>
          </div>
        </div>
      </div>

      {/* Overview Stat Cards Grid */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        {/* Total Progress Card */}
        <div className="glass-card rounded-2xl p-5 border border-slate-800 flex flex-col justify-between">
          <div className="flex items-center justify-between text-slate-400">
            <span className="text-xs font-semibold uppercase tracking-wider">Overall Solved</span>
            <Trophy className="h-4 w-4 text-emerald-400" />
          </div>
          <div className="mt-3">
            <div className="text-2xl font-black text-slate-100">
              {stats.completedProblems} <span className="text-sm text-slate-500 font-normal">/ {stats.totalProblems}</span>
            </div>
            <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden mt-3">
              <div 
                className="bg-gradient-to-r from-emerald-500 to-teal-400 h-full rounded-full transition-all duration-500"
                style={{ width: `${percentTotal}%` }}
              />
            </div>
          </div>
          <div className="text-[11px] text-slate-400 mt-2 font-medium">
            {percentTotal}% Complete
          </div>
        </div>

        {/* Easy Breakdown */}
        <div className="glass-card rounded-2xl p-5 border border-slate-800 flex flex-col justify-between">
          <div className="flex items-center justify-between text-slate-400">
            <span className="text-xs font-semibold uppercase tracking-wider text-emerald-400">Easy</span>
            <CheckCircle2 className="h-4 w-4 text-emerald-400" />
          </div>
          <div className="mt-3">
            <div className="text-2xl font-black text-slate-100">
              {stats.easyCompleted} <span className="text-sm text-slate-500 font-normal">/ {stats.easyCount}</span>
            </div>
            <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden mt-3">
              <div 
                className="bg-emerald-500 h-full rounded-full transition-all duration-500"
                style={{ width: `${Math.round((stats.easyCompleted / (stats.easyCount || 1)) * 100)}%` }}
              />
            </div>
          </div>
          <div className="text-[11px] text-emerald-400/80 mt-2 font-medium">
            Foundation Mastery
          </div>
        </div>

        {/* Medium Breakdown */}
        <div className="glass-card rounded-2xl p-5 border border-slate-800 flex flex-col justify-between">
          <div className="flex items-center justify-between text-slate-400">
            <span className="text-xs font-semibold uppercase tracking-wider text-amber-400">Medium</span>
            <Target className="h-4 w-4 text-amber-400" />
          </div>
          <div className="mt-3">
            <div className="text-2xl font-black text-slate-100">
              {stats.mediumCompleted} <span className="text-sm text-slate-500 font-normal">/ {stats.mediumCount}</span>
            </div>
            <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden mt-3">
              <div 
                className="bg-amber-500 h-full rounded-full transition-all duration-500"
                style={{ width: `${Math.round((stats.mediumCompleted / (stats.mediumCount || 1)) * 100)}%` }}
              />
            </div>
          </div>
          <div className="text-[11px] text-amber-400/80 mt-2 font-medium">
            Core Interview Topics
          </div>
        </div>

        {/* Hard Breakdown */}
        <div className="glass-card rounded-2xl p-5 border border-slate-800 flex flex-col justify-between">
          <div className="flex items-center justify-between text-slate-400">
            <span className="text-xs font-semibold uppercase tracking-wider text-rose-400">Hard</span>
            <Zap className="h-4 w-4 text-rose-400" />
          </div>
          <div className="mt-3">
            <div className="text-2xl font-black text-slate-100">
              {stats.hardCompleted} <span className="text-sm text-slate-500 font-normal">/ {stats.hardCount}</span>
            </div>
            <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden mt-3">
              <div 
                className="bg-rose-500 h-full rounded-full transition-all duration-500"
                style={{ width: `${Math.round((stats.hardCompleted / (stats.hardCount || 1)) * 100)}%` }}
              />
            </div>
          </div>
          <div className="text-[11px] text-rose-400/80 mt-2 font-medium">
            Advanced Algorithms
          </div>
        </div>
      </div>
    </div>
  );
};
