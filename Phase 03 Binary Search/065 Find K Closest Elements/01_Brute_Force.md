# Find K Closest Elements

- **Problem Number**: 658
- **Platform**: LeetCode #658
- **Difficulty**: Medium
- **Pattern**: Custom Sorting

---

## Brute Force Intuition

Sort the entire array `arr` using a custom comparator that ranks elements based on distance $|a - x|$, breaking ties using smaller value ($a < b$). After sorting, take the first $k$ elements and sort them in ascending numerical order.

---

## Algorithm

1. Copy `arr` into `sorted_arr`.
2. Sort `sorted_arr` with custom comparator:
   - `|a - x| < |b - x|` OR (`|a - x| == |b - x|` AND `a < b`).
3. Slice the first `k` elements into `res`.
4. Sort `res` in ascending order.
5. Return `res`.

---

## Code

```cpp
#include <vector>
#include <algorithm>
#include <cmath>

class Solution {
public:
    std::vector<int> findClosestElements(std::vector<int>& arr, int k, int x) {
        std::vector<int> sorted_arr = arr;
        
        std::sort(sorted_arr.begin(), sorted_arr.end(), [x](int a, int b) {
            int distA = std::abs(a - x);
            int distB = std::abs(b - x);
            if (distA == distB) {
                return a < b;
            }
            return distA < distB;
        });
        
        std::vector<int> res(sorted_arr.begin(), sorted_arr.begin() + k);
        std::sort(res.begin(), res.end());
        return res;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log N)$
  - Sorting array of length $N$ takes $\mathcal{O}(N \log N)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Storage for `sorted_arr` and result vector `res`.

---

## Why This Approach Is Not Optimal

Custom sorting takes $\mathcal{O}(N \log N)$ time and ignores the fact that **`arr` is pre-sorted**. Using **Binary Search for Window Left Bound**, we can locate the contiguous $k$-element subarray window directly in logarithmic $\mathcal{O}(\log(N - K) + K)$ time.
