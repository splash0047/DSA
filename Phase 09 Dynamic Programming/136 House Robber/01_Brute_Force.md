# House Robber

- **Problem Number**: 198
- **Platform**: LeetCode #198
- **Difficulty**: Medium
- **Pattern**: Unmemoized Include/Exclude Decision Recursion

---

## Brute Force Intuition

At each house $i$, the robber has two choices:
1. **Rob house $i$**: Earn `nums[i]` money, but cannot rob house $i-1$. Move to subproblem at house $i-2$.
2. **Skip house $i$**: Earn $0$ money from house $i$. Move to subproblem at house $i-1$.

The recurrence relation is:
$$\text{rob}(i) = \max(\text{nums}[i] + \text{rob}(i-2), \text{rob}(i-1))$$

A naive recursive implementation tests both choices at every index $i$ without storing subproblem results.

---

## Algorithm

1. `rob(nums, i)`:
   - If `i < 0`, return `0`.
   - Return `max(nums[i] + rob(nums, i - 2), rob(nums, i - 1))`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
private:
    int robHelper(const std::vector<int>& nums, int i) {
        if (i < 0) {
            return 0;
        }
        return std::max(nums[i] + robHelper(nums, i - 2), robHelper(nums, i - 1));
    }

public:
    int rob(std::vector<int>& nums) {
        return robHelper(nums, nums.size() - 1);
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(2^N)$
  - Generates $2^N$ subproblems due to duplicate recursive branches.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Recursion call stack depth equals $N$.

---

## Why This Approach Is Not Optimal

Evaluating duplicate subproblems takes exponential $\mathcal{O}(2^N)$ time. Using **Space-Optimized Dynamic Programming (Pick / Non-Pick DP)**, we can calculate the maximum loot in linear $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space!
