# Maximum Average Subarray I

- **Problem Number**: 643
- **Platform**: LeetCode #643
- **Difficulty**: Easy
- **Pattern**: Nested Loops Subarray Sum

---

## Brute Force Intuition

To find the maximum average of a contiguous subarray of fixed length $k$, calculate the sum of every possible contiguous subarray of size $k$ starting at index `i` (from `0` to `n - k`). Divide the maximum sum found by $k$.

---

## Algorithm

1. Initialize `max_sum = -INF`.
2. Loop `i` from `0` to `n - k`:
   a. Compute `sum` of `nums[i ... i + k - 1]`.
   b. `max_sum = max(max_sum, sum)`.
3. Return `(double)max_sum / k`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    double findMaxAverage(const std::vector<int>& nums, int k) {
        double max_sum = -1e18;
        int n = nums.size();
        
        for (int i = 0; i <= n - k; ++i) {
            double current_sum = 0;
            for (int j = i; j < i + k; ++j) {
                current_sum += nums[j];
            }
            max_sum = std::max(max_sum, current_sum);
        }
        
        return max_sum / k;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \times K)$
  - There are $N - K + 1$ subarrays of size $K$. Computing each sum takes $\mathcal{O}(K)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses constant extra space.

---

## Why This Approach Is Not Optimal

Re-computing the sum of overlapping windows of length $K$ from scratch takes $\mathcal{O}(N \times K)$ time. A **Fixed-Size Sliding Window** updates the window sum in $\mathcal{O}(1)$ time per step, reducing total execution time to linear $\mathcal{O}(N)$.
