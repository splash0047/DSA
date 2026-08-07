# Subarray Sums Divisible by K

- **Problem Number**: 974
- **Platform**: LeetCode #974
- **Difficulty**: Medium
- **Pattern**: Nested Loops Subarray Sum

---

## Brute Force Intuition

Compute the sum of every contiguous subarray `nums[i ... j]` using two nested loops. Check if `current_sum % k == 0`.

---

## Algorithm

1. `count = 0`.
2. Loop `i` from `0` to `n - 1`.
3. `current_sum = 0`.
4. Loop `j` from `i` to `n - 1`:
   a. `current_sum += nums[j]`.
   b. If `current_sum % k == 0`, `count++`.
5. Return `count`.

---

## Code

```cpp
#include <vector>

class Solution {
public:
    int subarraysDivByK(const std::vector<int>& nums, int k) {
        int count = 0;
        int n = nums.size();
        
        for (int i = 0; i < n; ++i) {
            int current_sum = 0;
            for (int j = i; j < n; ++j) {
                current_sum += nums[j];
                if (current_sum % k == 0) {
                    count++;
                }
            }
        }
        
        return count;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - Double loop takes $\mathcal{O}(N^2)$ time.
  - For $N = 3 \times 10^4$, $N^2 = 9 \times 10^8$ operations, causing TLE.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

Evaluating all subarrays takes quadratic time. Using **Modulo Arithmetic + Prefix Sum Frequency Counting**, we can find all divisible subarrays in linear $\mathcal{O}(N)$ time.
