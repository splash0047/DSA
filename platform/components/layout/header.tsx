'use client';

import React from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { 
  BookOpen, 
  Code2, 
  Search, 
  Flame, 
  CheckCircle2, 
  RotateCcw, 
  Network, 
  Sparkles,
  LayoutDashboard,
  BrainCircuit
} from 'lucide-react';
import { UserProgress } from '@/lib/types';

interface HeaderProps {
  progress: UserProgress;
  onOpenCommandPalette: () => void;
}

export const Header: React.FC<HeaderProps> = ({ progress, onOpenCommandPalette }) => {
  const pathname = usePathname();

  const navItems = [
    { name: 'Dashboard', href: '/', icon: LayoutDashboard },
    { name: 'Problems', href: '/problems', icon: BookOpen },
    { name: 'Revision', href: '/revision', icon: RotateCcw },
    { name: 'Patterns', href: '/patterns', icon: Network },
  ];

  return (
    <header className="sticky top-0 z-40 w-full glass-panel border-b border-slate-800/80">
      <div className="flex h-16 items-center justify-between px-4 sm:px-6">
        {/* Brand Logo & Title */}
        <div className="flex items-center gap-3">
          <Link href="/" className="flex items-center gap-2.5 group">
            <div className="h-9 w-9 rounded-xl bg-gradient-to-tr from-emerald-500 to-teal-400 p-2 text-slate-950 flex items-center justify-center font-bold shadow-lg shadow-emerald-500/20 group-hover:scale-105 transition-transform">
              <Code2 className="h-5 w-5 stroke-[2.5]" />
            </div>
            <div>
              <span className="text-lg font-extrabold tracking-tight bg-gradient-to-r from-slate-100 via-emerald-200 to-teal-300 bg-clip-text text-transparent">
                AlgoVault
              </span>
              <span className="ml-1.5 text-[10px] uppercase tracking-wider font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 px-1.5 py-0.5 rounded">
                Pro
              </span>
            </div>
          </Link>
        </div>

        {/* Center Navigation Links */}
        <nav className="hidden md:flex items-center gap-1 bg-slate-900/60 border border-slate-800/60 p-1 rounded-xl">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = pathname === item.href || (item.href !== '/' && pathname.startsWith(item.href));
            return (
              <Link
                key={item.href}
                href={item.href}
                className={`flex items-center gap-2 px-3.5 py-1.5 rounded-lg text-sm font-medium transition-all ${
                  isActive
                    ? 'bg-slate-800 text-emerald-400 shadow-sm'
                    : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/50'
                }`}
              >
                <Icon className={`h-4 w-4 ${isActive ? 'text-emerald-400' : 'text-slate-400'}`} />
                {item.name}
              </Link>
            );
          })}
        </nav>

        {/* Right Actions & Metrics */}
        <div className="flex items-center gap-3">
          {/* Quick Search Button / Command Palette Trigger */}
          <button
            onClick={onOpenCommandPalette}
            className="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-slate-900/80 border border-slate-800 hover:border-slate-700 text-slate-400 text-xs font-medium transition-all hover:text-slate-200"
          >
            <Search className="h-3.5 w-3.5 text-slate-400" />
            <span className="hidden sm:inline">Search problems...</span>
            <kbd className="hidden sm:inline-block bg-slate-800 text-slate-300 border border-slate-700 rounded px-1.5 py-0.5 text-[10px] font-mono">
              Ctrl+K
            </kbd>
          </button>

          {/* Solved Count Badge */}
          <div className="hidden lg:flex items-center gap-1.5 bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 px-3 py-1 rounded-xl text-xs font-semibold">
            <CheckCircle2 className="h-3.5 w-3.5" />
            <span>{progress.completedIds.length} / 154 Solved</span>
          </div>

          {/* Streak Indicator */}
          <div className="flex items-center gap-1.5 bg-amber-500/10 border border-amber-500/20 text-amber-400 px-2.5 py-1 rounded-xl text-xs font-semibold">
            <Flame className="h-4 w-4 fill-amber-400 text-amber-500" />
            <span>{progress.streak} Day</span>
          </div>
        </div>
      </div>
    </header>
  );
};
