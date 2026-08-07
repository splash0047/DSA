# Problem Summary

Convert a valid Roman numeral string `s` into its equivalent integer value. Using a **Single Pass with Lookahead Comparison**, if a symbol's value is less than the next symbol's value (e.g. `I` before `V`), we subtract its value; otherwise we add it. This parses Roman numbers in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- Parsing positional or subtractive notation systems.
- Comparing current character against next character (`lookahead`) to determine additive vs subtractive operations.

---

## Important Clues

1. **"Roman numerals are written largest to smallest"**: Standard addition rule.
2. **"6 subtractive cases (IV, IX, XL, XC, CD, CM)"**: Occurs whenever `value[i] < value[i+1]`.

---

## Example

### Input
`s = "MCMXCIV"`

### Visual Step-by-Step Progression

```text
M (1000 >= 100)  ->  + 1000  = 1000
C ( 100 < 1000)  ->  -  100  =  900
M (1000 >=  10)  ->  + 1000  = 1900
X (  10 <  100)  ->  -   10  = 1890
C ( 100 >=   1)  ->  +  100  = 1990
I (   1 <    5)  ->  -    1  = 1989
V (   5 >=   0)  ->  +    5  = 1994
```

---

## Alternative Solutions

### Right-to-Left Traversal
- Traverse string from right to left (index $N-1$ down to $0$).
- Track `max_seen_value`.
- If `current < max_seen_value`: subtract `current`.
- Else: add `current` and update `max_seen_value = current`.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **Single Symbol**: `s = "I"` -> Returns `1`.
2. **All Additive**: `s = "III"` -> Returns `3`.
3. **Subtractive Only**: `s = "IV"` -> Returns `4`.
4. **Max Value Input**: `s = "MMMCMXCIX"` -> Returns `3999`.

---

## Interview Tips

- **Prefer `switch` over Hash Map**: Mention that `switch` statement in C++ executes faster and avoids dynamic memory allocation compared to `std::unordered_map`.
- **Explain Subtraction Rule Cleanly**: Summarize as: *"If current value is less than next value, subtract; otherwise add."*

---

## Similar Problems

1. [LeetCode #12: Integer to Roman](https://leetcode.com/problems/integer-to-roman/)
2. [LeetCode #273: Integer to English Words](https://leetcode.com/problems/integer-to-english-words/)

---

## Revision Notes

- Problem: Convert Roman numeral string to integer.
- Lookahead rule: Compare `getValue(s[i])` vs `getValue(s[i+1])`.
- If `current < next`: `total -= current`.
- Else: `total += current`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
