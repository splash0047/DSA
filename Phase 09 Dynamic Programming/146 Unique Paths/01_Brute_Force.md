# Unique Paths

- **Problem Number**: 62
- **Platform**: LeetCode #62
- **Difficulty**: Medium
- **Pattern**: Grid Traversal Recursion

---

## Brute Force Intuition

From any cell `(r, c)`, the robot can only move either **Down** to `(r + 1, c)` or **Right** to `(r, c + 1)`.
The total unique paths to reach `(m-1, n-1)` from `(r, c)` is:
$$\text{paths}(r, c) = \text{paths}(r + 1, c) + \text{paths}(r, c + 1)$$

A naive recursive implementation explores both directions until reaching `(m-1, n-1)` (1 valid path) or going out of bounds (0 valid paths).

---

## Algorithm

1. `countPaths(r, c)`:
   - If `r == m - 1 && c == n - 1`, return `1`.
   - If `r >= m || c >= n`, return `0`.
   - Return `countPaths(r + 1, c) + countPaths(r, c + 1)`.

---

## Code

```cpp
class Solution {
private:
    int countPaths(int r, int c, int m, int n) {
        if (r == m - 1 && c == n - 1) return 1;
        if (r >= m || c >= n) return 0;
        
        return countPaths(r + 1, c, m, n) + countPaths(r, c + 1, m, n);
    }

public:
    int uniquePaths(int m, int n) {
        return countPaths(0, 0, m, n);
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(2^{M + N})$
  - Branching factor of 2 at each step of depth $M + N$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(M + N)$
  - Recursion call stack depth.

---

## Why This Approach Is Not Optimal

Evaluating identical cell subproblems repeatedly takes exponential $\mathcal{O}(2^{M + N})$ time. Using **Space-Optimized 1D Grid DP** (or **Combinatorics / Combinations Formula**), we compute unique paths in linear $\mathcal{O}(M)$ or $\mathcal{O}(M \times N)$ time!
