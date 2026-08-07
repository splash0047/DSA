# Problem Summary

Given an `m x n` 2D binary grid representing land `'1'` and water `'0'`, return the number of islands (4-directionally connected land components). The optimal approach uses **In-Place Grid Sink DFS**:
- Iterate over every cell `(r, c)` in grid.
- When finding `'1'`, increment `islands++` and launch `sink(grid, r, c)`.
- `sink` turns visited land `'1'` to `'0'` and recurses into up, down, left, right neighbors.
This computes the number of islands in $\mathcal{O}(M \times N)$ time and $\mathcal{O}(1)$ auxiliary space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to count **connected components in a 2D matrix/grid**.
- Grid Flood Fill / In-Place Sinking DFS pattern.

---

## Important Clues

1. **"Number of islands / connected components in 2D grid"**: DFS/BFS Flood Fill.
2. **"Connected horizontally or vertically"**: 4-directional traversal (`[+1,0], [-1,0], [0,+1], [0,-1]`).

---

## Example

### Input
```text
grid = [
  ["1","1","0"],
  ["1","0","0"],
  ["0","0","1"]
]
```

### Visual Step-by-Step Progression

```text
Step 1: Found '1' at (0,0) -> islands = 1
Flood fill sinks (0,0), (1,0), (0,1):
  ["0","0","0"],
  ["0","0","0"],
  ["0","0","1"]

Step 2: Found '1' at (2,2) -> islands = 2
Flood fill sinks (2,2):
  ["0","0","0"],
  ["0","0","0"],
  ["0","0","0"]

Result: 2
```

---

## Alternative Solutions

### 1. Queue-Based BFS ($\mathcal{O}(M \times N)$ Time, $\mathcal{O}(\min(M,N))$ Space)
- Enqueue land cells into `queue<pair<int,int>>` level-by-level to prevent deep recursion.

### 2. Disjoint Set Union (DSU / Union-Find) ($\mathcal{O}(M \times N \cdot \alpha(N))$ Time)
- Union adjacent land cells and count distinct component roots.

---

## Edge Cases

1. **Grid with all water**: Returns `0`.
2. **Grid with all land**: Returns `1`.
3. **$1 \times 1$ grid**: `[["1"]]` returns `1`, `[["0"]]` returns `0`.

---

## Interview Tips

- **Mention In-Place Sinking Strategy**: State *"By mutating visited `'1'`s directly to `'0'`, we avoid allocating an auxiliary $M \times N$ boolean array, keeping auxiliary space complexity to $\mathcal{O}(1)$."*

---

## Similar Problems

1. [LeetCode #695: Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
2. [LeetCode #130: Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)
3. [LeetCode #417: Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)
4. [LeetCode #994: Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
5. [LeetCode #286: Walls and Gates](https://leetcode.com/problems/walls-and-gates/)

---

## Revision Notes

- Problem: Count connected 4-directional land components in grid.
- Pattern: DFS Flood Fill with In-Place Sinking.
- `sink(r, c)`: `if (outOfBounds || grid[r][c] == '0') return; grid[r][c] = '0';` Recurse 4 directions.
- Counter: Loop grid, `if (grid[r][c] == '1') { islands++; sink(r, c); }`.
- Optimal Complexity: Time $\mathcal{O}(M \times N)$, Space $\mathcal{O}(1)$ auxiliary.
