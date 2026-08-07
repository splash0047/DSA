import React from 'react';
import { getAllPhasesAndProblems } from '@/lib/dsa-scanner';
import { DashboardClient } from './dashboard-client';

export const revalidate = 60; // Revalidate dynamic data

export default function DashboardPage() {
  const { phases, problems } = getAllPhasesAndProblems();

  return (
    <main className="min-h-screen bg-[#0b0f17] text-slate-100 pb-16">
      <DashboardClient initialPhases={phases} initialProblems={problems} />
    </main>
  );
}
