import React from 'react';
import { getAllPhasesAndProblems } from '@/lib/dsa-scanner';
import { PatternsClient } from './patterns-client';

export const revalidate = 60;

export default function PatternsPage() {
  const { phases, problems } = getAllPhasesAndProblems();

  return (
    <main className="min-h-screen bg-[#0b0f17] text-slate-100 pb-16">
      <PatternsClient initialPhases={phases} initialProblems={problems} />
    </main>
  );
}
