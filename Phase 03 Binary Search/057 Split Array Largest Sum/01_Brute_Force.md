# Split Array Largest Sum

- **Problem Number**: 410
- **Platform**: LeetCode #410
- **Difficulty**: Hard
- **Pattern**: Dynamic Programming (Partitioning)

---

## Brute Force Intuition

Define `dp(i, m)` as the minimized largest subarray sum when splitting subarray `nums[i ... n-1]` into `m` parts. For the current part, pick a split point `j` (from `i` to `n - m`):
$$\text{dp}(i, m) = \min_{i \le j \le n - m} \Big( \max(\text{sum}(nums[i \dots j]), \text{dp}(j + 1, m - 1)) \Big)$$

---

## Algorithm

1. Base case: `m == 1`, return sum of `nums[i ... n-1]`.
2. Initialize `min_largest_sum = INF`.
3. Loop split point `j` from `i` to `n - m`:
   a. `current_sum = sum(nums[i ... j])`.
   b. `sub_problem = dp(j + 1, m - 1)`.
   c. `max_part = max(current_sum, sub_problem)`.
   d. `min_largest_sum = min(min_largest_sum, max_part)`.
4. Return `min_largest_sum`.

---

## Code

```cpp
#include <vector>
#include <numeric>
#include <algorithm>

class Solution {
private:
    long long solve(const std::vector<int>& nums, int i, int k) {
        int n = nums.size();
        if (k == 1) {
            return std::accumulate(nums.begin() + i, nums.end(), 0LL);
        }
        
        long long min_largest = 1e18;
        long long current_sum = 0;
        
        for (int j = i; j <= n - k; ++j) {
            current_sum += nums[j];
            long long remaining_max = solve(nums, j + 1, k - 1);
            long long current_max = std::max(current_sum, remaining_max);
            min_largest = std::min(min_largest, current_max);
        }
        
        return min_largest;
    }
public:
    int splitArray(const std::vector<int>& nums, int k) {
        return static_cast<int>(solve(nums, 0, k));
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2 \times K)$ using 2D Dynamic Programming (or exponential without memoization).

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N \times K)$ memoization table space.

---

## Why This Approach Is Not Optimal

2D DP takes $\mathcal{O}(N^2 \times K)$ time. By framing the problem as **Binary Search on Answer Space (Maximum Subarray Sum)**, we can verify if a candidate maximum sum `mid` allows splitting into $\le k$ subarrays in $\mathcal{O}(N)$ simulation time, reducing overall complexity to $\mathcal{O}(N \log(\sum \text{nums}))$.
