# Single Number

## Pattern Used

- **Pattern**: **Bitwise XOR Reduction ($A \oplus A = 0, A \oplus 0 = A$)**
- **Concept**:
  - The Bitwise XOR operator ($\oplus$) has key algebraic properties:
    1. **Self-inverse**: $x \oplus x = 0$ (any number XORed with itself cancels out).
    2. **Identity element**: $x \oplus 0 = x$.
    3. **Commutative & Associative**: $a \oplus b \oplus a = (a \oplus a) \oplus b = 0 \oplus b = b$.
  - By XORing all elements in `nums` together, all duplicate pairs cancel each other out to `0`, leaving ONLY the single element!

---

## Observation

1. $4 \oplus 1 \oplus 2 \oplus 1 \oplus 2 = (1 \oplus 1) \oplus (2 \oplus 2) \oplus 4 = 0 \oplus 0 \oplus 4 = 4$.
2. XOR reduction operates in a single pass without allocating any extra memory!

---

## Intuition

XOR is like a toggle switch. If you toggle the switch twice for the same number, it returns to its original state (cancels out). Toggling every number in the array leaves only the number that was toggled once.

---

## Algorithm

1. `result = 0`.
2. For each `num` in `nums`:
   - `result ^= num`.
3. Return `result`.

---

## Clean C++17 Solution

```cpp
#include <vector>

class Solution {
public:
    int singleNumber(std::vector<int>& nums) {
        int result = 0;
        
        // XOR all elements in the array
        for (int num : nums) {
            result ^= num;
        }
        
        return result;
    }
};
```

---

## Dry Run

### Input
- `nums = [4, 1, 2, 1, 2]`

### Execution Trace

- `result = 0`.
- `num = 4`: `result = 0 ^ 4 = 4`.
- `num = 1`: `result = 4 ^ 1 = 5`.
- `num = 2`: `result = 5 ^ 2 = 7`.
- `num = 1`: `result = 7 ^ 1 = 6`.
- `num = 2`: `result = 6 ^ 2 = 4`.

### Result
- Output: `4`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single loop through `nums` array of size $N$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space (`result` integer variable).

---

## Why This is Optimal

- Meets all strict problem constraints: linear $\mathcal{O}(N)$ time and optimal constant $\mathcal{O}(1)$ space.

---

## Common Mistakes

1. **Initializing Result to 1 Instead of 0**: Initializing `result = 1` flips the bit representation. XOR identity element is `0`.
2. **Using Addition/Subtraction**: Attempting `sum - 2*duplicates` requires auxiliary storage or set insertion.
