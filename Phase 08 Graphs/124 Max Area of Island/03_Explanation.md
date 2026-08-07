# Problem Summary

Given an `m x n` binary grid, return the maximum area (number of connected land cells) of an island. The optimal approach uses **In-Place Sinking DFS**:
- Iterate through each cell `(r, c)`.
- When encountering `1`, calculate island area via `dfs(r, c)`.
- `dfs` sinks cell `grid[r][c] = 0` and returns `1 + dfs(up) + dfs(down) + dfs(left) + dfs(right)`.
- Track `maxArea = max(maxArea, area)`.
This evaluates max area in $\mathcal{O}(M \times N)$ time and $\mathcal{O}(1)$ auxiliary space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the **maximum size / area among connected components in a grid**.
- Grid DFS with Area Accumulation pattern.

---

## Important Clues

1. **"Maximum area of an island"**: Connected component area summation.
2. **"4-directionally connected land cells"**: Recursive 4-neighbor DFS traversal.

---

## Example

### Input
```text
grid = [
  [1, 1, 0],
  [1, 0, 0],
  [0, 0, 1]
]
```

### Visual Step-by-Step Progression

```text
Island 1:
(0,0), (0,1), (1,0) connected -> Area = 3

Island 2:
(2,2) isolated -> Area = 1

Max Area = max(3, 1) = 3
```

---

## Alternative Solutions

### Queue-Based BFS ($\mathcal{O}(M \times N)$ Time, $\mathcal{O}(\min(M, N))$ Space)
- Use `std::queue<pair<int,int>>` to count area of each island level-by-level.

---

## Edge Cases

1. **Grid with no land (all 0s)**: Returns `0`.
2. **Single cell grid**: `[[1]]` returns `1`, `[[0]]` returns `0`.
3. **Entire grid is land**: Returns $M \times N$.

---

## Interview Tips

- **Explain Recursive Return Summation**: State *"Returning `1 + dfs(up) + dfs(down) + dfs(left) + dfs(right)` accumulates the area of the current component recursively as the recursion unwinds."*

---

## Similar Problems

1. [LeetCode #200: Number of Islands](https://leetcode.com/problems/number-of-islands/)
2. [LeetCode #463: Island Perimeter](https://leetcode.com/problems/island-perimeter/)
3. [LeetCode #130: Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)

---

## Revision Notes

- Problem: Maximum area of 4-connected island in binary grid.
- Pattern: DFS Area Accumulation with In-Place Sinking.
- `int dfs(r, c)`: `if (outOfBounds || grid[r][c] == 0) return 0; grid[r][c] = 0; return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1);`
- Max area: `maxArea = max(maxArea, dfs(r, c));`
- Optimal Complexity: Time $\mathcal{O}(M \times N)$, Space $\mathcal{O}(1)$ auxiliary.
