# House Robber II

## Pattern Used

- **Pattern**: **Circular Array Splitting (Range-Bounded 1D DP)**
- **Concept**:
  - Because house `0` and house `n-1` are adjacent in the circular layout, they cannot both be robbed together.
  - Break the circular constraint into two mutually exclusive linear subproblems:
    - **Case 1**: Consider houses from index `0` to `n - 2` (exclude last house).
    - **Case 2**: Consider houses from index `1` to `n - 1` (exclude first house).
  - Helper function `robRange(nums, start, end)` computes max loot for range `[start, end]` in $\mathcal{O}(1)$ auxiliary space.
  - Result $= \max(\text{robRange}(0, n-2), \text{robRange}(1, n-1))$.

---

## Observation

1. Circular adjacency condition means at least one of the two end houses (`0` or `n-1`) MUST be left unrobbed!
2. Running standard House Robber I over `[0, n-2]` covers all valid choices excluding the last house.
3. Running standard House Robber I over `[1, n-1]` covers all valid choices excluding the first house.
4. The maximum of these two range queries covers all valid circular configurations!

---

## Intuition

If the first house and last house are connected in a loop, you can never rob both. So split the problem: pretend the last house doesn't exist and find the best loot. Then pretend the first house doesn't exist and find the best loot. The higher of the two results is your answer.

---

## Algorithm

1. If `n == 1`, return `nums[0]`.
2. Define `robRange(nums, start, end)`:
   - `prev2 = 0`, `prev1 = 0`.
   - Loop `i` from `start` to `end`:
     - `curr = max(nums[i] + prev2, prev1)`.
     - `prev2 = prev1`.
     - `prev1 = curr`.
   - Return `prev1`.
3. Return `max(robRange(nums, 0, n - 2), robRange(nums, 1, n - 1))`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>

class Solution {
private:
    int robRange(const std::vector<int>& nums, int start, int end) {
        int prev2 = 0;
        int prev1 = 0;
        
        for (int i = start; i <= end; ++i) {
            int curr = std::max(nums[i] + prev2, prev1);
            prev2 = prev1;
            prev1 = curr;
        }
        
        return prev1;
    }

public:
    int rob(std::vector<int>& nums) {
        int n = nums.size();
        if (n == 1) {
            return nums[0];
        }
        
        // Case 1: Rob within range [0, n-2] (Excludes last house)
        // Case 2: Rob within range [1, n-1] (Excludes first house)
        return std::max(robRange(nums, 0, n - 2), robRange(nums, 1, n - 1));
    }
};
```

---

## Dry Run

### Input
- `nums = [2, 3, 2]`

### Execution Trace

- `n = 3`. `n != 1`.
- `robRange(nums, 0, 1)` (Subarray `[2, 3]`):
  - `i=0 (2)`: `curr = max(2+0, 0) = 2`. `prev2=0, prev1=2`.
  - `i=1 (3)`: `curr = max(3+0, 2) = 3`. `prev2=2, prev1=3`.
  - Returns `3`.
- `robRange(nums, 1, 2)` (Subarray `[3, 2]`):
  - `i=1 (3)`: `curr = max(3+0, 0) = 3`. `prev2=0, prev1=3`.
  - `i=2 (2)`: `curr = max(2+0, 3) = 3`. `prev2=3, prev1=3`.
  - Returns `3`.
- `max(3, 3) = 3`.

### Result
- Output: `3`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - `robRange` runs twice over linear subarrays of length $N - 1$. Total time $= \mathcal{O}(N)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Operates directly on `nums` indices without allocating auxiliary vectors.

---

## Why This is Optimal

- Solves circular house robbing in linear $\mathcal{O}(N)$ time.
- Operates in $\mathcal{O}(1)$ space by using index range bounds instead of copying arrays.

---

## Common Mistakes

1. **Missing `n == 1` Base Case Check**: Passing `start = 0, end = -1` when $n = 1$ leads to undefined behavior.
2. **Double Counting Both Ends**: Allowing both house `0` and house `n-1` to be robbed simultaneously.
