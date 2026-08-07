# Single Element in a Sorted Array

## Pattern Used

- **Pattern**: **Binary Search on Even/Odd Index Parity**
- **Concept**: Before the single element, pairs start at an **even** index `(0, 1)`, `(2, 3)`, `(4, 5)`. After the single element, pairs shift and start at an **odd** index `(1, 2)`, `(3, 4)`.

---

## Observation

1. Let `mid` be an **even index**.
   - If `nums[mid] == nums[mid + 1]`: The single element has NOT appeared yet! The single element lies strictly to the right $\rightarrow$ `low = mid + 2`.
   - If `nums[mid] != nums[mid + 1]`: The single element has already appeared, or `nums[mid]` IS the single element! The single element lies to the left (including `mid`) $\rightarrow$ `high = mid`.
2. To ensure `mid` is always even:
   - Calculate `mid = low + (high - low) / 2`.
   - `if (mid % 2 == 1) mid--;` (adjust `mid` to even).

---

## Intuition

Before the single element: `(even_idx, odd_idx)` contain identical elements.
After the single element: `(odd_idx, even_idx)` contain identical elements.

By checking whether `nums[even_idx] == nums[even_idx + 1]`, we instantly know which side of the single element we are currently on!

---

## Algorithm

1. `low = 0`, `high = nums.size() - 1`.
2. While `low < high`:
   a. `mid = low + (high - low) / 2`.
   b. `if (mid % 2 == 1) mid--`. (Force `mid` to be even).
   c. If `nums[mid] == nums[mid + 1]`:
      - `low = mid + 2` (Single element is to the right).
   d. Else:
      - `high = mid` (Single element is at `mid` or to the left).
3. Return `nums[low]`.

---

## Clean C++17 Solution

```cpp
#include <vector>

class Solution {
public:
    int singleNonDuplicate(const std::vector<int>& nums) {
        int low = 0;
        int high = nums.size() - 1;
        
        while (low < high) {
            int mid = low + (high - low) / 2;
            
            // Force mid to be even index
            if (mid % 2 == 1) {
                mid--;
            }
            
            // If even-indexed element equals next element, single element is on the right
            if (nums[mid] == nums[mid + 1]) {
                low = mid + 2;
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
- `nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]`
- `n = 9`

### Execution Trace

| Step | `low` | `high` | Initial `mid` | Adjusted Even `mid` | `nums[mid]` | `nums[mid+1]` | Match (`nums[mid] == nums[mid+1]`) | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `0` | `8` | `4` | `4` | `nums[4] = 3` | `nums[5] = 4` | `3 != 4` (Mismatch) | `high = mid = 4` |
| 2 | `0` | `4` | `2` | `2` | `nums[2] = 2` | `nums[3] = 3` | `2 != 3` (Mismatch) | `high = mid = 2` |
| 3 | `0` | `2` | `1` | `0` | `nums[0] = 1` | `nums[1] = 1` | `1 == 1` (**Match!**) | `low = mid + 2 = 2` |
| End | `2` | `2` | - | - | - | - | `low == high` (Stop) | **Return `nums[2] = 2`** |

### Result
- Output: `2`

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

- Meets the mandatory $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space constraints.

---

## Common Mistakes

1. **Not Forcing `mid` to be Even**: Comparing `nums[mid] == nums[mid+1]` without checking index parity yields incorrect decisions when `mid` is odd.
2. **Out of Bounds Check**: Writing `nums[mid] == nums[mid-1]` without handling `mid == 0`. Forcing `mid` to even and checking `mid + 1` avoids negative index bounds.
