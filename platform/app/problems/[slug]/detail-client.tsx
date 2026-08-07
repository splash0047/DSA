'use client';

import React, { useState, useEffect } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { 
  CheckCircle2, 
  Circle, 
  Bookmark, 
  RotateCcw, 
  Clock, 
  ExternalLink, 
  Sparkles,
  ChevronLeft,
  ChevronRight,
  Code2,
  BookOpen,
  Zap,
  HelpCircle,
  FileText,
  Layers,
  Save,
  Check
} from 'lucide-react';
import { Problem, Phase, UserProgress } from '@/lib/types';
import { 
  getStoredProgress, 
  toggleCompleted, 
  toggleBookmarked, 
  toggleRevision, 
  saveUserNote, 
  addRecentlyViewed 
} from '@/lib/storage';
import { Header } from '@/components/layout/header';
import { Sidebar } from '@/components/layout/sidebar';
import { CommandPalette } from '@/components/layout/command-palette';
import { CodeBlock } from '@/components/problems/code-block';
import { MarkdownRenderer } from '@/components/problems/markdown-renderer';
import { AiDrawer } from '@/components/problems/ai-drawer';
import { DryRunVisualizer } from '@/components/problems/dry-run-visualizer';
import confetti from 'canvas-confetti';

interface ProblemDetailClientProps {
  problem: Problem;
  allPhases: Phase[];
  allProblems: Problem[];
}

