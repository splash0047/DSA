import { NextRequest, NextResponse } from 'next/server';
import { getProblemBySlug } from '@/lib/dsa-scanner';

export async function GET(
  request: NextRequest,
  { params }: { params: Promise<{ slug: string }> }
) {
  try {
    const { slug } = await params;
    const problem = getProblemBySlug(slug);
    
    if (!problem) {
      return NextResponse.json({ error: 'Problem not found' }, { status: 404 });
    }
    
    return NextResponse.json(problem);
  } catch (error) {
    console.error('Error getting problem detail:', error);
    return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
  }
}
