'use client';

import React, { useState, useEffect } from 'react';
import Link from 'next/link';
import { 
  RotateCcw, 
  Eye, 
  Check, 
  Sparkles, 
  HelpCircle, 
  Zap, 
  ChevronRight, 
  BrainCircuit,
  ThumbsUp,
  Meh,
  Frown
} from 'lucide-react';
import { Phase, Problem, UserProgress } from '@/lib/types';
import { getStoredProgress, setRating, toggleRevision } from '@/lib/storage';
import { Header } from '@/components/layout/header';
import { CommandPalette } from '@/components/layout/command-palette';
import { MarkdownRenderer } from '@/components/problems/markdown-renderer';
import { motion, AnimatePresence } from 'framer-motion';

interface RevisionClientProps {
  initialPhases: Phase[];
  initialProblems: Problem[];
}

export const RevisionClient: React.FC<RevisionClientProps> = ({
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
  const [currentIndex, setCurrentIndex] = useState(0);

  // Progressive reveal steps
  const [revealPattern, setRevealPattern] = useState(false);
  const [revealIntuition, setRevealIntuition] = useState(false);
  const [revealSolution, setRevealSolution] = useState(false);

  useEffect(() => {
    setProgress(getStoredProgress());
  }, []);

  // Filter problems for revision queue (explicitly marked OR all 154)
  const revisionDeck = React.useMemo(() => {
    if (progress.revisionIds && progress.revisionIds.length > 0) {
      const explicit = initialProblems.filter(p => progress.revisionIds.includes(p.id));
      if (explicit.length > 0) return explicit;
    }
    return initialProblems;
  }, [progress.revisionIds, initialProblems]);

  const currentProblem = revisionDeck[currentIndex] || initialProblems[0];

  const resetReveals = () => {
    setRevealPattern(false);
    setRevealIntuition(false);
    setRevealSolution(false);
  };

  const handleNextProblem = () => {
    resetReveals();
    setCurrentIndex(prev => (prev + 1) % revisionDeck.length);
  };

  const handleRating = (rating: 'easy' | 'good' | 'hard') => {
    const updated = setRating(currentProblem.id, rating);
    setProgress(updated);
    handleNextProblem();
  };

  return (
    <div className="min-h-screen flex flex-col">
      <Header progress={progress} onOpenCommandPalette={() => setIsCommandPaletteOpen(true)} />

      <CommandPalette
        isOpen={isCommandPaletteOpen}
        onClose={() => setIsCommandPaletteOpen(false)}
        problems={initialProblems}
      />

      <div className="flex-1 max-w-4xl mx-auto w-full px-4 sm:px-6 py-8 space-y-6">
        {/* Revision Header Banner */}
        <div className="flex items-center justify-between border-b border-slate-800 pb-4">
          <div>
            <h1 className="text-2xl font-extrabold text-slate-100 flex items-center gap-2.5">
              <RotateCcw className="h-6 w-6 text-purple-400" />
              <span>Active Recall & Spaced Revision</span>
            </h1>
            <p className="text-xs text-slate-400 mt-1">
              Card {currentIndex + 1} of {revisionDeck.length} in study queue • Test your memory before revealing solutions
            </p>
          </div>

          <div className="text-xs font-mono font-bold bg-purple-500/10 text-purple-400 border border-purple-500/20 px-3 py-1 rounded-xl">
            {revisionDeck.length} In Stack
          </div>
        </div>

        {/* Main Revision Flashcard Workspace */}
        {currentProblem && (
          <div className="glass-panel rounded-3xl p-6 sm:p-8 border border-slate-800 space-y-6 shadow-2xl relative">
            {/* Card Metadata Bar */}
            <div className="flex items-center justify-between text-xs border-b border-slate-800/80 pb-4">
              <div className="flex items-center gap-2">
                <span className="font-mono font-bold text-slate-500 bg-slate-900 px-2 py-0.5 rounded border border-slate-800">
                  #{String(currentProblem.number).padStart(3, '0')}
                </span>
                <span className="text-slate-300 font-medium">
                  Phase {currentProblem.phaseNumber}: {currentProblem.phaseTitle}
                </span>
              </div>

              <span className={`text-xs px-2.5 py-0.5 rounded-full border font-bold ${
                currentProblem.difficulty === 'Easy' ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20' :
                currentProblem.difficulty === 'Medium' ? 'bg-amber-500/10 text-amber-400 border-amber-500/20' :
                'bg-rose-500/10 text-rose-400 border-rose-500/20'
              }`}>
                {currentProblem.difficulty}
              </span>
            </div>

            {/* Problem Title & Prompt */}
            <div className="space-y-3">
              <h2 className="text-2xl font-bold text-slate-100">
                {currentProblem.title}
              </h2>
              <div className="p-4 rounded-2xl bg-slate-950/80 border border-slate-800 text-xs text-slate-300 leading-relaxed">
                <MarkdownRenderer content={currentProblem.questionMd.slice(0, 500) + '...'} />
              </div>
            </div>

            {/* Progressive Reveal Triggers */}
            <div className="space-y-4 pt-2">
              {/* Pattern Hint Reveal */}
              {!revealPattern ? (
                <button
                  onClick={() => setRevealPattern(true)}
                  className="w-full p-3.5 rounded-2xl bg-slate-900 hover:bg-slate-800 border border-slate-800 hover:border-slate-700 text-slate-300 text-xs font-bold flex items-center justify-between transition-all"
                >
                  <div className="flex items-center gap-2">
                    <Sparkles className="h-4 w-4 text-emerald-400" />
                    <span>Reveal Pattern Hint</span>
                  </div>
                  <Eye className="h-4 w-4 text-slate-500" />
                </button>
              ) : (
                <motion.div
                  initial={{ opacity: 0, y: -5 }}
                  animate={{ opacity: 1, y: 0 }}
                  className="p-4 rounded-2xl bg-emerald-500/10 border border-emerald-500/30 text-xs"
                >
                  <span className="font-bold text-emerald-400 uppercase tracking-wider block text-[10px] mb-1">
                    Pattern & Approach
                  </span>
                  <p className="text-emerald-200 font-semibold text-sm">
                    {currentProblem.pattern}
                  </p>
                </motion.div>
              )}

              {/* Intuition Reveal */}
              {!revealIntuition ? (
                <button
                  onClick={() => { setRevealPattern(true); setRevealIntuition(true); }}
                  className="w-full p-3.5 rounded-2xl bg-slate-900 hover:bg-slate-800 border border-slate-800 hover:border-slate-700 text-slate-300 text-xs font-bold flex items-center justify-between transition-all"
                >
                  <div className="flex items-center gap-2">
                    <BrainCircuit className="h-4 w-4 text-purple-400" />
                    <span>Reveal Key Intuition</span>
                  </div>
                  <Eye className="h-4 w-4 text-slate-500" />
                </button>
              ) : (
                <motion.div
                  initial={{ opacity: 0, y: -5 }}
                  animate={{ opacity: 1, y: 0 }}
                  className="p-4 rounded-2xl bg-purple-500/10 border border-purple-500/30 text-xs text-purple-200 leading-relaxed"
                >
                  <span className="font-bold text-purple-400 uppercase tracking-wider block text-[10px] mb-1">
                    Intuition Summary
                  </span>
                  <p>{currentProblem.summary || 'Analyze choices at each step and reduce redundant subproblems.'}</p>
                </motion.div>
              )}

              {/* Complete Optimal C++ Solution Reveal */}
              {!revealSolution ? (
                <button
                  onClick={() => { setRevealPattern(true); setRevealIntuition(true); setRevealSolution(true); }}
                  className="w-full p-4 rounded-2xl bg-gradient-to-r from-emerald-500/20 to-teal-500/20 border border-emerald-500/40 text-emerald-300 text-xs font-extrabold flex items-center justify-between transition-all shadow-lg shadow-emerald-500/10"
                >
                  <div className="flex items-center gap-2">
                    <Zap className="h-4 w-4 text-emerald-400" />
                    <span>Reveal Full Optimal C++ Solution</span>
                  </div>
                  <Eye className="h-4 w-4 text-emerald-400" />
                </button>
              ) : (
                <motion.div
                  initial={{ opacity: 0, y: -5 }}
                  animate={{ opacity: 1, y: 0 }}
                  className="space-y-4"
                >
                  <div className="flex items-center justify-between text-xs">
                    <span className="text-slate-400 font-semibold">Optimal C++17 Solution</span>
                    <div className="flex items-center gap-3 font-mono text-[11px]">
                      <span className="text-amber-400">Time: {currentProblem.timeComplexity}</span>
                      <span className="text-teal-400">Space: {currentProblem.spaceComplexity}</span>
                    </div>
                  </div>
                  <MarkdownRenderer content={`\`\`\`cpp\n${currentProblem.optimalCode || '// Code snippet available in workspace'}\n\`\`\``} />
                </motion.div>
              )}
            </div>

            {/* Self Rating Spaced Repetition Buttons */}
            {revealSolution && (
              <motion.div
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                className="pt-4 border-t border-slate-800 space-y-3"
              >
                <div className="text-center text-xs font-bold text-slate-300">
                  How well did you recall this solution?
                </div>

                <div className="grid grid-cols-3 gap-3">
                  <button
                    onClick={() => handleRating('hard')}
                    className="p-3 rounded-2xl bg-rose-500/10 hover:bg-rose-500/20 border border-rose-500/30 text-rose-400 font-bold text-xs flex items-center justify-center gap-2 transition-all"
                  >
                    <Frown className="h-4 w-4" />
                    <span>Hard (Review Soon)</span>
                  </button>

                  <button
                    onClick={() => handleRating('good')}
                    className="p-3 rounded-2xl bg-amber-500/10 hover:bg-amber-500/20 border border-amber-500/30 text-amber-400 font-bold text-xs flex items-center justify-center gap-2 transition-all"
                  >
                    <Meh className="h-4 w-4" />
                    <span>Good (Next Week)</span>
                  </button>

                  <button
                    onClick={() => handleRating('easy')}
                    className="p-3 rounded-2xl bg-emerald-500/10 hover:bg-emerald-500/20 border border-emerald-500/30 text-emerald-400 font-bold text-xs flex items-center justify-center gap-2 transition-all"
                  >
                    <ThumbsUp className="h-4 w-4" />
                    <span>Easy (Mastered)</span>
                  </button>
                </div>
              </motion.div>
            )}
          </div>
        )}
      </div>
    </div>
  );
};
