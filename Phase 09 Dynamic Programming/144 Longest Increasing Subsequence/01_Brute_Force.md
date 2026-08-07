# Longest Increasing Subsequence

- **Problem Number**: 300
- **Platform**: LeetCode #300
- **Difficulty**: Medium
- **Pattern**: 1D Dynamic Programming ($\mathcal{O}(N^2)$)

---

## Brute Force Intuition

Use 1D Dynamic Programming where `dp[i]` represents the length of the longest strictly increasing subsequence ending at index `i`.
- For each index `i` from `0` to `n - 1`:
  - Initialize `dp[i] = 1` (a single element is an LIS of length 1).
  - Look back at all preceding indices `j` ($0 \le j < i$).
  - If `nums[j] < nums[i]`, we can extend the LIS ending at `j`:
    - `dp[i] = max(dp[i], 1 + dp[j])`.
- Return `max(dp[0], dp[1], ..., dp[n-1])`.

---

## Algorithm

1. `dp` vector of size `n` initialized to `1`.
2. `maxLIS = 1`.
3. Loop `i` from `0` to `n - 1`:
   - Loop `j` from `0` to `i - 1`:
     - If `nums[j] < nums[i]`:
       - `dp[i] = max(dp[i], 1 + dp[j])`.
   - `maxLIS = max(maxLIS, dp[i])`.
4. Return `maxLIS`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int lengthOfLIS(std::vector<int>& nums) {
        if (nums.empty()) return 0;
        
        int n = nums.size();
        std::vector<int> dp(n, 1);
        int maxLIS = 1;
        
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[j] < nums[i]) {
                    dp[i] = std::max(dp[i], 1 + dp[j]);
                }
            }
            maxLIS = std::max(maxLIS, dp[i]);
        }
        
        return maxLIS;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - Nested loops iterate $\frac{N(N - 1)}{2}$ times.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - 1D DP table of size $N$.

---

## Why This Approach Is Not Optimal

Scanning all preceding indices `j` takes quadratic $\mathcal{O}(N^2)$ time. Using **Patience Sorting / Binary Search (`std::lower_bound`)**, we can track smallest tail candidates of increasing subsequences in $\mathcal{O}(N \log N)$ time and $\mathcal{O}(N)$ space!
