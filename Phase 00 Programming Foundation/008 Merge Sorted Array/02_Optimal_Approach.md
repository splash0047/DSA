# Merge Sorted Array

## Pattern Used

- **Pattern**: **Three Pointers (Backward Merge)**
- **Concept**: Merging backwards from right to left (index $m + n - 1$) so we can overwrite the empty trailing slots of `nums1` without needing auxiliary memory or accidentally overwriting unread elements in `nums1`.

---

## Observation

1. If we attempt to merge from left to right, placing elements into `nums1[0]` would overwrite unread elements of `nums1`, requiring an extra buffer vector.
2. However, the back of `nums1` (indices $m$ to $m + n - 1$) contains unused buffer slots.
3. Therefore, if we compare elements from the **back** of both arrays and place the **larger** element into the back of `nums1`, no unread data will ever be overwritten!

---

## Intuition

Set up three pointers:
- `p1 = m - 1`: Points to the last valid element in `nums1`.
- `p2 = n - 1`: Points to the last element in `nums2`.
- `p = m + n - 1`: Points to the rightmost insertion slot in `nums1`.

At each step, compare `nums1[p1]` and `nums2[p2]`. Place the larger of the two at `nums1[p]` and decrement the corresponding pointers.

---

## Algorithm

1. `p1 = m - 1`, `p2 = n - 1`, `p = m + n - 1`.
2. While `p2 >= 0`:
   a. If `p1 >= 0` and `nums1[p1] > nums2[p2]`:
      - Set `nums1[p] = nums1[p1]`, `p1--`.
   b. Else:
      - Set `nums1[p] = nums2[p2]`, `p2--`.
   c. Decrement `p--`.
3. Done (if `p1` finishes first, remaining `nums2` elements are copied; if `p2` finishes first, remaining `nums1` elements are already in their correct places).

---

## Clean C++17 Solution

```cpp
#include <vector>

class Solution {
public:
    void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n) {
        int p1 = m - 1;
        int p2 = n - 1;
        int p = m + n - 1;
        
        while (p2 >= 0) {
            if (p1 >= 0 && nums1[p1] > nums2[p2]) {
                nums1[p--] = nums1[p1--];
            } else {
                nums1[p--] = nums2[p2--];
            }
        }
    }
};
```

---

## Dry Run

### Input
- `nums1 = [1, 2, 3, 0, 0, 0]`, `m = 3`
- `nums2 = [2, 5, 6]`, `n = 3`

### Execution Trace

| Step | `p1` (`nums1[p1]`) | `p2` (`nums2[p2]`) | `p` | Larger Value | Action | `nums1` State |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Start| `2` (`3`) | `2` (`6`) | `5` | `6` (`nums2`) | Write `nums1[5] = 6`, `p2--`, `p--` | `[1, 2, 3, 0, 0, 6]` |
| 1 | `2` (`3`) | `1` (`5`) | `4` | `5` (`nums2`) | Write `nums1[4] = 5`, `p2--`, `p--` | `[1, 2, 3, 0, 5, 6]` |
| 2 | `2` (`3`) | `0` (`2`) | `3` | `3` (`nums1`) | Write `nums1[3] = 3`, `p1--`, `p--` | `[1, 2, 3, 3, 5, 6]` |
| 3 | `1` (`2`) | `0` (`2`) | `2` | `2` (`nums2`) | Write `nums1[2] = 2`, `p2--`, `p--` | `[1, 2, 2, 3, 5, 6]` |
| Done | - | `-1` | - | - | `p2 < 0`, Loop terminates | `[1, 2, 2, 3, 5, 6]` |

### Result
- `nums1 = [1, 2, 2, 3, 5, 6]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(m + n)$
  - Pointer `p` moves from $m + n - 1$ down to `0`, making at most $m + n$ iterations.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Modifications take place entirely **in-place** using the pre-allocated buffer space in `nums1`.

---

## Why This is Optimal

- Every element in both arrays must be evaluated at least once ($\Omega(m + n)$ lower bound).
- We achieve $\mathcal{O}(m + n)$ time with zero extra space.

---

## Common Mistakes

1. **Merging Forward**: Attempting to merge from left to right without an auxiliary vector, causing unread elements in `nums1` to be overwritten.
2. **Incorrect Loop Condition**: Using `while (p1 >= 0 && p2 >= 0)`. If `nums1` elements run out first (`p1 < 0`), remaining `nums2` elements must still be copied over! The outer loop condition MUST be `while (p2 >= 0)`.
