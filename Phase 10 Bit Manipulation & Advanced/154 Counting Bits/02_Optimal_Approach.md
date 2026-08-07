# Counting Bits

## Pattern Used

- **Pattern**: **Bitwise Dynamic Programming (`ans[i] = ans[i >> 1] + (i & 1)`)**
- **Concept**:
  - Any integer `i` can be represented as `(i >> 1)` shifted left by 1 bit, plus its least significant bit `(i & 1)`.
  - Right shifting `i >> 1` removes the last bit of `i`. Since `(i >> 1) < i`, its set bit count `ans[i >> 1]` has ALREADY been computed in our DP array!
  - Therefore:
    $$\text{ans}[i] = \text{ans}[i \gg 1] + (i \text{ \& } 1)$$

---

## Observation

1. `i >> 1` (equivalent to $i / 2$) drops the last bit.
2. `i & 1` (equivalent to $i \pmod 2$) checks if the last bit is 1.
3. Combining them allows computing `ans[i]` in $\mathcal{O}(1)$ constant time for every index $i$!

---

## Intuition

If you shift a number right by 1 bit, it becomes a smaller number whose 1-bit count you already calculated. Just look up that smaller number's bit count and add 1 if the original number was odd (had a trailing 1 bit).

---

## Algorithm

1. `ans` vector of size `n + 1` initialized to `0`.
2. Loop `i` from `1` to `n`:
   - `ans[i] = ans[i >> 1] + (i & 1)`.
3. Return `ans`.

---

## Clean C++17 Solution

```cpp
#include <vector>

class Solution {
public:
    std::vector<int> countBits(int n) {
        // ans[i] stores number of 1-bits in integer i
        std::vector<int> ans(n + 1, 0);
        
        // DP Bitwise Transition: ans[i] = ans[i >> 1] + (i & 1)
        for (int i = 1; i <= n; ++i) {
            ans[i] = ans[i >> 1] + (i & 1);
        }
        
        return ans;
    }
};
```

---

## Dry Run

### Input
- `n = 5`

### Execution Trace

- `ans[0] = 0`.
- `i = 1`: `ans[1] = ans[0] + 1 = 1`.
- `i = 2`: `ans[2] = ans[1] + 0 = 1`.
- `i = 3`: `ans[3] = ans[1] + 1 = 2`.
- `i = 4`: `ans[4] = ans[2] + 0 = 1`.
- `i = 5`: `ans[5] = ans[2] + 1 = 2`.

### Result
- Output: `[0, 1, 1, 2, 1, 2]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass loop from `1` to `N` doing $\mathcal{O}(1)$ operations per element.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space (excluding output array `ans`).

---

## Why This is Optimal

- Meets the follow-up requirement: computes bit counts for all numbers up to $n$ in a single pass in linear $\mathcal{O}(N)$ time.

---

## Common Mistakes

1. **Operator Precedence Error**: Writing `ans[i >> 1] + i & 1` without parentheses around `(i & 1)` (due to `+` taking precedence over `&`).
2. **Off-by-One Array Size**: Allocating array of size `n` instead of `n + 1`.
