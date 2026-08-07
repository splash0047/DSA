# Median of Two Sorted Arrays

- **Problem Number**: 4
- **Platform**: LeetCode #4
- **Difficulty**: Hard
- **Pattern**: Two-Pointer Merge

---

## Brute Force Intuition

Merge the two sorted arrays `nums1` and `nums2` into a single combined sorted array `merged` of size $M + N$ using Two Pointers. Then return the median element directly from the merged array.

---

## Algorithm

1. Allocate `merged` array of size $m + n$.
2. Merge `nums1` and `nums2` using Two Pointers into `merged`.
3. Total size `total = m + n`.
4. If `total` is odd: return `merged[total / 2]`.
5. If `total` is even: return `(merged[total / 2 - 1] + merged[total / 2]) / 2.0`.

---

## Code

```cpp
#include <vector>

class Solution {
public:
    double findMedianSortedArrays(const std::vector<int>& nums1, const std::vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        std::vector<int> merged;
        merged.reserve(m + n);
        
        int i = 0, j = 0;
        while (i < m && j < n) {
            if (nums1[i] <= nums2[j]) {
                merged.push_back(nums1[i++]);
            } else {
                merged.push_back(nums2[j++]);
            }
        }
        while (i < m) merged.push_back(nums1[i++]);
        while (j < n) merged.push_back(nums2[j++]);
        
        int total = m + n;
        if (total % 2 == 1) {
            return merged[total / 2];
        } else {
            return (merged[total / 2 - 1] + merged[total / 2]) / 2.0;
        }
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(M + N)$
  - Single pass to merge two sorted arrays of lengths $M$ and $N$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(M + N)$
  - Stores merged array of size $M + N$.

---

## Why This Approach Is Not Optimal

Merging takes $\mathcal{O}(M + N)$ time, violating the strict requirement for an $\mathcal{O}(\log(M + N))$ algorithm. By using **Binary Search on Array Partitions**, we can find the median in $\mathcal{O}(\log(\min(M, N)))$ time.
