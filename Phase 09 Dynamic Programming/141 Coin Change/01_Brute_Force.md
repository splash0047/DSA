# Coin Change

- **Problem Number**: 322
- **Platform**: LeetCode #322
- **Difficulty**: Medium
- **Pattern**: Unmemoized Backtracking Branching

---

## Brute Force Intuition

To form `amount`, try subtracting every coin denomination `c` from `coins`. The minimum coins to form `amount` is:
$$1 + \min_{c \in \text{coins}} (\text{coinChange}(\text{amount} - c))$$

A naive recursive implementation tests subtracting all coin denominations at every step until reaching base case `amount == 0` (0 coins needed) or `amount < 0` (invalid path).

---

## Algorithm

1. `minCoins(coins, amount)`:
   - If `amount == 0`, return `0`.
   - If `amount < 0`, return `INF`.
   - `res = INF`.
   - For each coin `c` in `coins`:
     - `subRes = minCoins(coins, amount - c)`.
     - If `subRes != INF`:
       - `res = min(res, 1 + subRes)`.
   - Return `res`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
private:
    const int INF = 1e9;
    
    int minCoins(const std::vector<int>& coins, int amount) {
        if (amount == 0) return 0;
        if (amount < 0) return INF;
        
        int res = INF;
        for (int coin : coins) {
            int subRes = minCoins(coins, amount - coin);
            if (subRes != INF) {
                res = std::min(res, 1 + subRes);
            }
        }
        
        return res;
    }

public:
    int coinChange(std::vector<int>& coins, int amount) {
        int ans = minCoins(coins, amount);
        return ans >= INF ? -1 : ans;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(S^A)$
  - Where $S$ is number of coins and $A$ is `amount`. Branching factor $S$ for depth $A$ yields exponential time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(A)$
  - Call stack depth equals `amount`.

---

## Why This Approach Is Not Optimal

Re-evaluating identical target amounts leads to exponential $\mathcal{O}(S^A)$ time. Using **Bottom-Up 1D Unbounded Knapsack DP**, we can compute minimum coins for all amounts up to `amount` in pseudo-polynomial $\mathcal{O}(\text{amount} \times \text{coins.length})$ time!
