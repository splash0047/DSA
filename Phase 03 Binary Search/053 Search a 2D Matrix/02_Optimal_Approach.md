# Search a 2D Matrix

## Pattern Used

- **Pattern**: **Virtual 1D Binary Search on 2D Matrix**
- **Concept**: Treat the $M \times N$ matrix as a single 1D array of length $M \times N$. Convert any 1D index `mid` to 2D matrix coordinates via:
  $$\text{row} = \text{mid} / n, \quad \text{col} = \text{mid} \pmod n$$

---

## Observation

1. Properties of the matrix:
   - Each row is sorted.
   - `matrix[i][0] > matrix[i-1][n-1]`.
2. This implies the entire 2D matrix is strictly non-decreasing when read row-by-row!
3. We can set `low = 0` and `high = (m * n) - 1`.
4. At each step `mid = low + (high - low) / 2`:
   - Access `val = matrix[mid / n][mid % n]`.
   - Perform standard binary search comparisons!

---

## Intuition

Flatten the 2D matrix conceptually into a 1D sorted array of length $M \times N$. Convert 1D binary search midpoint `mid` to matrix indices `(mid / n, mid % n)` in $\mathcal{O}(1)$ time.

---

## Algorithm

1. `m = matrix.size()`, `n = matrix[0].size()`.
2. `low = 0`, `high = (m * n) - 1`.
3. While `low <= high`:
   a. `mid = low + (high - low) / 2`.
   b. `val = matrix[mid / n][mid % n]`.
   c. If `val == target`, return `true`.
   d. If `val < target`, `low = mid + 1`.
   e. Else: `high = mid - 1`.
4. Return `false`.

---

## Clean C++17 Solution

```cpp
#include <vector>

class Solution {
public:
    bool searchMatrix(const std::vector<std::vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) return false;
        
        int m = matrix.size();
        int n = matrix[0].size();
        
        int low = 0;
        int high = (m * n) - 1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            int val = matrix[mid / n][mid % n];
            
            if (val == target) {
                return true;
            } else if (val < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        
        return false;
    }
};
```

---

## Dry Run

### Input
- `matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]` ($M=3, N=4$)
- `target = 3`

### Execution Trace

- `low = 0`, `high = 3 * 4 - 1 = 11`

| Step | `low` | `high` | `mid` | Row (`mid / 4`) | Col (`mid % 4`) | `val` | `val` vs Target (`3`) | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `0` | `11` | `5` | `1` | `1` | `matrix[1][1] = 11` | `11 > 3` | `high = mid - 1 = 4` |
| 2 | `0` | `4` | `2` | `0` | `2` | `matrix[0][2] = 5` | `5 > 3` | `high = mid - 1 = 1` |
| 3 | `0` | `1` | `0` | `0` | `0` | `matrix[0][0] = 1` | `1 < 3` | `low = mid + 1 = 1` |
| 4 | `1` | `1` | `1` | `0` | `1` | `matrix[0][1] = 3` | `3 == 3` (**Match!**) | **Return `true`** |

### Result
- Output: `true`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(\log(M \times N))$
  - Single binary search over $M \times N$ virtual 1D elements.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This is Optimal

- Meets the mandatory $\mathcal{O}(\log(M \times N))$ time and $\mathcal{O}(1)$ space constraints.

---

## Common Mistakes

1. **Confusing Row/Col Indexing**: Writing `mid / m` or `mid % m` instead of `mid / n` and `mid % n`. Divide and modulo must use the number of **columns** `n`!
2. **Integer Overflow for Large Dimensions**: If $M \times N > \text{INT\_MAX}$, `m * n` overflows. (Not an issue under $M, N \le 100$, but good to use `long long` for huge matrix dimensions).
