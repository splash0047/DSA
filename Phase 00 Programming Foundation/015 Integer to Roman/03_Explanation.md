# Problem Summary

Convert an integer `num` ($1 \le \text{num} \le 3999$) into a Roman numeral string. Using a **Greedy Table Lookup** with 13 base Roman values (including subtractive combinations `CM`, `CD`, `XC`, `XL`, `IX`, `IV`), we repeatedly subtract the largest possible value and append its symbol in $\mathcal{O}(1)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- Converting an integer into a custom number base or representation.
- Greedy change-making algorithm applies (where greedy choice property holds).

---

## Important Clues

1. **"Maximal value that can be subtracted"**: Directly describes Greedy subtraction.
2. **"6 subtractive forms (IV, IX, XL, XC, CD, CM)"**: Tells you to include these 6 pairs directly in the greedy lookup table.

---

## Example

### Input
`num = 1994`

### Visual Step-by-Step Progression

```text
1994 >= 1000  ->  subtract 1000 ("M"),  remains 994
 994 >=  900  ->  subtract  900 ("CM"), remains  94
  94 >=   90  ->  subtract   90 ("XC"), remains   4
   4 >=    4  ->  subtract    4 ("IV"), remains   0

Result: "MCMXCIV"
```

---

## Alternative Solutions

### Positional Digit Lookup
- Extract thousands, hundreds, tens, and units digits and index into 4 separate 10-element string vectors.
- **Time Complexity**: $\mathcal{O}(1)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **Min Input**: `num = 1` -> Returns `"I"`.
2. **Max Input**: `num = 3999` -> Returns `"MMMCMXCIX"`.
3. **Round Numbers**: `num = 2000` -> Returns `"MM"`.
4. **Subtractive Numbers**: `num = 444` -> Returns `"CDXLIV"`.

---

## Interview Tips

- **Show Why Greedy Works**: Explain that because Roman values include 900, 400, 90, 40, 9, and 4, the coin-change property holds and greedy choice always yields the canonical Roman representation.

---

## Similar Problems

1. [LeetCode #13: Roman to Integer](https://leetcode.com/problems/roman-to-integer/)
2. [LeetCode #273: Integer to English Words](https://leetcode.com/problems/integer-to-english-words/)

---

## Revision Notes

- Problem: Convert integer to Roman numeral string.
- Strategy: Greedy Table Lookup (13 values in descending order).
- Values: `[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]`.
- Symbols: `["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]`.
- While `num >= values[i]`: `result += symbols[i]`, `num -= values[i]`.
- Optimal Complexity: Time $\mathcal{O}(1)$, Space $\mathcal{O}(1)$.
