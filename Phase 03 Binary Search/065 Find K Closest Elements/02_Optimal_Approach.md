# Find K Closest Elements

## Pattern Used

- **Pattern**: **Binary Search for Window Starting Index**
- **Concept**: Since `arr` is pre-sorted, the $k$ closest elements MUST form a **contiguous subarray window** of length $k$. Binary search for the starting index `low` of this window in range $[0, N - K]$.

---

## Observation

1. Candidate Window: A valid window of length $k$ starts at index `mid` and ends at `mid + k - 1`.
2. Comparing Boundaries:
   - Consider element `arr[mid]` (left boundary of current window) and `arr[mid + k]` (element immediately past the right boundary).
   - If `x - arr[mid] > arr[mid + k] - x`:
     - Distance from `x` to `arr[mid]` is strictly larger than distance to `arr[mid + k]`.
     - Thus, `arr[mid]` is worse than `arr[mid + k]`. Shift window rightward $\rightarrow$ `low = mid + 1`.
   - Else (`x - arr[mid] <= arr[mid + k] - x`):
     - `arr[mid]` is at least as close (or closer due to smaller value tie-breaker). Shift window leftward $\rightarrow$ `high = mid`.
3. Loop condition: `while (low < high)`. Terminates when `low` is the optimal window starting index!

---

## Intuition

Binary search directly locates the optimal starting index `low` of the $k$-element contiguous subarray. We compare the distance of the element at `mid` vs the element at `mid + k` to decide whether to shift the window left or right.

---

## Algorithm

1. `low = 0`, `high = arr.size() - k`.
2. While `low < high`:
   a. `mid = low + (high - low) / 2`.
   b. If `x - arr[mid] > arr[mid + k] - x`:
      - `low = mid + 1`.
   c. Else:
      - `high = mid`.
3. Return subarray `std::vector<int>(arr.begin() + low, arr.begin() + low + k)`.

---

## Clean C++17 Solution

```cpp
#include <vector>

class Solution {
public:
    std::vector<int> findClosestElements(const std::vector<int>& arr, int k, int x) {
        int low = 0;
        int high = arr.size() - k;
        
        while (low < high) {
            int mid = low + (high - low) / 2;
            
            // Compare distance of left boundary element arr[mid] 
            // vs element just outside right boundary arr[mid + k]
            if (x - arr[mid] > arr[mid + k] - x) {
                low = mid + 1; // Shift window rightward
            } else {
                high = mid;    // Shift window leftward or stay
            }
        }
        
        return std::vector<int>(arr.begin() + low, arr.begin() + low + k);
    }
};
```

---

## Dry Run

### Input
- `arr = [1, 2, 3, 4, 5]`, `k = 4`, `x = 3`
- `low = 0`, `high = 5 - 4 = 1`

### Execution Trace

| Step | `low` | `high` | `mid` | `arr[mid]` | `arr[mid+k]` | Distance Comparison | `(x - arr[mid]) > (arr[mid+k] - x)`? | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `0` | `1` | `0` | `arr[0] = 1` | `arr[4] = 5` | `3 - 1 = 2` vs `5 - 3 = 2` | `2 > 2` (No) | `high = mid = 0` |
| End | `0` | `0` | - | - | - | - | `low == high` (Stop) | Return `arr[0...3] = [1, 2, 3, 4]` |

### Result
- Output: `[1, 2, 3, 4]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(\log(N - K) + K)$
  - Binary search for starting index takes $\mathcal{O}(\log(N - K))$.
  - Slicing output subarray takes $\mathcal{O}(K)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Auxiliary space excluding output array.

---

## Why This is Optimal

- Solves $K$ closest elements search in optimal $\mathcal{O}(\log(N - K) + K)$ time.
- Uses zero extra memory.

---

## Common Mistakes

1. **Forgetting Absolute Value Rationale**: Writing `abs(arr[mid] - x) > abs(arr[mid+k] - x)` without considering sign direction. Writing `x - arr[mid] > arr[mid + k] - x` correctly preserves the tie-breaker rule ($a < b$).
2. **Incorrect `high` Boundary**: Sizing `high = arr.size()` instead of `arr.size() - k`.
