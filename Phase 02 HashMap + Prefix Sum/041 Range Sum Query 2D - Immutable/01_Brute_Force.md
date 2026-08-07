# Range Sum Query 2D - Immutable

- **Problem Number**: 304
- **Platform**: LeetCode #304
- **Difficulty**: Medium
- **Pattern**: Direct 2D Matrix Sum Loop

---

## Brute Force Intuition

For every call to `sumRegion(row1, col1, row2, col2)`, iterate through every cell $(r, c)$ in the sub-grid from $r = \text{row1} \dots \text{row2}$ and $c = \text{col1} \dots \text{col2}$ and compute the sum on the fly.

---

## Algorithm

1. Constructor: Store a copy of `matrix`.
2. `sumRegion(row1, col1, row2, col2)`:
   a. `sum = 0`.
   b. Loop `r` from `row1` to `row2`:
      - Loop `c` from `col1` to `col2`:
        - `sum += grid[r][c]`.
   c. Return `sum`.

---

## Code

```cpp
#include <vector>

class NumMatrix {
private:
    std::vector<std::vector<int>> grid;
public:
    NumMatrix(const std::vector<std::vector<int>>& matrix) : grid(matrix) {}
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        int sum = 0;
        for (int r = row1; r <= row2; ++r) {
            for (int c = col1; c <= col2; ++c) {
                sum += grid[r][c];
            }
        }
        return sum;
    }
};
```

---

## Time Complexity

- **Constructor**: $\mathcal{O}(M \times N)$
- **`sumRegion`**: $\mathcal{O}(M \times N)$ per query worst case.
- For $Q = 10^4$ queries on a $200 \times 200$ matrix, total time is $\mathcal{O}(Q \times M \times N) = 4 \times 10^8$ operations, causing TLE.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(M \times N)$
  - Memory to store matrix.

---

## Why This Approach Is Not Optimal

Computing sub-matrix sums on the fly takes $\mathcal{O}(M \times N)$ per query. Using a **2D Prefix Sum Array**, pre-computations take $\mathcal{O}(M \times N)$ time once, allowing every subsequent `sumRegion` query to be answered in $\mathcal{O}(1)$ constant time.
