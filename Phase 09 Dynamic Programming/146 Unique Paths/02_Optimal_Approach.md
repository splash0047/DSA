# Unique Paths

## Pattern Used

- **Pattern**: **Space-Optimized 2D Grid DP** OR **Combinatorics Combinations $\binom{m+n-2}{m-1}$**
- **Optimal Approach 1 (Combinatorics - $\mathcal{O}(\min(M, N))$ Time, $\mathcal{O}(1)$ Space)**:
  - To reach `(m-1, n-1)` from `(0, 0)`, the robot MUST make exactly $(m - 1)$ Down moves and $(n - 1)$ Right moves, totaling $m + n - 2$ moves.
  - The number of unique paths is the number of ways to choose $(m - 1)$ Down moves out of $(m + n - 2)$ total moves:
    $$\text{Unique Paths} = \binom{m + n - 2}{m - 1} = \frac{(m + n - 2)!}{(m - 1)! \cdot (n - 1)!}$$
- **Optimal Approach 2 (1D DP Array - $\mathcal{O}(M \times N)$ Time, $\mathcal{O}(N)$ Space)**:
  - Maintain a 1D DP row `dp[N]` initialized to `1`.
  - For `r` from `1` to `m - 1`:
    - For `c` from `1` to `n - 1`:
      - `dp[c] += dp[c - 1]`.

---

## Observation

1. Combinatorics perspective: The total number of steps is fixed at $(m-1) + (n-1) = m+n-2$. Picking which of those steps are Down moves gives $\binom{m+n-2}{m-1}$.
2. DP perspective: Paths to cell `(r, c)` equal paths from top `(r-1, c)` plus paths from left `(r, c-1)`.

---

## Intuition (Combinatorics)

Every path from start to end consists of the exact same number of Right steps and Down steps. The problem simply boils down to choosing which steps in the total sequence of moves are Down steps.

---

## Algorithm (Combinatorics Formula)

1. `N = m + n - 2`.
2. `K = min(m - 1, n - 1)`.
3. `res = 1`.
4. Loop `i` from `1` to `K`:
   - `res = res * (N - K + i) / i`.
5. Return `res`.

---

## Clean C++17 Solution

### Approach 1: Combinatorics ($\mathcal{O}(\min(M, N))$ Time, $\mathcal{O}(1)$ Space) — Optimal

```cpp
#include <algorithm>

class Solution {
public:
    int uniquePaths(int m, int n) {
        // Total moves = (m - 1) + (n - 1) = m + n - 2
        // We need to calculate C(m + n - 2, m - 1)
        int N = m + n - 2;
        int K = std::min(m - 1, n - 1);
        long long res = 1;
        
        for (int i = 1; i <= K; ++i) {
            res = res * (N - K + i) / i;
        }
        
        return static_cast<int>(res);
    }
};
```

### Approach 2: 1D Space-Optimized DP ($\mathcal{O}(M \times N)$ Time, $\mathcal{O}(N)$ Space)

```cpp
#include <vector>

class Solution {
public:
    int uniquePaths(int m, int n) {
        std::vector<int> dp(n, 1);
        
        for (int r = 1; r < m; ++r) {
            for (int c = 1; c < n; ++c) {
                dp[c] += dp[c - 1]; // dp[c] (top) + dp[c-1] (left)
            }
        }
        
        return dp[n - 1];
    }
};
```

---

## Dry Run (Combinatorics)

### Input
- `m = 3, n = 7`

### Execution Trace

- `N = 3 + 7 - 2 = 8`.
- `K = min(2, 6) = 2`.
- `i = 1`: `res = 1 * (8 - 2 + 1) / 1 = 7`.
- `i = 2`: `res = 7 * (8 - 2 + 2) / 2 = 7 * 8 / 2 = 28`.

### Result
- Output: `28`

---

## Time Complexity

- **Combinatorics Approach**: $\mathcal{O}(\min(M, N))$
  - Single loop running $\min(m - 1, n - 1)$ times.
- **1D DP Approach**: $\mathcal{O}(M \times N)$
  - Nested loops iterate over $M \times N$ matrix.

---

## Space Complexity

- **Combinatorics Approach**: $\mathcal{O}(1)$
  - Uses constant extra space.
- **1D DP Approach**: $\mathcal{O}(N)$
  - 1D DP table of size $N$.

---

## Why This is Optimal

- Combinatorics formula evaluates total unique grid paths in constant/linear $\mathcal{O}(\min(M, N))$ time using $\mathcal{O}(1)$ auxiliary space.

---

## Common Mistakes

1. **Integer Overflow in Combination Calculation**: Multiplying factorials directly without dividing incrementally at each iteration (`res = res * (N - K + i) / i`).
2. **Allocating Full 2D Matrix**: Allocating an $M \times N$ matrix when 1D array or combinatorics formula solves it.
