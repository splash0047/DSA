# Surrounded Regions

- **Problem Number**: 130
- **Platform**: LeetCode #130
- **Difficulty**: Medium
- **Pattern**: Component Traversal with Border Reachability Flag

---

## Brute Force Intuition

For every unvisited `'O'` cell in the inner region of the board:
1. Run DFS to collect all `'O'` cells belonging to the current connected component.
2. During DFS, check if any cell in the component touches the board boundary (`r == 0 || r == m - 1 || c == 0 || c == n - 1`).
3. If no cell in the component touches the border, flip all collected `'O'` cells to `'X'`.

---

## Algorithm

1. `visited` boolean matrix initialized to `false`.
2. For each cell `(r, c)` in board:
   - If `board[r][c] == 'O'` and `!visited[r][c]`:
     - `component = []`, `touchesBorder = false`.
     - `dfs(r, c, component, touchesBorder)`.
     - If `!touchesBorder`:
       - Flip every cell in `component` to `'X'`.
3. `dfs(r, c, component, touchesBorder)`:
   - If out of bounds or `board[r][c] == 'X'` or `visited[r][c]`: return.
   - If `r == 0 || r == m - 1 || c == 0 || c == n - 1`: `touchesBorder = true`.
   - `visited[r][c] = true`.
   - Add `(r, c)` to `component`.
   - Recurse 4 directions.

---

## Code

```cpp
#include <vector>

class Solution {
private:
    void dfs(const std::vector<std::vector<char>>& board, int r, int c, 
             std::vector<std::vector<bool>>& visited, 
             std::vector<std::pair<int, int>>& component, bool& touchesBorder) {
        int m = board.size();
        int n = board[0].size();
        
        if (r < 0 || r >= m || c < 0 || c >= n || board[r][c] == 'X' || visited[r][c]) {
            return;
        }
        
        if (r == 0 || r == m - 1 || c == 0 || c == n - 1) {
            touchesBorder = true;
        }
        
        visited[r][c] = true;
        component.push_back({r, c});
        
        dfs(board, r + 1, c, visited, component, touchesBorder);
        dfs(board, r - 1, c, visited, component, touchesBorder);
        dfs(board, r, c + 1, visited, component, touchesBorder);
        dfs(board, r, c - 1, visited, component, touchesBorder);
    }

public:
    void solve(std::vector<std::vector<char>>& board) {
        if (board.empty() || board[0].empty()) return;
        
        int m = board.size();
        int n = board[0].size();
        std::vector<std::vector<bool>> visited(m, std::vector<bool>(n, false));
        
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (board[r][c] == 'O' && !visited[r][c]) {
                    std::vector<std::pair<int, int>> component;
                    bool touchesBorder = false;
                    dfs(board, r, c, visited, component, touchesBorder);
                    
                    if (!touchesBorder) {
                        for (auto& p : component) {
                            board[p.first][p.second] = 'X';
                        }
                    }
                }
            }
        }
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(M \times N)$
  - Inspects every cell and component once.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(M \times N)$
  - Stores auxiliary `visited` matrix and `component` vector.

---

## Why This Approach Is Not Optimal

Collecting component cell lists and allocating auxiliary visited arrays uses unnecessary memory. Using **Border DFS Protection (Mark 'E' Sentinel)**, we can mark all border-connected `'O'`s as safe in a single pass without storing cell coordinates or using auxiliary boolean matrices!
