# Target Sum

- **Problem Number**: 494
- **Platform**: LeetCode #494
- **Difficulty**: Medium
- **Pattern**: Unmemoized Binary Decision Tree Backtracking

---

## Brute Force Intuition

At each element `nums[i]`, try assigning both symbols:
1. Assign `'+'`: Recurse to `i + 1` with `currentSum + nums[i]`.
2. Assign `'-'`: Recurse to `i + 1` with `currentSum - nums[i]`.

When `i == nums.length()`, check if `currentSum == target`. Return 1 if matched, else 0.

---

## Algorithm

1. `countWays(i, currentSum)`:
   - Base Case: If `i == nums.size()`, return `currentSum == target ? 1 : 0`.
   - `add = countWays(i + 1, currentSum + nums[i])`.
   - `sub = countWays(i + 1, currentSum - nums[i])`.
   - Return `add + sub`.

---

## Code

```cpp
#include <vector>

class Solution {
private:
    int countWays(const std::vector<int>& nums, int i, int currentSum, int target) {
        if (i == nums.size()) {
            return currentSum == target ? 1 : 0;
        }
        
        int add = countWays(nums, i + 1, currentSum + nums[i], target);
        int sub = countWays(nums, i + 1, currentSum - nums[i], target);
        
        return add + sub;
    }

public:
    int findTargetSumWays(std::vector<int>& nums, int target) {
        return countWays(nums, 0, 0, target);
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(2^N)$
  - Branching factor of 2 at each of the $N$ elements creates $2^N$ decision paths.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Call stack depth equals $N$.

---

## Why This Approach Is Not Optimal

Evaluating all $2^N$ sign combinations takes exponential $\mathcal{O}(2^N)$ time. By **Mathematical Reduction to Subset Sum 0/1 Knapsack DP**, we can compute target sum ways in pseudo-polynomial $\mathcal{O}(N \times \text{subsetTarget})$ time and $\mathcal{O}(\text{subsetTarget})$ space!
