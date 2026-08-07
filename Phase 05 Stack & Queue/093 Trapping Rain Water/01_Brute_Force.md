# Trapping Rain Water

- **Problem Number**: 42
- **Platform**: LeetCode #42
- **Difficulty**: Hard
- **Pattern**: Element-wise Boundary Search

---

## Brute Force Intuition

For each bar `i`, the amount of water trapped directly above it is determined by the maximum height bar to its left `max_left` and the maximum height bar to its right `max_right`:
- $\text{Water at } i = \max(0, \min(\text{max\_left}, \text{max\_right}) - \text{height}[i])$.
- Sum the water trapped at all bars from index `0` to `n - 1`.

---

## Algorithm

1. `total_water = 0`.
2. Loop `i` from `0` to `n - 1`:
   a. `max_left = 0`, `max_right = 0`.
   b. For `l` from `0` to `i`: `max_left = max(max_left, height[l])`.
   c. For `r` from `i` to `n - 1`: `max_right = max(max_right, height[r])`.
   d. `total_water += min(max_left, max_right) - height[i]`.
3. Return `total_water`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int trap(const std::vector<int>& height) {
        int n = height.size();
        int total_water = 0;
        
        for (int i = 0; i < n; ++i) {
            int max_left = 0;
            for (int l = 0; l <= i; ++l) {
                max_left = std::max(max_left, height[l]);
            }
            
            int max_right = 0;
            for (int r = i; r < n; ++r) {
                max_right = std::max(max_right, height[r]);
            }
            
            total_water += std::min(max_left, max_right) - height[i];
        }
        
        return total_water;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - For each bar $i$, searching left and right boundaries takes $\mathcal{O}(N)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space.

---

## Why This Approach Is Not Optimal

Recomputing left and right maximum heights per element takes quadratic $\mathcal{O}(N^2)$ time. Using either **Two Pointers** or a **Monotonic Decreasing Stack**, we can compute trapped rain water in linear $\mathcal{O}(N)$ time.
