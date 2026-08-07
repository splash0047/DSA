# Grid Game

- **Problem Number**: 2017
- **Platform**: LeetCode #2017
- **Difficulty**: Medium
- **Pattern**: Minimax Simulation

---

## Brute Force Intuition

Robot 1 moves from `(0, 0)` to `(1, n-1)`. Since the grid has only 2 rows, Robot 1 can only transition from Row 0 to Row 1 at some column `i` (where $0 \le i < n$).

For every possible transition column `i` chosen by Robot 1:
1. Zero out Robot 1's path: `(0, 0...i)` and `(1, i...n-1)`.
2. Compute the maximum points Robot 2 can collect by trying all possible transition columns $j$ for Robot 2.
3. Robot 1 chooses $i$ to minimize Robot 2's maximum points.

---

## Algorithm

1. `min_second_robot_points = INF`.
2. Loop Robot 1 drop column `i` from `0` to `n - 1`:
   a. Create grid copy. Zero out Robot 1 path.
   b. `max_r2 = 0`.
   c. Loop Robot 2 drop column `j` from `0` to `n - 1`:
      - Compute sum of points collected by Robot 2 along path $j$.
      - `max_r2 = max(max_r2, r2_sum)`.
   d. `min_second_robot_points = min(min_second_robot_points, max_r2)`.
3. Return `min_second_robot_points`.

---

## Code

```cpp
#include <vector>
#include <numeric>
#include <algorithm>

class Solution {
public:
    long long gridGame(const std::vector<std::vector<int>>& grid) {
        int n = grid[0].size();
        long long min_second_robot = 1e18;
        
        for (int i = 0; i < n; ++i) { // Robot 1 drops down at column i
            // Robot 2 only has 2 viable path choices:
            // 1. Remain on Row 0 (collects grid[0][i+1 ... n-1])
            // 2. Drop to Row 1 immediately at col 0 (collects grid[1][0 ... i-1])
            long long top_rem = 0;
            for (int col = i + 1; col < n; ++col) top_rem += grid[0][col];
            
            long long bot_rem = 0;
            for (int col = 0; col < i; ++col) bot_rem += grid[1][col];
            
            long long r2_max = std::max(top_rem, bot_rem);
            min_second_robot = std::min(min_second_robot, r2_max);
        }
        
        return min_second_robot;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - For each column $i$, calculating remaining sums takes $\mathcal{O}(N)$ time.
  - For $N = 5 \times 10^4$, $N^2 = 2.5 \times 10^9$ operations, causing TLE.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary memory.

---

## Why This Approach Is Not Optimal

Re-computing top and bottom remaining sums for each column $i$ takes quadratic time. Using **Prefix Sums**, top and bottom remaining sums can be updated in $\mathcal{O}(1)$ time per step, achieving optimal $\mathcal{O}(N)$ linear time.
