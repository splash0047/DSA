# Target Sum

## Pattern Used

- **Pattern**: **Mathematical Reduction to 0/1 Knapsack Subset Sum Count**
- **Concept**:
  - Partition `nums` into two subsets: $P$ (elements assigned `+`) and $N$ (elements assigned `-`).
  - Equations:
    1. $\text{sum}(P) - \text{sum}(N) = \text{target}$
    2. $\text{sum}(P) + \text{sum}(N) = \text{totalSum}$
  - Add equation (1) and (2):
    $$2 \cdot \text{sum}(P) = \text{target} + \text{totalSum}$$
    $$\text{sum}(P) = \frac{\text{target} + \text{totalSum}}{2}$$
  - Therefore, the problem reduces to: **Count the number of subsets of `nums` that sum up to `subsetTarget = (target + totalSum) / 2`**!
  - Validity Guards:
    - If `(target + totalSum)` is odd OR `abs(target) > totalSum`, return `0`.

---

## Observation

1. Instead of dealing with negative sums during recursion, mathematical reduction transforms Target Sum directly into standard 0/1 Knapsack Subset Sum Counting.
2. Maintain `dp[t]` array of size `subsetTarget + 1` initialized to `0` with `dp[0] = 1`.
3. For each `num` in `nums`: iterate `t` backward from `subsetTarget` down to `num`, updating `dp[t] += dp[t - num]`.

---

## Intuition

Assigning `+` or `-` to numbers is mathematically equivalent to splitting numbers into two groups such that their difference is `target`. Solving for the sum of the positive group turns the problem into finding how many subsets sum up to a fixed target value.

---

## Algorithm

1. `totalSum = accumulate(nums)`.
2. If `abs(target) > totalSum` OR `(target + totalSum) % 2 != 0`, return `0`.
3. `subsetTarget = (target + totalSum) / 2`.
4. `dp` vector of size `subsetTarget + 1` filled with `0`. `dp[0] = 1`.
5. For each `num` in `nums`:
   - For `t` from `subsetTarget` down to `num`:
     - `dp[t] += dp[t - num]`.
6. Return `dp[subsetTarget]`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <numeric>
#include <cmath>
#include <cstdlib>

class Solution {
public:
    int findTargetSumWays(std::vector<int>& nums, int target) {
        int totalSum = std::accumulate(nums.begin(), nums.end(), 0);
        
        // Target is mathematically unreachable if target > totalSum or if (target + totalSum) is odd
        if (std::abs(target) > totalSum || (target + totalSum) % 2 != 0) {
            return 0;
        }
        
        int subsetTarget = (target + totalSum) / 2;
        
        // dp[t] stores number of subsets that sum up to t
        std::vector<int> dp(subsetTarget + 1, 0);
        dp[0] = 1; // Base case: 1 way to form sum 0 (empty subset)
        
        for (int num : nums) {
            // Iterate backward for 0/1 Knapsack (each element used at most once)
            for (int t = subsetTarget; t >= num; --t) {
                dp[t] += dp[t - num];
            }
        }
        
        return dp[subsetTarget];
    }
};
```

---

## Dry Run

### Input
- `nums = [1, 1, 1, 1, 1]`, `target = 3`

### Execution Trace

- `totalSum = 5`. `abs(3) <= 5` and `(3 + 5) % 2 == 0`. OK.
- `subsetTarget = (3 + 5) / 2 = 4`.
- `dp` initialized: `dp[0] = 1`, `dp[1..4] = 0`.
- Process 1st `1`: `dp[1] = 1`.
- Process 2nd `1`: `dp[2] = 1, dp[1] = 2`.
- Process 3rd `1`: `dp[3] = 1, dp[2] = 3, dp[1] = 3`.
- Process 4th `1`: `dp[4] = 1, dp[3] = 4, dp[2] = 6, dp[1] = 4`.
- Process 5th `1`: `dp[4] = dp[4] + dp[3] = 1 + 4 = 5`.

### Result
- Output: `5`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \times \text{subsetTarget})$
  - Outer loop runs $N$ times, inner loop runs $\text{subsetTarget}$ times.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(\text{subsetTarget})$
  - 1D DP table of size $\text{subsetTarget} + 1$.

---

## Why This is Optimal

- Reduces exponential $\mathcal{O}(2^N)$ binary sign choices into pseudo-polynomial $\mathcal{O}(N \times \text{subsetTarget})$ subset sum counting.
- Uses 1D DP array traversed backward for optimal space efficiency.

---

## Common Mistakes

1. **Missing `abs(target) > totalSum` Check**: When `target` is negative and larger than `totalSum` (e.g. `target = -10, totalSum = 5`), `(target + totalSum) / 2` produces a negative index!
2. **Forward Inner Loop**: Iterating `t` forward allows using the same element multiple times.
