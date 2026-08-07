# Problem Summary

Find the minimum number of coins needed to make up `amount` using unlimited coins of given denominations. Return `-1` if impossible. The optimal approach uses **Bottom-Up 1D Unbounded Knapsack DP**:
- `dp[i]` stores minimum coins to form amount `i`.
- Initialize `dp(amount + 1, amount + 1)` with base case `dp[0] = 0`.
- Outer loop `i` from `1` to `amount`, inner loop `coin` in `coins`:
  - `if (i - coin >= 0) dp[i] = min(dp[i], 1 + dp[i - coin]);`
- Return `dp[amount] > amount ? -1 : dp[amount]`.
This finds minimum coins in $\mathcal{O}(\text{amount} \times |\text{coins}|)$ time and $\mathcal{O}(\text{amount})$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need the **minimum items / cost to achieve a target sum with unlimited reusable choices**.
- Unbounded Knapsack DP pattern.

---

## Important Clues

1. **"Fewest number of coins"**: Minimum cost optimization.
2. **"Infinite number of each kind of coin"**: Unbounded items.

---

## Example

### Input
`coins = [1, 2, 5]`, `amount = 11`

### Visual Step-by-Step Progression

```text
Target: 11

dp[0] = 0
dp[1] = 1  (1)
dp[2] = 1  (2)
dp[5] = 1  (5)
dp[6] = 2  (5 + 1)
dp[10] = 2 (5 + 5)
dp[11] = 3 (5 + 5 + 1)

Result: 3
```

---

## Alternative Solutions

### BFS Shortest Path ($\mathcal{O}(\text{amount} \times |\text{coins}|)$ Time, $\mathcal{O}(\text{amount})$ Space)
- Level-by-level BFS queue tracking `(current_amount, step_count)`.

---

## Edge Cases

1. **`amount = 0`**: Returns `0`.
2. **Impossible target**: `coins = [2]`, `amount = 3` $\implies$ returns `-1`.
3. **Coin larger than amount**: Skipped safely by `i - coin >= 0`.

---

## Interview Tips

- **Explain Infinity Sentinel Choice**: State *"Initializing `dp` with `amount + 1` acts as a safe infinity sentinel because even if we used all 1-value coins, the maximum coins needed could never exceed `amount`. This prevents integer overflow when adding `1 + dp[i - coin]`."*

---

## Similar Problems

1. [LeetCode #518: Coin Change II](https://leetcode.com/problems/coin-change-ii/)
2. [LeetCode #279: Perfect Squares](https://leetcode.com/problems/perfect-squares/)
3. [LeetCode #377: Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)

---

## Revision Notes

- Problem: Fewest coins to form target `amount`.
- Pattern: Unbounded Knapsack 1D DP.
- Table: `vector<int> dp(amount + 1, amount + 1); dp[0] = 0;`
- Loop: `for (i = 1..amount) for (coin) if (i - coin >= 0) dp[i] = min(dp[i], 1 + dp[i - coin]);`
- Result: `return dp[amount] > amount ? -1 : dp[amount];`
- Optimal Complexity: Time $\mathcal{O}(A \cdot |C|)$, Space $\mathcal{O}(A)$.
