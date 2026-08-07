# Problem Summary

Find the number of ways to assign `+` and `-` symbols to elements in `nums` so that the expression evaluates to `target`. The optimal approach uses **Mathematical Reduction to 0/1 Knapsack Subset Sum**:
- Equation: $\text{sum}(P) - \text{sum}(N) = \text{target} \implies \text{sum}(P) = \frac{\text{target} + \text{totalSum}}{2}$.
- If `abs(target) > totalSum` or `(target + totalSum) % 2 != 0`, return `0`.
- Problem reduces to counting subsets summing to `subsetTarget = (target + totalSum) / 2`.
- `dp` array initialized to `0` with `dp[0] = 1`.
- For `num` in `nums`, for `t` from `subsetTarget` down to `num`:
  - `dp[t] += dp[t - num];`
- Return `dp[subsetTarget]`.
This counts target sum expressions in $\mathcal{O}(N \times \text{subsetTarget})$ time and $\mathcal{O}(\text{subsetTarget})$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **assign + / - signs to numbers to reach a target sum**.
- Mathematical Reduction to 0/1 Knapsack Subset Sum pattern.

---

## Important Clues

1. **"Assign '+' and '-' before each integer"**: Mathematical subset difference.
2. **"Evaluate to target"**: Subset sum target $\frac{\text{target} + \text{totalSum}}{2}$.

---

## Example

### Input
`nums = [1, 1, 1, 1, 1]`, `target = 3`

### Visual Step-by-Step Progression

```text
TotalSum = 5, Target = 3
SubsetTarget = (3 + 5) / 2 = 4

Count subsets summing to 4:
- [1, 1, 1, 1] (exclude 1st element)
- [1, 1, 1, 1] (exclude 2nd element)
- [1, 1, 1, 1] (exclude 3rd element)
- [1, 1, 1, 1] (exclude 4th element)
- [1, 1, 1, 1] (exclude 5th element)

Total ways = 5
```

---

## Alternative Solutions

### Top-Down Memoization Recursion ($\mathcal{O}(N \times \text{totalSum})$ Time, $\mathcal{O}(N \times \text{totalSum})$ Space)
- Recurse `dfs(i, currentSum)` using 2D memo hash map or offset array `memo[20][2001]`.

---

## Edge Cases

1. **`target` larger than `totalSum`**: Returns `0`.
2. **`target + totalSum` is odd**: Returns `0`.
3. **Zeros in input array**: Handled correctly (`dp[t] += dp[t - 0]` doubles valid subset counts).

---

## Interview Tips

- **Explain Mathematical Reduction**: State *"Let $P$ be the subset of numbers assigned positive signs and $N$ be the subset assigned negative signs. Since $P - N = \text{target}$ and $P + N = \text{totalSum}$, adding both equations gives $2P = \text{target} + \text{totalSum}$, so $P = \frac{\text{target} + \text{totalSum}}{2}$. This transforms symbol assignment into standard 0/1 Knapsack Subset Sum."*

---

## Similar Problems

1. [LeetCode #416: Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
2. [LeetCode #1049: Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/)
3. [LeetCode #518: Coin Change II](https://leetcode.com/problems/coin-change-ii/)

---

## Revision Notes

- Problem: Ways to assign +/- to numbers to sum to target.
- Pattern: Subset Sum reduction.
- Key Formula: `subsetTarget = (target + totalSum) / 2`.
- Guard: `if (abs(target) > totalSum || (target + totalSum) % 2 != 0) return 0;`
- Loop: `for (num) for (t = subsetTarget..num) dp[t] += dp[t - num];`
- Optimal Complexity: Time $\mathcal{O}(N \cdot T)$, Space $\mathcal{O}(T)$.
