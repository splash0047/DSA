# Peak Index in a Mountain Array

- **Problem Number**: 852
- **Platform**: LeetCode #852
- **Difficulty**: Medium
- **Pattern**: Linear Scan for Peak Drop

---

## Brute Force Intuition

Iterate through the array from left to right. The first index `i` where `arr[i] > arr[i + 1]` is the peak of the mountain array.

---

## Algorithm

1. Loop `i` from `0` to `n - 2`:
   a. If `arr[i] > arr[i + 1]`, return `i`.
2. Return `0`.

---

## Code

```cpp
#include <vector>

class Solution {
public:
    int peakIndexInMountainArray(const std::vector<int>& arr) {
        int n = arr.size();
        for (int i = 0; i < n - 1; ++i) {
            if (arr[i] > arr[i + 1]) {
                return i;
            }
        }
        return 0;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass through $N$ elements.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

Linear scan takes $\mathcal{O}(N)$ time. Because mountain arrays strictly increase up to the peak and strictly decrease thereafter, **Binary Search** can find the peak index in logarithmic $\mathcal{O}(\log N)$ time.
