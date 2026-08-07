# Number of Islands

## Pattern Used

- **Pattern**: **Grid Traversal via Depth-First Search (DFS) / Breadth-First Search (BFS) with In-Place Sinking**
- **Concept**:
  - Iterate through every cell `(r, c)` in the grid.
  - When encountering `'1'` (land):
    - Increment `islands`.
    - Immediately mutate `grid[r][c] = '0'` ("sink" the land) and recursively traverse 4 adjacent directions (up, down, left, right) sinking all connected `'1'`s.
  - Mutating visited land cells to `'0'` eliminates the need for an auxiliary `visited` matrix!

---

## Observation

1. An island is defined as a connected component of `'1'`s.
2. Changing visited `'1'`s to `'0'` ("sinking the island") serves as a natural visit flag, preventing infinite recursion loops without allocating extra memory.

---

## Intuition

Whenever you discover a piece of land `'1'`, you count a new island. Then, flood-fill that entire island by sinking all attached land cells to `'0'` so you don't count any part of the same island again later.

---

## Algorithm

1. `numIslands(grid)`:
   - Loop `r` from `0` to `m - 1` and `c` from `0` to `n - 1`:
     - If `grid[r][c] == '1'`:
       - `islands++`.
       - `sink(grid, r, c)`.
   - Return `islands`.
2. `sink(grid, r, c)`:
   - Base Case: If `r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == '0'`, return.
   - `grid[r][c] = '0'`.
   - Recursively call `sink` for `(r+1, c)`, `(r-1, c)`, `(r, c+1)`, `(r, c-1)`.

---

## Clean C++17 Solution

```cpp
#include <vector>

class Solution {
private:
    void sink(std::vector<std::vector<char>>& grid, int r, int c) {
        int m = grid.size();
        int n = grid[0].size();
        
        // Out of bounds or water cell check
        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == '0') {
            return;
        }
        
        // Mutate land cell to water to mark as visited
        grid[r][c] = '0';
        
        // Traverse 4 directional neighbors
        sink(grid, r + 1, c);
        sink(grid, r - 1, c);
        sink(grid, r, c + 1);
        sink(grid, r, c - 1);
    }

public:
    int numIslands(std::vector<std::vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        
        int m = grid.size();
        int n = grid[0].size();
        int islands = 0;
        
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == '1') {
                    islands++;
                    sink(grid, r, c);
                }
            }
        }
        
        return islands;
    }
};
```

---

## Dry Run

### Input
```text
grid = [
  ["1","1","0"],
  ["1","0","0"],
  ["0","0","1"]
]
```

### Execution Trace

1. `(r=0, c=0)`: `grid[0][0] == '1'` $\implies$ `islands = 1`. Call `sink(0, 0)`:
   - Sets `grid[0][0] = '0'`.
   - Visits `(1,0)` $\implies$ sets `grid[1][0] = '0'`.
   - Visits `(0,1)` $\implies$ sets `grid[0][1] = '0'`.
2. Scan continues: `(0,2)`, `(1,1)`, `(1,2)` are all `'0'`.
3. `(r=2, c=2)`: `grid[2][2] == '1'` $\implies$ `islands = 2`. Call `sink(2, 2)`:
   - Sets `grid[2][2] = '0'`.

### Result
- Output: `2`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(M \times N)$
  - Every cell in the grid is inspected once in the nested loop and visited at most once during DFS traversal.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(M \times N)$ worst-case call stack depth for a grid filled entirely with land (`'1'`). $\mathcal{O}(1)$ auxiliary heap memory.

---

## Why This is Optimal

- Operates in linear time relative to grid size $\mathcal{O}(M \times N)$.
- Eliminates auxiliary visited space by mutating input grid in-place.

---

## Common Mistakes

1. **Forgetting Boundary Checks**: Missing `r < 0 || r >= m || c < 0 || c >= n` leading to out-of-bounds array access.
2. **Not Checking for Water Before Recursive Calls**: Forgetting `grid[r][c] == '0'` causing stack overflow recursion loops.
