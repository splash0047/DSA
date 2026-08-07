# Counting Bits

- **Problem Number**: 338
- **Platform**: LeetCode #338
- **Difficulty**: Easy
- **Pattern**: Independent Popcount Loop per Integer

---

## Brute Force Intuition

For each integer `i` from `0` to `n`, run a separate bit counting function (like Brian Kernighan's algorithm `x &= (x - 1)` or built-in `__builtin_popcount`) to calculate the number of set 1-bits independently. Append the result to `ans[i]`.

---

## Algorithm

1. `ans` vector of size `n + 1`.
2. For `i` from `0` to `n`:
   - `temp = i`, `count = 0`.
   - While `temp > 0`:
     - `temp &= (temp - 1)`.
     - `count++`.
   - `ans[i] = count`.
3. Return `ans`.

---

## Code

```cpp
#include <vector>

class Solution {
private:
    int popcount(int x) {
        int count = 0;
        while (x > 0) {
            x &= (x - 1);
            count++;
        }
        return count;
    }

public:
    std::vector<int> countBits(int n) {
        std::vector<int> ans(n + 1);
        for (int i = 0; i <= n; ++i) {
            ans[i] = popcount(i);
        }
        return ans;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log N)$
  - Outer loop runs $N + 1$ times, inner popcount takes $\mathcal{O}(\log i)$ per number.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space (excluding output array `ans`).

---

## Why This Approach Is Not Optimal

Recomputing set bits for every number independently takes $\mathcal{O}(N \log N)$ time. Using **Dynamic Programming Bit Relation (`ans[i] = ans[i >> 1] + (i & 1)`)**, we can compute all bit counts in single-pass linear $\mathcal{O}(N)$ time!
