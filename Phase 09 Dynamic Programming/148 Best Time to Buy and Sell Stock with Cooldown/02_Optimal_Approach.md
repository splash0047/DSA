# Best Time to Buy and Sell Stock with Cooldown

## Pattern Used

- **Pattern**: **State Machine DP (Space-Optimized Finite State Automaton)**
- **Concept**:
  - Model stock trading state on day `i` as 3 possible states:
    1. `hold`: Maximum profit on day `i` if holding a stock.
    2. `sold`: Maximum profit on day `i` if just sold a stock today.
    3. `rest`: Maximum profit on day `i` if in a cooldown / non-holding state.
  - State Transitions:
    - `next_hold = max(hold, rest - price)` (Hold previous stock OR Buy new stock from `rest`).
    - `next_sold = hold + price` (Sell stock currently held).
    - `next_rest = max(rest, sold)` (Stay in `rest` OR transition from `sold` after 1-day cooldown).
  - Update `hold = next_hold, sold = next_sold, rest = next_rest`.
  - Return `max(sold, rest)`.

---

## Observation

1. Initial states before Day 1:
   - `hold = -INF` (Cannot hold stock before starting).
   - `sold = 0` (No stock sold yet).
   - `rest = 0` (In clean rest state).
2. The 1-day cooldown restriction is modeled naturally: Buying a stock (`next_hold`) requires coming from the `rest` state, NOT the `sold` state!

---

## Intuition

Think of your status every day as being in one of 3 modes: Holding a share, Just sold a share today, or Resting. Each day, evaluate how your max profit changes if you switch between these 3 modes.

---

## Algorithm

1. `hold = -INF`, `sold = 0`, `rest = 0`.
2. For each `price` in `prices`:
   - `prev_hold = hold`.
   - `hold = max(hold, rest - price)`.
   - `rest = max(rest, sold)`.
   - `sold = prev_hold + price`.
3. Return `max(sold, rest)`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>
#include <climits>

class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        if (prices.empty()) return 0;
        
        int hold = INT_MIN; // Max profit if currently holding a stock
        int sold = 0;       // Max profit if just sold a stock today
        int rest = 0;       // Max profit if resting / in cooldown
        
        for (int price : prices) {
            int prev_hold = hold;
            int prev_sold = sold;
            
            // Hold: Continue holding stock OR buy stock today (from rest state)
            hold = std::max(hold, rest - price);
            
            // Sold: Sell stock today (must have held stock previously)
            sold = prev_hold + price;
            
            // Rest: Stay resting OR enter rest after being in sold state (cooldown)
            rest = std::max(rest, prev_sold);
        }
        
        return std::max(sold, rest);
    }
};
```

---

## Dry Run

### Input
- `prices = [1, 2, 3, 0, 2]`

### Execution Trace

- Init: `hold = -INF, sold = 0, rest = 0`.
- Day 1 (`price = 1`):
  - `hold = max(-INF, 0 - 1) = -1`.
  - `sold = -INF + 1 = -INF`.
  - `rest = max(0, 0) = 0`.
- Day 2 (`price = 2`):
  - `hold = max(-1, 0 - 2) = -1`.
  - `sold = -1 + 2 = 1`.
  - `rest = max(0, -INF) = 0`.
- Day 3 (`price = 3`):
  - `hold = max(-1, 0 - 3) = -1`.
  - `sold = -1 + 3 = 2`.
  - `rest = max(0, 1) = 1`.
- Day 4 (`price = 0`):
  - `hold = max(-1, 1 - 0) = 1` (Buy at 0!).
  - `sold = -1 + 0 = -1`.
  - `rest = max(1, 2) = 2`.
- Day 5 (`price = 2`):
  - `hold = max(1, 2 - 2) = 1`.
  - `sold = 1 + 2 = 3` (Sell at 2!).
  - `rest = max(2, -1) = 2`.

### Result
- Output: `max(3, 2) = 3`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single loop through `prices` array of size $N$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses constant extra space (`hold`, `sold`, `rest`).

---

## Why This is Optimal

- Solves stock trading with cooldown in linear $\mathcal{O}(N)$ time.
- Uses $\mathcal{O}(1)$ space by maintaining 3 state variables instead of a full DP table.

---

## Common Mistakes

1. **Incorrect State Update Order**: Updating `rest` using the newly modified `sold` variable instead of `prev_sold`.
2. **Allowing Buy Immediately After Sell**: Buying from `sold` state instead of `rest` state (violates 1-day cooldown).