export const ProblemDetailClient: React.FC<ProblemDetailClientProps> = ({
  problem,
  allPhases,
  allProblems,
}) => {
  const router = useRouter();
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

  const [activeTab, setActiveTab] = useState<'question' | 'brute' | 'optimal' | 'explanation' | 'notes' | 'visualizer'>('optimal');
  const [isCommandPaletteOpen, setIsCommandPaletteOpen] = useState(false);
  const [isAiDrawerOpen, setIsAiDrawerOpen] = useState(false);
  const [userNote, setUserNote] = useState('');
  const [noteSaved, setNoteSaved] = useState(false);

  useEffect(() => {
    const p = getStoredProgress();
    setProgress(p);
    setUserNote(p.notes[problem.id] || '');
    addRecentlyViewed(problem.id);
  }, [problem.id]);

  const isCompleted = progress.completedIds.includes(problem.id);
  const isBookmarked = progress.bookmarkedIds.includes(problem.id);
  const isRevision = progress.revisionIds.includes(problem.id);

  const handleToggleComplete = () => {
    const updated = toggleCompleted(problem.id);
    setProgress(updated);
    if (!isCompleted) {
      confetti({
        particleCount: 80,
        spread: 60,
        origin: { y: 0.6 },
      });
    }
  };

  const handleToggleBookmark = () => {
    const updated = toggleBookmarked(problem.id);
    setProgress(updated);
  };

  const handleToggleRevision = () => {
    const updated = toggleRevision(problem.id);
    setProgress(updated);
  };

  const handleSaveNote = () => {
    const updated = saveUserNote(problem.id, userNote);
    setProgress(updated);
    setNoteSaved(true);
    setTimeout(() => setNoteSaved(false), 2000);
  };

  // Find Prev / Next Problems in curriculum
  const currentIndex = allProblems.findIndex(p => p.id === problem.id);
  const prevProblem = currentIndex > 0 ? allProblems[currentIndex - 1] : null;
  const nextProblem = currentIndex < allProblems.length - 1 ? allProblems[currentIndex + 1] : null;

  return (
    <div className="min-h-screen flex flex-col">
      <Header progress={progress} onOpenCommandPalette={() => setIsCommandPaletteOpen(true)} />

      <CommandPalette
        isOpen={isCommandPaletteOpen}
        onClose={() => setIsCommandPaletteOpen(false)}
        problems={allProblems}
      />

      <AiDrawer
        isOpen={isAiDrawerOpen}
        onClose={() => setIsAiDrawerOpen(false)}
        problem={problem}
      />

      <div className="flex-1 flex">
        {/* Sidebar */}
        <div className="hidden lg:block">
          <Sidebar 
            phases={allPhases} 
            progress={progress} 
            onToggleComplete={(id) => setProgress(toggleCompleted(id))} 
          />
        </div>

        {/* Workspace Container */}
        <div className="flex-1 max-w-6xl mx-auto w-full p-4 sm:p-6 md:p-8 space-y-6">
          {/* Top Breadcrumb & Next/Prev Navigation */}
          <div className="flex items-center justify-between text-xs text-slate-400">
            <div className="flex items-center gap-2">
              <Link href="/problems" className="hover:text-emerald-400 transition-colors">
                Problems
              </Link>
              <span>/</span>
              <span className="text-slate-300">Phase {problem.phaseNumber}: {problem.phaseTitle}</span>
              <span>/</span>
              <span className="text-emerald-400 font-mono font-bold">
                #{String(problem.number).padStart(3, '0')}
              </span>
            </div>

            <div className="flex items-center gap-2">
              {prevProblem && (
                <Link
                  href={`/problems/${prevProblem.slug}`}
                  className="flex items-center gap-1 px-2.5 py-1 rounded-lg bg-slate-900 border border-slate-800 hover:border-slate-700 text-slate-300 transition-colors"
                >
                  <ChevronLeft className="h-3.5 w-3.5" />
                  <span>Prev</span>
                </Link>
              )}

              {nextProblem && (
                <Link
                  href={`/problems/${nextProblem.slug}`}
                  className="flex items-center gap-1 px-2.5 py-1 rounded-lg bg-slate-900 border border-slate-800 hover:border-slate-700 text-slate-300 transition-colors"
                >
                  <span>Next</span>
                  <ChevronRight className="h-3.5 w-3.5" />
                </Link>
              )}
            </div>
          </div>

          {/* Sticky Workspace Header Banner */}
          <div className="glass-panel rounded-2xl p-5 sm:p-6 border border-slate-800 space-y-4">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
              <div className="space-y-2">
                <div className="flex flex-wrap items-center gap-2">
                  <span className="font-mono text-xs font-bold text-slate-500 bg-slate-900 px-2 py-0.5 rounded border border-slate-800">
                    #{String(problem.number).padStart(3, '0')}
                  </span>
                  
                  <span className={`text-xs px-2.5 py-0.5 rounded-full border font-bold ${
                    problem.difficulty === 'Easy' ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20' :
                    problem.difficulty === 'Medium' ? 'bg-amber-500/10 text-amber-400 border-amber-500/20' :
                    'bg-rose-500/10 text-rose-400 border-rose-500/20'
                  }`}>
                    {problem.difficulty}
                  </span>

                  <span className="text-xs px-2.5 py-0.5 rounded-full bg-slate-800 text-slate-300 border border-slate-700 font-medium">
                    {problem.pattern}
                  </span>

                  {problem.platformProblemNumber && (
                    <span className="text-xs font-semibold text-slate-400 flex items-center gap-1">
                      {problem.platform} {problem.platformProblemNumber}
                    </span>
                  )}
                </div>

                <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-100 tracking-tight">
                  {problem.title}
                </h1>
              </div>

              {/* Action Buttons Header */}
              <div className="flex items-center gap-2 shrink-0">
                <button
                  onClick={() => setIsAiDrawerOpen(true)}
                  className="px-3.5 py-2 rounded-xl bg-purple-500/10 text-purple-400 border border-purple-500/30 hover:bg-purple-500/20 transition-all font-bold text-xs flex items-center gap-1.5"
                >
                  <Sparkles className="h-4 w-4" />
                  <span>AI Tutor</span>
                </button>

                <button
                  onClick={handleToggleRevision}
                  className={`p-2 rounded-xl border transition-colors ${
                    isRevision
                      ? 'bg-purple-500/10 text-purple-400 border-purple-500/30'
                      : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-purple-400'
                  }`}
                  title="Mark for revision"
                >
                  <RotateCcw className="h-4 w-4" />
                </button>

                <button
                  onClick={handleToggleBookmark}
                  className={`p-2 rounded-xl border transition-colors ${
                    isBookmarked
                      ? 'bg-amber-500/10 text-amber-400 border-amber-500/30'
                      : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-amber-400'
                  }`}
                  title="Bookmark problem"
                >
                  <Bookmark className={`h-4 w-4 ${isBookmarked ? 'fill-amber-400' : ''}`} />
                </button>

                <button
                  onClick={handleToggleComplete}
                  className={`px-4 py-2 rounded-xl border font-bold text-xs transition-all flex items-center gap-2 ${
                    isCompleted
                      ? 'bg-emerald-500 text-slate-950 border-emerald-400 shadow-lg shadow-emerald-500/20'
                      : 'bg-slate-900 text-slate-200 border-slate-800 hover:border-emerald-500/50'
                  }`}
                >
                  {isCompleted ? (
                    <>
                      <CheckCircle2 className="h-4 w-4 fill-slate-950 text-emerald-400" />
                      <span>Completed</span>
                    </>
                  ) : (
                    <>
                      <Circle className="h-4 w-4" />
                      <span>Mark Complete</span>
                    </>
                  )}
                </button>
              </div>
            </div>

            {/* Quick Metadata Bar */}
            <div className="flex flex-wrap items-center justify-between gap-4 pt-3 border-t border-slate-800/60 text-xs text-slate-400 font-medium">
              <div className="flex items-center gap-4">
                <span>Time: <strong className="text-amber-400 font-mono">{problem.timeComplexity}</strong></span>
                <span>Space: <strong className="text-teal-400 font-mono">{problem.spaceComplexity}</strong></span>
                <span className="flex items-center gap-1">
                  <Clock className="h-3.5 w-3.5" />
                  {problem.readingTimeMinutes} min read
                </span>
              </div>

              {problem.url && (
                <a
                  href={problem.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-emerald-400 hover:text-emerald-300 flex items-center gap-1 font-semibold"
                >
                  <span>View on {problem.platform || 'LeetCode'}</span>
                  <ExternalLink className="h-3.5 w-3.5" />
                </a>
              )}
            </div>
          </div>

          {/* Navigation Tabs Bar */}
          <div className="flex items-center gap-1 bg-slate-900/80 border border-slate-800 p-1.5 rounded-2xl overflow-x-auto">
            <button
              onClick={() => setActiveTab('optimal')}
              className={`px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-2 shrink-0 ${
                activeTab === 'optimal'
                  ? 'bg-gradient-to-r from-emerald-500 to-teal-400 text-slate-950 shadow-md'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/50'
              }`}
            >
              <Zap className="h-3.5 w-3.5" />
              <span>Optimal Approach</span>
            </button>

            <button
              onClick={() => setActiveTab('question')}
              className={`px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-2 shrink-0 ${
                activeTab === 'question'
                  ? 'bg-slate-800 text-emerald-400 shadow-md'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/50'
              }`}
            >
              <FileText className="h-3.5 w-3.5" />
              <span>Question Statement</span>
            </button>

            <button
              onClick={() => setActiveTab('brute')}
              className={`px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-2 shrink-0 ${
                activeTab === 'brute'
                  ? 'bg-slate-800 text-emerald-400 shadow-md'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/50'
              }`}
            >
              <Code2 className="h-3.5 w-3.5" />
              <span>Brute Force</span>
            </button>

            <button
              onClick={() => setActiveTab('explanation')}
              className={`px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-2 shrink-0 ${
                activeTab === 'explanation'
                  ? 'bg-slate-800 text-emerald-400 shadow-md'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/50'
              }`}
            >
              <BookOpen className="h-3.5 w-3.5" />
              <span>Deep Dive & Revision</span>
            </button>

            <button
              onClick={() => setActiveTab('visualizer')}
              className={`px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-2 shrink-0 ${
                activeTab === 'visualizer'
                  ? 'bg-slate-800 text-teal-300 shadow-md'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/50'
              }`}
            >
              <Layers className="h-3.5 w-3.5" />
              <span>Dry Run Visualizer</span>
            </button>

            <button
              onClick={() => setActiveTab('notes')}
              className={`px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-2 shrink-0 ${
                activeTab === 'notes'
                  ? 'bg-slate-800 text-purple-400 shadow-md'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/50'
              }`}
            >
              <FileText className="h-3.5 w-3.5" />
              <span>My Personal Notes</span>
            </button>
          </div>

          {/* Active Tab Panel Output */}
          <div className="glass-panel rounded-2xl p-6 border border-slate-800 space-y-6">
            {activeTab === 'optimal' && (
              <div className="space-y-6">
                <MarkdownRenderer content={problem.optimalMd} />
              </div>
            )}

            {activeTab === 'question' && (
              <div className="space-y-6">
                <MarkdownRenderer content={problem.questionMd} />
              </div>
            )}

            {activeTab === 'brute' && (
              <div className="space-y-6">
                <MarkdownRenderer content={problem.bruteForceMd} />
              </div>
            )}

            {activeTab === 'explanation' && (
              <div className="space-y-6">
                <MarkdownRenderer content={problem.explanationMd} />
              </div>
            )}

            {activeTab === 'visualizer' && (
              <DryRunVisualizer problem={problem} />
            )}

            {activeTab === 'notes' && (
              <div className="space-y-4">
                <div className="flex items-center justify-between">
                  <h3 className="text-sm font-bold text-slate-100 flex items-center gap-2">
                    <FileText className="h-4 w-4 text-purple-400" />
                    <span>Personal Notes for {problem.title}</span>
                  </h3>

                  <button
                    onClick={handleSaveNote}
                    className="px-3.5 py-1.5 rounded-xl bg-purple-500 text-slate-950 font-bold text-xs flex items-center gap-1.5 hover:bg-purple-400 transition-colors"
                  >
                    {noteSaved ? (
                      <>
                        <Check className="h-3.5 w-3.5" /> Saved!
                      </>
                    ) : (
                      <>
                        <Save className="h-3.5 w-3.5" /> Save Note
                      </>
                    )}
                  </button>
                </div>

                <textarea
                  rows={10}
                  value={userNote}
                  onChange={(e) => setUserNote(e.target.value)}
                  placeholder="Write your personal study notes, edge case reminders, or interview insights here (automatically saved)..."
                  className="w-full bg-slate-950 border border-slate-800 rounded-xl p-4 text-xs font-mono text-slate-200 placeholder-slate-500 focus:outline-none focus:border-purple-500 focus:ring-1 focus:ring-purple-500 leading-relaxed"
                />
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};
