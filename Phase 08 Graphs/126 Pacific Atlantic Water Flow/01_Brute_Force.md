# Pacific Atlantic Water Flow

- **Problem Number**: 417
- **Platform**: LeetCode #417
- **Difficulty**: Medium
- **Pattern**: Naive Top-Down DFS Search from Every Cell

---

## Brute Force Intuition

For every cell `(r, c)` in the grid:
- Run a DFS search to determine if water can reach the **Pacific Ocean** (top/left borders).
- Run another DFS search to determine if water can reach the **Atlantic Ocean** (bottom/right borders).
- If both DFS searches return `true`, add `[r, c]` to the result list.

---

## Algorithm

1. For each cell `(r, c)` in $M \times N$:
   - `canReachPacific = dfsPacific(r, c, visitedP)`.
   - `canReachAtlantic = dfsAtlantic(r, c, visitedA)`.
   - If both are `true`, append `[r, c]` to `ans`.
2. `dfsPacific(r, c)`:
   - If `r == 0 || c == 0`, return `true` (reached Pacific).
   - Recurse to valid neighbors `(nr, nc)` where `heights[nr][nc] <= heights[r][c]`.
3. `dfsAtlantic(r, c)`:
   - If `r == m - 1 || c == n - 1`, return `true` (reached Atlantic).
   - Recurse to valid neighbors `(nr, nc)` where `heights[nr][nc] <= heights[r][c]`.

---

## Code

```cpp
#include <vector>

class Solution {
private:
    bool dfsP(const std::vector<std::vector<int>>& heights, int r, int c, std::vector<std::vector<bool>>& visited) {
        int m = heights.size();
        int n = heights[0].size();
        
        if (r == 0 || c == 0) return true; // Reached Pacific
        
        visited[r][c] = true;
        int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        for (auto& dir : dirs) {
            int nr = r + dir[0];
            int nc = c + dir[1];
            
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc] && heights[nr][nc] <= heights[r][c]) {
                if (dfsP(heights, nr, nc, visited)) return true;
            }
        }
        
        return false;
    }

    bool dfsA(const std::vector<std::vector<int>>& heights, int r, int c, std::vector<std::vector<bool>>& visited) {
        int m = heights.size();
        int n = heights[0].size();
        
        if (r == m - 1 || c == n - 1) return true; // Reached Atlantic
        
        visited[r][c] = true;
        int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        for (auto& dir : dirs) {
            int nr = r + dir[0];
            int nc = c + dir[1];
            
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc] && heights[nr][nc] <= heights[r][c]) {
                if (dfsA(heights, nr, nc, visited)) return true;
            }
        }
        
        return false;
    }

public:
    std::vector<std::vector<int>> pacificAtlantic(std::vector<std::vector<int>>& heights) {
        if (heights.empty() || heights[0].empty()) return {};
        
        int m = heights.size();
        int n = heights[0].size();
        std::vector<std::vector<int>> ans;
        
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                std::vector<std::vector<bool>> visitedP(m, std::vector<bool>(n, false));
                std::vector<std::vector<bool>> visitedA(m, std::vector<bool>(n, false));
                
                if (dfsP(heights, r, c, visitedP) && dfsA(heights, r, c, visitedA)) {
                    ans.push_back({r, c});
                }
            }
        }
        
        return ans;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}((M \times N)^2)$
  - For each of the $M \times N$ cells, we launch DFS traversals visiting up to $M \times N$ cells, leading to quadratic time complexity $\mathcal{O}((M \times N)^2)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(M \times N)$
  - Call stack and boolean matrices allocated per cell check.

---

## Why This Approach Is Not Optimal

Starting DFS from every internal cell leads to quadratic $\mathcal{O}((M \times N)^2)$ time, causing TLE. Using **Reverse Ocean Boundary Reachability DFS (Ocean to Continent)**, we can solve the problem in linear $\mathcal{O}(M \times N)$ time!
