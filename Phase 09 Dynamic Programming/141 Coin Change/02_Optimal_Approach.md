# Coin Change

## Pattern Used

- **Pattern**: **Bottom-Up 1D DP (Unbounded Knapsack / Minimum Cost Path)**
- **Concept**:
  - `dp[i]` represents the minimum number of coins needed to make up amount `i`.
  - Base Case: `dp[0] = 0` (0 coins needed for amount 0). All other `dp[i] = INF` (where `INF = amount + 1`).
  - State Transition:
    - For each amount `i` from `1` to `amount`:
      - For each `coin` in `coins`:
        - If `i - coin >= 0`:
          - `dp[i] = min(dp[i], 1 + dp[i - coin])`.
  - Return `dp[amount] > amount ? -1 : dp[amount]`.

---

## Observation

1. Unbounded Supply: Each coin can be reused an unlimited number of times.
2. Optimal Substructure: The minimum coins for amount `i` depends on `1 + dp[i - coin]` for all valid coin denominations.

---

## Intuition

Build up minimum coins needed for amounts from 1 up to `amount`. For target amount `i`, test taking each coin denomination. If you take a coin of value `coin`, the remaining amount is `i - coin`. Look up the minimum coins needed for `i - coin` in your DP table, add 1 (for the coin you just took), and keep the minimum result.

---

## Algorithm

1. `dp` vector of size `amount + 1` filled with `amount + 1`. `dp[0] = 0`.
2. For `i` from `1` to `amount`:
   - For each `coin` in `coins`:
     - If `i - coin >= 0`:
       - `dp[i] = min(dp[i], 1 + dp[i - coin])`.
3. Return `dp[amount] > amount ? -1 : dp[amount]`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int coinChange(std::vector<int>& coins, int amount) {
        // dp[i] stores minimum coins needed for amount i
        // Initialize with amount + 1 (sentinel value representing infinity)
        std::vector<int> dp(amount + 1, amount + 1);
        dp[0] = 0; // Base case: 0 coins for amount 0
        
        for (int i = 1; i <= amount; ++i) {
            for (int coin : coins) {
                if (i - coin >= 0) {
                    dp[i] = std::min(dp[i], 1 + dp[i - coin]);
                }
            }
        }
        
        return dp[amount] > amount ? -1 : dp[amount];
    }
};
```

---

## Dry Run

### Input
- `coins = [1, 2, 5]`, `amount = 11`

### Execution Trace

- `dp` initialized: `dp[0] = 0`, `dp[1..11] = 12`.
- `i = 1`: `dp[1] = min(12, 1 + dp[0]) = 1`.
- `i = 2`: `dp[2] = min(12, 1+dp[1], 1+dp[0]) = 1` (using coin 2).
- `i = 5`: `dp[5] = 1` (using coin 5).
- `i = 6`: `dp[6] = 1 + dp[5] = 2`.
- `i = 10`: `dp[10] = 1 + dp[5] = 2` (5 + 5).
- `i = 11`: `dp[11] = 1 + dp[10] = 3` (5 + 5 + 1).

### Result
- Output: `3`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(\text{amount} \times \text{coins.length})$
  - Outer loop runs `amount` times, inner loop runs `coins.length` times.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(\text{amount})$
  - 1D DP table of size `amount + 1`.

---

## Why This is Optimal

- Solves minimum coin change in pseudo-polynomial $\mathcal{O}(\text{amount} \times |\text{coins}|)$ time.
- Uses optimal $\mathcal{O}(\text{amount})$ 1D DP array.

---

## Common Mistakes

1. **Integer Overflow in Infinity Sentinel**: Initializing DP array with `INT_MAX` leads to integer overflow on `1 + dp[i - coin]`. Using `amount + 1` safely avoids overflow.
2. **Missing `amount == 0` Guard**: Failing to initialize `dp[0] = 0`.
