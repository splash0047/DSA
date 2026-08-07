# Rotting Oranges

## Pattern Used

- **Pattern**: **Multi-Source Queue-Based BFS (Level-by-Level Contamination Spread)**
- **Concept**:
  - Count total `freshOranges` and enqueue all initially rotten oranges `2` into a `queue<pair<int, int>> q`.
  - Perform level-order BFS:
    - At each level (representing 1 minute of time), record `sz = q.size()`.
    - Pop `sz` rotten oranges, inspect their 4-directional neighbors.
    - If a neighbor is fresh (`1`):
      - Mutate `grid[nr][nc] = 2` (rotten!).
      - Decrement `freshOranges--`.
      - Push `(nr, nc)` into `q`.
    - Increment `minutes` after processing level if any fresh orange was rotted.
  - Return `freshOranges == 0 ? minutes : -1`.

---

## Observation

1. All initially rotten oranges start rotting their neighbors simultaneously at minute 0. This is the exact definition of **Multi-Source BFS**!
2. BFS naturally processes cells level-by-level (minute-by-minute) along shortest path distances.

---

## Intuition

Put all initially rotten oranges into a queue at time 0. Each minute, pop all oranges currently in the queue and infect their 4 fresh neighbors. Add the newly infected oranges to the queue for the next minute. Continue until the queue is empty.

---

## Algorithm

1. `queue<pair<int, int>> q`. `fresh = 0`, `minutes = 0`.
2. Scan grid:
   - If `grid[r][c] == 2`: `q.push({r, c})`.
   - If `grid[r][c] == 1`: `fresh++`.
3. If `fresh == 0`, return `0`.
4. Directions: `dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}}`.
5. While `!q.empty() && fresh > 0`:
   a. `sz = q.size()`.
   b. `minutes++`.
   c. For `i` from `0` to `sz - 1`:
      - `curr = q.front(); q.pop();`
      - For each `d` in `dirs`:
        - `nr = curr.first + d[0]`, `nc = curr.second + d[1]`.
        - If `nr, nc` valid and `grid[nr][nc] == 1`:
          - `grid[nr][nc] = 2`.
          - `fresh--`.
          - `q.push({nr, nc})`.
6. Return `fresh == 0 ? minutes : -1`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <queue>

class Solution {
public:
    int orangesRotting(std::vector<std::vector<int>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        
        int m = grid.size();
        int n = grid[0].size();
        
        std::queue<std::pair<int, int>> q;
        int freshCount = 0;
        
        // Push all initial rotten oranges to queue & count fresh oranges
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == 2) {
                    q.push({r, c});
                } else if (grid[r][c] == 1) {
                    freshCount++;
                }
            }
        }
        
        // Edge Case: No fresh oranges to rot
        if (freshCount == 0) return 0;
        
        int minutes = 0;
        int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        // Multi-source BFS level traversal
        while (!q.empty() && freshCount > 0) {
            int sz = q.size();
            minutes++;
            
            for (int i = 0; i < sz; ++i) {
                auto [r, c] = q.front();
                q.pop();
                
                for (auto& d : dirs) {
                    int nr = r + d[0];
                    int nc = c + d[1];
                    
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2; // Mark as rotten
                        freshCount--;
                        q.push({nr, nc});
                    }
                }
            }
        }
        
        return freshCount == 0 ? minutes : -1;
    }
};
```

---

## Dry Run

### Input
- `grid = [[2,1,1],[1,1,0],[0,1,1]]`

### Execution Trace

- Initial scan: `q = [(0,0)]`, `freshCount = 6`.
- Minute 1 (`sz=1`): Pop `(0,0)`. Rots `(0,1)` and `(1,0)`. `freshCount = 4`. `q = [(0,1), (1,0)]`.
- Minute 2 (`sz=2`): Pop `(0,1)`, `(1,0)`. Rots `(0,2)`, `(1,1)`. `freshCount = 2`. `q = [(0,2), (1,1)]`.
- Minute 3 (`sz=2`): Pop `(0,2)`, `(1,1)`. Rots `(2,1)`. `freshCount = 1`. `q = [(2,1)]`.
- Minute 4 (`sz=1`): Pop `(2,1)`. Rots `(2,2)`. `freshCount = 0`. `q = [(2,2)]`.
- Loop terminates (`freshCount == 0`).

### Result
- Output: `4`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(M \times N)$
  - Every cell is enqueued and dequeued at most once.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(M \times N)$
  - Queue stores up to $M \times N$ cell coordinates.

---

## Why This is Optimal

- Multi-source BFS computes shortest propagation time to all reachable fresh oranges in linear $\mathcal{O}(M \times N)$ time.

---

## Common Mistakes

1. **Incrementing Minutes When Queue Is Empty**: Incrementing `minutes` after processing the last level when no fresh oranges were rotted adds 1 extra minute. `while (!q.empty() && freshCount > 0)` prevents this.
2. **Single Source BFS**: Running BFS independently for each rotten orange instead of multi-source enqueuing.
