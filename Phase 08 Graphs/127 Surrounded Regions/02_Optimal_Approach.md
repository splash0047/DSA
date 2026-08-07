# Surrounded Regions

## Pattern Used

- **Pattern**: **Boundary DFS Marking (Sentinel Value Substitution)**
- **Concept**:
  - Reverse the problem: Any `'O'` region that touches the border CANNOT be captured. Any `'O'` connected to a border `'O'` is also immune!
  - Step 1: Run DFS starting from all border `'O'`s (top, bottom, left, right edges) and temporarily mark all reached `'O'`s as `'E'` (Escaped/Safe).
  - Step 2: Iterate over the entire grid:
    - Flip any remaining `'O'` to `'X'` (these are strictly surrounded!).
    - Restore any `'E'` back to `'O'` (these were border-connected and safe!).

---

## Observation

1. Instead of identifying surrounded regions, identify **UNSURROUNDED** regions first by starting from border cells.
2. Replacing safe `'O'`s with temporary character `'E'` in-place acts as a visit marker and avoids auxiliary memory.

---

## Intuition

Think of `'O'`s on the border as "doors". Flood-fill through all open doors on the border and tag every reachable `'O'` as "escaped" (`'E'`). Once finished, any `'O'` still left inside the board is trapped and gets converted to `'X'`. Finally, turn all `'E'`s back to `'O'`.

---

## Algorithm

1. `markEscaped(r, c)`:
   - If out of bounds or `board[r][c] != 'O'`, return.
   - `board[r][c] = 'E'`.
   - Recurse 4 directions.
2. Step 1: Call `markEscaped` for all border cells:
   - Top row (`r = 0`) & Bottom row (`r = m - 1`).
   - Left col (`c = 0`) & Right col (`c = n - 1`).
3. Step 2: Iterate through entire matrix `(r, c)`:
   - If `board[r][c] == 'O'`: set `board[r][c] = 'X'`.
   - If `board[r][c] == 'E'`: set `board[r][c] = 'O'`.

---

## Clean C++17 Solution

```cpp
#include <vector>

class Solution {
private:
    void markEscaped(std::vector<std::vector<char>>& board, int r, int c) {
        int m = board.size();
        int n = board[0].size();
        
        // Out of bounds or not an 'O' cell
        if (r < 0 || r >= m || c < 0 || c >= n || board[r][c] != 'O') {
            return;
        }
        
        // Mark as 'E' (Escaped / Safe from being flipped)
        board[r][c] = 'E';
        
        // Flood fill 4 directions
        markEscaped(board, r + 1, c);
        markEscaped(board, r - 1, c);
        markEscaped(board, r, c + 1);
        markEscaped(board, r, c - 1);
    }

public:
    void solve(std::vector<std::vector<char>>& board) {
        if (board.empty() || board[0].empty()) return;
        
        int m = board.size();
        int n = board[0].size();
        
        // Step 1: Mark all border-connected 'O's as 'E'
        for (int c = 0; c < n; ++c) {
            if (board[0][c] == 'O') markEscaped(board, 0, c);
            if (board[m - 1][c] == 'O') markEscaped(board, m - 1, c);
        }
        for (int r = 0; r < m; ++r) {
            if (board[r][0] == 'O') markEscaped(board, r, 0);
            if (board[r][n - 1] == 'O') markEscaped(board, r, n - 1);
        }
        
        // Step 2: Flip remaining 'O' -> 'X', and restore 'E' -> 'O'
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (board[r][c] == 'O') {
                    board[r][c] = 'X';
                } else if (board[r][c] == 'E') {
                    board[r][c] = 'O';
                }
            }
        }
    }
};
```

---

## Dry Run

### Input
```text
board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]
```

### Execution Trace

1. Border `'O'` check:
   - Border cell `(3, 1)` is `'O'`. Call `markEscaped(3, 1)` $\implies$ sets `board[3][1] = 'E'`.
   - Neighbor of `(3,1)` is `(2,1)` which is `'X'`. DFS ends.
   - Board state:
     ```text
     ["X","X","X","X"],
     ["X","O","O","X"],
     ["X","X","O","X"],
     ["X","E","X","X"]
     ```
2. Scan and flip:
   - Internal `'O'`s at `(1,1)`, `(1,2)`, `(2,2)` become `'X'`.
   - `(3,1)` `'E'` restored back to `'O'`.

### Result
```text
[
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(M \times N)$
  - Each cell is visited constant times across DFS marking and matrix traversal.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(M \times N)$ worst-case recursion call stack depth. $\mathcal{O}(1)$ auxiliary heap memory.

---

## Why This is Optimal

- Solves surrounded regions capturing in optimal linear $\mathcal{O}(M \times N)$ time.
- Uses temporary character `'E'` in-place, eliminating auxiliary memory requirements.

---

## Common Mistakes

1. **Flipping Border Connected 'O's**: Forgetting that border-connected `'O'`s are safe.
2. **Missing Restore Step**: Forgetting to convert `'E'` back to `'O'` in the final pass.
