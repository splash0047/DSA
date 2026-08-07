# Aggressive Cows

## Pattern Used

- **Pattern**: **Binary Search on Answer Space (Maximize Minimum Distance)**
- **Concept**: Sort `stalls` first. Search for the maximum valid minimum distance $d \in [1, \text{stalls}[n-1] - \text{stalls}[0]]$. The predicate function `canPlace(d, k)` verifies if $k$ cows can be placed at least $d$ units apart.

---

## Observation

1. Why Sort? Sorting positions `stalls` allows greedy placement: placing cows at the earliest possible valid stall maximizes available remaining space for future cows.
2. Search Space:
   - `low = 1` (minimum possible stall distance).
   - `high = stalls[n-1] - stalls[0]` (maximum possible distance between extreme stalls).
3. Monotonicity:
   - If distance $d$ is valid (allows placing $\ge k$ cows), any distance $< d$ is ALSO valid.
   - We want to find the **maximum** distance $d$ for which `canPlace(d)` returns `true`.

---

## Intuition

1. Sort `stalls`.
2. `low = 1`, `high = stalls[n - 1] - stalls[0]`.
3. Test midpoint distance `mid`:
   - Place 1st cow at `stalls[0]`. For each subsequent stall, place a cow if `stalls[i] - last_pos >= mid`.
   - If `cows_placed >= k`: `mid` distance is valid! Record `ans = mid` and expand `low = mid + 1` to check if a larger minimum distance is possible.
   - If `cows_placed < k`: `mid` distance is too large. Contract `high = mid - 1`.

---

## Algorithm

1. Sort `stalls`.
2. `low = 1`, `high = stalls[n - 1] - stalls[0]`, `ans = 0`.
3. While `low <= high`:
   a. `mid = low + (high - low) / 2`.
   b. `cows_placed = 1`, `last_pos = stalls[0]`.
   c. For `i` from `1` to `n - 1`:
      - If `stalls[i] - last_pos >= mid`:
        - `cows_placed++`.
        - `last_pos = stalls[i]`.
   d. If `cows_placed >= k`:
      - `ans = mid`.
      - `low = mid + 1`.
   e. Else:
      - `high = mid - 1`.
4. Return `ans`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>

class Solution {
private:
    bool canPlaceCows(const std::vector<int>& stalls, int k, int dist) {
        int cows_placed = 1;
        int last_pos = stalls[0];
        
        for (size_t i = 1; i < stalls.size(); ++i) {
            if (stalls[i] - last_pos >= dist) {
                cows_placed++;
                last_pos = stalls[i];
            }
        }
        
        return cows_placed >= k;
    }
public:
    int aggressiveCows(std::vector<int>& stalls, int k) {
        std::sort(stalls.begin(), stalls.end());
        
        int low = 1;
        int high = stalls.back() - stalls.front();
        int ans = 0;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (canPlaceCows(stalls, k, mid)) {
                ans = mid;
                low = mid + 1;  // Try to maximize distance
            } else {
                high = mid - 1; // Distance too large, decrease distance
            }
        }
        
        return ans;
    }
};
```

---

## Dry Run

### Input
- `stalls = [1, 2, 4, 8, 9]`, `k = 3`
- `low = 1`, `high = 8`

### Execution Trace

| Step | `low` | `high` | `mid` (Distance) | Placed Stalls | `cows_placed` | `cows_placed >= 3`? | `ans` | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `1` | `8` | `4` | `1`, `8` (distance 7) | 2 | `2 >= 3` (No) | `0` | `high = mid - 1 = 3` |
| 2 | `1` | `3` | `2` | `1`, `4` (dist 3), `8` (dist 4) | 3 | `3 >= 3` (**Yes**) | `2` | `low = mid + 1 = 3` |
| 3 | `3` | `3` | `3` | `1`, `4` (dist 3), `8` (dist 4) | 3 | `3 >= 3` (**Yes**) | **`3`** | `low = mid + 1 = 4` |
| End | `4` | `3` | - | - | - | - | `low > high` (Stop) | Return `3` |

### Result
- Output: `3` (Cows placed at `[1, 4, 8]`)

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log N + N \log(\text{max\_dist}))$
  - Sorting takes $\mathcal{O}(N \log N)$.
  - Binary search takes $\mathcal{O}(\log(\text{max\_dist}))$ steps; verification takes $\mathcal{O}(N)$ per step.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$ or $\mathcal{O}(\log N)$ auxiliary space for sorting.

---

## Why This is Optimal

- Solves "Maximize Minimum Distance" in optimal $\mathcal{O}(N \log N + N \log D)$ time.
- Uses zero extra memory.

---

## Common Mistakes

1. **Forgetting to Sort `stalls`**: Greedy placement only works on a sorted array of positions!
2. **Expanding in Wrong Direction**: Setting `high = mid - 1` when `canPlace(mid)` is true. The goal is to MAXIMIZE minimum distance, so we must set `low = mid + 1`.
