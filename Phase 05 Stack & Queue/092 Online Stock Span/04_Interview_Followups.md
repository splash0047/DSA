# 04 Interview Follow-ups & System Variations: Online Stock Span

The problem calculates the span of a stock's price today (maximum consecutive days price was $\le$ today's price). The optimal solution uses a **Monotonic Decreasing Stack of Pairs** `(price, span)` in $\mathcal{O}(1)$ amortized time per call and $\mathcal{O}(N)$ space.

In technical interviews, this problem tests formal amortized complexity proofs and memory-bounded streaming.

---

## 1. Mathematical Proof of $\mathcal{O}(1)$ Amortized Complexity

### 💡 The Accounting Aggregate Method
- Each price is pushed onto the stack **at most once**.
- Each price is popped from the stack **at most once** across the entire lifetime of the data stream.
- For $N$ total calls to `next(price)`:
  $$	ext{Total Pushes} \le N, \quad 	ext{Total Pops} \le N$$
  $$	ext{Total Operations} \le 2N$$
- **Amortized Time per Call**: $rac{2N}{N} = \mathcal{O}(1)$ constant time.

---

## 2. Span Compression in Stack Nodes

```cpp
class StockSpanner {
    stack<pair<int, int>> stk; // {price, span}
public:
    int next(int price) {
        int span = 1;
        while (!stk.empty() && stk.top().first <= price) {
            span += stk.top().second;
            stk.pop(); // Compress past spans
        }
        stk.push({price, span});
        return span;
    }
};
```

---

## Summary Matrix: Trade-offs at a Glance

| Operation | Amortized Time | Worst-Case Single Call | Space |
| :--- | :--- | :--- | :--- |
| `next(price)` | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
