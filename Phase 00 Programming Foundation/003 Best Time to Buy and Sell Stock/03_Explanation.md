# Problem Summary

Given an array `prices` representing stock prices on consecutive days, find the maximum profit obtainable by making at most one transaction (buying one stock and selling it on a later day). If no profit can be made (e.g., prices decrease continuously), return `0`. The optimal solution tracks the minimum price seen so far in a single left-to-right pass.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the **maximum difference** $A[j] - A[i]$ subject to the constraint $j > i$.
- The sequence is dynamic over time, requiring prefix state tracking.
- The problem allows at most one transaction or single decision point.

---

## Important Clues

1. **"Single transaction"**: You buy once and sell once.
2. **"Different day in the future"**: Buying day index $i$ must be strictly less than selling day index $j$ ($i < j$).
3. **"Return 0 if no profit"**: Negative profits are not allowed; default answer is 0.

---

## Example

### Input
`prices = [7, 1, 5, 3, 6, 4]`

### Visual Step-by-Step Progression

```text
Prices:     [ 7 ,  1 ,  5 ,  3 ,  6 ,  4 ]
min_price:    7    1    1    1    1    1
profit:       0    0    4    2    5    3
                       ^         ^
                      (5-1)     (6-1) -> Max Profit = 5
```

---

## Alternative Solutions

### Kadane's Algorithm on Daily Differences
Transform the problem into the Maximum Subarray Sum problem:
1. Create a difference array `diff` where `diff[i] = prices[i] - prices[i-1]`.
2. Finding max profit across buy/sell days is equivalent to finding the maximum contiguous subarray sum of `diff`.
3. Apply Kadane's Algorithm in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Edge Cases

1. **Strictly Decreasing Prices**: `prices = [7, 6, 4, 3, 1]` -> Returns `0`.
2. **Strictly Increasing Prices**: `prices = [1, 2, 3, 4, 5]` -> Returns `5 - 1 = 4`.
3. **Flat Prices**: `prices = [5, 5, 5, 5]` -> Returns `0`.
4. **Single Day**: `prices = [5]` -> Returns `0`.
5. **Large Price Spikes**: `prices = [1, 10000]` -> Returns `9999`.

---

## Interview Tips

- **Mention Kadane's Connection**: Point out that this problem is isomorphic to Maximum Subarray Sum on adjacent price differences.
- **Clarify Transaction Rules**: Confirm whether multiple transactions or short-selling are allowed (this version allows at most one buy-sell pair).

---

## Similar Problems

1. [LeetCode #122: Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
2. [LeetCode #123: Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)
3. [LeetCode #188: Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)
4. [LeetCode #309: Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
5. [LeetCode #53: Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

---

## Revision Notes

- Problem: Maximize `prices[j] - prices[i]` for $j > i$.
- Single pass algorithm maintaining `min_price` and `max_profit`.
- Initialize `min_price = INT_MAX`, `max_profit = 0`.
- For each `price`: update `min_price = min(min_price, price)`, `max_profit = max(max_profit, price - min_price)`.
- Time Complexity: $\mathcal{O}(N)$.
- Space Complexity: $\mathcal{O}(1)$.
- Isomorphic to Kadane's Algorithm on daily price differences.
