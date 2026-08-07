# Search Insert Position

## Pattern Used

- **Pattern**: **Binary Search (Lower Bound)**
- **Concept**: Find the smallest index `i` such that `nums[i] >= target`. If all elements are `< target`, return `n`.

---

## Observation

1. Searching for insertion position in a sorted array is mathematically identical to finding the **Lower Bound** of `target`.
2. Maintain `low = 0`, `high = n - 1`, and `ans = n`.
3. If `nums[mid] >= target`:
   - `nums[mid]` is a valid insertion candidate! Record `ans = mid`.
   - Search left half for an even smaller index $\rightarrow$ `high = mid - 1`.
4. If `nums[mid] < target`:
   - Search right half $\rightarrow$ `low = mid + 1`.

---

## Intuition

Binary search for the first index where `nums[mid] >= target`. If found, save `mid` and contract `high` leftward to look for an earlier valid index.

---

## Algorithm

1. `low = 0`, `high = nums.size() - 1`, `ans = nums.size()`.
2. While `low <= high`:
   a. `mid = low + (high - low) / 2`.
   b. If `nums[mid] >= target`:
      - `ans = mid`.
      - `high = mid - 1`.
   c. Else:
      - `low = mid + 1`.
3. Return `ans`.

---

## Clean C++17 Solution

```cpp
#include <vector>

class Solution {
public:
    int searchInsert(const std::vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        int ans = nums.size();
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (nums[mid] >= target) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        
        return ans;
    }
};
```

---

## Dry Run

### Input
- `nums = [1, 3, 5, 6]`, `target = 2`

### Execution Trace

| Step | `low` | `high` | `mid` | `nums[mid]` | `nums[mid] >= 2`? | `ans` | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Init | `0` | `3` | - | - | - | `4` | - |
| 1 | `0` | `3` | `1` | `3` | `3 >= 2` (**Yes**) | `1` | `high = mid - 1 = 0` |
| 2 | `0` | `0` | `0` | `1` | `1 >= 2` (No) | `1` | `low = mid + 1 = 1` |
| End | `1` | `0` | - | - | `low > high` (Stop) | **`1`** | Return `1` |

### Result
- Output: `1`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(\log N)$
  - Binary search reduces search space by half at each step.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space used.

---

## Why This is Optimal

- Computes lower bound insertion point in logarithmic $\mathcal{O}(\log N)$ time.
- Uses zero extra memory.

---

## Common Mistakes

1. **Returning `low` vs `ans`**: Forgetting to initialize `ans = n` to handle cases where `target` is strictly greater than all array elements.
2. **Standard Library Shortcut**: In C++, `std::lower_bound(nums.begin(), nums.end(), target) - nums.begin()` directly computes this in $\mathcal{O}(\log N)$. Be prepared to implement manually in technical interviews!
