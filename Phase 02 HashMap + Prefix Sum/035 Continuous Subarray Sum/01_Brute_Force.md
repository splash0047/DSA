# Continuous Subarray Sum

- **Problem Number**: 523
- **Platform**: LeetCode #523
- **Difficulty**: Medium
- **Pattern**: Nested Loops Subarray Check

---

## Brute Force Intuition

Check all possible contiguous subarrays `nums[i ... j]` where length $j - i + 1 \ge 2$. For each subarray, check if its sum is a multiple of $k$ (`sum % k == 0`).

---

## Algorithm

1. Outer loop `i` from `0` to `n - 2`.
2. `current_sum = nums[i]`.
3. Inner loop `j` from `i + 1` to `n - 1`:
   a. `current_sum += nums[j]`.
   b. If `current_sum % k == 0`, return `true`.
4. Return `false`.

---

## Code

```cpp
#include <vector>

class Solution {
public:
    bool checkSubarraySum(const std::vector<int>& nums, int k) {
        int n = nums.size();
        
        for (int i = 0; i < n - 1; ++i) {
            long long current_sum = nums[i];
            for (int j = i + 1; j < n; ++j) {
                current_sum += nums[j];
                if (current_sum % k == 0) {
                    return true;
                }
            }
        }
        
        return false;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - Double loop takes $\mathcal{O}(N^2)$ time.
  - For $N = 10^5$, causes TLE.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant extra space.

---

## Why This Approach Is Not Optimal

Evaluating all pairs takes quadratic time. By storing the **earliest index of each prefix sum remainder** in a Hash Map, we can check if a valid subarray of length $\ge 2$ exists in linear $\mathcal{O}(N)$ time.
