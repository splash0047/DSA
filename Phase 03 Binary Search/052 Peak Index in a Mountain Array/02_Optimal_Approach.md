# Peak Index in a Mountain Array

## Pattern Used

- **Pattern**: **Binary Search on Mountain Slope**
- **Concept**: Compare `arr[mid]` with `arr[mid + 1]`:
  - If `arr[mid] < arr[mid + 1]`: We are on the **ascending slope**. The peak lies strictly to the right $\rightarrow$ `low = mid + 1`.
  - If `arr[mid] > arr[mid + 1]`: We are on the **descending slope** (or at the peak). The peak lies at or to the left $\rightarrow$ `high = mid`.

---

## Observation

1. Mountain Array Structure:
   - Left of peak: Strictly Increasing ($arr[i] < arr[i+1]$).
   - Peak: Maximum element.
   - Right of peak: Strictly Decreasing ($arr[i] > arr[i+1]$).
2. Monotonicity enables Binary Search:
   - If `arr[mid] < arr[mid + 1]`: Move rightward (`low = mid + 1`).
   - If `arr[mid] > arr[mid + 1]`: Move leftward (`high = mid`).
3. Loop condition: `while (low < high)`. Terminates when `low == high` at the peak index.

---

## Intuition

Inspect midpoint slope:
- Going Uphill (`arr[mid] < arr[mid + 1]`) $\rightarrow$ Push `low` rightward (`mid + 1`).
- Going Downhill (`arr[mid] > arr[mid + 1]`) $\rightarrow$ Pull `high` leftward (`mid`).

---

## Algorithm

1. `low = 0`, `high = arr.size() - 1`.
2. While `low < high`:
   a. `mid = low + (high - low) / 2`.
   b. If `arr[mid] < arr[mid + 1]`:
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
    int peakIndexInMountainArray(const std::vector<int>& arr) {
        int low = 0;
        int high = arr.size() - 1;
        
        while (low < high) {
            int mid = low + (high - low) / 2;
            
            if (arr[mid] < arr[mid + 1]) {
                low = mid + 1; // Ascending slope -> Peak is to the right
            } else {
                high = mid;    // Descending slope -> Peak is to the left or at mid
            }
        }
        
        return low;
    }
};
```

---

## Dry Run

### Input
- `arr = [0, 10, 5, 2]`

### Execution Trace

| Step | `low` | `high` | `mid` | `arr[mid]` | `arr[mid+1]` | `arr[mid] < arr[mid+1]`? | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `0` | `3` | `1` | `10` | `5` | `10 < 5` (No) | `high = mid = 1` |
| 2 | `0` | `1` | `0` | `0` | `10` | `0 < 10` (**Yes**) | `low = mid + 1 = 1` |
| End | `1` | `1` | - | - | - | `low == high` (Stop) | **Return `1`** |

### Result
- Output: `1` (Value `10` is the peak)

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

- Solves peak search in a unimodal mountain array in logarithmic $\mathcal{O}(\log N)$ time.
- Uses zero extra memory.

---

## Common Mistakes

1. **Writing `high = mid - 1`**: When `arr[mid] > arr[mid + 1]`, `mid` itself could be the peak element! Setting `high = mid - 1` discards the correct peak index. Use `high = mid`.
2. **Infinite Loop Condition**: Using `while (low <= high)` with `high = mid` causes an infinite loop when `low == high`. Use `while (low < high)`.
