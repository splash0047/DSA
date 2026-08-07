# Next Greater Element I

- **Problem Number**: 496
- **Platform**: LeetCode #496
- **Difficulty**: Easy
- **Pattern**: Nested Linear Scan

---

## Brute Force Intuition

For each element `x` in `nums1`:
1. Find the index `j` in `nums2` where `nums2[j] == x`.
2. Scan to the right of index `j` (from `j + 1` to `nums2.size() - 1`) for the first element greater than `x`.
3. If found, assign `ans[i] = nums2[k]`; otherwise `ans[i] = -1`.

---

## Algorithm

1. Initialize `ans` of size `nums1.size()` with `-1`.
2. For `i` from `0` to `nums1.size() - 1`:
   a. Find index `j` in `nums2` where `nums2[j] == nums1[i]`.
   b. For `k` from `j + 1` to `nums2.size() - 1`:
      - If `nums2[k] > nums1[i]`:
        - `ans[i] = nums2[k]`.
        - Break.
3. Return `ans`.

---

## Code

```cpp
#include <vector>

class Solution {
public:
    std::vector<int> nextGreaterElement(const std::vector<int>& nums1, const std::vector<int>& nums2) {
        std::vector<int> ans;
        ans.reserve(nums1.size());
        
        for (int x : nums1) {
            // Find position of x in nums2
            int j = 0;
            while (j < nums2.size() && nums2[j] != x) {
                j++;
            }
            
            // Find next greater element to the right
            int next_greater = -1;
            for (int k = j + 1; k < nums2.size(); ++k) {
                if (nums2[k] > x) {
                    next_greater = nums2[k];
                    break;
                }
            }
            
            ans.push_back(next_greater);
        }
        
        return ans;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N_1 \times N_2)$
  - For each of the $N_1$ elements in `nums1`, scanning `nums2` takes up to $N_2$ steps.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space excluding output vector.

---

## Why This Approach Is Not Optimal

Nested linear scanning takes $\mathcal{O}(N_1 \times N_2)$ time. Using a **Monotonic Stack + Hash Map**, we precompute the Next Greater Element for all numbers in `nums2` in linear $\mathcal{O}(N_1 + N_2)$ time.
