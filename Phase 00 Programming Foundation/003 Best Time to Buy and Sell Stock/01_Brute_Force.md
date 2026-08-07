# Best Time to Buy and Sell Stock

- **Problem Number**: 121
- **Platform**: LeetCode #121
- **Difficulty**: Easy
- **Pattern**: Brute Force Pair Comparison / Nested Loops

---

## Brute Force Intuition

To maximize profit from buying on day `i` and selling on day `j` (where `j > i`), the most straightforward brute-force approach is to evaluate every possible combination of buy day and sell day.

We compare `prices[j] - prices[i]` for all valid pairs $(i, j)$ such that $i < j$. By keeping track of the maximum profit found across all valid pairs, we guarantee finding the optimal transaction.

---

## Algorithm

1. Initialize `max_profit = 0`.
2. Outer loop `i` iterates from `0` to `n - 2` (buying day).
3. Inner loop `j` iterates from `i + 1` to `n - 1` (selling day).
4. Calculate profit: `current_profit = prices[j] - prices[i]`.
5. Update `max_profit = max(max_profit, current_profit)`.
6. Return `max_profit`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int maxProfit(const std::vector<int>& prices) {
        int max_profit = 0;
        int n = prices.size();
        
        for (int i = 0; i < n - 1; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int profit = prices[j] - prices[i];
                if (profit > max_profit) {
                    max_profit = profit;
                }
            }
        }
        
        return max_profit;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - Total pair comparisons evaluated: $\frac{N(N-1)}{2} = \mathcal{O}(N^2)$.
  - For $N = 10^5$, $N^2 = 10^{10}$ operations, causing a **Time Limit Exceeded (TLE)** on LeetCode.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Operates directly on the input vector using constant auxiliary space.

---

## Why This Approach Is Not Optimal

The brute force approach repeatedly scans future days for every buy day. However, if we process the array sequentially, we only need to keep track of the **minimum purchase price seen so far**. For any sell day `prices[j]`, the maximum potential profit is simply `prices[j] - min_price_so_far`. This eliminates the inner loop entirely.
