# Max Consecutive Ones III

- **Problem Number**: 1004
- **Platform**: LeetCode #1004
- **Difficulty**: Medium
- **Pattern**: All Substrings Check

---

## Brute Force Intuition

Reframe the problem: **Find the longest contiguous subarray containing at most $k$ zeroes**.

The brute force approach checks every subarray `nums[i ... j]`, counts the number of zeroes inside the subarray, and tracks the maximum length `j - i + 1` among all subarrays containing $\le k$ zeroes.

---

## Algorithm

1. `max_len = 0`.
2. Outer loop `i` from `0` to `n - 1`.
3. Inner loop `j` from `i` to `n - 1`:
   a. If `nums[j] == 0`, increment `zero_count++`.
   b. If `zero_count <= k`: `max_len = max(max_len, j - i + 1)`.
   c. Else: break inner loop.
4. Return `max_len`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int longestOnes(const std::vector<int>& nums, int k) {
        int max_len = 0;
        int n = nums.size();
        
        for (int i = 0; i < n; ++i) {
            int zero_count = 0;
            for (int j = i; j < n; ++j) {
                if (nums[j] == 0) {
                    zero_count++;
                }
                if (zero_count <= k) {
                    max_len = std::max(max_len, j - i + 1);
                } else {
                    break;
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
  - For $N = 10^5$, causes TLE.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

Nested loops take quadratic time. A **Variable-Size Sliding Window (Zero Counter)** tracks `zero_count` dynamically in $\mathcal{O}(1)$ per step, reducing execution time to linear $\mathcal{O}(N)$.
