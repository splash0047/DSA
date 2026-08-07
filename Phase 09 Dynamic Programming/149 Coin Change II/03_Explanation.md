# Problem Summary

Find the number of combinations to make up `amount` using unlimited coins of given denominations. The optimal approach uses **Unbounded Knapsack 1D DP (Outer Coin Loop)**:
- Maintain `dp[amount + 1]` initialized to `0` with `dp[0] = 1`.
- Outer loop `coin` in `coins` (guarantees unordered combinations):
  - Inner loop `a` from `coin` to `amount`:
    - `dp[a] += dp[a - coin];`
- Return `dp[amount]`.
This counts total coin combinations in $\mathcal{O}(\text{amount} \times |\text{coins}|)$ time and $\mathcal{O}(\text{amount})$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need the **number of combinations (unordered sets) to make a target sum with unlimited items**.
- Unbounded Knapsack Combination Counting DP pattern.

---

## Important Clues

1. **"Number of combinations that make up amount"**: Unordered combination counting.
2. **"Infinite number of each kind of coin"**: Forward inner loop Unbounded Knapsack.

---

## Example

### Input
`amount = 5`, `coins = [1, 2, 5]`

### Visual Step-by-Step Progression

```text
Target: 5

dp init: [1, 0, 0, 0, 0, 0]
After coin 1: [1, 1, 1, 1, 1, 1]
After coin 2: [1, 1, 2, 2, 3, 3]
After coin 5: [1, 1, 2, 2, 3, 4]

Result: 4
```

---

## Alternative Solutions

### Top-Down Memoization Recursion ($\mathcal{O}(A \cdot |C|)$ Time, $\mathcal{O}(A \cdot |C|)$ Space)
- Recurse with `memo[idx][amount]` table storing combination counts.

---

## Edge Cases

1. **`amount = 0`**: Returns `1` (empty set).
2. **Impossible target**: `coins = [2]`, `amount = 3` $\implies$ returns `0`.
3. **Single coin matches amount**: `coins = [10]`, `amount = 10` $\implies$ returns `1`.

---

## Interview Tips

- **Explain Combinations vs Permutations Loop Order**: State *"Placing the `coin` loop on the OUTSIDE forces coins to be processed in a fixed order, ensuring combinations like `1+2` and `2+1` are counted as a single unique combination. If `amount` were on the outside, it would count ordered permutations."*

---

## Similar Problems

1. [LeetCode #322: Coin Change](https://leetcode.com/problems/coin-change/)
2. [LeetCode #377: Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)
3. [LeetCode #494: Target Sum](https://leetcode.com/problems/target-sum/)

---

## Revision Notes

- Problem: Count coin combinations to form `amount`.
- Pattern: Unbounded Knapsack 1D DP.
- Crucial loop order: Outer `coin`, Inner `amount`.
- Loop: `for (coin) for (a = coin..amount) dp[a] += dp[a - coin];`
- Base Case: `dp[0] = 1;`
- Optimal Complexity: Time $\mathcal{O}(A \cdot |C|)$, Space $\mathcal{O}(A)$.
