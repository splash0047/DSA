# Best Time to Buy and Sell Stock

## Pattern Used

- **Pattern**: **Single Pass Prefix Tracking / Greedy**
- **Concept**: Maintaining a running minimum purchase price `min_price` while iterating through the array to calculate the maximum profit achievable on each day.

---

## Observation

To maximize profit $\text{prices}[j] - \text{prices}[i]$ where $j > i$:
- For a fixed sell day $j$, the optimal buy day $i$ is the day in the range $[0 \dots j-1]$ that had the **lowest price**.
- Therefore, as we traverse the array from left to right, we only need to maintain a single variable `min_price` tracking the lowest stock price seen prior to the current day.

---

## Intuition

Imagine walking through the stock prices day by day:
1. On each day, you check: *"If I sell today, how much profit would I make relative to the lowest price I've seen so far?"*
2. If today's price is lower than any price seen before, update your record of the lowest price (`min_price`).
3. Otherwise, check if selling today yields a higher profit than your previous best (`max_profit`).

This reduces the problem to a single pass $\mathcal{O}(N)$ scan.

---

## Algorithm

1. Initialize `min_price = INT_MAX` and `max_profit = 0`.
2. Iterate through each `price` in `prices`:
   a. If `price < min_price`: update `min_price = price`.
   b. Else if `price - min_price > max_profit`: update `max_profit = price - min_price`.
3. Return `max_profit`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>
#include <climits>

class Solution {
public:
    int maxProfit(const std::vector<int>& prices) {
        int min_price = INT_MAX;
        int max_profit = 0;
        
        for (int price : prices) {
            if (price < min_price) {
                min_price = price;
            } else if (price - min_price > max_profit) {
                max_profit = price - min_price;
            }
        }
        
        return max_profit;
    }
};
```

---

## Dry Run

### Input
- `prices = [7, 1, 5, 3, 6, 4]`

### Execution Trace

| Step | Day | `price` | `min_price` | `price - min_price` | `max_profit` | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 0 | `7` | `7` | `0` | `0` | Set `min_price = 7` |
| 2 | 1 | `1` | `1` | `0` | `0` | Set `min_price = 1` |
| 3 | 2 | `5` | `1` | `4` | `4` | Update `max_profit = 4` |
| 4 | 3 | `3` | `1` | `2` | `4` | No update (`2 < 4`) |
| 5 | 4 | `6` | `1` | `5` | `5` | Update `max_profit = 5` |
| 6 | 5 | `4` | `1` | `3` | `5` | No update (`3 < 5`) |

### Result
- Output: `5`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - We traverse the `prices` array of size $N$ exactly once.
  - Each element comparison takes $\mathcal{O}(1)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Only two primitive integer variables (`min_price`, `max_profit`) are used.

---

## Why This is Optimal

- We must inspect every element in `prices` at least once to ensure we don't miss a price spike or dip. Thus, $\Omega(N)$ is a strict lower bound on time complexity.
- Our single-pass solution achieves $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ auxiliary space, which is theoretically optimal.

---

## Common Mistakes

1. **Selling Before Buying**: Allowing `prices[j] - prices[i]` when $j < i$. (Prevented by updating `min_price` sequentially during left-to-right traversal).
2. **Initializing `min_price` to `0`**: If `min_price = 0`, valid prices will never be smaller than `min_price`. Initialize to `INT_MAX` or `prices[0]`.
3. **Allowing Negative Profit**: Returning a negative profit when prices strictly decrease. (Constraint requires returning `0`).
