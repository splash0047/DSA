# Search in Rotated Sorted Array II

- **Problem Number**: 81
- **Platform**: LeetCode #81
- **Difficulty**: Medium
- **Pattern**: Linear Scan

---

## Brute Force Intuition

Iterate through every element `nums[i]` from index `0` to `n - 1`. If `nums[i] == target`, return `true`. If loop finishes without finding `target`, return `false`.

---

## Algorithm

1. Loop `i` from `0` to `n - 1`.
2. If `nums[i] == target`, return `true`.
3. Return `false`.

---

## Code

```cpp
#include <vector>

class Solution {
public:
    bool search(const std::vector<int>& nums, int target) {
        for (int num : nums) {
            if (num == target) {
                return true;
            }
        }
        return false;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Scans all $N$ elements linearly.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

While linear scan works in $\mathcal{O}(N)$ time, it does not leverage the sorted/rotated properties of the array. Using **Modified Binary Search with Duplicate Trimming**, we achieve $\mathcal{O}(\log N)$ average time complexity.
