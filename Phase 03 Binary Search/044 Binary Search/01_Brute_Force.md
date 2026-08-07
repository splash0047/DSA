# Binary Search

- **Problem Number**: 704
- **Platform**: LeetCode #704
- **Difficulty**: Easy
- **Pattern**: Linear Scan

---

## Brute Force Intuition

Iterate through every element `nums[i]` in the array from index `0` to `n - 1`. If `nums[i] == target`, return `i`. If the loop finishes without finding `target`, return `-1`.

---

## Algorithm

1. Loop `i` from `0` to `n - 1`.
2. If `nums[i] == target`, return `i`.
3. Return `-1`.

---

## Code

```cpp
#include <vector>

class Solution {
public:
    int search(const std::vector<int>& nums, int target) {
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            if (nums[i] == target) {
                return i;
            }
        }
        return -1;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Scans up to $N$ elements linearly.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

Linear scan takes $\mathcal{O}(N)$ time, ignoring the crucial problem constraint that **`nums` is pre-sorted in ascending order**. Using **Iterative Binary Search**, we cut the search space in half at each step, achieving logarithmic $\mathcal{O}(\log N)$ time.
