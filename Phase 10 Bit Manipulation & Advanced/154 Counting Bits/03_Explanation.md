# Problem Summary

Generate an array `ans` of length `n + 1` where `ans[i]` is the number of 1-bits in the binary representation of `i`. The optimal approach uses **Bitwise Dynamic Programming**:
- `ans[n + 1]` initialized to `0`.
- Loop `i` from `1` to `n`:
  - `ans[i] = ans[i >> 1] + (i & 1);`
- Return `ans`.
This computes all bit counts in single-pass linear $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ auxiliary space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **compute bit counts for all numbers up to N in linear time**.
- Bitwise Dynamic Programming pattern.

---

## Important Clues

1. **"Single pass O(N) follow-up"**: Dynamic programming reuse of previously shifted bit counts.
2. **"Without using built-in popcount"**: Bit shift recurrence relation.

---

## Example

### Input
`n = 5`

### Visual Step-by-Step Progression

```text
i = 0: 000 -> ans[0] = 0
i = 1: 001 -> ans[1] = ans[0] + 1 = 1
i = 2: 010 -> ans[2] = ans[1] + 0 = 1
i = 3: 011 -> ans[3] = ans[1] + 1 = 2
i = 4: 100 -> ans[4] = ans[2] + 0 = 1
i = 5: 101 -> ans[5] = ans[2] + 1 = 2

Result: [0, 1, 1, 2, 1, 2]
```

---

## Alternative Solutions

### 1. Clearing Lowest Set Bit DP (`ans[i] = ans[i & (i - 1)] + 1`) ($\mathcal{O}(N)$ Time, $\mathcal{O}(1)$ Space)
- Use `ans[i] = ans[i & (i - 1)] + 1`.

### 2. Independent Popcount Loop ($\mathcal{O}(N \log N)$ Time, $\mathcal{O}(1)$ Space)
- Run Brian Kernighan popcount for each number from 0 to $N$.

---

## Edge Cases

1. **`n = 0`**: Returns `[0]`.
2. **`n = 1`**: Returns `[0, 1]`.

---

## Interview Tips

- **Explain Bit Recurrence Relation**: State *"Right-shifting `i` by 1 (`i >> 1`) removes its least significant bit. Because `(i >> 1) < i`, its 1-bit count `ans[i >> 1]` is already calculated. Adding `(i & 1)` (which is 1 if `i` is odd and 0 if even) gives `ans[i]` in $\mathcal{O}(1)$ time."*

---

## Similar Problems

1. [LeetCode #191: Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
2. [LeetCode #190: Reverse Bits](https://leetcode.com/problems/reverse-bits/)
3. [LeetCode #461: Hamming Distance](https://leetcode.com/problems/hamming-distance/)

---

## Revision Notes

- Problem: Count 1-bits for all numbers from 0 to `n`.
- Pattern: Bitwise DP.
- Recurrence: `ans[i] = ans[i >> 1] + (i & 1)`.
- Key Insight: `i >> 1` drops last bit; `i & 1` checks if last bit is 1.
- Optimal Complexity: Time $\mathcal{O}(N)$, Auxiliary Space $\mathcal{O}(1)$.
