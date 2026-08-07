# Contains Duplicate

- **Problem Number**: 217
- **Platform**: LeetCode #217
- **Difficulty**: Easy
- **Pattern**: Nested Loops / Pairwise Comparison

---

## Brute Force Intuition

To determine if any element appears at least twice in an array, the simplest approach is to check every possible pair of elements. If we find any pair of indices $(i, j)$ with $i \neq j$ where `nums[i] == nums[j]`, we immediately know the array contains duplicates.

---

## Algorithm

1. Loop `i` from `0` to `n - 2`.
2. Loop `j` from `i + 1` to `n - 1`.
3. If `nums[i] == nums[j]`, return `true`.
4. If loops finish without finding matching elements, return `false`.

---

## Code

```cpp
#include <vector>

class Solution {
public:
    bool containsDuplicate(const std::vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n - 1; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (nums[i] == nums[j]) {
                    return true;
                }
            }
        }
        return false;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - We compare $\frac{N(N-1)}{2}$ pairs in the worst case.
  - For $N = 10^5$, this results in $\sim 5 \times 10^9$ operations, causing TLE.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Operates directly on the input array using constant auxiliary memory.

---

## Why This Approach Is Not Optimal

Comparing every element against all subsequent elements takes $\mathcal{O}(N^2)$ time. We can reduce the search time by either sorting the array ($\mathcal{O}(N \log N)$) or trading space for time using a Hash Set ($\mathcal{O}(N)$).
