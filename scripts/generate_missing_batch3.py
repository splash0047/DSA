import os

DSA_ROOT = r"c:\Users\Pinak chimurkar\DSA"

def write_problem(phase_dir, folder_name, q_content, bf_content, opt_content, exp_content, fol_content):
    target_dir = os.path.join(DSA_ROOT, phase_dir, folder_name)
    os.makedirs(target_dir, exist_ok=True)
    
    files = {
        "00_Question.md": q_content,
        "01_Brute_Force.md": bf_content,
        "02_Optimal_Approach.md": opt_content,
        "03_Explanation.md": exp_content,
        "04_Interview_Followups.md": fol_content,
    }
    
    for filename, content in files.items():
        filepath = os.path.join(target_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
    print(f"Created: {phase_dir}/{folder_name}")

# Heap: Meeting Rooms II
write_problem(
    "Phase 07 Heap", "Meeting Rooms II",
    r"""# Meeting Rooms II

- **Platform**: LeetCode / Premium / GFG
- **Problem Number**: #253
- **Difficulty**: Medium
- **URL**: [LeetCode #253 - Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)

---

## Problem Statement

Given an array of meeting time intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of conference rooms required.
""",
    r"""# Meeting Rooms II - Brute Force (Chronological Simulation)

- **Problem Number**: 253
- **Pattern**: Overlapping Interval Count per Timestamp
""",
    r"""# Meeting Rooms II - Optimal Approach (Min-Heap / Chronological Line Sweep)

- **Problem Number**: 253
- **Pattern**: Min-Heap of Active End Times / Two Pointers on Sorted Starts & Ends

```cpp
#include <vector>
#include <queue>
#include <algorithm>

class Solution {
public:
    int minMeetingRooms(std::vector<std::vector<int>>& intervals) {
        if (intervals.empty()) return 0;
        std::sort(intervals.begin(), intervals.end());

        std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;
        min_heap.push(intervals[0][1]);

        for (size_t i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] >= min_heap.top()) {
                min_heap.pop(); // Room freed up
            }
            min_heap.push(intervals[i][1]); // Allocate room
        }
        return min_heap.size();
    }
};
```
""",
    r"""# Meeting Rooms II - Deep Explanation

The Min-Heap always maintains the earliest ending meeting. If a new meeting starts after or at the earliest end time, we reuse that room by popping and pushing the new end time.
""",
    r"""# 04 Interview Follow-ups: Meeting Rooms II

## 1. Line Sweep Alternative
- Separate starts and ends, sort both, and use two pointers in $\mathcal{O}(N \log N)$ time and $\mathcal{O}(N)$ space without heap overhead.
"""
)

# Graphs missing
graphs = [
    ("Flood Fill", 733, "DFS / BFS Color Replacement", "Multi-directional Flood Fill"),
    ("Number of Provinces", 547, "DFS / BFS Visited Components", "Disjoint Set Union with Path Compression"),
    ("Redundant Connection", 684, "DFS Cycle Detection", "Disjoint Set Union (Union-Find)")
]

for title, num, bf_pat, opt_pat in graphs:
    q = f"""# {title}\n\n- **Platform**: LeetCode\n- **Problem Number**: #{num}\n- **Difficulty**: {"Easy" if num == 733 else "Medium"}\n- **URL**: [LeetCode #{num} - {title}](https://leetcode.com/problems/{title.lower().replace(' ', '-')}/)\n\n---\n\n## Problem Statement\n\nStandard LeetCode #{num}: {title}.\n"""
    bf = f"""# {title} - Brute Force\n\n- **Pattern**: {bf_pat}\n"""
    opt = f"""# {title} - Optimal Approach\n\n- **Pattern**: {opt_pat}\n"""
    exp = f"""# {title} - Deep Explanation\n\nRuns in linear $\\mathcal{{O}}(V + E)$ or grid $\\mathcal{{O}}(M \\times N)$ time.\n"""
    fol = f"""# 04 Interview Follow-ups: {title}\n\n## 1. Scaling to Massive Graphs\n- Distributed Graph partitioning and Disjoint Set streaming.\n"""
    write_problem("Phase 08 Graphs", title, q, bf, opt, exp, fol)

# Backtracking (Phase 09 Backtracking)
backtracking = [
    ("Subsets", 78, "Cascading Iteration", "Backtracking Choice Tree", "Bitmask 2^N Iteration"),
    ("Subsets II", 90, "Set of Vectors", "Backtracking with Duplicate Skipping (`if (i > start && nums[i] == nums[i-1]) continue;`)", "Frequency Map Backtracking"),
    ("Permutations", 46, "Generate All Permutations", "Backtracking with Visited / In-place Swapping", "Heap's Algorithm"),
    ("Permutations II", 47, "Set of Permutations", "Backtracking with Frequency Array & Sorted Guard", "In-place Swap Pruning"),
    ("Combination Sum", 39, "Recursion with Duplicates", "Backtracking (Reuse current element index)", "DP Unbounded Knapsack"),
    ("Combination Sum II", 40, "Set of Vectors", "Backtracking with Single-use & Duplicate Skipping", "Branch and Bound"),
    ("N-Queens", 51, "Brute Force Permutation of Board", "Backtracking with Column & Diagonal Bitsets", "Bitwise N-Queens Solver"),
    ("Generate Parentheses", 22, "Brute Force All 2^(2N) Strings + Validation", "Backtracking with `open < n` and `close < open` Counts", "Catalan Number Closed Form"),
    ("Letter Combinations of a Phone Number", 17, "Iterative Cross Product", "Backtracking DFS with Digit Mapping", "BFS Queue String Generation"),
    ("Palindrome Partitioning", 131, "Generate All 2^(N-1) Partitions", "Backtracking + Palindrome Verification / DP Lookup", "Manacher Precomputation")
]

for title, num, bf_pat, opt_pat, fol_pat in backtracking:
    q = f"""# {title}\n\n- **Platform**: LeetCode\n- **Problem Number**: #{num}\n- **Difficulty**: {"Hard" if num == 51 else "Medium"}\n- **URL**: [LeetCode #{num} - {title}](https://leetcode.com/problems/{title.lower().replace(' ', '-')}/)\n\n---\n\n## Problem Statement\n\nStandard LeetCode #{num}: {title}.\n"""
    bf = f"""# {title} - Brute Force\n\n- **Pattern**: {bf_pat}\n"""
    opt = f"""# {title} - Optimal Approach\n\n- **Pattern**: {opt_pat}\n"""
    exp = f"""# {title} - Deep Explanation\n\nStandard backtracking decision tree exploring solution space with state restoration.\n"""
    fol = f"""# 04 Interview Follow-ups: {title}\n\n## 1. Optimal Pruning & Variations\n- {fol_pat}.\n"""
    write_problem("Phase 09 Backtracking", title, q, bf, opt, exp, fol)

# Greedy (Phase 10 Greedy)
greedy = [
    ("Jump Game", 55, "Backtracking / DFS", "Greedy Farthest Reachable Index Tracking"),
    ("Jump Game II", 45, "BFS Shortest Path", "Greedy Current/Next Window BFS (O(N))"),
    ("Gas Station", 134, "Test Starting from Every Station (O(N^2))", "Greedy Running Tank + Total Gas Balance (O(N))"),
    ("Candy", 135, "Brute Force Iterative Propagation", "Two-Pass Greedy (Left-to-Right and Right-to-Left)"),
    ("Non-overlapping Intervals", 435, "Power Set Compatibility Check", "Greedy Earliest End Time Interval Scheduling"),
    ("Merge Intervals", 56, "Pairwise Merging", "Sort by Start Time + Continuous Interval Extension"),
    ("Insert Interval", 57, "Insert & Full Re-sort", "3-Phase Linear Scan (Before, Overlapping Merge, After)"),
    ("Partition Labels", 763, "All String Partitions", "Greedy Last-Occurrence Index Window Extension")
]

for title, num, bf_pat, opt_pat in greedy:
    q = f"""# {title}\n\n- **Platform**: LeetCode\n- **Problem Number**: #{num}\n- **Difficulty**: {"Hard" if num == 135 else "Medium"}\n- **URL**: [LeetCode #{num} - {title}](https://leetcode.com/problems/{title.lower().replace(' ', '-')}/)\n\n---\n\n## Problem Statement\n\nStandard LeetCode #{num}: {title}.\n"""
    bf = f"""# {title} - Brute Force\n\n- **Pattern**: {bf_pat}\n"""
    opt = f"""# {title} - Optimal Approach\n\n- **Pattern**: {opt_pat}\n"""
    exp = f"""# {title} - Deep Explanation\n\nGreedy choice property guarantees global optimality through local optimal decisions.\n"""
    fol = f"""# 04 Interview Follow-ups: {title}\n\n## 1. System Scaling & Streaming\n- Stream intervals / events with interval trees or Segment Trees.\n"""
    write_problem("Phase 10 Greedy", title, q, bf, opt, exp, fol)

# DP missing: Minimum Path Sum
write_problem(
    "Phase 09 Dynamic Programming", "Minimum Path Sum",
    r"""# Minimum Path Sum

- **Platform**: LeetCode
- **Problem Number**: #64
- **Difficulty**: Medium
- **URL**: [LeetCode #64 - Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)
""",
    r"""# Minimum Path Sum - Brute Force (Recursion)
- **Time**: $\mathcal{O}(2^{M+N})$
""",
    r"""# Minimum Path Sum - Optimal Approach (1D Rolling DP)

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int minPathSum(std::vector<std::vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        std::vector<int> dp(n, 0);

        dp[0] = grid[0][0];
        for (int j = 1; j < n; j++) dp[j] = dp[j - 1] + grid[0][j];

        for (int i = 1; i < m; i++) {
            dp[0] += grid[i][0];
            for (int j = 1; j < n; j++) {
                dp[j] = std::min(dp[j], dp[j - 1]) + grid[i][j];
            }
        }
        return dp[n - 1];
    }
};
```
""",
    r"""# Minimum Path Sum - Deep Explanation

Uses 1D vector `dp` where `dp[j]` stores the minimum path sum to column `j` in the current row.
""",
    r"""# 04 Interview Follow-ups: Minimum Path Sum

## 1. In-place Mutation
- Modify `grid[i][j]` directly for strictly $\mathcal{O}(1)$ extra memory.
"""
)

# Bits missing: Missing Number, Reverse Bits
bits = [
    ("Missing Number", 268, "Sort / Hash Set", "XOR Sum Cancellation (O(N) time, O(1) space) or Gauss Formula (n*(n+1)/2 - sum)"),
    ("Reverse Bits", 190, "Bit-by-Bit Loop", "Bitwise Shift Accumulation / Byte-Level Lookup Table (O(1))")
]

for title, num, bf_pat, opt_pat in bits:
    q = f"""# {title}\n\n- **Platform**: LeetCode\n- **Problem Number**: #{num}\n- **Difficulty**: Easy\n- **URL**: [LeetCode #{num} - {title}](https://leetcode.com/problems/{title.lower().replace(' ', '-')}/)\n\n---\n\n## Problem Statement\n\nStandard LeetCode #{num}: {title}.\n"""
    bf = f"""# {title} - Brute Force\n\n- **Pattern**: {bf_pat}\n"""
    opt = f"""# {title} - Optimal Approach\n\n- **Pattern**: {opt_pat}\n"""
    exp = f"""# {title} - Deep Explanation\n\nBitwise properties operate directly inside CPU registers in $\\mathcal{{O}}(1)$ or $\\mathcal{{O}}(N)$ time.\n"""
    fol = f"""# 04 Interview Follow-ups: {title}\n\n## 1. Hardware SIMD & Cache Tables\n- Byte-level static 256-entry table for parallel bit reversals.\n"""
    write_problem("Phase 10 Bit Manipulation & Advanced", title, q, bf, opt, exp, fol)

# Tries (Phase 13 Tries)
tries = [
    ("Implement Trie (Prefix Tree)", 208, "List of Strings Linear Scan", "TrieNode with 26-pointer child array & isEnd boolean"),
    ("Design Add and Search Words Data Structure", 211, "Regex String Search", "Trie with DFS Backtracking on Wildcard '.'"),
    ("Word Search II", 212, "DFS from Every Cell for Every Word (O(W * M * N * 4^L))", "Trie-Guided Backtracking on 2D Board (O(M * N * 4^L))")
]

for title, num, bf_pat, opt_pat in tries:
    q = f"""# {title}\n\n- **Platform**: LeetCode\n- **Problem Number**: #{num}\n- **Difficulty**: {"Hard" if num == 212 else "Medium"}\n- **URL**: [LeetCode #{num} - {title}](https://leetcode.com/problems/{title.lower().replace(' ', '-')}/)\n\n---\n\n## Problem Statement\n\nStandard LeetCode #{num}: {title}.\n"""
    bf = f"""# {title} - Brute Force\n\n- **Pattern**: {bf_pat}\n"""
    opt = f"""# {title} - Optimal Approach\n\n- **Pattern**: {opt_pat}\n"""
    exp = f"""# {title} - Deep Explanation\n\nTrie prefix tree accelerates dictionary prefix queries to $\\mathcal{{O}}(L)$ where $L$ is word length.\n"""
    fol = f"""# 04 Interview Follow-ups: {title}\n\n## 1. Memory Optimization (Radix Tree / Suffix Automaton)\n- Compress single-child paths into Radix / Patricia Trie nodes.\n"""
    write_problem("Phase 13 Tries", title, q, bf, opt, exp, fol)

print("Batch 3 completed successfully!")
