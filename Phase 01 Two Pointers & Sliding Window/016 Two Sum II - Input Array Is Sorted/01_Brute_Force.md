# Two Sum II - Input Array Is Sorted

- **Problem Number**: 167
- **Platform**: LeetCode #167
- **Difficulty**: Medium
- **Pattern**: Binary Search Lookups

---

## Brute Force Intuition

For each element `numbers[i]`, we need to find its complement `target - numbers[i]`. Since the array is pre-sorted, instead of a linear scan, we can use Binary Search (`std::lower_bound`) on the subarray `numbers[i+1 ... n-1]` to find the complement in $\mathcal{O}(\log N)$ time.

---

## Algorithm

1. Loop `i` from `0` to `n - 2`.
2. Compute `complement = target - numbers[i]`.
3. Binary search for `complement` in range `[i + 1, n - 1]`.
4. If found at index `j`, return `{i + 1, j + 1}` (1-based indices).

---

## Code

```cpp
#include <vector>

class Solution {
public:
    std::vector<int> twoSum(const std::vector<int>& numbers, int target) {
        int n = numbers.size();

        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {

                if (numbers[i] + numbers[j] == target) {
                    return {i + 1, j + 1};
                }
            }
        }

        return {};
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log N)$
  - Outer loop runs $N$ times; binary search takes $\mathcal{O}(\log N)$ per step.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses constant extra space.

---

## Why This Approach Is Not Optimal

While using $\mathcal{O}(1)$ space, Binary Search takes $\mathcal{O}(N \log N)$ time. Because the array is pre-sorted, **Two Pointers (Opposite Ends)** can shrink the search space from both ends in linear $\mathcal{O}(N)$ time.
