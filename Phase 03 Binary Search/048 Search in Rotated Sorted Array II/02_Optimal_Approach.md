# Search in Rotated Sorted Array II

## Pattern Used

- **Pattern**: **Modified Binary Search with Duplicate Shrinking**
- **Concept**: Duplicate elements can cause ambiguity where `nums[low] == nums[mid] == nums[high]`. In this scenario, we cannot deterministically decide which half is sorted. We handle this by shrinking boundary pointers `low++` and `high--`.

---

## Observation

1. Consider `nums = [3, 1, 2, 3, 3, 3, 3]`:
   - `low = 0` (`3`), `mid = 3` (`3`), `high = 6` (`3`).
   - Here `nums[low] == nums[mid] == nums[high]`. We cannot determine whether left or right half is sorted!
2. Solution to Ambiguity:
   - When `nums[low] == nums[mid] && nums[mid] == nums[high]`:
     - Shrink both ends: `low++` and `high--`.
3. Otherwise, use standard Rotated Sorted Array Binary Search logic.

---

## Intuition

1. Calculate `mid`. If `nums[mid] == target`, return `true`.
2. If `nums[low] == nums[mid] && nums[mid] == nums[high]`:
   - Shrink search space: `low++`, `high--`.
3. Else if Left Half is sorted (`nums[low] <= nums[mid]`):
   - If `nums[low] <= target && target < nums[mid]`: `high = mid - 1`.
   - Else: `low = mid + 1`.
4. Else (Right Half is sorted):
   - If `nums[mid] < target && target <= nums[high]`: `low = mid + 1`.
   - Else: `high = mid - 1`.

---

## Algorithm

1. `low = 0`, `high = nums.size() - 1`.
2. While `low <= high`:
   a. `mid = low + (high - low) / 2`.
   b. If `nums[mid] == target`, return `true`.
   c. If `nums[low] == nums[mid] && nums[mid] == nums[high]`:
      - `low++`, `high--`.
   d. Else if `nums[low] <= nums[mid]` (Left half is sorted):
      - If `nums[low] <= target && target < nums[mid]`: `high = mid - 1`.
      - Else: `low = mid + 1`.
   e. Else (Right half is sorted):
      - If `nums[mid] < target && target <= nums[high]`: `low = mid + 1`.
      - Else: `high = mid - 1`.
3. Return `false`.

---

## Clean C++17 Solution

```cpp
#include <vector>

class Solution {
public:
    bool search(const std::vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (nums[mid] == target) {
                return true;
            }
            
            // Ambiguity case caused by duplicates
            if (nums[low] == nums[mid] && nums[mid] == nums[high]) {
                low++;
                high--;
                continue;
            }
            
            // Check if left half is sorted
            if (nums[low] <= nums[mid]) {
                if (nums[low] <= target && target < nums[mid]) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            } 
            // Otherwise, right half is sorted
            else {
                if (nums[mid] < target && target <= nums[high]) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
        }
        
        return false;
    }
};
```

---

## Dry Run

### Input
- `nums = [2, 5, 6, 0, 0, 1, 2]`, `target = 0`

### Execution Trace

| Step | `low` | `high` | `mid` | `nums[mid]` | Duplicate Ambiguity? | Sorted Half | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `0` (`2`) | `6` (`2`) | `3` | `0` | `nums[mid] == 0 == target` | - | **Return `true`** |

### Result
- Output: `true`

---

## Time Complexity

- **Average Time Complexity**: $\mathcal{O}(\log N)$
  - When duplicates are few, binary search halves search space at each step.
- **Worst-Case Time Complexity**: $\mathcal{O}(N)$
  - Occurs when all elements are identical (e.g. `[1, 1, 1, 1, 1]`), causing `low++` and `high--` to shrink element-by-element.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This is Optimal

- Handles duplicates correctly while preserving $\mathcal{O}(\log N)$ average binary search time.
- Uses zero extra memory ($\mathcal{O}(1)$ space).

---

## Common Mistakes

1. **Ignoring Ambiguity Case**: Not checking `nums[low] == nums[mid] && nums[mid] == nums[high]`, causing algorithm to misclassify an unsorted half as sorted!
2. **Infinite Loop**: Forgetting `continue` or not incrementing/decrementing `low`/`high` when duplicates match.
