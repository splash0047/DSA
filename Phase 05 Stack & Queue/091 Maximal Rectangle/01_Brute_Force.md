# Maximal Rectangle

- **Problem Number**: 85
- **Platform**: LeetCode #85
- **Difficulty**: Hard
- **Pattern**: Quadruple Loop Subgrid Check

---

## Brute Force Intuition

Check all possible top-left `(r1, c1)` and bottom-right `(r2, c2)` subgrid boundaries in the matrix. Verify if every cell within `(r1, c1)` to `(r2, c2)` contains `'1'`. If valid, update `max_area` with `(r2 - r1 + 1) * (c2 - c1 + 1)`.

---

## Algorithm

1. `max_area = 0`.
2. Loop `r1` from `0` to `rows - 1`:
   a. Loop `c1` from `0` to `cols - 1`:
      - Loop `r2` from `r1` to `rows - 1`:
        - Loop `c2` from `c1` to `cols - 1`:
          - Check if all cells in subgrid `(r1, c1)` to `(r2, c2)` are `'1'`.
          - If valid: `max_area = max(max_area, (r2 - r1 + 1) * (c2 - c1 + 1))`.
3. Return `max_area`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int maximalRectangle(const std::vector<std::vector<char>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return 0;
        
        int rows = matrix.size();
        int cols = matrix[0].size();
        int max_area = 0;
        
        for (int r1 = 0; r1 < rows; ++r1) {
            for (int c1 = 0; c1 < cols; ++c1) {
                for (int r2 = r1; r2 < rows; ++r2) {
                    for (int c2 = c1; c2 < cols; ++c2) {
                        bool all_ones = true;
                        for (int r = r1; r <= r2 && all_ones; ++r) {
                            for (int c = c1; c <= c2 && all_ones; ++c) {
                                if (matrix[r][c] == '0') {
                                    all_ones = false;
                                }
                            }
                        }
                        if (all_ones) {
                            int area = (r2 - r1 + 1) * (c2 - c1 + 1);
                            max_area = std::max(max_area, area);
                        }
                    }
                }
            }
        }
        
        return max_area;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(R^3 \times C^3)$
  - Generating all subgrids takes $\mathcal{O}(R^2 \times C^2)$; verifying each subgrid takes $\mathcal{O}(R \times C)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space.

---

## Why This Approach Is Not Optimal

Six nested loops take $\mathcal{O}(R^3 \times C^3)$ time. By reducing the 2D matrix problem row-by-row into **Largest Rectangle in Histogram (LeetCode #84)**, we can solve Maximal Rectangle in $\mathcal{O}(R \times C)$ time.
