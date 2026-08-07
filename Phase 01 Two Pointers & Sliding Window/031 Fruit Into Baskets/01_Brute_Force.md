# Fruit Into Baskets

- **Problem Number**: 904
- **Platform**: LeetCode #904
- **Difficulty**: Medium
- **Pattern**: Nested Loops Subarray Check

---

## Brute Force Intuition

The problem asks for the maximum number of fruits we can pick using 2 baskets. This is mathematically equivalent to: **Find the length of the longest contiguous subarray containing at most 2 distinct integers**.

The brute-force approach checks every possible subarray `fruits[i ... j]`, counts the number of distinct fruit types using a `std::unordered_set`, and tracks the maximum length `j - i + 1` among all subarrays containing $\le 2$ distinct fruit types.

---

## Algorithm

1. `max_len = 0`.
2. Outer loop `i` from `0` to `n - 1`.
3. Inner loop `j` from `i` to `n - 1`:
   a. Insert `fruits[j]` into `seen` set.
   b. If `seen.size() > 2`: break inner loop.
   c. `max_len = max(max_len, j - i + 1)`.
4. Return `max_len`.

---

## Code

```cpp
#include <vector>
#include <unordered_set>
#include <algorithm>

class Solution {
public:
    int totalFruit(const std::vector<int>& fruits) {
        int max_len = 0;
        int n = fruits.size();
        
        for (int i = 0; i < n; ++i) {
            std::unordered_set<int> types;
            for (int j = i; j < n; ++j) {
                types.insert(fruits[j]);
                if (types.size() > 2) {
                    break;
                }
                max_len = std::max(max_len, j - i + 1);
            }
        }
        
        return max_len;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - Double loop takes $\mathcal{O}(N^2)$ time in worst case.
  - For $N = 10^5$, causes TLE.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Set holds at most 3 elements.

---

## Why This Approach Is Not Optimal

Nested loops re-inspect overlapping subarrays from scratch. A **Variable-Size Sliding Window (Hash Map Count)** allows tracking fruit frequencies dynamically in $\mathcal{O}(1)$ per step, reducing total time complexity to linear $\mathcal{O}(N)$.
