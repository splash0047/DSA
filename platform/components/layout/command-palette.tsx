'use client';

import React, { useState, useEffect, useMemo } from 'react';
import { useRouter } from 'next/navigation';
import { Search, Code2, BookOpen, RotateCcw, Network, Sparkles, X, ChevronRight } from 'lucide-react';
import { Problem } from '@/lib/types';
import { motion, AnimatePresence } from 'framer-motion';

interface CommandPaletteProps {
  isOpen: boolean;
  onClose: () => void;
  problems: Problem[];
}

export const CommandPalette: React.FC<CommandPaletteProps> = ({ isOpen, onClose, problems }) => {
  const router = useRouter();
  const [query, setQuery] = useState('');
  const [selectedIndex, setSelectedIndex] = useState(0);

  // Filter problems based on query
  const filteredProblems = useMemo(() => {
    if (!query.trim()) return problems.slice(0, 8); // Top default problems
    const q = query.toLowerCase();
    return problems.filter(p => 
      p.title.toLowerCase().includes(q) ||
      p.pattern.toLowerCase().includes(q) ||
      p.phaseTitle.toLowerCase().includes(q) ||
      String(p.number).includes(q)
    ).slice(0, 15);
  }, [query, problems]);

  useEffect(() => {
    setSelectedIndex(0);
  }, [query]);

  // Global Ctrl+K / Cmd+K key listener
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        if (isOpen) {
          onClose();
        } else {
          // Trigger open logic
        }
      }
      if (e.key === 'Escape' && isOpen) {
        onClose();
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  const handleSelectProblem = (slug: string) => {
    onClose();
    router.push(`/problems/${slug}`);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      setSelectedIndex(prev => (prev + 1) % Math.max(1, filteredProblems.length));
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      setSelectedIndex(prev => (prev - 1 + filteredProblems.length) % Math.max(1, filteredProblems.length));
    } else if (e.key === 'Enter') {
      e.preventDefault();
      if (filteredProblems[selectedIndex]) {
        handleSelectProblem(filteredProblems[selectedIndex].slug);
      }
    }
  };

  const handleRandomProblem = () => {
    if (problems.length > 0) {
      const randomIdx = Math.floor(Math.random() * problems.length);
      handleSelectProblem(problems[randomIdx].slug);
    }
  };

  return (
    <AnimatePresence>
      {isOpen && (
        <div className="fixed inset-0 z-50 flex items-start justify-center pt-20 px-4 bg-slate-950/80 backdrop-blur-md">
          {/* Backdrop click to dismiss */}
          <div className="absolute inset-0" onClick={onClose} />

          <motion.div
            initial={{ opacity: 0, scale: 0.95, y: -10 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.95, y: -10 }}
            transition={{ duration: 0.15 }}
            className="relative w-full max-w-2xl bg-slate-900 border border-slate-800 rounded-2xl shadow-2xl overflow-hidden z-10"
          >
            {/* Search Input Bar */}
            <div className="flex items-center px-4 border-b border-slate-800 bg-slate-900/90">
              <Search className="h-5 w-5 text-emerald-400 mr-3" />
              <input
                type="text"
                autoFocus
                placeholder="Search by problem name, number (e.g. 129), or pattern (e.g. BFS)..."
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                onKeyDown={handleKeyDown}
                className="w-full bg-transparent py-4 text-sm text-slate-100 placeholder-slate-500 focus:outline-none"
              />
              <button 
                onClick={onClose}
                className="p-1 text-slate-500 hover:text-slate-300 rounded-lg"
              >
                <X className="h-5 w-5" />
              </button>
            </div>

            {/* Quick Actions Shortcuts */}
            <div className="px-4 py-2 bg-slate-950/50 border-b border-slate-800/60 flex items-center gap-2 overflow-x-auto text-xs">
              <button
                onClick={handleRandomProblem}
                className="flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 hover:bg-emerald-500/20 transition-all font-medium"
              >
                <Sparkles className="h-3.5 w-3.5" />
                Random Problem
              </button>

              <button
                onClick={() => { onClose(); router.push('/revision'); }}
                className="flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-purple-500/10 text-purple-400 border border-purple-500/20 hover:bg-purple-500/20 transition-all font-medium"
              >
                <RotateCcw className="h-3.5 w-3.5" />
                Spaced Revision
              </button>

              <button
                onClick={() => { onClose(); router.push('/patterns'); }}
                className="flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-blue-500/10 text-blue-400 border border-blue-500/20 hover:bg-blue-500/20 transition-all font-medium"
              >
                <Network className="h-3.5 w-3.5" />
                Pattern Map
              </button>
            </div>

            {/* Search Results List */}
            <div className="max-h-96 overflow-y-auto p-2 space-y-1">
              {filteredProblems.length === 0 ? (
                <div className="p-8 text-center text-slate-500 text-sm">
                  No matching problems found for "{query}".
                </div>
              ) : (
                filteredProblems.map((problem, idx) => {
                  const isSelected = idx === selectedIndex;
                  return (
                    <button
                      key={problem.id}
                      onClick={() => handleSelectProblem(problem.slug)}
                      onMouseEnter={() => setSelectedIndex(idx)}
                      className={`w-full flex items-center justify-between p-3 rounded-xl text-left transition-all ${
                        isSelected 
                          ? 'bg-slate-800 text-slate-100 border border-slate-700' 
                          : 'text-slate-300 hover:bg-slate-800/40'
                      }`}
                    >
                      <div className="flex items-center gap-3 min-w-0">
                        <span className="font-mono text-xs font-semibold text-slate-500 w-8">
                          #{String(problem.number).padStart(3, '0')}
                        </span>
                        <div className="truncate">
                          <div className="font-semibold text-sm truncate flex items-center gap-2">
                            <span>{problem.title}</span>
                            <span className="text-[10px] px-1.5 py-0.5 rounded bg-slate-800 text-slate-400 font-normal border border-slate-700">
                              {problem.pattern}
                            </span>
                          </div>
                          <p className="text-xs text-slate-500 truncate mt-0.5">
                            Phase {problem.phaseNumber}: {problem.phaseTitle}
                          </p>
                        </div>
                      </div>

                      <div className="flex items-center gap-2 shrink-0">
                        <span className={`text-[10px] px-2 py-0.5 rounded border font-semibold ${
                          problem.difficulty === 'Easy' ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20' :
                          problem.difficulty === 'Medium' ? 'bg-amber-500/10 text-amber-400 border-amber-500/20' :
                          'bg-rose-500/10 text-rose-400 border-rose-500/20'
                        }`}>
                          {problem.difficulty}
                        </span>
                        <ChevronRight className="h-4 w-4 text-slate-600" />
                      </div>
                    </button>
                  );
                })
              )}
            </div>

            {/* Command Palette Footer */}
            <div className="px-4 py-2.5 bg-slate-950 border-t border-slate-800/80 flex items-center justify-between text-[11px] text-slate-500">
              <div className="flex items-center gap-3">
                <span><kbd className="px-1 py-0.5 bg-slate-900 border border-slate-800 rounded">↑</kbd> <kbd className="px-1 py-0.5 bg-slate-900 border border-slate-800 rounded">↓</kbd> to navigate</span>
                <span><kbd className="px-1 py-0.5 bg-slate-900 border border-slate-800 rounded">↵</kbd> to select</span>
                <span><kbd className="px-1 py-0.5 bg-slate-900 border border-slate-800 rounded">ESC</kbd> to close</span>
              </div>
              <span>Showing {filteredProblems.length} of {problems.length} problems</span>
            </div>
          </motion.div>
        </div>
      )}
    </AnimatePresence>
  );
};
