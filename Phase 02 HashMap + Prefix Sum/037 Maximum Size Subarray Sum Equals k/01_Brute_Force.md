# Maximum Size Subarray Sum Equals k

- **Problem Number**: 325
- **Platform**: LeetCode #325 / GeeksforGeeks
- **Difficulty**: Medium
- **Pattern**: Nested Loops Subarray Sum

---

## Brute Force Intuition

Compute the sum of every contiguous subarray `nums[i ... j]` using two nested loops. Whenever `current_sum == k`, update `max_len = max(max_len, j - i + 1)`.

---

## Algorithm

1. `max_len = 0`.
2. Outer loop `i` from `0` to `n - 1`.
3. `current_sum = 0`.
4. Inner loop `j` from `i` to `n - 1`:
   a. `current_sum += nums[j]`.
   b. If `current_sum == k`:
      - `max_len = max(max_len, j - i + 1)`.
5. Return `max_len`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int maxSubArrayLen(const std::vector<int>& nums, int k) {
        int max_len = 0;
        int n = nums.size();
        
        for (int i = 0; i < n; ++i) {
            long long current_sum = 0;
            for (int j = i; j < n; ++j) {
                current_sum += nums[j];
                if (current_sum == k) {
                    max_len = std::max(max_len, j - i + 1);
                }
            }
        }
        
        return max_len;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - Double loop takes $\mathcal{O}(N^2)$ time.
  - For $N = 2 \times 10^5$, causes TLE.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

Evaluating all pairs takes quadratic time. Using a **Prefix Sum + Earliest Index Hash Map**, we can locate the maximum subarray length in linear $\mathcal{O}(N)$ time.
