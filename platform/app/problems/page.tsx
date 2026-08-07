import React, { Suspense } from 'react';
import { getAllPhasesAndProblems } from '@/lib/dsa-scanner';
import { ProblemsClient } from './problems-client';

export const revalidate = 60;

export default function ProblemsPage() {
  const { phases, problems } = getAllPhasesAndProblems();

  return (
    <main className="min-h-screen bg-[#0b0f17] text-slate-100 pb-16">
      <Suspense fallback={
        <div className="min-h-screen flex items-center justify-center text-slate-400">
          Loading Problems Directory...
        </div>
      }>
        <ProblemsClient initialPhases={phases} initialProblems={problems} />
      </Suspense>
    </main>
  );
}
