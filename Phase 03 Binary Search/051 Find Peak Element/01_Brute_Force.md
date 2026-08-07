# Find Peak Element

- **Problem Number**: 162
- **Platform**: LeetCode #162
- **Difficulty**: Medium
- **Pattern**: Linear Peak Scan

---

## Brute Force Intuition

Traverse `nums` from left to right. The first element `nums[i]` that is greater than its right neighbor `nums[i + 1]` must be a peak element! (Because if we reach index `i`, we already know `nums[i] > nums[i - 1]`).

---

## Algorithm

1. Loop `i` from `0` to `n - 2`:
   a. If `nums[i] > nums[i + 1]`, return `i`.
2. Return `n - 1`.

---

## Code

```cpp
#include <vector>

class Solution {
public:
    int findPeakElement(const std::vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n - 1; ++i) {
            if (nums[i] > nums[i + 1]) {
                return i;
            }
        }
        return n - 1;
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

Linear scan takes $\mathcal{O}(N)$ time. The problem requires an $\mathcal{O}(\log N)$ time solution. Using **Binary Search on Slope Direction**, we can locate a peak in logarithmic $\mathcal{O}(\log N)$ time.
