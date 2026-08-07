# Problem Summary

Find the maximum profit from buying and selling stock with a mandatory 1-day cooldown after selling. The optimal approach uses **3-State Machine DP**:
- States: `hold` (holding stock), `sold` (just sold today), `rest` (resting/in cooldown).
- Initialize `hold = INT_MIN`, `sold = 0`, `rest = 0`.
- For `price` in `prices`:
  - `hold = max(prev_hold, rest - price);` (buy from rest state)
  - `sold = prev_hold + price;` (sell held stock)
  - `rest = max(prev_rest, prev_sold);` (cooldown from sold state)
- Return `max(sold, rest)`.
This calculates max profit in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need **maximum profit in stock trading with transaction cooldown / fee constraints**.
- State Machine Finite Automaton DP pattern.

---

## Important Clues

1. **"Mandatory 1-day cooldown after selling"**: Buying requires coming from `rest` state instead of `sold` state.
2. **"Multiple transactions allowed"**: Iterative state transitions.

---

## Example

### Input
`prices = [1, 2, 3, 0, 2]`

### Visual Step-by-Step Progression

```text
Prices: [1, 2, 3, 0, 2]

State Transitions:
- Day 1 (1): Buy @ 1 -> hold = -1, sold = 0, rest = 0
- Day 2 (2): Sell @ 2 -> hold = -1, sold = 1, rest = 0
- Day 3 (3): Rest -> hold = -1, sold = 2, rest = 1
- Day 4 (0): Buy @ 0 -> hold = 1, sold = -1, rest = 2
- Day 5 (2): Sell @ 2 -> hold = 1, sold = 3, rest = 2

Result: 3
```

---

## Alternative Solutions

### 2D State Table DP ($\mathcal{O}(N)$ Time, $\mathcal{O}(N)$ Space)
- Maintain `dp[N][2]` table storing max profit at day `i` with holding flag `0` or `1`.

---

## Edge Cases

1. **Monotonically decreasing prices**: `prices = [5, 4, 3, 2, 1]` $\implies$ returns `0`.
2. **Single day price**: `prices = [1]` $\implies$ returns `0`.
3. **Two days**: `prices = [1, 5]` $\implies$ returns `4`.

---

## Interview Tips

- **Explain Why Cooldown Is Enforced**: State *"By requiring `hold = max(hold, rest - price)` to buy only from the `rest` state, we guarantee that a stock cannot be bought on the day immediately following a `sold` state, cleanly enforcing the 1-day cooldown requirement."*

---

## Similar Problems

1. [LeetCode #122: Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
2. [LeetCode #714: Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)
3. [LeetCode #123: Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

---

## Revision Notes

- Problem: Stock trading max profit with 1-day cooldown after selling.
- Pattern: 3-State Machine DP (`hold`, `sold`, `rest`).
- Transitions:
  - `hold = max(hold, rest - price);`
  - `sold = prev_hold + price;`
  - `rest = max(rest, prev_sold);`
- Result: `return max(sold, rest);`
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
