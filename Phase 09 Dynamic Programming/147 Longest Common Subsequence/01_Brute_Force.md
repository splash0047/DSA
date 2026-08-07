# Longest Common Subsequence

- **Problem Number**: 1143
- **Platform**: LeetCode #1143
- **Difficulty**: Medium
- **Pattern**: Unmemoized Dual Pointer Recursion

---

## Brute Force Intuition

Compare characters of `text1[i]` and `text2[j]` starting from indices $i = 0, j = 0$:
1. If `text1[i] == text2[j]`: Character matches $\implies$ `return 1 + lcs(i + 1, j + 1)`.
2. If `text1[i] != text2[j]`: Mismatch $\implies$ return `max(lcs(i + 1, j), lcs(i, j + 1))` (test skipping character from `text1` vs skipping character from `text2`).

---

## Algorithm

1. `lcs(i, j)`:
   - If `i == text1.length() || j == text2.length()`, return `0`.
   - If `text1[i] == text2[j]`:
     - Return `1 + lcs(i + 1, j + 1)`.
   - Else:
     - Return `max(lcs(i + 1, j), lcs(i, j + 1))`.

---

## Code

```cpp
#include <string>
#include <algorithm>

class Solution {
private:
    int lcsHelper(const std::string& t1, const std::string& t2, int i, int j) {
        if (i == t1.size() || j == t2.size()) {
            return 0;
        }
        
        if (t1[i] == t2[j]) {
            return 1 + lcsHelper(t1, t2, i + 1, j + 1);
        } else {
            return std::max(lcsHelper(t1, t2, i + 1, j), lcsHelper(t1, t2, i, j + 1));
        }
    }

public:
    int longestCommonSubsequence(std::string text1, std::string text2) {
        return lcsHelper(text1, text2, 0, 0);
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(2^{M + N})$
  - Branching factor of 2 at each step of depth $M + N$ creates an exponential recursion tree.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(M + N)$
  - Recursion call stack depth.

---

## Why This Approach Is Not Optimal

Re-evaluating identical index subproblems $(i, j)$ repeatedly takes exponential $\mathcal{O}(2^{M + N})$ time. Using **Space-Optimized 2D/1D Dynamic Programming**, we can compute LCS length in quadratic $\mathcal{O}(M \times N)$ time and $\mathcal{O}(N)$ space!
