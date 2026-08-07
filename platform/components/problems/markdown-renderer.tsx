'use client';

import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import rehypeHighlight from 'rehype-highlight';
import { Check, Copy, Code2 } from 'lucide-react';

interface MarkdownRendererProps {
  content: string;
}

// Helper to recursively extract raw text from React elements
function getReactNodeText(node: any): string {
  if (!node) return '';
  if (typeof node === 'string') return node;
  if (typeof node === 'number') return String(node);
  if (Array.isArray(node)) return node.map(getReactNodeText).join('');
  if (node.props) {
    if (node.props.children) return getReactNodeText(node.props.children);
    if (node.props.value) return node.props.value;
  }
  return '';
}

const PreBlock = ({ children }: any) => {
  const [copied, setCopied] = useState(false);
  const rawCode = getReactNodeText(children).replace(/\n$/, '');

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(rawCode);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (err) {
      console.error('Failed to copy code', err);
    }
  };

  return (
    <div className="rounded-xl border border-slate-800 bg-[#0d1117] overflow-hidden my-4 shadow-xl">
      {/* Codeblock Header bar */}
      <div className="flex items-center justify-between px-4 py-2.5 bg-slate-900/90 border-b border-slate-800 select-none">
        <div className="flex items-center gap-2">
          <div className="flex gap-1.5 mr-2">
            <span className="w-2.5 h-2.5 rounded-full bg-rose-500/80 inline-block" />
            <span className="w-2.5 h-2.5 rounded-full bg-amber-500/80 inline-block" />
            <span className="w-2.5 h-2.5 rounded-full bg-emerald-500/80 inline-block" />
          </div>
          <Code2 className="h-4 w-4 text-emerald-400" />
          <span className="font-mono text-xs font-semibold text-slate-300">
            Solution.cpp
          </span>
          <span className="text-[10px] font-mono uppercase bg-slate-800 text-emerald-400 px-1.5 py-0.5 rounded border border-slate-700 font-medium">
            C++17
          </span>
        </div>

        {/* Copy button */}
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

      {/* Code highlighting block wrapped in pre to preserve whitespaces and newlines */}
      <div className="overflow-x-auto p-4 text-xs font-mono leading-relaxed">
        <pre style={{ whiteSpace: 'pre', margin: 0, padding: 0 }} className="font-mono">
          {children}
        </pre>
      </div>
    </div>
  );
};

export const MarkdownRenderer: React.FC<MarkdownRendererProps> = ({ content }) => {
  return (
    <div className="prose-dark font-sans leading-relaxed">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        rehypePlugins={[rehypeHighlight]}
        components={{
          pre({ children }) {
            return <PreBlock>{children}</PreBlock>;
          },
          table({ children }) {
            return (
              <div className="overflow-x-auto my-4 rounded-xl border border-slate-800">
                <table className="w-full border-collapse text-sm">{children}</table>
              </div>
            );
          },
          a({ href, children }) {
            return (
              <a 
                href={href} 
                target="_blank" 
                rel="noopener noreferrer" 
                className="text-emerald-400 hover:text-emerald-300 underline font-medium"
              >
                {children}
              </a>
            );
          }
        }}
      >
        {content}
      </ReactMarkdown>
    </div>
  );
};
