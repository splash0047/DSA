# Search in Rotated Sorted Array

- **Problem Number**: 33
- **Platform**: LeetCode #33
- **Difficulty**: Medium
- **Pattern**: Linear Scan

---

## Brute Force Intuition

Iterate through every element `nums[i]` from left to right. If `nums[i] == target`, return `i`. If loop finishes without finding `target`, return `-1`.

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
  - Scans all $N$ elements linearly.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

Linear scan takes $\mathcal{O}(N)$ time. By utilizing the property that **at least one half of a rotated sorted array is always strictly sorted**, we can adapt **Binary Search** to run in logarithmic $\mathcal{O}(\log N)$ time.
