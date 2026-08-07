# Sliding Window Maximum

- **Problem Number**: 239
- **Platform**: LeetCode #239
- **Difficulty**: Hard
- **Pattern**: Sliding Window Linear Search

---

## Brute Force Intuition

For each sliding window position starting at index `i` from `0` to `n - k`, iterate through all $k$ elements in `nums[i ... i + k - 1]` to find and record the maximum element.

---

## Algorithm

1. `n = nums.size()`, `ans` vector of size `n - k + 1`.
2. Loop `i` from `0` to `n - k`:
   a. `max_val = nums[i]`.
   b. Loop `j` from `i` to `i + k - 1`:
      - `max_val = max(max_val, nums[j])`.
   c. `ans[i] = max_val`.
3. Return `ans`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> maxSlidingWindow(const std::vector<int>& nums, int k) {
        int n = nums.size();
        std::vector<int> ans;
        ans.reserve(n - k + 1);
        
        for (int i = 0; i <= n - k; ++i) {
            int max_val = nums[i];
            for (int j = i; j < i + k; ++j) {
                max_val = std::max(max_val, nums[j]);
            }
            ans.push_back(max_val);
        }
        
        return ans;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}((N - K + 1) \times K) \approx \mathcal{O}(N \times K)$
  - Scanning $K$ elements for each of the $N - K + 1$ windows takes quadratic time when $K \approx N/2$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space excluding output vector.

---

## Why This Approach Is Not Optimal

Scanning $K$ elements per window takes $\mathcal{O}(N \times K)$ time, causing Time Limit Exceeded (TLE) for $N = 10^5$. Using a **Monotonic Decreasing Double-Ended Queue (Deque)**, we can compute the sliding window maximum for all positions in linear $\mathcal{O}(N)$ time.
