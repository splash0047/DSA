'use client';

import React, { useState } from 'react';
import { Check, Copy, Code2, Terminal } from 'lucide-react';

interface CodeBlockProps {
  code: string;
  language?: string;
  filename?: string;
}

export const CodeBlock: React.FC<CodeBlockProps> = ({ 
  code, 
  language = 'cpp', 
  filename = 'Solution.cpp' 
}) => {
  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    if (!code) return;
    try {
      await navigator.clipboard.writeText(code);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (err) {
      console.error('Failed to copy code', err);
    }
  };

  const lines = code.split('\n');

  return (
    <div className="rounded-xl border border-slate-800 bg-slate-950 overflow-hidden my-4 shadow-xl">
      {/* VS Code Header */}
      <div className="flex items-center justify-between px-4 py-2.5 bg-slate-900/90 border-b border-slate-800">
        <div className="flex items-center gap-2">
          <div className="flex gap-1.5 mr-2">
            <span className="w-2.5 h-2.5 rounded-full bg-rose-500/80 inline-block" />
            <span className="w-2.5 h-2.5 rounded-full bg-amber-500/80 inline-block" />
            <span className="w-2.5 h-2.5 rounded-full bg-emerald-500/80 inline-block" />
          </div>
          <Code2 className="h-4 w-4 text-emerald-400" />
          <span className="font-mono text-xs font-semibold text-slate-300">
            {filename}
          </span>
          <span className="text-[10px] font-mono uppercase bg-slate-800 text-emerald-400 px-1.5 py-0.5 rounded border border-slate-700 font-medium">
            C++17
          </span>
        </div>

        {/* Copy Button */}
        <button
          onClick={handleCopy}
          className="flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-medium text-slate-300 hover:text-slate-100 transition-colors border border-slate-700/60"
        >
          {copied ? (
            <>
              <Check className="h-3.5 w-3.5 text-emerald-400" />
              <span className="text-emerald-400 font-semibold">Copied!</span>
            </>
          ) : (
            <>
              <Copy className="h-3.5 w-3.5 text-slate-400" />
              <span>Copy</span>
            </>
          )}
        </button>
      </div>

      {/* Code Area with Line Numbers */}
      <div className="flex overflow-x-auto text-xs font-mono p-4 leading-relaxed bg-[#0d1117]">
        {/* Line Numbers */}
        <div className="flex flex-col text-slate-600 select-none pr-4 text-right border-r border-slate-800/60">
          {lines.map((_, i) => (
            <span key={i}>{i + 1}</span>
          ))}
        </div>

        {/* Highlighted Code Text */}
        <pre className="pl-4 flex-1 text-slate-200 overflow-x-auto">
          <code>{code}</code>
        </pre>
      </div>
    </div>
  );
};
