'use client';

import React, { useState } from 'react';
import { Sparkles, Bot, X, Send, HelpCircle, Cpu, FileQuestion, CheckCircle2 } from 'lucide-react';
import { Problem } from '@/lib/types';
import { motion, AnimatePresence } from 'framer-motion';

interface AiDrawerProps {
  isOpen: boolean;
  onClose: () => void;
  problem: Problem;
}

export const AiDrawer: React.FC<AiDrawerProps> = ({ isOpen, onClose, problem }) => {
  const [activePrompt, setActivePrompt] = useState<string | null>(null);
  const [customQuery, setCustomQuery] = useState('');
  const [response, setResponse] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const presets = [
    {
      id: 'eli5',
      title: "Explain like I'm 5",
      icon: HelpCircle,
      description: 'Simple intuitive breakdown without complex jargon',
    },
    {
      id: 'complexity',
      title: 'Analyze Time & Space Complexity',
      icon: Cpu,
      description: 'Detailed Big-O derivation for time and memory',
    },
    {
      id: 'interview',
      title: 'Generate Mock Interview Questions',
      icon: FileQuestion,
      description: '3 follow-up questions an interviewer might ask',
    },
  ];

  const handleRunPreset = (presetId: string) => {
    setActivePrompt(presetId);
    setLoading(true);
    setResponse(null);

    setTimeout(() => {
      setLoading(false);
      if (presetId === 'eli5') {
        setResponse(`### 👶 Intuitive ELI5 Explanation: ${problem.title}

Imagine you have a box of cards labeled with numbers or items. 

1. **The Goal**: We want to solve **${problem.title}** using the **${problem.pattern}** pattern.
2. **The Trick**: Instead of checking every single item one by one ($\mathcal{O}(N^2)$ brute force), we use a smart trick: **${problem.pattern}**.
3. **How it works**:
   - We maintain a dynamic helper (like two fingers pointing at cards or a table recording past answers).
   - At each step, we make the best immediate decision based on what we've seen so far.
   - Once complete, we return the optimal answer in **${problem.timeComplexity}** time!`);
      } else if (presetId === 'complexity') {
        setResponse(`### ⏱️ Big-O Complexity Breakdown for ${problem.title}

- **Time Complexity**: \`${problem.timeComplexity}\`
  - **Derivation**: Each element or edge in the input is processed at most once/twice.
  - The optimal algorithm avoids redundant recalculations by using **${problem.pattern}**.

- **Space Complexity**: \`${problem.spaceComplexity}\`
  - **Derivation**: Uses constant scalar variables or dynamic auxiliary storage proportional to input size.`);
      } else if (presetId === 'interview') {
        setResponse(`### 🎤 Top 3 Follow-Up Interview Questions

1. **Constraint Variation**: *What if the input size $N$ is up to $10^9$ and cannot fit in memory?*
   - *Hint*: Use stream processing or disk-backed external sorting.
2. **Space Optimization**: *Can we further reduce auxiliary space complexity?*
   - *Hint*: Currently running at \`${problem.spaceComplexity}\`. Check if scalar state variables can replace the full table.
3. **Edge Case Handling**: *How does your solution handle negative values or empty inputs?*
   - *Hint*: Check boundary guards in \`02_Optimal_Approach.md\`.`);
      }
    }, 700);
  };

  const handleCustomSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!customQuery.trim()) return;

    setLoading(true);
    setResponse(null);

    setTimeout(() => {
      setLoading(false);
      setResponse(`### 🤖 AI Tutor Response for: "${customQuery}"

Regarding **${problem.title}** using **${problem.pattern}**:

The optimal C++17 solution operates in \`${problem.timeComplexity}\` time and \`${problem.spaceComplexity}\` space.

- **Key Takeaway**: ${problem.summary || 'Make sure to handle boundary base cases.'}
- **Pattern Connection**: This pattern frequently recurs in similar problems like ${problem.similarProblems.map(s => s.title).slice(0, 2).join(', ')}.`);
    }, 600);
  };

  return (
    <AnimatePresence>
      {isOpen && (
        <div className="fixed inset-0 z-50 overflow-hidden">
          <div className="absolute inset-0 bg-slate-950/60 backdrop-blur-sm" onClick={onClose} />

          <div className="fixed inset-y-0 right-0 max-w-full flex pl-10">
            <motion.div
              initial={{ x: '100%' }}
              animate={{ x: 0 }}
              exit={{ x: '100%' }}
              transition={{ type: 'spring', damping: 25, stiffness: 200 }}
              className="w-screen max-w-md bg-slate-900 border-l border-slate-800 shadow-2xl flex flex-col"
            >
              {/* Drawer Header */}
              <div className="p-4 border-b border-slate-800 flex items-center justify-between bg-slate-950/80">
                <div className="flex items-center gap-2">
                  <div className="p-1.5 rounded-lg bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                    <Sparkles className="h-4 w-4" />
                  </div>
                  <div>
                    <h2 className="text-sm font-bold text-slate-100">AI Study Tutor</h2>
                    <p className="text-[10px] text-slate-400">Contextual helper for {problem.title}</p>
                  </div>
                </div>

                <button onClick={onClose} className="p-1 text-slate-400 hover:text-slate-200">
                  <X className="h-5 w-5" />
                </button>
              </div>

              {/* Drawer Content */}
              <div className="flex-1 overflow-y-auto p-4 space-y-4">
                {/* Presets Grid */}
                <div className="space-y-2">
                  <h3 className="text-xs font-semibold text-slate-400 uppercase tracking-wider">
                    Quick AI Actions
                  </h3>
                  <div className="grid gap-2">
                    {presets.map((preset) => {
                      const Icon = preset.icon;
                      const isSelected = activePrompt === preset.id;
                      return (
                        <button
                          key={preset.id}
                          onClick={() => handleRunPreset(preset.id)}
                          className={`p-3 rounded-xl border text-left transition-all flex items-start gap-3 ${
                            isSelected 
                              ? 'bg-emerald-500/10 border-emerald-500/40 text-emerald-300' 
                              : 'bg-slate-950/50 border-slate-800 hover:border-slate-700 text-slate-300'
                          }`}
                        >
                          <Icon className="h-4 w-4 text-emerald-400 shrink-0 mt-0.5" />
                          <div>
                            <div className="text-xs font-bold">{preset.title}</div>
                            <div className="text-[11px] text-slate-400 mt-0.5">{preset.description}</div>
                          </div>
                        </button>
                      );
                    })}
                  </div>
                </div>

                {/* AI Response Output Area */}
                {loading && (
                  <div className="p-6 text-center text-slate-400 space-y-2 glass-card rounded-xl">
                    <Sparkles className="h-6 w-6 text-emerald-400 animate-spin mx-auto" />
                    <p className="text-xs">Generating AI breakdown for {problem.title}...</p>
                  </div>
                )}

                {response && !loading && (
                  <motion.div
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="p-4 rounded-xl bg-slate-950 border border-slate-800 prose-dark text-xs leading-relaxed"
                  >
                    <div className="flex items-center gap-1.5 text-emerald-400 font-bold mb-2 text-xs">
                      <Bot className="h-4 w-4" />
                      AI Tutor Output
                    </div>
                    <div className="space-y-2 whitespace-pre-wrap">
                      {response}
                    </div>
                  </motion.div>
                )}
              </div>

              {/* Custom Query Input Footer */}
              <div className="p-3 border-t border-slate-800 bg-slate-950">
                <form onSubmit={handleCustomSubmit} className="flex gap-2">
                  <input
                    type="text"
                    placeholder="Ask AI anything about this problem..."
                    value={customQuery}
                    onChange={(e) => setCustomQuery(e.target.value)}
                    className="flex-1 bg-slate-900 border border-slate-800 rounded-xl px-3 py-2 text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:border-emerald-500"
                  />
                  <button
                    type="submit"
                    className="p-2 rounded-xl bg-emerald-500 text-slate-950 font-bold hover:bg-emerald-400 transition-colors shrink-0"
                  >
                    <Send className="h-4 w-4" />
                  </button>
                </form>
              </div>
            </motion.div>
          </div>
        </div>
      )}
    </AnimatePresence>
  );
};
