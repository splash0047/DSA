# Subarray Sum Equals K

- **Problem Number**: 560
- **Platform**: LeetCode #560
- **Difficulty**: Medium
- **Pattern**: Nested Loops Subarray Sum

---

## Brute Force Intuition

Compute the sum of every contiguous subarray `nums[i ... j]` using two nested loops. Whenever the running sum equals `k`, increment the count.

---

## Algorithm

1. `count = 0`.
2. Loop `i` from `0` to `n - 1`.
3. `current_sum = 0`.
4. Loop `j` from `i` to `n - 1`:
   a. `current_sum += nums[j]`.
   b. If `current_sum == k`, `count++`.
5. Return `count`.

---

## Code

```cpp
#include <vector>

class Solution {
public:
    int subarraySum(const std::vector<int>& nums, int k) {
        int count = 0;
        int n = nums.size();
        
        for (int i = 0; i < n; ++i) {
            int current_sum = 0;
            for (int j = i; j < n; ++j) {
                current_sum += nums[j];
                if (current_sum == k) {
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
  - Double loop visits $\frac{N(N+1)}{2}$ subarrays.
  - For $N = 2 \times 10^4$, $N^2 = 4 \times 10^8$ operations, causing TLE.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

Because `nums` can contain **negative numbers**, sliding window does not work (monotonicity fails). However, using **Prefix Sum + Hash Map**, we can find all target sub-ranges in linear $\mathcal{O}(N)$ time.
