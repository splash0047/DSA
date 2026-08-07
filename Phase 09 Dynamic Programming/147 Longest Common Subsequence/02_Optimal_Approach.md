# Longest Common Subsequence

## Pattern Used

- **Pattern**: **2D Grid DP (Space-Optimized 1D Row Double Buffering)**
- **Concept**:
  - `dp[i][j]` represents the LCS length between `text1[0...i-1]` and `text2[0...j-1]`.
  - State Transitions:
    - If `text1[i-1] == text2[j-1]`:
      - `dp[i][j] = 1 + dp[i-1][j-1]`
    - Else:
      - `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`
  - Space Optimization: Since row `i` depends only on row `i-1`, we can use two 1D rows (`prev` and `curr`) of size $N + 1$ to reduce auxiliary memory to $\mathcal{O}(N)$.

---

## Observation

1. If the last characters match (`text1[i-1] == text2[j-1]`), they MUST contribute 1 to the LCS length, and the remaining problem is LCS of prefixes `text1[0...i-2]` and `text2[0...j-2]`.
2. If they do not match, the LCS is either in `text1[0...i-2]` and `text2[0...j-1]`, OR in `text1[0...i-1]` and `text2[0...j-2]`.

---

## Intuition

Fill a grid bottom-up where row `i` represents prefixes of `text1` and column `j` represents prefixes of `text2`. When characters match, add 1 to the diagonal value (`1 + dp[i-1][j-1]`). When they mismatch, take the max of top (`dp[i-1][j]`) and left (`dp[i][j-1]`).

---

## Algorithm

1. `m = text1.size()`, `n = text2.size()`.
2. `vector<int> prev(n + 1, 0)`, `curr(n + 1, 0)`.
3. Loop `i` from `1` to `m`:
   - For `j` from `1` to `n`:
     - If `text1[i - 1] == text2[j - 1]`:
       - `curr[j] = 1 + prev[j - 1]`.
     - Else:
       - `curr[j] = max(prev[j], curr[j - 1])`.
   - `prev = curr`.
4. Return `prev[n]`.

---

## Clean C++17 Solution

```cpp
#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    int longestCommonSubsequence(std::string text1, std::string text2) {
        int m = text1.size();
        int n = text2.size();
        
        // Optimize space by making text2 the shorter string
        if (m < n) {
            return longestCommonSubsequence(text2, text1);
        }
        
        // prev stores results of row i-1, curr stores results of row i
        std::vector<int> prev(n + 1, 0);
        std::vector<int> curr(n + 1, 0);
        
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (text1[i - 1] == text2[j - 1]) {
                    curr[j] = 1 + prev[j - 1]; // Character match: 1 + diagonal
                } else {
                    curr[j] = std::max(prev[j], curr[j - 1]); // Mismatch: max(top, left)
                }
            }
            prev = curr;
        }
        
        return prev[n];
    }
};
```

---

## Dry Run

### Input
- `text1 = "abcde"`, `text2 = "ace"`

### Execution Trace

- `m = 5, n = 3`. `prev = [0, 0, 0, 0]`.
- `i = 1 ('a')`:
  - `j = 1 ('a')`: match $\implies$ `curr[1] = 1 + prev[0] = 1`.
  - `j = 2 ('c')`: mismatch $\implies$ `curr[2] = max(prev[2], curr[1]) = 1`.
  - `j = 3 ('e')`: mismatch $\implies$ `curr[3] = max(prev[3], curr[2]) = 1`.
  - `prev = [0, 1, 1, 1]`.
- `i = 2 ('b')`: `prev = [0, 1, 1, 1]`.
- `i = 3 ('c')`: `curr[2]` matches $\implies$ `curr[2] = 1 + prev[1] = 2`. `prev = [0, 1, 2, 2]`.
- `i = 4 ('d')`: `prev = [0, 1, 2, 2]`.
- `i = 5 ('e')`: `curr[3]` matches $\implies$ `curr[3] = 1 + prev[2] = 3`. `prev = [0, 1, 2, 3]`.

### Result
- Output: `3` (Subsequence `"ace"`)

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(M \times N)$
  - Double loop iterates $M \times N$ times.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(\min(M, N))$
  - Uses two 1D vectors of size $\min(M, N) + 1$.

---

## Why This is Optimal

- Computes LCS length in quadratic $\mathcal{O}(M \times N)$ time.
- Uses space optimization to reduce memory from $\mathcal{O}(M \times N)$ to $\mathcal{O}(\min(M, N))$.

---

## Common Mistakes

1. **Off-by-One Indexing**: Confusing 1-based DP indices `i, j` with 0-based string character indices `i-1, j-1`.
2. **Forgetting Swap for Min Space**: Failing to ensure `text2` is the shorter string to minimize 1D row size.
