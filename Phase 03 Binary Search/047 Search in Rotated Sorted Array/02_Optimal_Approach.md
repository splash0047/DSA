# Search in Rotated Sorted Array

## Pattern Used

- **Pattern**: **Modified Binary Search (Identify Sorted Half)**
- **Concept**: In any rotated sorted array, dividing the range at `mid` guarantees that **at least one half (left or right) is strictly sorted**.

---

## Observation

1. Compare `nums[low]` and `nums[mid]`:
   - If `nums[low] <= nums[mid]`: The **Left Half** `[low ... mid]` is sorted!
     - Check if `target` lies inside left half (`nums[low] <= target && target < nums[mid]`):
       - Yes $\rightarrow$ `high = mid - 1`.
       - No $\rightarrow$ `low = mid + 1`.
   - Else: The **Right Half** `[mid ... high]` is sorted!
     - Check if `target` lies inside right half (`nums[mid] < target && target <= nums[high]`):
       - Yes $\rightarrow$ `low = mid + 1`.
       - No $\rightarrow$ `high = mid - 1`.

---

## Intuition

At every step of binary search:
1. Identify which half is properly sorted (left or right).
2. Check if the `target` falls within the range of that sorted half.
3. If it does, narrow search to that sorted half. Otherwise, narrow search to the opposite half.

---

## Algorithm

1. `low = 0`, `high = nums.size() - 1`.
2. While `low <= high`:
   a. `mid = low + (high - low) / 2`.
   b. If `nums[mid] == target`, return `mid`.
   c. If `nums[low] <= nums[mid]` (Left half is sorted):
      - If `nums[low] <= target && target < nums[mid]`: `high = mid - 1`.
      - Else: `low = mid + 1`.
   d. Else (Right half is sorted):
      - If `nums[mid] < target && target <= nums[high]`: `low = mid + 1`.
      - Else: `high = mid - 1`.
3. Return `-1`.

---

## Clean C++17 Solution

```cpp
#include <vector>

class Solution {
public:
    int search(const std::vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (nums[mid] == target) {
                return mid;
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
        
        return -1;
    }
};
```

---

## Dry Run

### Input
- `nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 0`

### Execution Trace

| Step | `low` | `high` | `mid` | `nums[mid]` | Sorted Half | `target` Range Check | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `0` (`4`) | `6` (`2`) | `3` | `7` | Left `[4..7]` (`4 <= 7`) | `4 <= 0 < 7`? (**No**) | `low = mid + 1 = 4` |
| 2 | `4` (`0`) | `6` (`2`) | `5` | `1` | Left `[0..1]` (`0 <= 1`) | `0 <= 0 < 1`? (**Yes**) | `high = mid - 1 = 4` |
| 3 | `4` (`0`) | `4` (`0`) | `4` | `0` | `nums[4] == 0` | **Exact Match!** | **Return `4`** |

### Result
- Output: `4`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(\log N)$
  - Binary search reduces search space by half at each step.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This is Optimal

- Solves search in a rotated sorted array in logarithmic $\mathcal{O}(\log N)$ time.
- Uses zero extra memory ($\mathcal{O}(1)$ space).

---

## Common Mistakes

1. **Incorrect Bound Comparisons**: Using `<` instead of `<=` when checking `nums[low] <= nums[mid]` or `nums[low] <= target`. Strictly less `<` fails when `low == mid`.
2. **Not Verifying Range Inclusion**: Branching based solely on whether `nums[mid] < target` without checking if `target` is within `[nums[low], nums[mid])` or `(nums[mid], nums[high]]`.
