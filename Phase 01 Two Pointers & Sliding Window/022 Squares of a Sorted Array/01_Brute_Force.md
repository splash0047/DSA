# Squares of a Sorted Array

- **Problem Number**: 977
- **Platform**: LeetCode #977
- **Difficulty**: Easy
- **Pattern**: Square and Sort

---

## Brute Force Intuition

Square every element in `nums`, then call `std::sort` to sort the squared numbers in non-decreasing order.

---

## Algorithm

1. Iterate through each element `x` in `nums`:
   - Replace `x = x * x`.
2. Sort `nums` using `std::sort(nums.begin(), nums.end())`.
3. Return `nums`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> sortedSquares(std::vector<int>& nums) {
        for (int& x : nums) {
            x = x * x;
        }
        std::sort(nums.begin(), nums.end());
        return nums;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log N)$
  - Squaring takes $\mathcal{O}(N)$ time; sorting takes $\mathcal{O}(N \log N)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$ or $\mathcal{O}(\log N)$ depending on sorting algorithm implementation.

---

## Why This Approach Is Not Optimal

This approach ignores the fact that the original input array `nums` is **already sorted**. Negative numbers become positive when squared, meaning the largest squared values must reside at the far left (large negative values) or far right (large positive values). Using **Two Pointers (Outside-In)** achieves linear $\mathcal{O}(N)$ time.
