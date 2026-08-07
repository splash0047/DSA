# Search Insert Position

- **Problem Number**: 35
- **Platform**: LeetCode #35
- **Difficulty**: Easy
- **Pattern**: Linear Scan

---

## Brute Force Intuition

Iterate through `nums` from left to right. The first index `i` where `nums[i] >= target` is the exact insertion position. If no element is $\ge \text{target}$, the target belongs at index `n` (the end of the array).

---

## Algorithm

1. Loop `i` from `0` to `n - 1`:
   a. If `nums[i] >= target`, return `i`.
2. Return `n`.

---

## Code

```cpp
#include <vector>

class Solution {
public:
    int searchInsert(const std::vector<int>& nums, int target) {
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            if (nums[i] >= target) {
                return i;
            }
        }
        return n;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass through $N$ elements.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

Linear scan takes $\mathcal{O}(N)$ time. Since `nums` is sorted, finding the **Lower Bound** (`std::lower_bound`) using Binary Search reduces complexity to $\mathcal{O}(\log N)$.
