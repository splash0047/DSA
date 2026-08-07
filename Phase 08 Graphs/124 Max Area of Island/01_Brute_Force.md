# Max Area of Island

- **Problem Number**: 695
- **Platform**: LeetCode #695
- **Difficulty**: Medium
- **Pattern**: Grid Traversal with Visited Matrix

---

## Brute Force Intuition

Iterate over every cell `(r, c)` in the binary matrix. When encountering an unvisited land cell `1`:
- Perform Depth-First Search (DFS) to visit all 4-directionally connected land cells.
- Count the number of land cells visited in this connected component (the area).
- Keep track of visited cells using an auxiliary `vector<vector<bool>> visited`.
- Update `max_area = max(max_area, current_island_area)`.

---

## Algorithm

1. Create boolean matrix `visited[m][n]` initialized to `false`.
2. `maxArea = 0`.
3. Loop `r` from `0` to `m - 1` and `c` from `0` to `n - 1`:
   - If `grid[r][c] == 1` and `!visited[r][c]`:
     - `area = getArea(grid, r, c, visited)`.
     - `maxArea = max(maxArea, area)`.
4. `getArea(grid, r, c, visited)`:
   - If `r < 0 || r >= m || c < 0 || c >= n` or `grid[r][c] == 0` or `visited[r][c]`: return `0`.
   - `visited[r][c] = true`.
   - Return `1 + getArea(r+1,c) + getArea(r-1,c) + getArea(r,c+1) + getArea(r,c-1)`.
5. Return `maxArea`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
private:
    int getArea(const std::vector<std::vector<int>>& grid, int r, int c, std::vector<std::vector<bool>>& visited) {
        int m = grid.size();
        int n = grid[0].size();
        
        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0 || visited[r][c]) {
            return 0;
        }
        
        visited[r][c] = true;
        
        return 1 + getArea(grid, r + 1, c, visited)
                 + getArea(grid, r - 1, c, visited)
                 + getArea(grid, r, c + 1, visited)
                 + getArea(grid, r, c - 1, visited);
    }

public:
    int maxAreaOfIsland(std::vector<std::vector<int>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        
        int m = grid.size();
        int n = grid[0].size();
        std::vector<std::vector<bool>> visited(m, std::vector<bool>(n, false));
        int maxArea = 0;
        
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == 1 && !visited[r][c]) {
                    int area = getArea(grid, r, c, visited);
                    maxArea = std::max(maxArea, area);
                }
            }
        }
        
        return maxArea;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(M \times N)$
  - Inspects every cell in the $M \times N$ grid once.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(M \times N)$
  - Requires auxiliary $M \times N$ boolean matrix for `visited`.

---

## Why This Approach Is Not Optimal

Allocating an extra boolean matrix consumes unnecessary memory. Mutating the input grid in-place (`grid[r][c] = 0`) eliminates extra auxiliary space!
