# Online Stock Span

- **Problem Number**: 901
- **Platform**: LeetCode #901
- **Difficulty**: Medium
- **Pattern**: Vector History Backward Scan

---

## Brute Force Intuition

Store all incoming stock prices in a `std::vector<int> prices`. On each `next(price)` call, append `price` to `prices`, then scan backward from the end of `prices` as long as `prices[i] <= price` to count the span length.

---

## Algorithm

1. `prices.push_back(price)`.
2. `span = 0`.
3. Loop `i` from `prices.size() - 1` down to `0`:
   - If `prices[i] <= price`: `span++`.
   - Else: break loop.
4. Return `span`.

---

## Code

```cpp
#include <vector>

class StockSpanner {
private:
    std::vector<int> prices;
public:
    StockSpanner() {}
    
    int next(int price) {
        prices.push_back(price);
        int span = 0;
        
        for (int i = prices.size() - 1; i >= 0; --i) {
            if (prices[i] <= price) {
                span++;
            } else {
                break;
            }
        }
        
        return span;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$ per `next()` call.
  - Scanning backward over $N$ historical prices takes $\mathcal{O}(N)$ worst-case time.
  - Total time for $N$ calls = $\mathcal{O}(N^2)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Stores all $N$ historical prices in vector memory.

---

## Why This Approach Is Not Optimal

Backward linear scan takes $\mathcal{O}(N)$ time per query ($\mathcal{O}(N^2)$ overall). Using a **Monotonic Decreasing Pair Stack**, we can compute stock span in amortized $\mathcal{O}(1)$ time per query.
