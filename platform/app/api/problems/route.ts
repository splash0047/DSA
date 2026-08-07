import { NextResponse } from 'next/server';
import { getAllPhasesAndProblems } from '@/lib/dsa-scanner';

export async function GET() {
  try {
    const data = getAllPhasesAndProblems();
    return NextResponse.json(data);
  } catch (error) {
    console.error('Error scanning DSA problems:', error);
    return NextResponse.json({ error: 'Failed to scan problems' }, { status: 500 });
  }
}
