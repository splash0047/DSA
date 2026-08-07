# Number of 1 Bits

## Pattern Used

- **Pattern**: **Brian Kernighan's Algorithm (`n &= (n - 1)`)**
- **Concept**:
  - Subtracting 1 from a binary number `n - 1` flips all bits from the rightmost set bit (least significant 1-bit) down to the end.
  - Performing Bitwise AND `n &= (n - 1)` clears (turns to 0) the **rightmost set bit** of `n` in a single operation!
  - Loop `while (n > 0)` clearing one set bit at a time and incrementing `count++`.

---

## Observation

1. `n & (n - 1)` clears exactly 1 set bit per operation.
2. The number of iterations of the while loop equals the exact number of 1-bits (Hamming Weight) in `n`.

---

## Intuition

Instead of scanning all 32 binary slots, use the secret identity `n & (n - 1)` to knock out the lowest '1' bit in a single strike. Repeat until all 1s are knocked out.

---

## Algorithm

1. `count = 0`.
2. While `n > 0`:
   - `n &= (n - 1)`. // Clears lowest set bit
   - `count++`.
3. Return `count`.

---

## Clean C++17 Solution

```cpp
#include <cstdint>

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        
        // Brian Kernighan's Algorithm: n & (n - 1) clears the rightmost set bit
        while (n > 0) {
            n &= (n - 1);
            count++;
        }
        
        return count;
    }
};
```

---

## Dry Run

### Input
- `n = 11` (Binary `1011`)

### Execution Trace

- Init: `count = 0`.
- Iteration 1:
  - `n - 1 = 1010`.
  - `n &= (1011 & 1010) = 1010` (8 + 2 = 10).
  - `count = 1`.
- Iteration 2:
  - `n - 1 = 1001`.
  - `n &= (1010 & 1001) = 1000` (8).
  - `count = 2`.
- Iteration 3:
  - `n - 1 = 0111`.
  - `n &= (1000 & 0111) = 0000` (0).
  - `count = 3`.
- `n == 0` loop terminates.

### Result
- Output: `3`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(S)$
  - Where $S$ is the number of set 1-bits in `n` ($S \le 32$).

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This is Optimal

- Runs in $\mathcal{O}(S)$ time proportional ONLY to the number of set bits (e.g. 1 iteration for $n = 128$ instead of 32 iterations).

---

## Common Mistakes

1. **Confusing Bitwise AND with Logical AND**: Writing `n && (n - 1)` instead of `n & (n - 1)`.
2. **Infinite Loop on Negative Signed Integers**: Using signed `int` instead of `uint32_t` can lead to sign-extension issues during right shifts.
