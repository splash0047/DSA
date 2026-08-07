# Kth Smallest Element in an Array

- **Problem Number**: 114
- **Platform**: GeeksForGeeks / LeetCode
- **Difficulty**: Medium
- **Pattern**: Full Array Sorting

---

## Brute Force Intuition

Sort the entire array in non-decreasing order. In a sorted array, the $1^{st}$ smallest element is at index `0`, the $2^{nd}$ smallest is at index `1`, and the $k^{th}$ smallest element is located at 0-based index `k - 1`.

---

## Algorithm

1. Sort the input array `arr` using `std::sort`.
2. Return `arr[k - 1]`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int kthSmallest(std::vector<int>& arr, int k) {
        std::sort(arr.begin(), arr.end());
        return arr[k - 1];
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log N)$
  - Sorting an array of $N$ elements takes $\mathcal{O}(N \log N)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(\log N)$
  - Auxiliary stack space consumed by `std::sort`.

---

## Why This Approach Is Not Optimal

Sorting orders all $N$ elements unnecessarily when we only require the single element at index $k - 1$. Using a **Max-Heap** of size $k$, we can find the $k^{th}$ smallest element in $\mathcal{O}(N \log k)$ time and $\mathcal{O}(k)$ space.
