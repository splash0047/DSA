# Maximum Product Subarray

- **Problem Number**: 152
- **Platform**: LeetCode #152
- **Difficulty**: Medium
- **Pattern**: All Subarrays Product Evaluation

---

## Brute Force Intuition

Generate all contiguous subarrays `nums[i...j]` using nested loops ($0 \le i \le j < N$). Maintain a running product for each start index `i` and track the maximum product observed across all subarrays.

---

## Algorithm

1. `maxProd = nums[0]`.
2. Loop `i` from `0` to `n - 1`:
   - `curProd = 1`.
   - Loop `j` from `i` to `n - 1`:
     - `curProd *= nums[j]`.
     - `maxProd = max(maxProd, curProd)`.
3. Return `maxProd`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int maxProduct(std::vector<int>& nums) {
        int n = nums.size();
        int maxProd = nums[0];
        
        for (int i = 0; i < n; ++i) {
            int curProd = 1;
            for (int j = i; j < n; ++j) {
                curProd *= nums[j];
                maxProd = std::max(maxProd, curProd);
            }
        }
        
        return maxProd;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - Nested loops iterate over $\mathcal{O}(N^2)$ contiguous subarrays.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses constant extra space.

---

## Why This Approach Is Not Optimal

Testing all subarrays takes quadratic $\mathcal{O}(N^2)$ time, which TLEs for $N = 20,000$. Using **Dual Tracking DP (Min & Max Product Tracking)**, we can find the maximum product subarray in linear $\mathcal{O}(N)$ time!
