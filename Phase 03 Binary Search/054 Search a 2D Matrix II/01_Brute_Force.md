# Search a 2D Matrix II

- **Problem Number**: 240
- **Platform**: LeetCode #240
- **Difficulty**: Medium
- **Pattern**: Binary Search Each Row

---

## Brute Force Intuition

For each row in `matrix`, call `std::binary_search` to check if `target` exists in that row.

---

## Algorithm

1. Loop through each row `row` in `matrix`:
   a. Run binary search on `row` for `target`.
   b. If found, return `true`.
2. Return `false`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    bool searchMatrix(const std::vector<std::vector<int>>& matrix, int target) {
        for (const auto& row : matrix) {
            if (std::binary_search(row.begin(), row.end(), target)) {
                return true;
            }
        }
        return false;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(M \log N)$
  - Binary search takes $\mathcal{O}(\log N)$ per row, repeated for $M$ rows.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

Running binary search on each row takes $\mathcal{O}(M \log N)$ time and ignores the fact that **columns are also sorted**. Starting at the **Top-Right Corner (or Bottom-Left Corner)** allows us to prune an entire row or column at each step in linear $\mathcal{O}(M + N)$ time.
