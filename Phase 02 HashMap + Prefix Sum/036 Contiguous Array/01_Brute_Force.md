# Contiguous Array

- **Problem Number**: 525
- **Platform**: LeetCode #525
- **Difficulty**: Medium
- **Pattern**: Nested Loops Subarray Count

---

## Brute Force Intuition

Check all possible contiguous subarrays `nums[i ... j]`. For each subarray, count the total number of `0`s and `1`s. If `count0 == count1`, update `max_len = max(max_len, j - i + 1)`.

---

## Algorithm

1. `max_len = 0`.
2. Outer loop `i` from `0` to `n - 1`.
3. `count0 = 0`, `count1 = 0`.
4. Inner loop `j` from `i` to `n - 1`:
   a. If `nums[j] == 0`, `count0++`, else `count1++`.
   b. If `count0 == count1`, `max_len = max(max_len, j - i + 1)`.
5. Return `max_len`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int findMaxLength(const std::vector<int>& nums) {
        int max_len = 0;
        int n = nums.size();
        
        for (int i = 0; i < n; ++i) {
            int count0 = 0, count1 = 0;
            for (int j = i; j < n; ++j) {
                if (nums[j] == 0) count0++;
                else count1++;
                
                if (count0 == count1) {
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
  - For $N = 10^5$, causes TLE.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

Evaluating all pairs takes quadratic time. By transforming `0`s to `-1`s, the problem reduces to finding the **longest subarray with sum equal to 0**. Using a **Prefix Sum Hash Map**, we solve this in linear $\mathcal{O}(N)$ time.
