'use client';

import React from 'react';
import { Search, Filter, LayoutGrid, List, CheckCircle2, Bookmark, RotateCcw } from 'lucide-react';
import { Difficulty, Phase } from '@/lib/types';

interface ProblemFiltersProps {
  searchQuery: string;
  onSearchChange: (query: string) => void;
  selectedPhase: string;
  onPhaseChange: (phase: string) => void;
  selectedDifficulty: string;
  onDifficultyChange: (diff: string) => void;
  selectedStatus: string;
  onStatusChange: (status: string) => void;
  viewMode: 'table' | 'grid';
  onViewModeChange: (mode: 'table' | 'grid') => void;
  phases: Phase[];
}

export const ProblemFilters: React.FC<ProblemFiltersProps> = ({
  searchQuery,
  onSearchChange,
  selectedPhase,
  onPhaseChange,
  selectedDifficulty,
  onDifficultyChange,
  selectedStatus,
  onStatusChange,
  viewMode,
  onViewModeChange,
  phases,
}) => {
  return (
    <div className="space-y-4 bg-slate-900/80 border border-slate-800 p-4 rounded-2xl backdrop-blur-md">
      <div className="flex flex-col md:flex-row items-center justify-between gap-3">
        {/* Search Bar */}
        <div className="relative flex-1 w-full">
          <Search className="absolute left-3.5 top-3 h-4 w-4 text-slate-500" />
          <input
            type="text"
            placeholder="Search 154 problems by title, pattern (e.g., Two Pointers, BFS, DP), or number..."
            value={searchQuery}
            onChange={(e) => onSearchChange(e.target.value)}
            className="w-full bg-slate-950 border border-slate-800 rounded-xl pl-10 pr-4 py-2.5 text-xs text-slate-100 placeholder-slate-500 focus:outline-none focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500"
          />
        </div>

        {/* View Mode Toggle */}
        <div className="flex items-center gap-1 bg-slate-950 border border-slate-800 p-1 rounded-xl shrink-0 self-end md:self-auto">
          <button
            onClick={() => onViewModeChange('table')}
            className={`p-2 rounded-lg text-xs font-medium transition-colors flex items-center gap-1.5 ${
              viewMode === 'table' ? 'bg-slate-800 text-emerald-400 font-bold' : 'text-slate-400 hover:text-slate-200'
            }`}
            title="Table View"
          >
            <List className="h-4 w-4" />
            <span className="hidden sm:inline">Table</span>
          </button>
          <button
            onClick={() => onViewModeChange('grid')}
            className={`p-2 rounded-lg text-xs font-medium transition-colors flex items-center gap-1.5 ${
              viewMode === 'grid' ? 'bg-slate-800 text-emerald-400 font-bold' : 'text-slate-400 hover:text-slate-200'
            }`}
            title="Grid View"
          >
            <LayoutGrid className="h-4 w-4" />
            <span className="hidden sm:inline">Grid</span>
          </button>
        </div>
      </div>

      {/* Filter Dropdowns Row */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        {/* Phase Select */}
        <select
          value={selectedPhase}
          onChange={(e) => onPhaseChange(e.target.value)}
          className="bg-slate-950 border border-slate-800 text-slate-300 rounded-xl px-3 py-2 focus:outline-none focus:border-emerald-500"
        >
          <option value="all">All Phases (00 - 10)</option>
          {phases.map((p) => (
            <option key={p.id} value={String(p.number)}>
              Phase {p.number}: {p.title}
            </option>
          ))}
        </select>

        {/* Difficulty Select */}
        <select
          value={selectedDifficulty}
          onChange={(e) => onDifficultyChange(e.target.value)}
          className="bg-slate-950 border border-slate-800 text-slate-300 rounded-xl px-3 py-2 focus:outline-none focus:border-emerald-500"
        >
          <option value="all">All Difficulties</option>
          <option value="Easy">Easy</option>
          <option value="Medium">Medium</option>
          <option value="Hard">Hard</option>
        </select>

        {/* Status Select */}
        <select
          value={selectedStatus}
          onChange={(e) => onStatusChange(e.target.value)}
          className="bg-slate-950 border border-slate-800 text-slate-300 rounded-xl px-3 py-2 focus:outline-none focus:border-emerald-500"
        >
          <option value="all">All Statuses</option>
          <option value="completed">Solved ✓</option>
          <option value="unsolved">Unsolved</option>
          <option value="bookmarked">Bookmarked ★</option>
          <option value="revision">Marked for Revision 🔄</option>
        </select>

        {/* Reset Filters */}
        <button
          onClick={() => {
            onSearchChange('');
            onPhaseChange('all');
            onDifficultyChange('all');
            onStatusChange('all');
          }}
          className="bg-slate-950 border border-slate-800 text-slate-400 hover:text-slate-200 rounded-xl px-3 py-2 font-medium text-center transition-colors hover:bg-slate-900"
        >
          Reset Filters
        </button>
      </div>
    </div>
  );
};
