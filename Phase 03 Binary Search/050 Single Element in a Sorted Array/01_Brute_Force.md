# Single Element in a Sorted Array

- **Problem Number**: 540
- **Platform**: LeetCode #540
- **Difficulty**: Medium
- **Pattern**: Bitwise XOR / Linear Scan

---

## Brute Force Intuition

Use Bitwise XOR operator (`^`). Since $x \oplus x = 0$ and $x \oplus 0 = x$, XORing all numbers in `nums` causes all paired duplicates to cancel out to `0`, leaving only the single unique element.

---

## Algorithm

1. `ans = 0`.
2. For each `x` in `nums`:
   - `ans ^= x`.
3. Return `ans`.

---

## Code

```cpp
#include <vector>

class Solution {
public:
    int singleNonDuplicate(const std::vector<int>& nums) {
        int ans = 0;
        for (int x : nums) {
            ans ^= x;
        }
        return ans;
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

XOR linear scan takes $\mathcal{O}(N)$ time. The problem statement mandates an $\mathcal{O}(\log N)$ time solution. Using **Binary Search on Index Parity**, we can locate the single element in logarithmic $\mathcal{O}(\log N)$ time.
