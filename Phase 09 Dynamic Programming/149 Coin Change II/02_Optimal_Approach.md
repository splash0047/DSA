# Coin Change II

## Pattern Used

- **Pattern**: **Unbounded Knapsack 1D DP (Outer Coin Loop for Combinations)**
- **Concept**:
  - `dp[i]` represents number of unique coin combinations that sum up to amount `i`.
  - Base Case: `dp[0] = 1` (1 way to form amount 0: empty set).
  - Loop order is **CRITICAL** to count **COMBINATIONS** (unordered sets) instead of **PERMUTATIONS** (ordered sequences):
    - Outer Loop: `for (int coin : coins)`
    - Inner Loop: `for (int a = coin; a <= amount; ++a)`
      - `dp[a] += dp[a - coin]`

---

## Observation

1. **Outer Coin Loop $\implies$ Combinations**: By processing each coin denomination one by one in the outer loop, we guarantee that coins are considered in a fixed order, ensuring combinations like `[1, 2]` and `[2, 1]` are counted as 1 single unique combination!
2. **Forward Inner Loop $\implies$ Unbounded Supply**: Iterating `a` forward from `coin` up to `amount` allows the current `coin` to be reused multiple times.

---

## Intuition

Start with a table of combinations. Introduce one coin type at a time. For each coin, update how many ways every target amount can be formed using this new coin combined with previously processed coins.

---

## Algorithm

1. `dp` vector of size `amount + 1` filled with `0`. `dp[0] = 1`.
2. For each `coin` in `coins`:
   - For `a` from `coin` up to `amount`:
     - `dp[a] += dp[a - coin]`.
3. Return `dp[amount]`.

---

## Clean C++17 Solution

```cpp
#include <vector>

class Solution {
public:
    int change(int amount, std::vector<int>& coins) {
        // dp[i] stores number of combinations to make up amount i
        std::vector<uint32_t> dp(amount + 1, 0);
        dp[0] = 1; // Base case: 1 way to make amount 0
        
        // Outer loop over coins ensures unique COMBINATIONS (order doesn't matter)
        for (int coin : coins) {
            for (int a = coin; a <= amount; ++a) {
                dp[a] += dp[a - coin];
            }
        }
        
        return dp[amount];
    }
};
```

---

## Dry Run

### Input
- `amount = 5`, `coins = [1, 2, 5]`

### Execution Trace

- `dp` init: `dp[0] = 1`, `dp[1..5] = 0`.
- Coin 1:
  - `dp[1] += dp[0] = 1`
  - `dp[2] += dp[1] = 1`
  - `dp[3] += dp[2] = 1`
  - `dp[4] += dp[3] = 1`
  - `dp[5] += dp[4] = 1`
  - `dp = [1, 1, 1, 1, 1, 1]`.
- Coin 2:
  - `a = 2`: `dp[2] += dp[0] = 2` (1+1, 2)
  - `a = 3`: `dp[3] += dp[1] = 2` (1+1+1, 2+1)
  - `a = 4`: `dp[4] += dp[2] = 3` (1+1+1+1, 2+1+1, 2+2)
  - `a = 5`: `dp[5] += dp[3] = 3` (1+1+1+1+1, 2+1+1+1, 2+2+1)
- Coin 5:
  - `a = 5`: `dp[5] += dp[0] = 4` (+5)

### Result
- Output: `4`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(\text{amount} \times \text{coins.length})$
  - Outer loop runs `coins.length` times, inner loop runs `amount` times.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(\text{amount})$
  - 1D DP table of size `amount + 1`.

---

## Why This is Optimal

- Computes total coin combinations in pseudo-polynomial $\mathcal{O}(\text{amount} \times |\text{coins}|)$ time.
- Uses optimal $\mathcal{O}(\text{amount})$ 1D DP array.

---

## Common Mistakes

1. **Swapping Outer and Inner Loops**: Putting `amount` in outer loop and `coins` in inner loop computes PERMUTATIONS (like LeetCode #377 Combination Sum IV) instead of COMBINATIONS.
2. **Missing `dp[0] = 1` Base Case**: Failing to set `dp[0] = 1` causes all combination counts to remain 0.
