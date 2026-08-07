# Merge Sorted Array

- **Problem Number**: 88
- **Platform**: LeetCode #88
- **Difficulty**: Easy
- **Pattern**: Concatenate and Sort

---

## Brute Force Intuition

The most straightforward approach is to copy all $n$ elements of `nums2` directly into the trailing zero positions of `nums1` (from index `m` to `m + n - 1`), and then sort `nums1` using standard library sorting (`std::sort`).

---

## Algorithm

1. Loop `i` from `0` to `n - 1`:
   - Set `nums1[m + i] = nums2[i]`.
2. Call `std::sort(nums1.begin(), nums1.end())`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n) {
        for (int i = 0; i < n; ++i) {
            nums1[m + i] = nums2[i];
        }
        std::sort(nums1.begin(), nums1.end());
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}((m + n) \log (m + n))$
  - Copying takes $\mathcal{O}(n)$ time.
  - Sorting an array of length $m + n$ takes $\mathcal{O}((m + n) \log (m + n))$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$ (or $\mathcal{O}(\log(m+n))$ depending on sorting implementation).

---

## Why This Approach Is Not Optimal

This approach completely ignores the fact that both `nums1` and `nums2` are **already individually sorted**. By utilizing the sorted property of both input arrays, we can merge them in linear $\mathcal{O}(m + n)$ time using **Three Pointers (Backward Merge)**.
