# Find First and Last Position of Element in Sorted Array

- **Problem Number**: 34
- **Platform**: LeetCode #34
- **Difficulty**: Medium
- **Pattern**: Linear Scan

---

## Brute Force Intuition

Traverse the array from left to right to find the first occurrence of `target`, and then continue scanning until the element changes to find the last occurrence.

---

## Algorithm

1. `first = -1`, `last = -1`.
2. Loop `i` from `0` to `n - 1`:
   a. If `nums[i] == target`:
      - If `first == -1`, `first = i`.
      - `last = i`.
3. Return `{first, last}`.

---

## Code

```cpp
#include <vector>

class Solution {
public:
    std::vector<int> searchRange(const std::vector<int>& nums, int target) {
        int first = -1, last = -1;
        int n = nums.size();
        
        for (int i = 0; i < n; ++i) {
            if (nums[i] == target) {
                if (first == -1) {
                    first = i;
                }
                last = i;
            }
        }
        
        return {first, last};
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

Linear scan takes $\mathcal{O}(N)$ time, violating the strict $\mathcal{O}(\log N)$ problem requirement. Running **Two Binary Searches** (Lower Bound for First Occurance and Upper Bound for Last Occurrence) achieves logarithmic $\mathcal{O}(\log N)$ time.
