# Largest Rectangle in Histogram

- **Problem Number**: 84
- **Platform**: LeetCode #84
- **Difficulty**: Hard
- **Pattern**: Expand Boundaries for Every Bar

---

## Brute Force Intuition

For each bar `i` with height `heights[i]`, find how far the rectangle of height `heights[i]` can expand to the left and to the right:
- Expand left until finding a bar strictly smaller than `heights[i]` (index `left_limit`).
- Expand right until finding a bar strictly smaller than `heights[i]` (index `right_limit`).
- Width $= \text{right\_limit} - \text{left\_limit} - 1$.
- $\text{Area} = \text{heights}[i] \times \text{width}$.

---

## Algorithm

1. `max_area = 0`.
2. For `i` from `0` to `n - 1`:
   a. `left = i`.
   b. While `left >= 0 && heights[left] >= heights[i]`: `left--`.
   c. `right = i`.
   d. While `right < n && heights[right] >= heights[i]`: `right++`.
   e. `width = right - left - 1`.
   f. `max_area = max(max_area, heights[i] * width)`.
3. Return `max_area`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int largestRectangleArea(const std::vector<int>& heights) {
        int n = heights.size();
        int max_area = 0;
        
        for (int i = 0; i < n; ++i) {
            int left = i;
            while (left >= 0 && heights[left] >= heights[i]) {
                left--;
            }
            
            int right = i;
            while (right < n && heights[right] >= heights[i]) {
                right++;
            }
            
            int width = right - left - 1;
            max_area = std::max(max_area, heights[i] * width);
        }
        
        return max_area;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - Expanding left and right boundaries for each of the $N$ bars takes $\mathcal{O}(N)$ time, leading to quadratic runtime.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space.

---

## Why This Approach Is Not Optimal

Expanding boundaries linearly takes $\mathcal{O}(N^2)$ time. Using a **Monotonic Increasing Stack**, we can find Previous Smaller Element and Next Smaller Element boundaries for all bars in a **single pass**, computing maximum area in linear $\mathcal{O}(N)$ time.
