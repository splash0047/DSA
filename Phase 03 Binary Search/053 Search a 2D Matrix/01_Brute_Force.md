# Search a 2D Matrix

- **Problem Number**: 74
- **Platform**: LeetCode #74
- **Difficulty**: Medium
- **Pattern**: 2D Matrix Scan

---

## Brute Force Intuition

Iterate through every cell `matrix[r][c]` in the 2D matrix. If `matrix[r][c] == target`, return `true`.

---

## Algorithm

1. Loop `r` from `0` to `m - 1`.
2. Loop `c` from `0` to `n - 1`:
   a. If `matrix[r][c] == target`, return `true`.
3. Return `false`.

---

## Code

```cpp
#include <vector>

class Solution {
public:
    bool searchMatrix(const std::vector<std::vector<int>>& matrix, int target) {
        for (const auto& row : matrix) {
            for (int val : row) {
                if (val == target) {
                    return true;
                }
            }
        }
        return false;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(M \times N)$
  - Scans all $M \times N$ matrix elements.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

Linear scan takes $\mathcal{O}(M \times N)$ time. Because the first element of each row is greater than the last element of the previous row, the entire $M \times N$ matrix is **virtually a single sorted 1D array**. Using **1D Virtual Binary Search**, we can search the matrix in logarithmic $\mathcal{O}(\log(M \times N))$ time.
