# Problem Summary

Count the number of set bits (1s) in the binary representation of integer `n`. The optimal approach uses **Brian Kernighan's Algorithm (`n &= (n - 1)`)**:
- `count = 0`.
- While `n > 0`:
  - `n &= (n - 1);` (clears the rightmost set bit in 1 step)
  - `count++;`
- Return `count`.
This calculates Hamming Weight in $\mathcal{O}(S)$ time (where $S$ is number of 1-bits) and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **count set bits / clear lowest set bit**.
- Brian Kernighan Bit Manipulation pattern.

---

## Important Clues

1. **"Number of set bits (Hamming weight)"**: Bit count pattern.
2. **"Optimize loop iterations"**: `n &= (n - 1)` clears lowest set bit.

---

## Example

### Input
`n = 11` (Binary `1011`)

### Visual Step-by-Step Progression

```text
1011 (11) -> n & (n - 1) -> 1010 (10) [count = 1]
1010 (10) -> n & (n - 1) -> 1000 (8)  [count = 2]
1000 (8)  -> n & (n - 1) -> 0000 (0)  [count = 3]

Result: 3
```

---

## Alternative Solutions

### 1. Standard Shift Loop ($\mathcal{O}(32)$ Time, $\mathcal{O}(1)$ Space)
- Check `n & 1` and right shift `n >>= 1` 32 times.

### 2. Built-in Compiler Intrinsic ($\mathcal{O}(1)$ Time, $\mathcal{O}(1)$ Space)
- Return `__builtin_popcount(n)` in GCC / Clang.

---

## Edge Cases

1. **Power of 2**: `n = 16` (`10000`) $\implies$ loop runs 1 time, returns `1`.
2. **All 1s**: `n = 4294967295` (`1111...1111`) $\implies$ loop runs 32 times, returns `32`.

---

## Interview Tips

- **Explain Why `n & (n - 1)` Clears Lowest 1-Bit**: State *"Subtracting 1 flips the rightmost set bit from 1 to 0 and turns all trailing 0s into 1s. Performing Bitwise AND with original `n` zeros out that rightmost set bit without altering any higher bits."*

---

## Similar Problems

1. [LeetCode #338: Counting Bits](https://leetcode.com/problems/counting-bits/)
2. [LeetCode #231: Power of Two](https://leetcode.com/problems/power-of-two/)
3. [LeetCode #190: Reverse Bits](https://leetcode.com/problems/reverse-bits/)

---

## Revision Notes

- Problem: Count set 1-bits in integer `n`.
- Pattern: Brian Kernighan's Algorithm.
- Code: `while (n > 0) { n &= (n - 1); count++; }`
- Key Operation: `n &= (n - 1)` clears lowest set bit.
- Optimal Complexity: Time $\mathcal{O}(S)$, Space $\mathcal{O}(1)$.
