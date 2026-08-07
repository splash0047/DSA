# Problem Summary

Design a class `StockSpanner` that calculates the **span** of a stock price on each day (the maximum number of consecutive days backward with prices $\le \text{today's price}$). The optimal approach uses a **Monotonic Decreasing Pair Stack** `std::stack<pair<int, int>>` storing `{price, span}`:
- When a new `price` arrives, set `span = 1`.
- While `st.top().first <= price`, pop `st.top()` and accumulate `span += st.top().second`.
- Push `{price, span}` and return `span`.
This evaluates each stock span query in amortized $\mathcal{O}(1)$ time and $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to track **consecutive smaller / equal elements backward in an online stream**.
- Monotonic Decreasing Pair Stack Span Compression pattern.

---

## Important Clues

1. **"Maximum consecutive days going backward with price <= today's price"**: Monotonic Stack Span.
2. **"Online stream query algorithm"**: Incremental stack compression.

---

## Example

### Input Calls
`next(100)`, `next(80)`, `next(60)`, `next(70)`, `next(60)`, `next(75)`, `next(85)`

### Visual Step-by-Step Progression

```text
Processing price 75:
Stack before: [{100, 1}, {80, 1}, {70, 2}, {60, 1}]

- 75 >= 60 -> Pop {60, 1} (span = 1+1 = 2)
- 75 >= 70 -> Pop {70, 2} (span = 2+2 = 4)
- 75 < 80  -> Stop!

Push {75, 4} -> Return 4
```

---

## Alternative Solutions

### Vector Backward Linear Search (Brute Force)
- Store all prices in `vector<int> prices`. Scan backward on each `next()` call.
- **Time Complexity**: $\mathcal{O}(N)$ per query ($\mathcal{O}(N^2)$ overall).
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **Monotonically Increasing Prices**: `10, 20, 30, 40` -> Spans return `1, 2, 3, 4`.
2. **Monotonically Decreasing Prices**: `40, 30, 20, 10` -> Spans return `1, 1, 1, 1`.
3. **Identical Prices**: `50, 50, 50` -> Spans return `1, 2, 3`.

---

## Interview Tips

- **Explain Amortized Complexity Rationale**: State *"Although a single call to `next()` may pop multiple items from the stack in $\mathcal{O}(K)$ time, each price item is pushed ONCE and popped AT MOST ONCE over all $N$ operations. Thus, the total cost across $N$ queries is $\mathcal{O}(N)$, giving an average amortized time of $\mathcal{O}(1)$ per query."*

---

## Similar Problems

1. [LeetCode #739: Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
2. [LeetCode #496: Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)
3. [LeetCode #84: Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

---

## Revision Notes

- Problem: Online stock span (consecutive days backward with price $\le$ today).
- Pattern: Monotonic Decreasing Stack (`stack<pair<int, int>> st` of `{price, span}`).
- `next(price)`:
  - `span = 1;`
  - `while (!st.empty() && st.top().first <= price)`:
    - `span += st.top().second; st.pop();`
  - `st.push({price, span});`
  - `return span;`
- Optimal Complexity: Amortized Time $\mathcal{O}(1)$, Space $\mathcal{O}(N)$.
