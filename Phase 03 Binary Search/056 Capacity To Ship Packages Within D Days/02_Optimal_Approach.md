# Capacity To Ship Packages Within D Days

## Pattern Used

- **Pattern**: **Binary Search on Answer Space (Monotonic Predicate Function)**
- **Concept**: The ship capacity $C$ must lie within range $[\max(\text{weights}), \sum \text{weights}]$. Use Binary Search to find the minimum capacity $C$ such that `canShip(C, days)` returns `true`.

---

## Observation

1. Search Space Boundaries:
   - Minimum capacity: `low = max(weights)` (capacity must be at least as large as the heaviest single package, otherwise that package can never be loaded!).
   - Maximum capacity: `high = sum(weights)` (capacity large enough to ship all packages in a single day).
2. Monotonicity:
   - If capacity $C$ finishes shipping in $\le D$ days, any capacity $> C$ will ALSO finish in $\le D$ days.
   - If capacity $C$ requires $> D$ days, any capacity $< C$ is too small.

---

## Intuition

Set search space `low = max(weights)` and `high = sum(weights)`. Test midpoint capacity `mid`:
- If `canShip(mid)` is `true`: `mid` is a valid capacity candidate. Record `ans = mid` and contract `high = mid - 1` to look for a smaller valid capacity.
- If `canShip(mid)` is `false`: `mid` is too small. Increase capacity `low = mid + 1`.

---

## Algorithm

1. `low = max(weights)`, `high = sum(weights)`, `ans = high`.
2. While `low <= high`:
   a. `mid = low + (high - low) / 2`.
   b. `days_needed = 1`, `current_load = 0`.
   c. For each `w` in `weights`:
      - If `current_load + w > mid`:
        - `days_needed++`.
        - `current_load = w`.
      - Else: `current_load += w`.
   d. If `days_needed <= days`:
      - `ans = mid`.
      - `high = mid - 1`.
   e. Else:
      - `low = mid + 1`.
3. Return `ans`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <numeric>
#include <algorithm>

class Solution {
private:
    bool canShip(const std::vector<int>& weights, int days, int cap) {
        int days_needed = 1;
        int current_load = 0;
        
        for (int w : weights) {
            if (current_load + w > cap) {
                days_needed++;
                current_load = w;
            } else {
                current_load += w;
            }
        }
        
        return days_needed <= days;
    }
public:
    int shipWithinDays(const std::vector<int>& weights, int days) {
        int low = *std::max_element(weights.begin(), weights.end());
        int high = std::accumulate(weights.begin(), weights.end(), 0);
        int ans = high;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (canShip(weights, days, mid)) {
                ans = mid;
                high = mid - 1; // Try smaller capacity
            } else {
                low = mid + 1;  // Capacity too small, increase capacity
            }
        }
        
        return ans;
    }
};
```

---

## Dry Run

### Input
- `weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, `days = 5`
- `low = 10` ($\max$), `high = 55` ($\sum$)

### Execution Trace

| Step | `low` | `high` | `mid` (Capacity) | Simulation Days Needed | `days_needed <= 5`? | `ans` | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `10` | `55` | `32` | 2 days | `2 <= 5` (**Yes**) | `32` | `high = mid - 1 = 31` |
| 2 | `10` | `31` | `20` | 3 days | `3 <= 5` (**Yes**) | `20` | `high = mid - 1 = 19` |
| 3 | `10` | `19` | `14` | 6 days | `6 <= 5` (No) | `20` | `low = mid + 1 = 15` |
| 4 | `15` | `19` | `17` | 4 days | `4 <= 5` (**Yes**) | `17` | `high = mid - 1 = 16` |
| 5 | `15` | `16` | `15` | 5 days | `5 <= 5` (**Yes**) | **`15`** | `high = mid - 1 = 14` |
| End | `15` | `14` | - | - | - | `low > high` (Stop) | Return `15` |

### Result
- Output: `15`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log(\sum W))$
  - Binary search over capacity range takes $\mathcal{O}(\log(\sum W))$ steps; simulation takes $\mathcal{O}(N)$ per step.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This is Optimal

- Computes least required ship capacity in optimal $\mathcal{O}(N \log(\sum W))$ time.
- Uses zero extra memory.

---

## Common Mistakes

1. **Incorrect Search Lower Bound**: Setting `low = 0` or `low = 1` instead of `max(weights)`. If capacity is smaller than `max(weights)`, the ship can NEVER load the heaviest package!
2. **Initial Day Count**: Starting simulation with `days_needed = 0` instead of `1`.
