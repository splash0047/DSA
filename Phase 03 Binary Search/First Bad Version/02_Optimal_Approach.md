# First Bad Version - Optimal Approach (Binary Search)

- **Problem Number**: 278
- **Platform**: LeetCode #278
- **Difficulty**: Easy
- **Pattern**: Lower Bound Binary Search

---

## Optimal Intuition

The versions represent a monotonic boolean predicate array `[F, F, ..., F, T, T, ..., T]`. We can find the transition boundary using Binary Search in $\mathcal{O}(\log N)$ API calls.

---

## Code

```cpp
class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1, right = n;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid)) {
                right = mid; // First bad could be mid or to the left
            } else {
                left = mid + 1; // Must be to the right
            }
        }
        return left;
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(\log N)$
- **Space Complexity**: $\mathcal{O}(1)$
