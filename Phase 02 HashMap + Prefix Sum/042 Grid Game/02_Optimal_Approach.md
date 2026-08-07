# Grid Game

## Pattern Used

- **Pattern**: **Prefix Sum / Suffix Sum Minimax Reduction**
- **Concept**: If Robot 1 transitions from Row 0 to Row 1 at column `i`, it zeroes out:
  - Row 0 from index `0` to `i`.
  - Row 1 from index `i` to `n - 1`.

---

## Observation

1. Once Robot 1 makes its path at column `i`, only two non-zero regions remain for Robot 2:
   - **Top Remaining**: `grid[0][i+1 ... n-1]` (remaining elements in Row 0).
   - **Bottom Remaining**: `grid[1][0 ... i-1]` (remaining elements in Row 1).
2. Robot 2 wants to **maximize** its score, so Robot 2 will choose:
   $$\text{Robot 2 Points} = \max(\text{Top Remaining}, \text{Bottom Remaining})$$
3. Robot 1 wants to **minimize** this value over all possible choice columns $i \in [0, n-1]$:
   $$\text{Answer} = \min_{0 \le i < n} \Big( \max(\text{top\_sum}[i+1 \dots n-1], \text{bottom\_sum}[0 \dots i-1]) \Big)$$
4. By initializing `top_sum` to sum of Row 0 and `bottom_sum` to 0, we can update both sums in $\mathcal{O}(1)$ time as $i$ increments from $0$ to $n-1$.

---

## Intuition

- `top_sum` starts as the total sum of Row 0.
- `bottom_sum` starts at 0.
- As column `i` advances from `0` to `n - 1`:
  - Subtract `grid[0][i]` from `top_sum`.
  - Robot 2's maximum points for this split: `r2_score = max(top_sum, bottom_sum)`.
  - Update `result = min(result, r2_score)`.
  - Add `grid[1][i]` to `bottom_sum`.

---

## Algorithm

1. `long long top_sum = std::accumulate(grid[0].begin(), grid[0].end(), 0LL)`.
2. `long long bottom_sum = 0`.
3. `long long result = 1e18`.
4. Loop `i` from `0` to `n - 1`:
   a. `top_sum -= grid[0][i]`.
   b. `long long r2 = std::max(top_sum, bottom_sum)`.
   c. `result = std::min(result, r2)`.
   d. `bottom_sum += grid[1][i]`.
5. Return `result`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <numeric>
#include <algorithm>

class Solution {
public:
    long long gridGame(const std::vector<std::vector<int>>& grid) {
        int n = grid[0].size();
        
        long long top_sum = 0;
        for (int c = 0; c < n; ++c) {
            top_sum += grid[0][c];
        }
        
        long long bottom_sum = 0;
        long long result = 1e18;
        
        for (int i = 0; i < n; ++i) {
            // Robot 1 takes cell grid[0][i], so it is no longer available to Robot 2
            top_sum -= grid[0][i];
            
            // Robot 2 gets the max of what's left on top or bottom
            long long r2_points = std::max(top_sum, bottom_sum);
            result = std::min(result, r2_points);
            
            // Robot 1 takes cell grid[1][i], adding it to bottom_sum for next iterations
            bottom_sum += grid[1][i];
        }
        
        return result;
    }
};
```

---

## Dry Run

### Input
- `grid = [[2, 5, 4], [1, 5, 1]]`

### Execution Trace

- Initial `top_sum = 2 + 5 + 4 = 11`, `bottom_sum = 0`, `result = INF`.

| `i` | `grid[0][i]` | `top_sum` (after subtract) | `bottom_sum` (before add) | `r2_points = max(top, bot)` | `result` (min) | `bottom_sum` (after add) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | `2` | `11 - 2 = 9` | `0` | `max(9, 0) = 9` | `9` | `0 + 1 = 1` |
| 1 | `5` | `9 - 5 = 4` | `1` | `max(4, 1) = 4` | **`4`** | `1 + 5 = 6` |
| 2 | `4` | `4 - 4 = 0` | `6` | `max(0, 6) = 6` | `4` | `6 + 1 = 7` |

### Result
- Output: `4`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass through $N$ columns.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses a few `long long` variables.

---

## Why This is Optimal

- Robot 1 must consider all $N$ potential drop-down columns ($\Omega(N)$ time lower bound).
- Calculates Minimax score in single pass using constant $\mathcal{O}(1)$ space.

---

## Common Mistakes

1. **Integer Overflow**: Using standard 32-bit `int` instead of `long long`. For $N = 50,000$ and grid values up to $10^5$, sum can reach $5 \times 10^9$, exceeding 32-bit int.
2. **Confusing Robot 1 and Robot 2 Objectives**: Robot 1 wants to **minimize** Robot 2's maximum score, while Robot 2 wants to **maximize** its score.
