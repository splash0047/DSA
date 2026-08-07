# Find Minimum in Rotated Sorted Array

- **Problem Number**: 153
- **Platform**: LeetCode #153
- **Difficulty**: Medium
- **Pattern**: Linear Minimum Scan

---

## Brute Force Intuition

Iterate through `nums` from index `0` to `n - 1` and keep track of the minimum value seen.

---

## Algorithm

1. `min_val = nums[0]`.
2. Loop `i` from `1` to `n - 1`:
   - `min_val = min(min_val, nums[i])`.
3. Return `min_val`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int findMin(const std::vector<int>& nums) {
        int min_val = nums[0];
        for (int x : nums) {
            min_val = std::min(min_val, x);
        }
        return min_val;
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

Linear scan takes $\mathcal{O}(N)$ time. By using **Binary Search** comparing `nums[mid]` with `nums[high]`, we can locate the rotation pivot (minimum element) in logarithmic $\mathcal{O}(\log N)$ time.
