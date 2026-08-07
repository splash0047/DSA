# Search a 2D Matrix II

## Pattern Used

- **Pattern**: **Top-Right Corner Pointer Traversal (BST Analogy)**
- **Concept**: Start at the top-right corner `(r = 0, c = n - 1)`. At this cell:
  - All elements to its **left** are smaller.
  - All elements below it in its **column** are larger.
  - This behaves exactly like a **Binary Search Tree**!

---

## Observation

1. Position at `matrix[r][c]`:
   - If `matrix[r][c] == target`: Found target! Return `true`.
   - If `matrix[r][c] > target`: Target MUST be smaller. Because column `c` goes downward (getting even larger), no element in column `c` can equal `target`. We eliminate column `c` $\rightarrow$ `c--`.
   - If `matrix[r][c] < target`: Target MUST be larger. Because row `r` goes leftward (getting even smaller), no element in row `r` can equal `target`. We eliminate row `r` $\rightarrow$ `r++`.
2. In each step, we eliminate either 1 row or 1 column!

---

## Intuition

Start at top-right `(0, n-1)`:
- Number too big? Move left (`c--`).
- Number too small? Move down (`r++`).
- Stops in at most $M + N$ steps.

---

## Algorithm

1. `r = 0`, `c = matrix[0].size() - 1`.
2. While `r < matrix.size()` and `c >= 0`:
   a. `val = matrix[r][c]`.
   b. If `val == target`: return `true`.
   c. If `val > target`: `c--`.
   d. Else: `r++`.
3. Return `false`.

---

## Clean C++17 Solution

```cpp
#include <vector>

class Solution {
public:
    bool searchMatrix(const std::vector<std::vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) return false;
        
        int r = 0;
        int c = matrix[0].size() - 1;
        int m = matrix.size();
        
        while (r < m && c >= 0) {
            int val = matrix[r][c];
            
            if (val == target) {
                return true;
            } else if (val > target) {
                c--; // Move left (smaller numbers)
            } else {
                r++; // Move down (larger numbers)
            }
        }
        
        return false;
    }
};
```

---

## Dry Run

### Input
- `matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22]]` ($M=3, N=5$)
- `target = 5`

### Execution Trace

| Step | `r` | `c` | `matrix[r][c]` | Compare with Target (`5`) | Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `0` | `4` | `15` | `15 > 5` | `c--` (`c=3`) |
| 2 | `0` | `3` | `11` | `11 > 5` | `c--` (`c=2`) |
| 3 | `0` | `2` | `7` | `7 > 5` | `c--` (`c=1`) |
| 4 | `0` | `1` | `4` | `4 < 5` | `r++` (`r=1`) |
| 5 | `1` | `1` | `5` | `5 == 5` (**Match!**) | **Return `true`** |

### Result
- Output: `true`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(M + N)$
  - At each step, either `r` increments or `c` decrements.
  - The loop runs at most $M + N$ times.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This is Optimal

- Prunes matrix in linear $\mathcal{O}(M + N)$ time.
- Uses zero extra memory.

---

## Common Mistakes

1. **Starting at Top-Left `(0, 0)`**: Starting at `(0, 0)` is ambiguous because both moving right and moving down increase the value! Starting at top-right `(0, n-1)` provides orthogonal decisions (left decreases, down increases).
2. **Out-of-Bounds Loop Condition**: Writing `c > 0` instead of `c >= 0` misses checking column 0.
