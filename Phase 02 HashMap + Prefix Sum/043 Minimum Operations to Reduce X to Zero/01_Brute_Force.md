# Minimum Operations to Reduce X to Zero

- **Problem Number**: 1658
- **Platform**: LeetCode #1658
- **Difficulty**: Medium
- **Pattern**: Recursive Choice / Backtracking

---

## Brute Force Intuition

At each step, we can choose to remove either the leftmost element (`left` pointer) or rightmost element (`right` pointer), subtracting its value from `x`. This can be modeled as a recursive function `solve(left, right, current_x)`:
- Base case 1: `current_x == 0` $\rightarrow$ return `0` operations.
- Base case 2: `current_x < 0` or `left > right` $\rightarrow$ return $\infty$.
- Recurrence: $\min(1 + \text{solve}(left + 1, right, current_x - nums[left]), 1 + \text{solve}(left, right - 1, current_x - nums[right]))$.

---

## Algorithm

1. Define recursive function `solve(left, right, current_x)`:
   a. If `current_x == 0`, return `0`.
   b. If `current_x < 0 || left > right`, return `1e9`.
   c. `take_left = 1 + solve(left + 1, right, current_x - nums[left])`.
   d. `take_right = 1 + solve(left, right - 1, current_x - nums[right])`.
   e. Return `min(take_left, take_right)`.
2. Return result or `-1` if result $\ge 1e9$.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
private:
    int solve(const std::vector<int>& nums, int left, int right, int current_x) {
        if (current_x == 0) return 0;
        if (current_x < 0 || left > right) return 1e9;
        
        int take_left = 1 + solve(nums, left + 1, right, current_x - nums[left]);
        int take_right = 1 + solve(nums, left, right - 1, current_x - nums[right]);
        
        return std::min(take_left, take_right);
    }
public:
    int minOperations(const std::vector<int>& nums, int x) {
        int ans = solve(nums, 0, nums.size() - 1, x);
        return ans >= 1e9 ? -1 : ans;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(2^N)$
  - Exponential time complexity due to 2 recursive branches at each step.
  - Causes severe TLE for $N > 30$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$ recursion stack depth.

---

## Why This Approach Is Not Optimal

Exponential recursion is far too slow. By reframing the problem inversely: **Find the longest contiguous middle subarray whose sum equals $\text{total\_sum} - x$**, we can solve it using a **Variable-Size Sliding Window** or **Prefix Sum Hash Map** in linear $\mathcal{O}(N)$ time.
