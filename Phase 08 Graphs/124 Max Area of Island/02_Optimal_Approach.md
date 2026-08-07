# Max Area of Island

## Pattern Used

- **Pattern**: **In-Place Sinking DFS / Area Accumulation**
- **Concept**:
  - Iterate through every cell `(r, c)` in `grid`.
  - When encountering `1` (land):
    - Compute area of island using recursive DFS helper `dfs(grid, r, c)`.
    - `dfs` sinks visited land cells by setting `grid[r][c] = 0` and returns `1 + dfs(up) + dfs(down) + dfs(left) + dfs(right)`.
    - Update `maxArea = max(maxArea, area)`.

---

## Observation

1. Sinking visited land cells `grid[r][c] = 0` in-place prevents visiting the same land cell multiple times without allocating an auxiliary boolean array.
2. The area of an island is equal to `1` (current cell) plus the sum of areas of its 4 neighboring sub-regions.

---

## Intuition

Whenever you step on an island, measure its size by walking through all connected land cells, marking each cell as visited by sinking it to `0` so it won't be counted again. Track the maximum island size seen across the entire grid.

---

## Algorithm

1. `maxAreaOfIsland(grid)`:
   - `maxArea = 0`.
   - Loop `r` from `0` to `m - 1` and `c` from `0` to `n - 1`:
     - If `grid[r][c] == 1`:
       - `area = dfs(grid, r, c)`.
       - `maxArea = max(maxArea, area)`.
   - Return `maxArea`.
2. `dfs(grid, r, c)`:
   - Base case: If `r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0`, return `0`.
   - Sink cell: `grid[r][c] = 0`.
   - Return `1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>

class Solution {
private:
    int dfs(std::vector<std::vector<int>>& grid, int r, int c) {
        int m = grid.size();
        int n = grid[0].size();
        
        // Out-of-bounds or water check
        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0) {
            return 0;
        }
        
        // Mark cell as visited by sinking it
        grid[r][c] = 0;
        
        // Sum current cell (1) + all 4 directional connected land areas
        return 1 + dfs(grid, r + 1, c)
                 + dfs(grid, r - 1, c)
                 + dfs(grid, r, c + 1)
                 + dfs(grid, r, c - 1);
    }

public:
    int maxAreaOfIsland(std::vector<std::vector<int>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        
        int m = grid.size();
        int n = grid[0].size();
        int maxArea = 0;
        
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == 1) {
                    int area = dfs(grid, r, c);
                    maxArea = std::max(maxArea, area);
                }
            }
        }
        
        return maxArea;
    }
};
```

---

## Dry Run

### Input
```text
grid = [
  [1, 1, 0],
  [1, 0, 0],
  [0, 0, 1]
]
```

### Execution Trace

1. `(r=0, c=0)`: `grid[0][0] == 1`. Call `dfs(0, 0)`:
   - `grid[0][0]` set to `0`. Recurse:
     - `(1,0)` set to `0`, returns `1`.
     - `(0,1)` set to `0`, returns `1`.
   - Total area returned for component = `1 + 1 + 1 = 3`.
   - `maxArea = max(0, 3) = 3`.
2. `(r=2, c=2)`: `grid[2][2] == 1`. Call `dfs(2, 2)`:
   - `grid[2][2]` set to `0`. Area returned = `1`.
   - `maxArea = max(3, 1) = 3`.

### Result
- Output: `3`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(M \times N)$
  - Every cell in the grid is visited constant times.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(M \times N)$ worst-case call stack depth for a completely filled land grid. $\mathcal{O}(1)$ auxiliary space.

---

## Why This is Optimal

- Computes max island area in a single linear pass over the grid.
- Modifies input grid in-place to achieve $\mathcal{O}(1)$ auxiliary heap memory.

---

## Common Mistakes

1. **Forgetting to Sink Cell**: Forgetting `grid[r][c] = 0` leads to infinite call stack recursion.
2. **Missing Boundary Guard**: Not checking bounds `r < 0 || r >= m || c < 0 || c >= n` leads to segmentation faults.
