# Rotting Oranges

- **Problem Number**: 994
- **Platform**: LeetCode #994
- **Difficulty**: Medium
- **Pattern**: Minute-by-Minute Full Grid Scan Simulation

---

## Brute Force Intuition

Simulate the rotting process minute by minute. On each minute:
1. Scan the grid to find all currently rotten oranges (`2`).
2. Rot any adjacent fresh orange (`1`), creating a newly rotted set of oranges.
3. If no fresh orange becomes rotted in a minute, check if any fresh orange remains. If fresh oranges remain, return `-1` (impossible). Otherwise, return total minutes.

---

## Algorithm

1. `minutes = 0`.
2. Loop:
   - Identify all `(r, c)` where `grid[r][c] == 2`.
   - `rottedThisTurn = false`.
   - For each rotten cell `(r, c)` found in snapshot:
     - Check 4 directions: if neighbor `(nr, nc)` is `1`, change `grid[nr][nc] = 2` and set `rottedThisTurn = true`.
   - If `!rottedThisTurn`: break.
   - `minutes++`.
3. Check if any `grid[r][c] == 1` exists. If yes, return `-1`.
4. Return `minutes`.

---

## Code

```cpp
#include <vector>

class Solution {
public:
    int orangesRotting(std::vector<std::vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int minutes = 0;
        int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        while (true) {
            std::vector<std::pair<int, int>> toRot;
            
            for (int r = 0; r < m; ++r) {
                for (int c = 0; c < n; ++c) {
                    if (grid[r][c] == 2) {
                        for (auto& d : dirs) {
                            int nr = r + d[0];
                            int nc = c + d[1];
                            if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                                toRot.push_back({nr, nc});
                            }
                        }
                    }
                }
            }
            
            if (toRot.empty()) break;
            
            for (auto& p : toRot) {
                grid[p.first][p.second] = 2;
            }
            
            minutes++;
        }
        
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == 1) return -1;
            }
        }
        
        return minutes;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}((M \times N)^2)$
  - Scanning the entire grid takes $\mathcal{O}(M \times N)$ per minute. In the worst case, $M \times N$ minutes elapse, resulting in quadratic runtime $\mathcal{O}((M \times N)^2)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(M \times N)$
  - Stores newly rotted cell pairs on each turn.

---

## Why This Approach Is Not Optimal

Scanning the whole grid repeatedly on every minute is redundant. Using **Multi-Source BFS**, we queue all initial rotten oranges simultaneously and process the contamination wave level-by-level in a single linear pass taking $\mathcal{O}(M \times N)$ time!
