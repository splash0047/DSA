# Problem Summary

Find the single element in an array `nums` where every other element appears exactly twice. The optimal approach uses **Bitwise XOR Reduction ($A \oplus A = 0$)**:
- Initialize `result = 0`.
- Loop `num` in `nums`:
  - `result ^= num;`
- Return `result`.
Because $A \oplus A = 0$ and $A \oplus 0 = A$, all duplicate numbers cancel out, isolating the single element in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find **a single unique element where all other elements appear in pairs**.
- Bitwise XOR Cancellation pattern.

---

## Important Clues

1. **"Every element appears twice except for one"**: XOR cancellation property.
2. **"Linear time complexity and constant space requirement"**: Single pass bitwise operator.

---

## Example

### Input
`nums = [4, 1, 2, 1, 2]`

### Visual Step-by-Step Progression

```text
Expression: 4 ^ 1 ^ 2 ^ 1 ^ 2
Group terms: (1 ^ 1) ^ (2 ^ 2) ^ 4
Calculates:  0 ^ 0 ^ 4 = 4

Result: 4
```

---

## Alternative Solutions

### Hash Map Frequency Count ($\mathcal{O}(N)$ Time, $\mathcal{O}(N)$ Space)
- Store element frequencies in `unordered_map<int, int>` and return key with frequency 1.

---

## Edge Cases

1. **Single element array**: `nums = [1]` $\implies$ returns `1`.
2. **Negative numbers**: XOR works identically on signed bit representations.

---

## Interview Tips

- **Explain XOR Algebraic Properties**: State *"XOR is commutative and associative ($a \oplus b = b \oplus a$). Since $x \oplus x = 0$ and $x \oplus 0 = x$, XORing all numbers together cancels out all paired numbers, leaving only the single unpaired number in $\mathcal{O}(1)$ space."*

---

## Similar Problems

1. [LeetCode #137: Single Number II](https://leetcode.com/problems/single-number-ii/)
2. [LeetCode #260: Single Number III](https://leetcode.com/problems/single-number-iii/)
3. [LeetCode #268: Missing Number](https://leetcode.com/problems/missing-number/)

---

## Revision Notes

- Problem: Find element appearing once while others appear twice.
- Pattern: Bitwise XOR Reduction.
- Code: `int res = 0; for (int num : nums) res ^= num; return res;`
- Key Property: $x \oplus x = 0$, $x \oplus 0 = x$.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
