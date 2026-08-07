# Problem Summary

Capture all regions of `'O'`s 4-directionally surrounded by `'X'`s by flipping them to `'X'`. Any `'O'` connected to the board boundary cannot be captured. The optimal approach uses **Boundary DFS Marking ('E' Sentinel)**:
- Start DFS from all border `'O'`s and temporarily mark reachable `'O'`s as `'E'` (Escaped/Safe).
- Traverse matrix: flip remaining `'O'`s to `'X'` (captured!) and restore `'E'`s back to `'O'`.
This captures surrounded regions in $\mathcal{O}(M \times N)$ time and $\mathcal{O}(1)$ auxiliary space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **capture/flip regions in a grid that do NOT touch boundaries**.
- Reverse Boundary Flood Fill pattern.

---

## Important Clues

1. **"Capture regions surrounded by 'X'"**: Boundary-connected cells are safe.
2. **"'O' on border is NOT surrounded"**: Start marking from borders.

---

## Example

### Input
```text
["X","X","X","X"]
["X","O","O","X"]
["X","X","O","X"]
["X","O","X","X"]
```

### Visual Step-by-Step Progression

```text
1. Mark border-connected 'O' at (3,1) as 'E':
   ["X","X","X","X"]
   ["X","O","O","X"]
   ["X","X","O","X"]
   ["X","E","X","X"]

2. Flip remaining 'O' -> 'X', restore 'E' -> 'O':
   ["X","X","X","X"]
   ["X","X","X","X"]
   ["X","X","X","X"]
   ["X","O","X","X"]
```

---

## Alternative Solutions

### Queue-Based BFS from Borders ($\mathcal{O}(M \times N)$ Time, $\mathcal{O}(M + N)$ Space)
- Enqueue border `'O'`s into BFS queue and mark reachable cells as `'E'`.

---

## Edge Cases

1. **Board with no border 'O's**: All inner `'O'`s are flipped to `'X'`.
2. **Board with all 'O's**: No cell is flipped.
3. **Small board ($1 \times 1$ or $2 \times 2$)**: All cells are border cells, no flips occur.

---

## Interview Tips

- **Explain Reverse Boundary Marking Insight**: State *"Instead of testing if inner components hit the border, we flip the problem: mark all UNSURROUNDED components starting from the border first. Everything remaining inside is guaranteed to be surrounded."*

---

## Similar Problems

1. [LeetCode #200: Number of Islands](https://leetcode.com/problems/number-of-islands/)
2. [LeetCode #417: Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)
3. [LeetCode #1020: Number of Enclaves](https://leetcode.com/problems/number-of-enclaves/)

---

## Revision Notes

- Problem: Flip surrounded `'O'` regions to `'X'`.
- Pattern: Border DFS with `'E'` sentinel.
- Step 1: DFS from all 4 borders, convert `'O'` $\rightarrow$ `'E'`.
- Step 2: Traverse grid: `'O'` $\rightarrow$ `'X'` (trapped), `'E'` $\rightarrow$ `'O'` (safe).
- Optimal Complexity: Time $\mathcal{O}(M \times N)$, Space $\mathcal{O}(1)$ auxiliary.
