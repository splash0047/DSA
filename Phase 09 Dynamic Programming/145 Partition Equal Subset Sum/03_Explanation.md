# Problem Summary

Determine if array `nums` can be partitioned into two subsets of equal sum. The optimal approach uses **0/1 Knapsack Subset Sum 1D DP**:
- If `totalSum % 2 != 0`, return `false`. Set `target = totalSum / 2`.
- `dp[target + 1]` boolean array with `dp[0] = true`.
- Loop `num` in `nums`:
  - Loop `t` from `target` down to `num` (reverse order prevents element reuse):
    - `dp[t] = dp[t] || dp[t - num];`
- Return `dp[target]`.
This checks subset sum equality in $\mathcal{O}(N \times \text{target})$ time and $\mathcal{O}(\text{target})$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **partition elements into two equal sum subsets / target subset sum**.
- 0/1 Knapsack Subset Sum DP pattern.

---

## Important Clues

1. **"Partition array into two subsets of equal sum"**: Subset sum equals $\frac{\text{totalSum}}{2}$.
2. **"Each element used at most once per subset"**: Reverse inner loop 0/1 Knapsack.

---

## Example

### Input
`nums = [1, 5, 11, 5]`

### Visual Step-by-Step Progression

```text
TotalSum = 22 -> Target = 11

dp init: dp[0]=T, others F

- Process 1: dp[1]=T
- Process 5: dp[6]=T, dp[5]=T
- Process 11: dp[11]=T (since dp[0]=T)

dp[11] is True! -> Result: true
```

---

## Alternative Solutions

### `std::bitset` Optimization ($\mathcal{O}(N \times \frac{\text{target}}{64})$ Time, $\mathcal{O}(\text{target})$ Space)
- Use `std::bitset<10001> bits(1); for (int num : nums) bits |= (bits << num); return bits[target];`

---

## Edge Cases

1. **Odd Total Sum**: `nums = [1, 2, 4]` $\implies$ `sum = 7` $\implies$ returns `false`.
2. **Single Element**: `nums = [1]` $\implies$ returns `false`.
3. **Element greater than Target**: Handled naturally by loop condition `t >= num`.

---

## Interview Tips

- **Explain Reverse Inner Loop Rule**: State *"In 1D 0/1 Knapsack DP, iterating the target sum loop backwards from `target` down to `num` ensures that `dp[t - num]` represents the state from the PREVIOUS item, preventing the current item from being reused multiple times."*

---

## Similar Problems

1. [LeetCode #494: Target Sum](https://leetcode.com/problems/target-sum/)
2. [LeetCode #698: Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)
3. [LeetCode #1049: Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/)

---

## Revision Notes

- Problem: Partition array into 2 equal-sum subsets.
- Pattern: 0/1 Knapsack 1D DP.
- Guard: `if (totalSum % 2 != 0) return false; target = totalSum / 2;`
- Loop: `for (num) for (t = target..num) dp[t] = dp[t] || dp[t - num];`
- Crucial detail: Reverse inner loop `t` down to `num`.
- Optimal Complexity: Time $\mathcal{O}(N \cdot T)$, Space $\mathcal{O}(T)$.
