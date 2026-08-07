# Median of Two Sorted Arrays

## Pattern Used

- **Pattern**: **Binary Search on Array Partitions**
- **Concept**: Partition `nums1` at index `px` and `nums2` at index `py` such that:
  1. $\text{px} + \text{py} = \frac{m + n + 1}{2}$ (left half contains half of total elements).
  2. $\text{maxLeft1} \le \text{minRight2}$ AND $\text{maxLeft2} \le \text{minRight1}$.

---

## Observation

1. To minimize runtime, ensure `nums1` is the shorter array ($m \le n$) by swapping if necessary. Then binary search range for `px` is $[0, m]$.
2. For any cut `px` in `nums1`:
   - `py = (m + n + 1) / 2 - px`.
   - `maxLeft1 = (px == 0) ? -INF : nums1[px - 1]`
   - `minRight1 = (px == m) ? +INF : nums1[px]`
   - `maxLeft2 = (py == 0) ? -INF : nums2[py - 1]`
   - `minRight2 = (py == n) ? +INF : nums2[py]`
3. Partition Validation:
   - If `maxLeft1 <= minRight2` AND `maxLeft2 <= minRight1`: Valid partition!
     - If total length $(m + n)$ is odd: `median = max(maxLeft1, maxLeft2)`.
     - If total length $(m + n)$ is even: `median = (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0`.
   - If `maxLeft1 > minRight2`: `px` is too far right $\rightarrow$ `high = px - 1`.
   - If `maxLeft2 > minRight1`: `px` is too far left $\rightarrow$ `low = px + 1`.

---

## Intuition

Place vertical cuts in both arrays such that all elements on the left side of the cuts are smaller than or equal to all elements on the right side of the cuts. Binary search adjusts the cut position in the shorter array in $\mathcal{O}(\log(\min(M, N)))$ time.

---

## Algorithm

1. If `nums1.size() > nums2.size()`, return `findMedianSortedArrays(nums2, nums1)`.
2. `m = nums1.size()`, `n = nums2.size()`.
3. `low = 0`, `high = m`.
4. While `low <= high`:
   a. `px = low + (high - low) / 2`.
   b. `py = (m + n + 1) / 2 - px`.
   c. Set boundary values `maxLeft1`, `minRight1`, `maxLeft2`, `minRight2` with infinity handles.
   d. If `maxLeft1 <= minRight2 && maxLeft2 <= minRight1`:
      - If `(m + n) % 2 == 1`: return `max(maxLeft1, maxLeft2)`.
      - Else: return `(max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0`.
   e. Else if `maxLeft1 > minRight2`: `high = px - 1`.
   f. Else: `low = px + 1`.
5. Return `0.0`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>
#include <climits>

class Solution {
public:
    double findMedianSortedArrays(const std::vector<int>& nums1, const std::vector<int>& nums2) {
        // Ensure nums1 is the smaller array to guarantee O(log(min(M, N))) time
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }
        
        int m = nums1.size();
        int n = nums2.size();
        int low = 0;
        int high = m;
        
        while (low <= high) {
            int px = low + (high - low) / 2;
            int py = (m + n + 1) / 2 - px;
            
            int maxLeft1 = (px == 0) ? INT_MIN : nums1[px - 1];
            int minRight1 = (px == m) ? INT_MAX : nums1[px];
            
            int maxLeft2 = (py == 0) ? INT_MIN : nums2[py - 1];
            int minRight2 = (py == n) ? INT_MAX : nums2[py];
            
            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
                if ((m + n) % 2 == 1) {
                    return std::max(maxLeft1, maxLeft2);
                } else {
                    return (std::max(maxLeft1, maxLeft2) + std::min(minRight1, minRight2)) / 2.0;
                }
            } else if (maxLeft1 > minRight2) {
                high = px - 1; // Partition 1 is too far right
            } else {
                low = px + 1;  // Partition 1 is too far left
            }
        }
        
        return 0.0;
    }
};
```

---

## Dry Run

### Input
- `nums1 = [1, 3]`, `nums2 = [2]` ($m=2, n=1$)
- Swap inputs $\rightarrow$ `nums1 = [2]` ($m=1$), `nums2 = [1, 3]` ($n=2$).

### Execution Trace

- `low = 0`, `high = 1`, `(m + n + 1) / 2 = (1 + 2 + 1) / 2 = 2`.

| Step | `low` | `high` | `px` | `py = 2 - px` | `maxLeft1` | `minRight1` | `maxLeft2` | `minRight2` | Valid? | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `0` | `1` | `0` | `2` | `INT_MIN` | `nums1[0] = 2` | `nums2[1] = 3` | `INT_MAX` | `INT_MIN <= INT_MAX` && `3 <= 2` (**No**) | `maxLeft2 > minRight1` $\rightarrow$ `low = px + 1 = 1` |
| 2 | `1` | `1` | `1` | `1` | `nums1[0] = 2` | `INT_MAX` | `nums2[0] = 1` | `nums2[1] = 3` | `2 <= 3` && `1 <= INT_MAX` (**Yes!**) | Total len 3 (odd) $\rightarrow$ Return `max(2, 1) = 2.0` |

### Result
- Output: `2.0`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(\log(\min(M, N)))$
  - Binary search is strictly performed over the smaller array of size $\min(M, N)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This is Optimal

- Meets the strict $\mathcal{O}(\log(M + N))$ problem requirement by achieving an even faster $\mathcal{O}(\log(\min(M, N)))$ time.
- Uses zero extra memory ($\mathcal{O}(1)$ space).

---

## Common Mistakes

1. **Not Ensuring `nums1` is Smaller**: Running binary search on the larger array can cause `py` to go out of bounds ($py < 0$ or $py > n$). Always swap arrays if `m > n`.
2. **Missing `INT_MIN` / `INT_MAX` Edge Handles**: Out-of-bounds error when `px == 0`, `px == m`, `py == 0`, or `py == n`.
