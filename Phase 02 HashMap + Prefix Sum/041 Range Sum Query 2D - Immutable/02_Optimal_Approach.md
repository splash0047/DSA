# Range Sum Query 2D - Immutable

## Pattern Used

- **Pattern**: **2D Prefix Sum Array Pre-computation (Inclusion-Exclusion Principle)**
- **Concept**: Pre-compute a 2D prefix sum grid `pref` of size $(M + 1) \times (N + 1)$ where `pref[r][c]` stores the total sum of the sub-matrix from `(0, 0)` to `(r-1, c-1)`.

---

## Observation

1. **2D Prefix Sum Build Formula**:
   $$\text{pref}[r][c] = \text{matrix}[r-1][c-1] + \text{pref}[r-1][c] + \text{pref}[r][c-1] - \text{pref}[r-1][c-1]$$
2. **2D Region Query Formula (Inclusion-Exclusion Principle)**:
   The sum of sub-matrix `(row1, col1)` to `(row2, col2)` is:
   $$\text{sumRegion} = \text{pref}[r2+1][c2+1] - \text{pref}[r1][c2+1] - \text{pref}[r2+1][c1] + \text{pref}[r1][c1]$$
   where $r1 = \text{row1}$, $c1 = \text{col1}$, $r2 = \text{row2}$, $c2 = \text{col2}$.

---

## Intuition

Think of inclusion-exclusion on a 2D grid:
- To get the sum of a target sub-rectangle $(r1, c1)$ to $(r2, c2)$:
  1. Take the full rectangle from $(0, 0)$ to $(r2, c2)$ (`pref[r2+1][c2+1]`).
  2. Subtract top unneeded area $(0, 0)$ to $(r1-1, c2)$ (`pref[r1][c2+1]`).
  3. Subtract left unneeded area $(0, 0)$ to $(r2, c1-1)$ (`pref[r2+1][c1]`).
  4. Add back top-left intersection area $(0, 0)$ to $(r1-1, c1-1)$ (`pref[r1][c1]`) because it was subtracted twice!

---

## Algorithm

### Constructor
1. `m = matrix.size()`, `n = matrix[0].size()`.
2. Allocate `pref` grid of size $(m + 1) \times (n + 1)$ initialized to `0`.
3. Loop `r` from `1` to `m`:
   - Loop `c` from `1` to `n`:
     - `pref[r][c] = matrix[r-1][c-1] + pref[r-1][c] + pref[r][c-1] - pref[r-1][c-1]`.

### `sumRegion(r1, c1, r2, c2)`
1. Return `pref[r2+1][c2+1] - pref[r1][c2+1] - pref[r2+1][c1] + pref[r1][c1]`.

---

## Clean C++17 Solution

```cpp
#include <vector>

class NumMatrix {
private:
    std::vector<std::vector<int>> pref;
public:
    NumMatrix(const std::vector<std::vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return;
        
        int m = matrix.size();
        int n = matrix[0].size();
        pref.assign(m + 1, std::vector<int>(n + 1, 0));
        
        for (int r = 1; r <= m; ++r) {
            for (int c = 1; c <= n; ++c) {
                pref[r][c] = matrix[r - 1][c - 1] 
                           + pref[r - 1][c] 
                           + pref[r][c - 1] 
                           - pref[r - 1][c - 1];
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        return pref[row2 + 1][col2 + 1] 
             - pref[row1][col2 + 1] 
             - pref[row2 + 1][col1] 
             + pref[row1][col1];
    }
};
```

---

## Dry Run

### Input
- `matrix = [[3, 0, 1], [5, 6, 3], [1, 2, 0]]`

### 2D Prefix Matrix Construction
- `pref[1][1] = 3`
- `pref[1][2] = 3 + 0 = 3`
- `pref[1][3] = 3 + 1 = 4`
- `pref[2][1] = 3 + 5 = 8`
- `pref[2][2] = 6 + 3 + 8 - 3 = 14`
- `pref[2][3] = 3 + 4 + 14 - 3 = 18`
- `pref[3][1] = 8 + 1 = 9`
- `pref[3][2] = 2 + 14 + 9 - 8 = 17`
- `pref[3][3] = 0 + 18 + 17 - 14 = 21`

### Query `sumRegion(1, 1, 2, 2)` (Sub-matrix `[[6, 3], [2, 0]]`, sum = 11)
- Formula: `pref[3][3] - pref[1][3] - pref[3][1] + pref[1][1]`
- Calculation: `21 - 4 - 9 + 3 = 11` (Matches expected 11!)

---

## Time Complexity

- **Constructor**: $\mathcal{O}(M \times N)$
  - Single pass through $M \times N$ cells.
- **`sumRegion`**: $\mathcal{O}(1)$
  - 4 array lookups and arithmetic operations per query.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(M \times N)$
  - Memory for $(M + 1) \times (N + 1)$ 2D prefix sum grid.

---

## Why This is Optimal

- Computes sub-rectangle sums in constant $\mathcal{O}(1)$ time.
- Standard 2D Inclusion-Exclusion optimal solution.

---

## Common Mistakes

1. **Forgetting to Add Back Intersection Area**: Writing `pref[r2+1][c2+1] - pref[r1][c2+1] - pref[r2+1][c1]` without adding back `+ pref[r1][c1]`.
2. **Incorrect Off-by-One Indices**: Sizing 2D grid to $M \times N$ instead of $(M + 1) \times (N + 1)$, requiring boundary checks for `row1 == 0` or `col1 == 0`.
