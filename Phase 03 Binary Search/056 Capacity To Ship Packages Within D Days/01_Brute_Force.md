# Capacity To Ship Packages Within D Days

- **Problem Number**: 1011
- **Platform**: LeetCode #1011
- **Difficulty**: Medium
- **Pattern**: Linear Search on Capacity Space

---

## Brute Force Intuition

Test every possible ship capacity `cap` starting from `max(weights)` up to `sum(weights)`. For each candidate capacity `cap`, simulate the shipping process day-by-day:
- Load packages onto the ship sequentially until adding the next package exceeds `cap`.
- Increment required day count.
- If total required days $\le \text{days}$, return `cap`.

---

## Algorithm

1. `low = max(weights)`, `high = sum(weights)`.
2. Loop capacity `cap` from `low` to `high`:
   a. `current_load = 0`, `days_needed = 1`.
   b. For each `w` in `weights`:
      - If `current_load + w > cap`:
        - `days_needed++`.
        - `current_load = w`.
      - Else: `current_load += w`.
   c. If `days_needed <= days`, return `cap`.
3. Return `high`.

---

## Code

```cpp
#include <vector>
#include <numeric>
#include <algorithm>

class Solution {
public:
    int shipWithinDays(const std::vector<int>& weights, int days) {
        int max_w = *std::max_element(weights.begin(), weights.end());
        int sum_w = std::accumulate(weights.begin(), weights.end(), 0);
        
        for (int cap = max_w; cap <= sum_w; ++cap) {
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
            
            if (days_needed <= days) {
                return cap;
            }
        }
        
        return sum_w;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}((\text{sum}(W) - \max(W)) \times N)$
  - Testing each capacity takes $\mathcal{O}(N)$ simulation time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

Linear search over the capacity range takes $\mathcal{O}((\sum W - \max W) \times N)$ time. Because the shipping feasibility function `canShip(capacity)` is **monotonic** (if capacity $C$ can ship packages within $D$ days, any capacity $> C$ can also ship them), we can apply **Binary Search on Answer Space** in $\mathcal{O}(N \log(\sum W))$ time.
