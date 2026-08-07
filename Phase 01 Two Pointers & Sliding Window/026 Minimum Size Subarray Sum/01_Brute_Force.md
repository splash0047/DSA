# Minimum Size Subarray Sum

- **Problem Number**: 209
- **Platform**: LeetCode #209
- **Difficulty**: Medium
- **Pattern**: Nested Loops Subarray Check

---

## Brute Force Intuition

Compute the sum of every possible contiguous subarray `nums[i ... j]` starting at index `i` (from `0` to `n-1`) and ending at index `j` (from `i` to `n-1`). Track the minimal length `j - i + 1` among all subarrays whose sum is $\ge \text{target}$.

---

## Algorithm

1. Initialize `min_len = INF`.
2. Outer loop `i` from `0` to `n - 1`.
3. Inner loop `j` from `i` to `n - 1`:
   a. Compute `sum` of `nums[i ... j]`.
   b. If `sum >= target`:
      - `min_len = min(min_len, j - i + 1)`
      - Break inner loop (since adding further positive elements only increases subarray length).
4. Return `min_len == INF ? 0 : min_len`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int minSubArrayLen(int target, const std::vector<int>& nums) {
        int min_len = 1e9;
        int n = nums.size();
        
        for (int i = 0; i < n; ++i) {
            long long current_sum = 0;
            for (int j = i; j < n; ++j) {
                current_sum += nums[j];
                if (current_sum >= target) {
                    min_len = std::min(min_len, j - i + 1);
                    break;
                }
            }
        }
        
        return min_len == 1e9 ? 0 : min_len;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - Double loop takes $\mathcal{O}(N^2)$ time in worst case.
  - For $N = 10^5$, this causes TLE.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

Re-evaluating subarray sums from scratch takes quadratic time. Because all array elements are strictly **positive**, adding elements strictly increases the sum and shrinking the left border strictly decreases the sum. This monotonic property allows a **Variable-Size Sliding Window** to solve the problem in linear $\mathcal{O}(N)$ time.
