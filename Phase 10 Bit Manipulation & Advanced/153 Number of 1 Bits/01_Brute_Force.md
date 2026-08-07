# Number of 1 Bits

- **Problem Number**: 191
- **Platform**: LeetCode #191
- **Difficulty**: Easy
- **Pattern**: Bit Shift & Bitwise AND Loop

---

## Brute Force Intuition

Iterate through all 32 bit positions of integer `n`. Check if the least significant bit is set (`n & 1`). Right shift `n` by 1 (`n >>= 1`) at each step and repeat 32 times.

---

## Algorithm

1. `count = 0`.
2. While `n > 0`:
   - `count += (n & 1)`.
   - `n >>= 1`.
3. Return `count`.

---

## Code

```cpp
#include <cstdint>

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        while (n > 0) {
            count += (n & 1);
            n >>= 1;
        }
        return count;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(K)$
  - Where $K = 32$ is total number of bits in integer `n`. Iterates up to 32 times regardless of set bits count.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant extra space.

---

## Why This Approach Is Not Optimal

Iterating through 0-bits takes 32 checks every time. Using **Brian Kernighan's Bit Clearing Algorithm (`n &= (n - 1)`)**, the loop runs ONLY as many times as there are set 1-bits in `n`!
