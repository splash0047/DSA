# Find Minimum in Rotated Sorted Array

## Pattern Used

- **Pattern**: **Binary Search (Compare Mid with Right Boundary)**
- **Concept**: Compare `nums[mid]` with `nums[high]`:
  - If `nums[mid] > nums[high]`: The minimum element **must** lie strictly to the right of `mid` $\rightarrow$ `low = mid + 1`.
  - If `nums[mid] <= nums[high]`: `nums[mid]` could be the minimum, or the minimum lies to the left $\rightarrow$ `high = mid`.

---

## Observation

1. In a rotated sorted array of unique elements, the minimum element is the only element that is smaller than its left neighbor (the rotation pivot).
2. Comparing `nums[mid]` with `nums[high]`:
   - Case 1: `nums[mid] > nums[high]` (e.g. `[4, 5, 6, 7, 0, 1, 2]`, `mid` is `7`, `high` is `2`). The drop/rotation occurs to the right of `mid`. Set `low = mid + 1`.
   - Case 2: `nums[mid] <= nums[high]` (e.g. `[7, 0, 1, 2, 4, 5, 6]`, `mid` is `2`, `high` is `6`). The right portion `[mid ... high]` is properly sorted, so the minimum is at `mid` or to its left. Set `high = mid`.
3. Loop condition: `while (low < high)`. When `low == high`, `nums[low]` is guaranteed to be the minimum element!

---

## Intuition

Binary search to narrow down the pivot drop point:
- Is `nums[mid]` larger than `nums[high]`? Minimum is to the right!
- Otherwise, minimum is at `mid` or to the left!

---

## Algorithm

1. `low = 0`, `high = nums.size() - 1`.
2. While `low < high`:
   a. `mid = low + (high - low) / 2`.
   b. If `nums[mid] > nums[high]`:
      - `low = mid + 1`.
   c. Else:
      - `high = mid`.
3. Return `nums[low]`.

---

## Clean C++17 Solution

```cpp
#include <vector>

class Solution {
public:
    int findMin(const std::vector<int>& nums) {
        int low = 0;
        int high = nums.size() - 1;
        
        while (low < high) {
            int mid = low + (high - low) / 2;
            
            if (nums[mid] > nums[high]) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        
        return nums[low];
    }
};
```

---

## Dry Run

### Input
- `nums = [4, 5, 6, 7, 0, 1, 2]`

### Execution Trace

| Step | `low` | `high` | `mid` | `nums[mid]` | `nums[high]` | `nums[mid] > nums[high]`? | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `0` (`4`) | `6` (`2`) | `3` | `7` | `2` | `7 > 2` (**Yes**) | `low = mid + 1 = 4` |
| 2 | `4` (`0`) | `6` (`2`) | `5` | `1` | `2` | `1 > 2` (No) | `high = mid = 5` |
| 3 | `4` (`0`) | `5` (`1`) | `4` | `0` | `1` | `0 > 1` (No) | `high = mid = 4` |
| End | `4` | `4` | - | - | - | `low == high` (Stop) | **Return `nums[4] = 0`** |

### Result
- Output: `0`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(\log N)$
  - Search space shrinks by half in each step.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This is Optimal

- Finds minimum in a rotated sorted array in logarithmic $\mathcal{O}(\log N)$ time.
- Uses zero extra memory ($\mathcal{O}(1)$ space).

---

## Common Mistakes

1. **Comparing `nums[mid]` with `nums[low]`**: Comparing `mid` with `low` fails when the array is NOT rotated (already sorted), e.g. `[1, 2, 3, 4, 5]`. Comparing `mid` with `high` works unconditionally.
2. **Writing `high = mid - 1` when `nums[mid] <= nums[high]`**: `nums[mid]` itself might be the minimum! Setting `high = mid - 1` discards the valid answer. Set `high = mid`.
