# Number of Islands

- **Problem Number**: 200
- **Platform**: LeetCode #200
- **Difficulty**: Medium
- **Pattern**: Grid Traversal with Auxiliary Visited Matrix

---

## Brute Force Intuition

Iterate through every cell `(r, c)` in the 2D grid. When an unvisited land cell `'1'` is encountered:
- Increment island count `islands++`.
- Launch a recursive Depth-First Search (DFS) from `(r, c)` to mark all 4-directionally connected land cells `'1'` as visited using an auxiliary boolean matrix `visited[m][n]`.

---

## Algorithm

1. Create a 2D boolean array `visited[m][n]` initialized to `false`.
2. `islands = 0`.
3. Loop through row `r` from `0` to `m - 1` and column `c` from `0` to `n - 1`:
   - If `grid[r][c] == '1'` and `!visited[r][c]`:
     - `islands++`.
     - `dfs(grid, r, c, visited)`.
4. `dfs(grid, r, c, visited)`:
   - If `r < 0 || r >= m || c < 0 || c >= n` or `grid[r][c] == '0'` or `visited[r][c]`: return.
   - Set `visited[r][c] = true`.
   - Recursively call `dfs` on `(r+1, c)`, `(r-1, c)`, `(r, c+1)`, `(r, c-1)`.
5. Return `islands`.

---

## Code

```cpp
#include <vector>

class Solution {
private:
    void dfs(const std::vector<std::vector<char>>& grid, int r, int c, std::vector<std::vector<bool>>& visited) {
        int m = grid.size();
        int n = grid[0].size();
        
        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == '0' || visited[r][c]) {
            return;
        }
        
        visited[r][c] = true;
        
        dfs(grid, r + 1, c, visited);
        dfs(grid, r - 1, c, visited);
        dfs(grid, r, c + 1, visited);
        dfs(grid, r, c - 1, visited);
    }

public:
    int numIslands(std::vector<std::vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        
        int m = grid.size();
        int n = grid[0].size();
        std::vector<std::vector<bool>> visited(m, std::vector<bool>(n, false));
        int islands = 0;
        
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == '1' && !visited[r][c]) {
                    islands++;
                    dfs(grid, r, c, visited);
                }
            }
        }
        
        return islands;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(M \times N)$
  - Every cell in the $M \times N$ grid is visited at most constant times.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(M \times N)$
  - Requires extra $\mathcal{O}(M \times N)$ memory for the boolean `visited` matrix plus call stack space.

---

## Why This Approach Is Not Optimal

Allocating an extra $M \times N$ boolean array consumes unnecessary auxiliary memory. Using **In-Place Grid Sink DFS (Mutating Grid)** or **BFS / Disjoint Set Union (DSU)**, we can achieve $\mathcal{O}(1)$ extra auxiliary memory by mutating visited land cells `'1'` directly to `'0'`!
