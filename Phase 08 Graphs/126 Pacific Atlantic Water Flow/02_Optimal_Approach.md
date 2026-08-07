# Pacific Atlantic Water Flow

## Pattern Used

- **Pattern**: **Multi-Source Reverse DFS / BFS from Ocean Boundaries**
- **Concept**:
  - Instead of flowing water downward from inner cells to oceans, **flow water upward** from the ocean boundaries into the island!
  - Maintain two boolean matrices:
    - `pacific[m][n]`: `true` if water can reach cell from Pacific.
    - `atlantic[m][n]`: `true` if water can reach cell from Atlantic.
  - Run DFS starting from Pacific border cells (top row + left column) upwards to higher/equal cells.
  - Run DFS starting from Atlantic border cells (bottom row + right column) upwards to higher/equal cells.
  - Any cell `(r, c)` where `pacific[r][c] && atlantic[r][c]` is `true` can flow water to both oceans!

---

## Observation

1. Water flowing downward from height $H_1$ to $H_2$ ($H_1 \ge H_2$) is mathematically identical to water flowing upward from $H_2$ to $H_1$ ($H_2 \le H_1$).
2. By starting from the 4 ocean borders, we perform only TWO multi-source DFS traversals instead of $M \times N$ individual searches!

---

## Intuition

Imagine ocean water rising:
- Start at the Pacific ocean borders (top row and left col) and let water flow uphill to all reachable higher/equal ground. Mark all reached cells in `pacific` map.
- Start at the Atlantic ocean borders (bottom row and right col) and let water flow uphill. Mark all reached cells in `atlantic` map.
- Cells marked in BOTH maps can flow water downhill to both oceans!

---

## Algorithm

1. Initialize `pacific[m][n]` and `atlantic[m][n]` boolean matrices to `false`.
2. For top row (`r=0`) and bottom row (`r=m-1`):
   - `dfs(0, c, pacific, heights[0][c])`.
   - `dfs(m-1, c, atlantic, heights[m-1][c])`.
3. For left col (`c=0`) and right col (`c=n-1`):
   - `dfs(r, 0, pacific, heights[r][0])`.
   - `dfs(r, n-1, atlantic, heights[r][n-1])`.
4. `dfs(r, c, ocean, prevHeight)`:
   - If out-of-bounds or `ocean[r][c] == true` or `heights[r][c] < prevHeight`, return.
   - `ocean[r][c] = true`.
   - Recurse 4 directions passing `heights[r][c]` as `prevHeight`.
5. Loop all `(r, c)`: If `pacific[r][c] && atlantic[r][c]`, push `[r, c]` to `ans`.
6. Return `ans`.

---

## Clean C++17 Solution

```cpp
#include <vector>

class Solution {
private:
    void dfs(const std::vector<std::vector<int>>& heights, int r, int c, 
             std::vector<std::vector<bool>>& ocean, int prevHeight) {
        int m = heights.size();
        int n = heights[0].size();
        
        // Out-of-bounds, already visited, or height is lower than previous (uphill flow condition fails)
        if (r < 0 || r >= m || c < 0 || c >= n || ocean[r][c] || heights[r][c] < prevHeight) {
            return;
        }
        
        ocean[r][c] = true;
        
        // Flow uphill to 4 directional neighbors
        dfs(heights, r + 1, c, ocean, heights[r][c]);
        dfs(heights, r - 1, c, ocean, heights[r][c]);
        dfs(heights, r, c + 1, ocean, heights[r][c]);
        dfs(heights, r, c - 1, ocean, heights[r][c]);
    }

public:
    std::vector<std::vector<int>> pacificAtlantic(std::vector<std::vector<int>>& heights) {
        if (heights.empty() || heights[0].empty()) return {};
        
        int m = heights.size();
        int n = heights[0].size();
        
        std::vector<std::vector<bool>> pacific(m, std::vector<bool>(n, false));
        std::vector<std::vector<bool>> atlantic(m, std::vector<bool>(n, false));
        
        // DFS from Pacific (Top border) and Atlantic (Bottom border)
        for (int c = 0; c < n; ++c) {
            dfs(heights, 0, c, pacific, heights[0][c]);
            dfs(heights, m - 1, c, atlantic, heights[m - 1][c]);
        }
        
        // DFS from Pacific (Left border) and Atlantic (Right border)
        for (int r = 0; r < m; ++r) {
            dfs(heights, r, 0, pacific, heights[r][0]);
            dfs(heights, r, n - 1, atlantic, heights[r][n - 1]);
        }
        
        // Collect cells reachable from both oceans
        std::vector<std::vector<int>> result;
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (pacific[r][c] && atlantic[r][c]) {
                    result.push_back({r, c});
                }
            }
        }
        
        return result;
    }
};
```

---

## Dry Run

### Input
- $2 \times 2$ grid: `[[1, 2], [2, 1]]`

### Execution Trace

- Pacific borders: `(0,0)`, `(0,1)`, `(1,0)`.
  - `(0,0)=1` $\implies$ flows to `(0,1)=2` and `(1,0)=2`. `pacific` = `[[T, T], [T, F]]`.
- Atlantic borders: `(1,1)`, `(1,0)`, `(0,1)`.
  - `(1,1)=1` $\implies$ flows to `(0,1)=2` and `(1,0)=2`. `atlantic` = `[[F, T], [T, T]]`.
- Overlap `pacific && atlantic`:
  - `(0,1)` is T & T $\implies$ `[0, 1]`.
  - `(1,0)` is T & T $\implies$ `[1, 0]`.

### Result
- Output: `[[0, 1], [1, 0]]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(M \times N)$
  - Each cell is visited at most twice (once during Pacific DFS, once during Atlantic DFS).

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(M \times N)$
  - Stores two $M \times N$ boolean matrices `pacific` and `atlantic` plus call stack space.

---

## Why This is Optimal

- Reversing flow direction from ocean borders inward reduces time from quadratic $\mathcal{O}((M \times N)^2)$ to optimal linear $\mathcal{O}(M \times N)$.

---

## Common Mistakes

1. **Reversing Flow Condition**: Writing `heights[r][c] > prevHeight` instead of `heights[r][c] < prevHeight` in reverse DFS.
2. **Missing Boundary Cells**: Forgetting that corner cells belong to both ocean boundaries.
