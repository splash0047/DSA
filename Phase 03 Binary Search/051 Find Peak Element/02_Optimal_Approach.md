# Find Peak Element

## Pattern Used

- **Pattern**: **Binary Search on Gradient / Slope Direction**
- **Concept**: Compare `nums[mid]` with its adjacent right neighbor `nums[mid + 1]`. The array is guaranteed to contain at least one peak on the side that goes uphill!

---

## Observation

1. If `nums[mid] < nums[mid + 1]`:
   - The array is currently in an **ascending slope** going rightward.
   - Because `nums[n] = -\infty`, the slope MUST eventually turn downward to reach $-\infty$. Therefore, a peak **must exist to the right** of `mid` $\rightarrow$ `low = mid + 1`.
2. If `nums[mid] > nums[mid + 1]`:
   - The array is currently in a **descending slope** going rightward (or `mid` itself is a peak).
   - A peak **must exist at or to the left** of `mid` $\rightarrow$ `high = mid`.
3. When `low == high`, `low` is guaranteed to be a valid peak index!

---

## Intuition

Think of walking on a mountain:
- If stepping to `mid + 1` takes you higher uphill, keep walking right!
- If stepping to `mid + 1` takes you downhill, a peak must be at or behind you on the left!

---

## Algorithm

1. `low = 0`, `high = nums.size() - 1`.
2. While `low < high`:
   a. `mid = low + (high - low) / 2`.
   b. If `nums[mid] < nums[mid + 1]`:
      - `low = mid + 1`.
   c. Else:
      - `high = mid`.
3. Return `low`.

---

## Clean C++17 Solution

```cpp
#include <vector>

class Solution {
public:
    int findPeakElement(const std::vector<int>& nums) {
        int low = 0;
        int high = nums.size() - 1;
        
        while (low < high) {
            int mid = low + (high - low) / 2;
            
            if (nums[mid] < nums[mid + 1]) {
                low = mid + 1; // Ascending slope -> Peak on the right
            } else {
                high = mid;    // Descending slope -> Peak on left or at mid
            }
        }
        
        return low;
    }
};
```

---

## Dry Run

### Input
- `nums = [1, 2, 1, 3, 5, 6, 4]`

### Execution Trace

| Step | `low` | `high` | `mid` | `nums[mid]` | `nums[mid+1]` | Slope Check (`<`) | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `0` | `6` | `3` | `3` | `5` | `3 < 5` (Ascending) | `low = mid + 1 = 4` |
| 2 | `4` | `6` | `5` | `6` | `4` | `6 < 4` (Descending) | `high = mid = 5` |
| 3 | `4` | `5` | `4` | `5` | `6` | `5 < 6` (Ascending) | `low = mid + 1 = 5` |
| End | `5` | `5` | - | - | - | `low == high` (Stop) | **Return `5`** |

### Result
- Output: `5` (Value `6` is a peak element)

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(\log N)$
  - Halves search space at each iteration.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This is Optimal

- Meets the mandatory $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space constraints.

---

## Common Mistakes

1. **Out of Bounds Access**: Writing `nums[mid - 1]` without bounds checking. Comparing `nums[mid]` with `nums[mid + 1]` inside `while (low < high)` guarantees `mid + 1` is always in bounds!
2. **Writing `high = mid - 1`**: If `nums[mid] > nums[mid + 1]`, `mid` itself could be the peak element! Setting `high = mid - 1` would erroneously discard the peak. Use `high = mid`.
