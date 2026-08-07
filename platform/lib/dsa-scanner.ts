import fs from 'fs';
import path from 'path';
import { Problem, Phase, Difficulty } from './types';

// Root directory of the DSA knowledge base
const DSA_ROOT_DIR = process.env.DSA_DATA_PATH 
  ? process.env.DSA_DATA_PATH 
  : path.resolve(process.cwd(), '..');

export function getDsaRootDir(): string {
  if (fs.existsSync(DSA_ROOT_DIR) && fs.existsSync(path.join(DSA_ROOT_DIR, 'Phase 00 Programming Foundation'))) {
    return DSA_ROOT_DIR;
  }
  // Fallback to absolute path on user system
  const absPath = 'c:\\Users\\Pinak chimurkar\\DSA';
  if (fs.existsSync(absPath)) {
    return absPath;
  }
  return process.cwd();
}

function extractDifficulty(text: string): Difficulty {
  if (/difficulty\s*:\s*hard/i.test(text) || /\bhard\b/i.test(text)) return 'Hard';
  if (/difficulty\s*:\s*easy/i.test(text) || /\beasy\b/i.test(text)) return 'Easy';
  return 'Medium';
}

function extractCppCode(mdText: string): string {
  const match = mdText.match(/```cpp([\s\S]*?)```/);
  return match ? match[1].trim() : '';
}

function extractPattern(optimalMd: string, bruteMd: string): string {
  const patternMatch = optimalMd.match(/-\s*\*\*Pattern\*\*:\s*\*?\*?([^\n\r*]+)\*?\*?/) 
    || bruteMd.match(/-\s*\*\*Pattern\*\*:\s*\*?\*?([^\n\r*]+)\*?\*?/)
    || optimalMd.match(/## Pattern Used[\s\S]*?-\s*\*\*Pattern\*\*:\s*\*?\*?([^\n\r*]+)\*?\*?/);
  
  if (patternMatch && patternMatch[1]) {
    return patternMatch[1].replace(/[*_]/g, '').trim();
  }
  
  // Fallback pattern extraction
  if (/two pointer/i.test(optimalMd)) return 'Two Pointers';
  if (/sliding window/i.test(optimalMd)) return 'Sliding Window';
  if (/binary search/i.test(optimalMd)) return 'Binary Search';
  if (/dynamic programming|dp/i.test(optimalMd)) return 'Dynamic Programming';
  if (/bfs|kahn|breadth/i.test(optimalMd)) return 'BFS Traversal';
  if (/dfs|depth/i.test(optimalMd)) return 'DFS Search';
  if (/dsu|union-find|disjoint/i.test(optimalMd)) return 'Disjoint Set Union';
  if (/heap|priority queue/i.test(optimalMd)) return 'Heap / Priority Queue';
  if (/hash|map|prefix/i.test(optimalMd)) return 'HashMap & Prefix';
  if (/stack|queue/i.test(optimalMd)) return 'Stack & Queue';
  if (/linked list/i.test(optimalMd)) return 'Linked List';
  if (/tree|binary tree/i.test(optimalMd)) return 'Binary Tree';
  if (/bit/i.test(optimalMd)) return 'Bit Manipulation';
  
  return 'General Technique';
}

function extractUrl(text: string): string {
  const urlMatch = text.match(/https:\/\/leetcode\.com\/problems\/[a-zA-Z0-9-]+\/?/)
    || text.match(/\[LeetCode[^\]]*\]\((https:\/\/[^\)]+)\)/);
  return urlMatch ? (urlMatch[1] || urlMatch[0]) : '';
}

function extractPlatformNumber(text: string): { platform: string; platformProblemNumber: string } {
  const lcMatch = text.match(/LeetCode\s*#?(\d+)/i) || text.match(/#(\d+)/);
  if (lcMatch) {
    return { platform: 'LeetCode', platformProblemNumber: `#${lcMatch[1]}` };
  }
  return { platform: 'LeetCode', platformProblemNumber: '' };
}

function extractComplexity(text: string, type: 'Time' | 'Space'): string {
  const regex = new RegExp(`## ${type} Complexity[\\s\\S]*?-\\s*\\*\\*${type} Complexity\\*\\*:\\s*([^\\n\\r]+)`, 'i');
  const match = text.match(regex);
  if (match && match[1]) {
    return match[1].trim();
  }
  return 'Not specified';
}

function extractSimilarProblems(text: string): Array<{ title: string; url: string }> {
  const similarSection = text.match(/## Similar Problems([\s\S]*?)(?=##|$)/i);
  if (!similarSection) return [];
  
  const lines = similarSection[1].split('\n');
  const result: Array<{ title: string; url: string }> = [];
  
  for (const line of lines) {
    const linkMatch = line.match(/\[([^\]]+)\]\((https:\/\/[^\)]+)\)/);
    if (linkMatch) {
      result.push({
        title: linkMatch[1].trim(),
        url: linkMatch[2].trim(),
      });
    }
  }
  
  return result;
}

