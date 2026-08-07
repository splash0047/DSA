# Container With Most Water

## Pattern Used

- **Pattern**: **Two Pointers (Boundary Shrinking)**
- **Concept**: Start with the widest possible container (`left = 0`, `right = n - 1`). Incrementally shrink the window by moving the pointer that points to the **shorter line**.

---

## Observation

The area formula is:
$$\text{Area} = \min(\text{height}[\text{left}], \text{height}[\text{right}]) \times (\text{right} - \text{left})$$

Suppose `height[left] < height[right]`:
- The current container height is limited by `height[left]`.
- If we move the taller line `right` inward to `right - 1`, the width decreases by 1, while the container height is *still* bounded by `height[left]` (or less). Thus, moving the taller line can **never** increase the area.
- Therefore, to potentially find a larger area, we **must** move the shorter line `left` inward in hopes of finding a taller line!

---

## Intuition

Start at maximum width. At each step:
1. Calculate the water area for current `left` and `right`.
2. Update `max_water = max(max_water, area)`.
3. Move the pointer pointing to the **shorter** height inward (if `height[left] < height[right]`, `left++`, else `right--`).

This greedy elimination guarantees we never miss the optimal pair while inspecting the array in a single pass.

---

## Algorithm

1. `left = 0`, `right = height.size() - 1`, `max_water = 0`.
2. While `left < right`:
   a. `width = right - left`.
   b. `current_height = min(height[left], height[right])`.
   c. `max_water = max(max_water, current_height * width)`.
   d. If `height[left] < height[right]`: `left++`.
   e. Else: `right--`.
3. Return `max_water`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int maxArea(const std::vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int max_water = 0;
        
        while (left < right) {
            int width = right - left;
            int current_height = std::min(height[left], height[right]);
            int area = current_height * width;
            
            max_water = std::max(max_water, area);
            
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        
        return max_water;
    }
};
```

---

## Dry Run

### Input
- `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`

### Execution Trace

| Step | `left` (`h[left]`) | `right` (`h[right]`) | `width` | `current_h` | `area` | `max_water` | Pointer Moved |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `0` (`1`) | `8` (`7`) | `8` | `1` | `8` | `8` | `left++` (`1 < 7`) |
| 2 | `1` (`8`) | `8` (`7`) | `7` | `7` | `49` | `49` | `right--` (`7 < 8`) |
| 3 | `1` (`8`) | `7` (`3`) | `6` | `3` | `18` | `49` | `right--` (`3 < 8`) |
| 4 | `1` (`8`) | `6` (`8`) | `5` | `8` | `40` | `49` | `right--` |
| 5 | `1` (`8`) | `5` (`4`) | `4` | `4` | `16` | `49` | `right--` |
| 6 | `1` (`8`) | `4` (`5`) | `3` | `5` | `15` | `49` | `right--` |
| 7 | `1` (`8`) | `3` (`2`) | `2` | `2` | `4` | `49` | `right--` |
| 8 | `1` (`8`) | `2` (`6`) | `1` | `6` | `6` | `49` | `right--` |

### Result
- Output: `49`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - In each step, distance between `left` and `right` decreases by 1. Loop runs $N - 1$ times.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Operates strictly in-place with constant memory.

---

## Why This is Optimal

- Examining all lines requires $\Omega(N)$ time.
- Moving the shorter line eliminates all sub-optimal pairs without missing the global maximum, guaranteeing $\mathcal{O}(N)$ optimality.

---

## Common Mistakes

1. **Moving the Taller Line Pointer**: Moving the taller line can only reduce width without increasing height. Always move the shorter line pointer.
2. **Moving Both Pointers Simultaneously**: Skipping both lines can miss valid containers if both lines have equal heights. Move one at a time.
