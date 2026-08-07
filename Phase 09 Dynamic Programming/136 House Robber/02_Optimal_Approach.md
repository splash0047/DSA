# House Robber

## Pattern Used

- **Pattern**: **Space-Optimized 1D DP (Include / Exclude Decision)**
- **Concept**:
  - `dp[i]` represents max money robbed from first `i` houses.
  - Recurrence: `dp[i] = max(nums[i] + dp[i-2], dp[i-1])`.
  - Notice that computing `dp[i]` depends only on `dp[i-1]` (previous house max) and `dp[i-2]` (two houses ago max).
  - Use two variables `prev2` and `prev1` to update state iteratively in $\mathcal{O}(1)$ auxiliary space.

---

## Observation

1. At house $i$:
   - Option A: Rob house $i \implies \text{loot} = \text{nums}[i] + \text{prev2}$.
   - Option B: Skip house $i \implies \text{loot} = \text{prev1}$.
2. `curr = max(nums[i] + prev2, prev1)`.

---

## Intuition

As you walk down the street house-by-house, keep track of the maximum loot you could have obtained up to two houses ago (`prev2`) and up to the previous house (`prev1`). For the current house, decide whether to rob it (adding its value to `prev2`) or skip it (retaining `prev1`).

---

## Algorithm

1. `prev2 = 0`, `prev1 = 0`.
2. For each `num` in `nums`:
   - `curr = max(num + prev2, prev1)`.
   - `prev2 = prev1`.
   - `prev1 = curr`.
3. Return `prev1`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int rob(std::vector<int>& nums) {
        int prev2 = 0; // Max money robbed 2 houses ago
        int prev1 = 0; // Max money robbed 1 house ago
        
        for (int num : nums) {
            int curr = std::max(num + prev2, prev1);
            prev2 = prev1;
            prev1 = curr;
        }
        
        return prev1;
    }
};
```

---

## Dry Run

### Input
- `nums = [2, 7, 9, 3, 1]`

### Execution Trace

- Init `prev2 = 0`, `prev1 = 0`.
- House 1 (`num = 2`): `curr = max(2 + 0, 0) = 2`. `prev2 = 0, prev1 = 2`.
- House 2 (`num = 7`): `curr = max(7 + 0, 2) = 7`. `prev2 = 2, prev1 = 7`.
- House 3 (`num = 9`): `curr = max(9 + 2, 7) = 11`. `prev2 = 7, prev1 = 11`.
- House 4 (`num = 3`): `curr = max(3 + 7, 11) = 11`. `prev2 = 11, prev1 = 11`.
- House 5 (`num = 1`): `curr = max(1 + 11, 11) = 12`. `prev2 = 11, prev1 = 12`.

### Result
- Output: `12`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass through `nums` array of size $N$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses constant extra space (`prev1`, `prev2`, `curr`).

---

## Why This is Optimal

- Solves house robbing decisions in a single pass taking $\mathcal{O}(N)$ time.
- Uses $\mathcal{O}(1)$ space instead of allocating a full $\mathcal{O}(N)$ DP array.

---

## Common Mistakes

1. **Incorrect Base Case Initialization**: Initializing `prev1` or `prev2` with negative values or bad initial state.
2. **Accessing Index i-2 Out of Bounds**: Handled cleanly by initializing `prev2 = 0` and `prev1 = 0` before the loop.