function extractRevisionNotes(text: string): string {
  const match = text.match(/## Revision Notes([\s\S]*?)$/i);
  return match ? match[1].trim() : '';
}

function extractSummary(text: string): string {
  const match = text.match(/# Problem Summary[\s\S]*?([\s\S]*?)(?=---|\n##|$)/i);
  return match ? match[1].trim() : '';
}

export function getAllPhasesAndProblems(): { phases: Phase[]; problems: Problem[] } {
  const rootDir = getDsaRootDir();
  const phases: Phase[] = [];
  const allProblems: Problem[] = [];

  if (!fs.existsSync(rootDir)) {
    console.warn(`DSA Root Dir not found at: ${rootDir}`);
    return { phases: [], problems: [] };
  }

  const entries = fs.readdirSync(rootDir, { withFileTypes: true });
  const phaseDirs = entries
    .filter(e => e.isDirectory() && e.name.startsWith('Phase '))
    .map(e => e.name)
    .sort((a, b) => {
      const numA = parseInt(a.match(/Phase\s*(\d+)/i)?.[1] || '0', 10);
      const numB = parseInt(b.match(/Phase\s*(\d+)/i)?.[1] || '0', 10);
      return numA - numB;
    });

  for (const phaseFolderName of phaseDirs) {
    const phaseNumMatch = phaseFolderName.match(/Phase\s*(\d+)\s*(.*)/i);
    const phaseNum = phaseNumMatch ? parseInt(phaseNumMatch[1], 10) : 0;
    const phaseTitle = phaseNumMatch ? phaseNumMatch[2].trim() : phaseFolderName;

    const phasePath = path.join(rootDir, phaseFolderName);
    const problemEntries = fs.readdirSync(phasePath, { withFileTypes: true });
    
    const problemDirs = problemEntries
      .filter(e => e.isDirectory())
      .map(e => e.name)
      .sort((a, b) => {
        const numA = parseInt(a.match(/^(\d+)/)?.[1] || '0', 10);
        const numB = parseInt(b.match(/^(\d+)/)?.[1] || '0', 10);
        return numA - numB;
      });

    const phaseProblems: Problem[] = [];

    for (const problemFolderName of problemDirs) {
      const probNumMatch = problemFolderName.match(/^(\d+)\s*(.*)/);
      const probNum = probNumMatch ? parseInt(probNumMatch[1], 10) : 0;
      const probRawTitle = probNumMatch ? probNumMatch[2].trim() : problemFolderName;

      const problemPath = path.join(phasePath, problemFolderName);
      
      const qPath = path.join(problemPath, '00_Question.md');
      const bPath = path.join(problemPath, '01_Brute_Force.md');
      const oPath = path.join(problemPath, '02_Optimal_Approach.md');
      const ePath = path.join(problemPath, '03_Explanation.md');

      const questionMd = fs.existsSync(qPath) ? fs.readFileSync(qPath, 'utf-8') : '';
      const bruteForceMd = fs.existsSync(bPath) ? fs.readFileSync(bPath, 'utf-8') : '';
      const optimalMd = fs.existsSync(oPath) ? fs.readFileSync(oPath, 'utf-8') : '';
      const explanationMd = fs.existsSync(ePath) ? fs.readFileSync(ePath, 'utf-8') : '';

      const fullText = `${questionMd}\n${bruteForceMd}\n${optimalMd}\n${explanationMd}`;
      const wordCount = fullText.split(/\s+/).filter(Boolean).length;
      const readingTimeMinutes = Math.max(1, Math.ceil(wordCount / 200));

      const difficulty = extractDifficulty(questionMd || bruteForceMd || optimalMd);
      const pattern = extractPattern(optimalMd, bruteForceMd);
      const url = extractUrl(questionMd || fullText);
      const { platform, platformProblemNumber } = extractPlatformNumber(questionMd || fullText);
      const bruteCode = extractCppCode(bruteForceMd);
      const optimalCode = extractCppCode(optimalMd);
      const timeComplexity = extractComplexity(optimalMd, 'Time');
      const spaceComplexity = extractComplexity(optimalMd, 'Space');
      const similarProblems = extractSimilarProblems(explanationMd);
      const revisionNotes = extractRevisionNotes(explanationMd);
      const summary = extractSummary(explanationMd);

      const formattedNum = String(probNum).padStart(3, '0');
      const slug = `${formattedNum}-${probRawTitle.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '')}`;

      const problemObj: Problem = {
        id: slug,
        number: probNum,
        title: probRawTitle,
        slug,
        phaseFolder: phaseFolderName,
        problemFolder: problemFolderName,
        phaseNumber: phaseNum,
        phaseTitle,
        difficulty,
        platform,
        platformProblemNumber,
        url,
        pattern,
        readingTimeMinutes,
        questionMd,
        bruteForceMd,
        optimalMd,
        explanationMd,
        bruteCode,
        optimalCode,
        summary,
        timeComplexity,
        spaceComplexity,
        similarProblems,
        revisionNotes,
      };

      phaseProblems.push(problemObj);
      allProblems.push(problemObj);
    }

    phases.push({
      id: `phase-${phaseNum}`,
      number: phaseNum,
      title: phaseTitle,
      folderName: phaseFolderName,
      problemCount: phaseProblems.length,
      problems: phaseProblems,
    });
  }

  return { phases, problems: allProblems };
}

export function getProblemBySlug(slug: string): Problem | undefined {
  const { problems } = getAllPhasesAndProblems();
  return problems.find(p => p.slug === slug || p.id === slug);
}
