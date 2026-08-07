# Find Pivot Index

- **Problem Number**: 724
- **Platform**: LeetCode #724
- **Difficulty**: Easy
- **Pattern**: Left and Right Sub-array Sums

---

## Brute Force Intuition

For every index `i`, compute the left sum `nums[0 ... i-1]` and right sum `nums[i+1 ... n-1]` using inner loops. Return the first index `i` where `left_sum == right_sum`.

---

## Algorithm

1. Loop `i` from `0` to `n - 1`:
   a. Compute `left_sum` by summing elements `0` to `i - 1`.
   b. Compute `right_sum` by summing elements `i + 1` to `n - 1`.
   c. If `left_sum == right_sum`, return `i`.
2. Return `-1`.

---

## Code

```cpp
#include <vector>
#include <numeric>

class Solution {
public:
    int pivotIndex(const std::vector<int>& nums) {
        int n = nums.size();
        
        for (int i = 0; i < n; ++i) {
            int left_sum = 0;
            for (int j = 0; j < i; ++j) {
                left_sum += nums[j];
            }
            
            int right_sum = 0;
            for (int j = i + 1; j < n; ++j) {
                right_sum += nums[j];
            }
            
            if (left_sum == right_sum) {
                return i;
            }
        }
        
        return -1;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - For each index $i$, inner loops sum $N - 1$ elements.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

Re-computing left and right sums for each index takes quadratic time. Using **Total Sum + Running Left Sum**, we can check `left_sum == right_sum` in constant $\mathcal{O}(1)$ time per index, reducing total time to linear $\mathcal{O}(N)$.
