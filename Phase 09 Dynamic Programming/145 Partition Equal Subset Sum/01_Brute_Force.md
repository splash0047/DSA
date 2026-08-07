# Partition Equal Subset Sum

- **Problem Number**: 416
- **Platform**: LeetCode #416
- **Difficulty**: Medium
- **Pattern**: Unmemoized Backtracking / Subset Sum Search

---

## Brute Force Intuition

1. Compute `totalSum = sum(nums)`.
2. If `totalSum % 2 != 0`, return `false` (an odd sum cannot be divided into two equal integer subsets).
3. Target sum for each subset is `target = totalSum / 2`.
4. Run backtracking recursion `canFindSubset(index, target)`: at each element, test either including `nums[index]` in the subset or excluding it.

---

## Algorithm

1. `totalSum = accumulate(nums)`.
2. If `totalSum % 2 != 0`, return `false`.
3. `target = totalSum / 2`.
4. `canFindSubset(i, target)`:
   - Base Case 1: `if (target == 0) return true;`
   - Base Case 2: `if (i < 0 || target < 0) return false;`
   - Return `canFindSubset(i - 1, target - nums[i]) || canFindSubset(i - 1, target)`.

---

## Code

```cpp
#include <vector>
#include <numeric>

class Solution {
private:
    bool canFindSubset(const std::vector<int>& nums, int i, int target) {
        if (target == 0) return true;
        if (i < 0 || target < 0) return false;
        
        // Include nums[i] OR Exclude nums[i]
        return canFindSubset(nums, i - 1, target - nums[i]) || 
               canFindSubset(nums, i - 1, target);
    }

public:
    bool canPartition(std::vector<int>& nums) {
        int totalSum = std::accumulate(nums.begin(), nums.end(), 0);
        if (totalSum % 2 != 0) return false;
        
        return canFindSubset(nums, nums.size() - 1, totalSum / 2);
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(2^N)$
  - Generating $2^N$ subset combinations for array of size $N$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Call stack depth equals $N$.

---

## Why This Approach Is Not Optimal

Evaluating duplicate subproblem states $(i, \text{target})$ repeatedly takes exponential $\mathcal{O}(2^N)$ time. Using **Space-Optimized 0/1 Knapsack 1D DP (or `std::bitset`)**, we solve partition equal subset sum in pseudo-polynomial $\mathcal{O}(N \times \text{target})$ time and $\mathcal{O}(\text{target})$ space!
