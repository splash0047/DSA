# K-th Element of Two Sorted Arrays

## Pattern Used

- **Pattern**: **Binary Search on Array Partitions**
- **Concept**: Partition array `a` into `px` elements and array `b` into `py = k - px` elements such that:
  1. `px + py == k` (the combined left partition contains exactly $k$ elements).
  2. `maxLeftA <= minRightB` AND `maxLeftB <= minRightA`.
  3. When valid, the $k^{\text{th}}$ element is simply $\max(\text{maxLeftA}, \text{maxLeftB})$.

---

## Observation

1. Ensure `a` is the smaller array ($n \le m$) to guarantee logarithmic performance.
2. Search Range Constraints for `px` (elements taken from array `a`):
   - `low = max(0, k - m)` (if $k > m$, array `b` alone cannot provide $k$ elements, so `a` must contribute at least $k - m$ elements).
   - `high = min(n, k)` (cannot take more than $n$ elements from `a` nor more than $k$ total elements).
3. At each step:
   - `px = low + (high - low) / 2`.
   - `py = k - px`.
   - Boundary fallback handles:
     - `maxLeftA = (px == 0) ? -INF : a[px - 1]`
     - `minRightA = (px == n) ? +INF : a[px]`
     - `maxLeftB = (py == 0) ? -INF : b[py - 1]`
     - `minRightB = (py == m) ? +INF : b[py]`
4. If `maxLeftA <= minRightB` AND `maxLeftB <= minRightA`: Valid partition! Return $\max(\text{maxLeftA}, \text{maxLeftB})$.

---

## Intuition

Divide both arrays into left and right halves such that the total number of elements in both left halves equals $k$, and all elements in both left halves are $\le$ all elements in both right halves. The largest element among the left halves is the $k^{\text{th}}$ element!

---

## Algorithm

1. If `a.size() > b.size()`, return `kthElement(b, a, k)`.
2. `n = a.size()`, `m = b.size()`.
3. `low = max(0, k - m)`, `high = min(n, k)`.
4. While `low <= high`:
   a. `px = low + (high - low) / 2`.
   b. `py = k - px`.
   c. Set boundary values `maxLeftA`, `minRightA`, `maxLeftB`, `minRightB` using `INT_MIN` / `INT_MAX`.
   d. If `maxLeftA <= minRightB && maxLeftB <= minRightA`:
      - Return `max(maxLeftA, maxLeftB)`.
   e. Else if `maxLeftA > minRightB`: `high = px - 1`.
   f. Else: `low = px + 1`.
5. Return `-1`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>
#include <climits>

class Solution {
public:
    int kthElement(const std::vector<int>& a, const std::vector<int>& b, int k) {
        // Ensure array 'a' is smaller to optimize binary search
        if (a.size() > b.size()) {
            return kthElement(b, a, k);
        }
        
        int n = a.size();
        int m = b.size();
        
        int low = std::max(0, k - m);
        int high = std::min(n, k);
        
        while (low <= high) {
            int px = low + (high - low) / 2;
            int py = k - px;
            
            int maxLeftA = (px == 0) ? INT_MIN : a[px - 1];
            int minRightA = (px == n) ? INT_MAX : a[px];
            
            int maxLeftB = (py == 0) ? INT_MIN : b[py - 1];
            int minRightB = (py == m) ? INT_MAX : b[py];
            
            if (maxLeftA <= minRightB && maxLeftB <= minRightA) {
                return std::max(maxLeftA, maxLeftB);
            } else if (maxLeftA > minRightB) {
                high = px - 1; // Take fewer elements from array A
            } else {
                low = px + 1;  // Take more elements from array A
            }
        }
        
        return -1;
    }
};
```

---

## Dry Run

### Input
- `a = [2, 3, 6, 7, 9]`, `b = [1, 4, 8, 10]`, `k = 5`
- Swap `a` and `b` $\rightarrow$ `a = [1, 4, 8, 10]` ($n=4$), `b = [2, 3, 6, 7, 9]` ($m=5$).
- `low = max(0, 5 - 5) = 0`, `high = min(4, 5) = 4`.

### Execution Trace

| Step | `low` | `high` | `px` | `py = 5 - px` | `maxLeftA` | `minRightA` | `maxLeftB` | `minRightB` | Valid? | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `0` | `4` | `2` | `3` | `a[1] = 4` | `a[2] = 8` | `b[2] = 6` | `b[3] = 7` | `4 <= 7` && `6 <= 8` (**Yes!**) | Return `max(4, 6) = 6` |

### Result
- Output: `6`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(\log(\min(N, M)))$
  - Binary search performed on the smaller array size $\min(N, M)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This is Optimal

- Computes $k^{\text{th}}$ element in optimal $\mathcal{O}(\log(\min(N, M)))$ time.
- Uses zero extra memory.

---

## Common Mistakes

1. **Incorrect `low` / `high` Search Space**: Sizing `low = 0` and `high = n` without considering $k$. If $k > m$, `low` MUST be at least $k - m$, otherwise `py` becomes larger than $m$, causing out-of-bounds access!
2. **Missing `std::max(0, k - m)`**: Failing to constrain `low` causes `py = k - px > m` overflow.
