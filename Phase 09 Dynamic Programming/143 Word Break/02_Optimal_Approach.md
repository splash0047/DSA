# Word Break

## Pattern Used

- **Pattern**: **1D Substring Partitioning DP**
- **Concept**:
  - `dp[i]` is a boolean flag indicating if prefix `s[0...i-1]` can be segmented into dictionary words.
  - Base Case: `dp[0] = true` (empty string is always validly segmented).
  - State Transition:
    - For `i` from `1` to `N`:
      - For `j` from `0` to `i - 1`:
        - If `dp[j] == true` AND `wordSet.count(s[j...i-1])`:
          - `dp[i] = true`.
          - Break inner loop early!

---

## Observation

1. A prefix `s[0...i-1]` can be validly segmented if there exists ANY split point `j` ($0 \le j < i$) such that:
   - Prefix `s[0...j-1]` is validly segmentable (`dp[j] == true`), AND
   - Substring `s[j...i-1]` is a valid dictionary word (`wordSet.count(s.substr(j, i - j))`).

---

## Intuition

Walk through the string character by character. For each length `i`, look back at all previous positions `j` that were successfully segmented. Check if the substring connecting `j` to `i` is in the dictionary. If yes, mark position `i` as successfully segmented!

---

## Algorithm

1. `wordSet = unordered_set<string>(wordDict.begin(), wordDict.end())`.
2. `dp` vector of size `n + 1` filled with `false`. `dp[0] = true`.
3. Loop `i` from `1` to `n`:
   - Loop `j` from `0` to `i - 1`:
     - If `dp[j] == true` and `wordSet.count(s.substr(j, i - j))`:
       - `dp[i] = true`.
       - Break.
4. Return `dp[n]`.

---

## Clean C++17 Solution

```cpp
#include <string>
#include <vector>
#include <unordered_set>

class Solution {
public:
    bool wordBreak(std::string s, std::vector<std::string>& wordDict) {
        std::unordered_set<std::string> wordSet(wordDict.begin(), wordDict.end());
        int n = s.size();
        
        // dp[i] represents whether s[0...i-1] can be segmented
        std::vector<bool> dp(n + 1, false);
        dp[0] = true; // Base case: empty string
        
        for (int i = 1; i <= n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (dp[j] && wordSet.find(s.substr(j, i - j)) != wordSet.end()) {
                    dp[i] = true;
                    break; // Found a valid segmentation split for prefix of length i
                }
            }
        }
        
        return dp[n];
    }
};
```

---

## Dry Run

### Input
- `s = "leetcode"`, `wordDict = ["leet", "code"]`

### Execution Trace

- `dp[0] = true`. `dp[1..8] = false`.
- `i = 4` (`"leet"`):
  - `j = 0`: `dp[0]` is `true`, `s.substr(0, 4) = "leet"` in `wordSet` $\implies$ `dp[4] = true`.
- `i = 8` (`"leetcode"`):
  - `j = 4`: `dp[4]` is `true`, `s.substr(4, 4) = "code"` in `wordSet` $\implies$ `dp[8] = true`.

### Result
- Output: `true`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2 \cdot L)$
  - Outer loop `i` runs $N$ times, inner loop `j` runs $N$ times. `substr` extraction takes $\mathcal{O}(L)$ time where $L$ is max word length.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N + W)$
  - `dp` vector of size $N + 1$ and `wordSet` storing dictionary words.

---

## Why This is Optimal

- Solves word segmentation in polynomial $\mathcal{O}(N^2 \cdot L)$ time, avoiding exponential backtracking.
- Uses linear $\mathcal{O}(N)$ 1D DP table.

---

## Common Mistakes

1. **Missing `dp[0] = true` Base Case**: Failing to set `dp[0] = true` prevents any initial word matching from index 0.
2. **Substr Length Error**: Writing `s.substr(j, i)` instead of `s.substr(j, i - j)`.
