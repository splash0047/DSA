# Best Time to Buy and Sell Stock with Cooldown

- **Problem Number**: 309
- **Platform**: LeetCode #309
- **Difficulty**: Medium
- **Pattern**: Unmemoized Decision State Recursion

---

## Brute Force Intuition

At each day `i`, we maintain a state variable `buying` (boolean flag):
1. **If `buying == true`**:
   - Option A: **Buy stock on day `i`** $\implies$ pay `prices[i]`, transition to `buying = false` at day `i + 1`.
   - Option B: **Skip day `i`** $\implies$ remain `buying = true` at day `i + 1`.
2. **If `buying == false` (Holding stock to sell)**:
   - Option A: **Sell stock on day `i`** $\implies$ earn `prices[i]`, transition to `buying = true` at day `i + 2` (mandatory **1-day cooldown** skips day `i + 1`).
   - Option B: **Skip day `i`** $\implies$ remain `buying = false` at day `i + 1`.

---

## Algorithm

1. `dfs(i, buying)`:
   - Base Case: If `i >= prices.length()`, return `0`.
   - If `buying`:
     - `buy = -prices[i] + dfs(i + 1, false)`.
     - `cooldown = dfs(i + 1, true)`.
     - Return `max(buy, cooldown)`.
   - Else:
     - `sell = prices[i] + dfs(i + 2, true)` (skips `i + 1` for cooldown!).
     - `cooldown = dfs(i + 1, false)`.
     - Return `max(sell, cooldown)`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
private:
    int dfs(const std::vector<int>& prices, int i, bool buying) {
        if (i >= prices.size()) {
            return 0;
        }
        
        if (buying) {
            int buy = -prices[i] + dfs(prices, i + 1, false);
            int skip = dfs(prices, i + 1, true);
            return std::max(buy, skip);
        } else {
            int sell = prices[i] + dfs(prices, i + 2, true); // Cooldown skips to i + 2
            int skip = dfs(prices, i + 1, false);
            return std::max(sell, skip);
        }
    }

public:
    int maxProfit(std::vector<int>& prices) {
        return dfs(prices, 0, true);
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(2^N)$
  - Branching factor of 2 at each day yields exponential recursion depth.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Call stack depth.

---

## Why This Approach Is Not Optimal

Re-evaluating identical $(i, \text{buying})$ states repeatedly takes exponential $\mathcal{O}(2^N)$ time. Using **State Machine DP (Space-Optimized 3-State Machine)**, we compute maximum profit in linear $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space!
