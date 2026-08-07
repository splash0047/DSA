# Container With Most Water

- **Problem Number**: 11
- **Platform**: LeetCode #11
- **Difficulty**: Medium
- **Pattern**: All-Pairs Evaluation / Nested Loops

---

## Brute Force Intuition

To find the maximum area of water that can be contained, the simplest approach is to check every pair of vertical lines $(i, j)$ where $j > i$.

The area formed by two lines at indices `i` and `j` is determined by the shorter line height multiplied by the distance between them:
$$\text{Area} = \min(\text{height}[i], \text{height}[j]) \times (j - i)$$

By computing this area for all possible pairs and tracking the maximum, we find the optimal container.

---

## Algorithm

1. Initialize `max_water = 0`.
2. Outer loop `i` from `0` to `n - 2`.
3. Inner loop `j` from `i + 1` to `n - 1`.
4. `area = min(height[i], height[j]) * (j - i)`.
5. `max_water = max(max_water, area)`.
6. Return `max_water`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int maxArea(const std::vector<int>& height) {
        int max_water = 0;
        int n = height.size();
        
        for (int i = 0; i < n - 1; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int current_height = std::min(height[i], height[j]);
                int width = j - i;
                int area = current_height * width;
                max_water = std::max(max_water, area);
            }
        }
        
        return max_water;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - Evaluates $\frac{N(N-1)}{2}$ pairs.
  - For $N = 10^5$, $N^2 = 10^{10}$ operations, causing TLE.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant extra memory used.

---

## Why This Approach Is Not Optimal

Evaluating all pairs is redundant. As we narrow the width between lines, the area can only increase if we find a taller line. Using **Two Pointers (Boundary Shrinking)** allows us to prune unpromising pairs and achieve linear $\mathcal{O}(N)$ time.
