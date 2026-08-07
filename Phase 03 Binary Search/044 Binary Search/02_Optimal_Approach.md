# Binary Search

## Pattern Used

- **Pattern**: **Classic Binary Search (Divide and Conquer)**
- **Concept**: Maintain `low = 0` and `high = n - 1`. Calculate `mid = low + (high - low) / 2`. Compare `nums[mid]` with `target` to eliminate half the search space per iteration.

---

## Observation

1. Because `nums` is sorted:
   - If `nums[mid] == target`: Found target! Return `mid`.
   - If `nums[mid] < target`: Target must lie in right half $\rightarrow$ `low = mid + 1`.
   - If `nums[mid] > target`: Target must lie in left half $\rightarrow$ `high = mid - 1`.
2. Overflow Guard: Calculate `mid` using `low + (high - low) / 2` instead of `(low + high) / 2` to prevent 32-bit integer overflow.

---

## Intuition

Start with the entire search space `[0 ... n - 1]`. At each step, inspect the midpoint:
- If exact match, return index immediately.
- Otherwise, discard the half that cannot possibly contain `target`.

---

## Algorithm

1. `low = 0`, `high = nums.size() - 1`.
2. While `low <= high`:
   a. `mid = low + (high - low) / 2`.
   b. If `nums[mid] == target`: return `mid`.
   c. Else if `nums[mid] < target`: `low = mid + 1`.
   d. Else: `high = mid - 1`.
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
            } else if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        
        return -1;
    }
};
```

---

## Dry Run

### Input
- `nums = [-1, 0, 3, 5, 9, 12]`, `target = 9`

### Execution Trace

| Step | `low` | `high` | `mid = low + (high - low) / 2` | `nums[mid]` | Compare with Target (`9`) | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `0` | `5` | `2` | `3` | `3 < 9` (Target is larger) | `low = mid + 1 = 3` |
| 2 | `3` | `5` | `4` | `9` | `9 == 9` (**Exact Match!**) | **Return `4`** |

### Result
- Output: `4`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(\log N)$
  - Search space halves in each iteration.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses constant extra space (`low`, `high`, `mid`).

---

## Why This is Optimal

- Logarithmic $\mathcal{O}(\log N)$ time is the optimal theoretical lower bound for searching in a sorted 1D array.
- Uses zero auxiliary memory ($\mathcal{O}(1)$ space).

---

## Common Mistakes

1. **Integer Overflow in Mid Calculation**: Writing `mid = (low + high) / 2` causes integer overflow when `low + high > INT_MAX`. Use `mid = low + (high - low) / 2`.
2. **Incorrect Loop Termination**: Writing `while (low < high)` skips evaluating single-element ranges (`low == high`).
