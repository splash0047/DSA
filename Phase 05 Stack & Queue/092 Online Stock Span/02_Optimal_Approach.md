# Online Stock Span

## Pattern Used

- **Pattern**: **Monotonic Decreasing Pair Stack (Amortized O(1))**
- **Concept**: Maintain a stack `std::stack<std::pair<int, int>> st` storing `{price, span}` pairs.
  - When a new `price` arrives:
    - Initialize `span = 1`.
    - While `!st.empty()` and `st.top().first <= price`:
      - Accumulate `span += st.top().second`.
      - Pop `st.pop()`.
    - Push `{price, span}` onto `st`.
    - Return `span`.

---

## Observation

1. Monotonic Stack Collapse: Any previous price smaller than or equal to today's `price` is permanently subsumed by today's price!
2. A future price $> \text{today's price}$ will span across both today's price AND all days subsumed by today's price.
3. Therefore, collapsing smaller `{price, span}` pairs into a single combined `{price, total_span}` pair avoids redundant checks, giving amortized $\mathcal{O}(1)$ performance.

---

## Intuition

Each node on the stack remembers how many consecutive days backward it dominates. When a higher price comes, it absorbs the span counts of all smaller prices below it.

---

## Algorithm

1. Primary Stack: `std::stack<std::pair<int, int>> st` (`{price, span}`).
2. `next(price)`:
   a. `span = 1`.
   b. While `!st.empty()` and `st.top().first <= price`:
      - `span += st.top().second`.
      - `st.pop()`.
   c. `st.push({price, span})`.
   d. Return `span`.

---

## Clean C++17 Solution

```cpp
#include <stack>
#include <utility>

class StockSpanner {
private:
    std::stack<std::pair<int, int>> st; // {price, span}
public:
    StockSpanner() {}
    
    int next(int price) {
        int span = 1;
        
        while (!st.empty() && st.top().first <= price) {
            span += st.top().second;
            st.pop();
        }
        
        st.push({price, span});
        return span;
    }
};
```

---

## Dry Run

### Input Calls
`next(100)`, `next(80)`, `next(60)`, `next(70)`, `next(60)`, `next(75)`, `next(85)`

### Execution Trace

| Call | Price | Stack Action / Evictions | Stack Entry Pushed `{price, span}` | Return Value |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `100` | Stack empty | `{100, 1}` | `1` |
| 2 | `80` | `80 < 100` | `{80, 1}` | `1` |
| 3 | `60` | `60 < 80` | `{60, 1}` | `1` |
| 4 | `70` | `70 >= 60` $\implies$ Pop `{60, 1}`, `span = 1 + 1 = 2` | `{70, 2}` | **`2`** |
| 5 | `60` | `60 < 70` | `{60, 1}` | `1` |
| 6 | `75` | Pop `{60, 1}` (`span=2`), Pop `{70, 2}` (`span=4`) | `{75, 4}` | **`4`** |
| 7 | `85` | Pop `{75, 4}` (`span=5`), Pop `{80, 1}` (`span=6`) | `{85, 6}` | **`6`** |

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(1)$ amortized per `next()` call.
  - Every price is pushed into `st` once and popped from `st` at most once across all $N$ calls. Total operations over $N$ queries $= \mathcal{O}(N) \implies \mathcal{O}(1)$ amortized.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Stack stores at most $N$ price-span pairs.

---

## Why This is Optimal

- Solves online stock span query in amortized $\mathcal{O}(1)$ time.
- Uses minimal stack space.

---

## Common Mistakes

1. **Strictly Greater vs Greater or Equal**: Using `<` instead of `<=`. The problem specifies prices **less than or equal to** today's price, so equal prices MUST be absorbed into today's span!
2. **Forgetting to Accumulate Spans**: Adding `1` instead of `st.top().second` when popping smaller prices.
