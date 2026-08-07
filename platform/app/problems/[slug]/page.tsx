import React from 'react';
import { notFound } from 'next/navigation';
import { getAllPhasesAndProblems, getProblemBySlug } from '@/lib/dsa-scanner';
import { ProblemDetailClient } from './detail-client';

export const revalidate = 60;

export default async function ProblemDetailPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const problem = getProblemBySlug(slug);

  if (!problem) {
    notFound();
  }

  const { phases, problems } = getAllPhasesAndProblems();

  return (
    <main className="min-h-screen bg-[#0b0f17] text-slate-100 pb-16">
      <ProblemDetailClient problem={problem} allPhases={phases} allProblems={problems} />
    </main>
  );
}
