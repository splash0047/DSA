'use client';

import React, { useState, useEffect } from 'react';
import { Play, Pause, SkipBack, SkipForward, RotateCcw, Sliders, Layers, CheckCircle } from 'lucide-react';
import { Problem } from '@/lib/types';

interface DryRunVisualizerProps {
  problem: Problem;
}

export const DryRunVisualizer: React.FC<DryRunVisualizerProps> = ({ problem }) => {
  const [currentStep, setCurrentStep] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [speed, setSpeed] = useState(1000);

  // Generate dynamic simulation steps based on pattern
  const steps = [
    {
      step: 1,
      title: 'Initialize State',
      description: `Setup initial variables and structures for ${problem.pattern}.`,
      state: { index: 0, status: 'Initializing', activeElement: 'Start' },
    },
    {
      step: 2,
      title: 'Evaluate Condition',
      description: `Check algorithm invariant for current element/node.`,
      state: { index: 1, status: 'Scanning', activeElement: 'In Range' },
    },
    {
      step: 3,
      title: 'State Transition',
      description: `Update optimal memory / pointers according to ${problem.pattern} logic.`,
      state: { index: 2, status: 'Updating', activeElement: 'Optimal Decision' },
    },
    {
      step: 4,
      title: 'Final Optimal Convergence',
      description: `Algorithm completes in ${problem.timeComplexity} time with total ${problem.spaceComplexity} auxiliary space.`,
      state: { index: 3, status: 'Complete', activeElement: 'Result Verified' },
    },
  ];

  useEffect(() => {
    let timer: any;
    if (isPlaying) {
      timer = setInterval(() => {
        setCurrentStep((prev) => {
          if (prev >= steps.length - 1) {
            setIsPlaying(false);
            return prev;
          }
          return prev + 1;
        });
      }, speed);
    }
    return () => clearInterval(timer);
  }, [isPlaying, speed, steps.length]);

  const active = steps[currentStep];

  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-950 p-5 space-y-5 my-4 shadow-xl">
      {/* Visualizer Header Controls */}
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 border-b border-slate-800/80 pb-4">
        <div>
          <div className="flex items-center gap-2">
            <Layers className="h-5 w-5 text-emerald-400" />
            <h3 className="text-sm font-bold text-slate-100">
              Interactive Dry Run Visualizer
            </h3>
            <span className="text-[10px] uppercase font-mono px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 font-bold">
              {problem.pattern}
            </span>
          </div>
          <p className="text-xs text-slate-400 mt-1">
            Step-by-step state transition simulator for {problem.title}
          </p>
        </div>

        {/* Step Controls & Playback */}
        <div className="flex items-center gap-2 self-stretch sm:self-auto justify-end">
          <button
            onClick={() => setCurrentStep(0)}
            className="p-2 rounded-xl bg-slate-900 border border-slate-800 text-slate-400 hover:text-slate-200"
            title="Reset"
          >
            <RotateCcw className="h-4 w-4" />
          </button>
          
          <button
            onClick={() => setCurrentStep(prev => Math.max(0, prev - 1))}
            disabled={currentStep === 0}
            className="p-2 rounded-xl bg-slate-900 border border-slate-800 text-slate-400 hover:text-slate-200 disabled:opacity-40"
            title="Step Back"
          >
            <SkipBack className="h-4 w-4" />
          </button>

          <button
            onClick={() => setIsPlaying(!isPlaying)}
            className="px-3 py-2 rounded-xl bg-emerald-500 text-slate-950 font-bold flex items-center gap-1.5 hover:bg-emerald-400 transition-colors text-xs"
          >
            {isPlaying ? (
              <>
                <Pause className="h-4 w-4" /> Pause
              </>
            ) : (
              <>
                <Play className="h-4 w-4 fill-slate-950" /> Play
              </>
            )}
          </button>

          <button
            onClick={() => setCurrentStep(prev => Math.min(steps.length - 1, prev + 1))}
            disabled={currentStep === steps.length - 1}
            className="p-2 rounded-xl bg-slate-900 border border-slate-800 text-slate-400 hover:text-slate-200 disabled:opacity-40"
            title="Step Forward"
          >
            <SkipForward className="h-4 w-4" />
          </button>
        </div>
      </div>

      {/* Progress Stepper Bar */}
      <div className="grid grid-cols-4 gap-2">
        {steps.map((s, idx) => (
          <button
            key={s.step}
            onClick={() => setCurrentStep(idx)}
            className={`h-2 rounded-full transition-all ${
              idx <= currentStep 
                ? 'bg-gradient-to-r from-emerald-500 to-teal-400 shadow-sm shadow-emerald-500/30' 
                : 'bg-slate-800'
            }`}
          />
        ))}
      </div>

      {/* Active Step Details Panel */}
      <div className="grid md:grid-cols-2 gap-4">
        <div className="p-4 rounded-xl bg-slate-900/60 border border-slate-800 space-y-2">
          <div className="flex items-center justify-between text-xs text-slate-400">
            <span>Step {active.step} of {steps.length}</span>
            <span className="text-emerald-400 font-semibold">{active.state.status}</span>
          </div>
          <h4 className="text-sm font-bold text-slate-100">{active.title}</h4>
          <p className="text-xs text-slate-300 leading-relaxed">{active.description}</p>
        </div>

        {/* State Display Cards */}
        <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800 flex flex-col justify-between space-y-3">
          <div className="text-xs font-semibold text-slate-400 uppercase tracking-wider">
            Memory & Pointer State
          </div>

          <div className="grid grid-cols-3 gap-2 text-center">
            <div className="p-2 rounded-lg bg-slate-950 border border-slate-800">
              <div className="text-[10px] text-slate-500">Step Index</div>
              <div className="text-sm font-mono font-bold text-emerald-400">{active.state.index}</div>
            </div>
            <div className="p-2 rounded-lg bg-slate-950 border border-slate-800">
              <div className="text-[10px] text-slate-500">Active State</div>
              <div className="text-xs font-mono font-bold text-teal-300 truncate">{active.state.activeElement}</div>
            </div>
            <div className="p-2 rounded-lg bg-slate-950 border border-slate-800">
              <div className="text-[10px] text-slate-500">Complexity</div>
              <div className="text-xs font-mono font-bold text-amber-400">{problem.timeComplexity}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
