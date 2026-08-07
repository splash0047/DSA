# Partition Equal Subset Sum

## Pattern Used

- **Pattern**: **0/1 Knapsack Subset Sum (1D DP Space Optimization)**
- **Concept**:
  - `totalSum = sum(nums)`. If `totalSum % 2 != 0`, return `false`.
  - `target = totalSum / 2`.
  - Reduce problem to: Can we find a subset of `nums` that sums to `target`?
  - Maintain boolean array `dp[target + 1]` initialized to `false` with `dp[0] = true`.
  - For each number `num` in `nums`:
    - Iterate `t` **backward** from `target` down to `num`:
      - `dp[t] = dp[t] || dp[t - num]`.
  - Return `dp[target]`.

---

## Observation

1. Iterating `t` backward from `target` down to `num` ensures each element `num` is used at most ONCE per subset calculation (0/1 Knapsack property).
2. `dp[t] = dp[t] || dp[t - num]` means target sum `t` is achievable if it was already achievable OR if target sum `t - num` was achievable before adding `num`.

---

## Intuition

Calculate `target = totalSum / 2`. Maintain a notepad of all reachable subset sums (`dp` array). For each number in the input, update the notepad backward so you don't reuse the same number twice. Check if `target` becomes reachable at the end.

---

## Algorithm

1. `totalSum = accumulate(nums)`.
2. If `totalSum % 2 != 0`, return `false`.
3. `target = totalSum / 2`.
4. `vector<bool> dp(target + 1, false)`. `dp[0] = true`.
5. For each `num` in `nums`:
   - For `t` from `target` down to `num`:
     - `dp[t] = dp[t] || dp[t - num]`.
6. Return `dp[target]`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <numeric>

class Solution {
public:
    bool canPartition(std::vector<int>& nums) {
        int totalSum = std::accumulate(nums.begin(), nums.end(), 0);
        
        // An odd sum cannot be divided into two equal integer subsets
        if (totalSum % 2 != 0) {
            return false;
        }
        
        int target = totalSum / 2;
        
        // dp[t] indicates if a subset sum of t is achievable
        std::vector<bool> dp(target + 1, false);
        dp[0] = true; // Base case: 0 sum is always achievable (empty subset)
        
        for (int num : nums) {
            // Iterate backward to prevent using the same element multiple times
            for (int t = target; t >= num; --t) {
                dp[t] = dp[t] || dp[t - num];
            }
        }
        
        return dp[target];
    }
};
```

---

## Dry Run

### Input
- `nums = [1, 5, 11, 5]`

### Execution Trace

- `totalSum = 22`. `target = 11`. `dp` size 12. `dp[0] = true`.
- `num = 1`: `dp[1] = true`.
- `num = 5`: `dp[6] = true`, `dp[5] = true`.
- `num = 11`: `dp[11] = dp[11] || dp[0] = true`.
- `num = 5`: `dp[11]` is already `true`.
- Loop finishes. `dp[11]` is `true`.

### Result
- Output: `true` (Subsets `[1, 5, 5]` and `[11]`)

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \times \text{target})$
  - Outer loop runs $N$ times, inner loop runs $\text{target} = \frac{\text{totalSum}}{2}$ times.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(\text{target})$
  - 1D DP table of size $\text{target} + 1$.

---

## Why This is Optimal

- Transforms exponential $\mathcal{O}(2^N)$ subset generation into pseudo-polynomial $\mathcal{O}(N \times \text{target})$ time.
- Uses optimal 1D space by traversing target loop in reverse.

---

## Common Mistakes

1. **Forward Loop Traversal**: Iterating `t` from `num` UP to `target` enables reusing the same element multiple times (turning 0/1 Knapsack into Unbounded Knapsack!).
2. **Missing Odd TotalSum Check**: Failing to check `totalSum % 2 != 0` up front.
