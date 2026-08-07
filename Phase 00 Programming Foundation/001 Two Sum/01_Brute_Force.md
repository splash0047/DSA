# Two Sum

- **Problem Number**: 1
- **Platform**: LeetCode #1
- **Difficulty**: Easy
- **Pattern**: Brute Force Search / Nested Loops

---

## Brute Force Intuition

When presented with the problem of finding two numbers in an array that add up to a target value, the most straightforward approach is to test all possible pairs of elements. 

Starting from the first element, we compare it with every subsequent element to check if their sum equals the target. If no match is found, we move to the second element and repeat the process for all remaining elements. This exhaustive pair checking ensures that if a valid pair exists, we will eventually evaluate it.

---

## Algorithm

1. Outer loop iterates through index `i` from `0` to `n - 2` (where `n` is the length of the array).
2. Inner loop iterates through index `j` from `i + 1` to `n - 1`.
3. In each iteration of the inner loop, compute the sum `nums[i] + nums[j]`.
4. If `nums[i] + nums[j] == target`, return `{i, j}` immediately.
5. If the loop completes without finding a pair, return an empty vector `{}` (though problem constraints guarantee exactly one solution).

---

## Code

```cpp
#include <vector>

class Solution {
public:
    std::vector<int> twoSum(const std::vector<int>& nums, int target) {
        int n = nums.size();
        for (int i = 0; i < n - 1; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {};
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - The outer loop runs $N - 1$ times.
  - For each iteration $i$, the inner loop runs $N - 1 - i$ times.
  - Total number of pair comparisons: $\frac{N(N - 1)}{2} = \mathcal{O}(N^2)$.
  - In the worst case (when the matching pair is at the very end of the array), we perform roughly $\frac{N^2}{2}$ operations.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - The algorithm operates directly on the input vector without allocating any auxiliary data structures.
  - Only a fixed number of loop variables (`i`, `j`, `n`) are used, consuming constant extra memory.

---

## Why This Approach Is Not Optimal

The bottleneck of the brute force approach is **redundant lookups**. For each element `nums[i]`, we redundantly iterate through the remaining elements to search for the complement `target - nums[i]`. 

Because a linear scan is used to search for the required complementary value, each lookup takes $\mathcal{O}(N)$ time. By replacing the linear scan with a constant-time $\mathcal{O}(1)$ lookup data structure (such as a Hash Table), we can reduce the overall time complexity from $\mathcal{O}(N^2)$ to $\mathcal{O}(N)$.
