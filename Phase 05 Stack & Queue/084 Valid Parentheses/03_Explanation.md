# Problem Summary

Given a string `s` of parentheses `'()[]{}'`, determine if the input string is valid. The optimal approach uses a **LIFO Stack**. We push opening brackets `(`, `{`, `[` onto the stack. When encountering a closing bracket, we verify that the stack is non-empty and `st.top()` matches the corresponding opening bracket type. If valid, pop `st.top()`. The string is valid if `st.empty()` at the end, running in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to verify **nested structures / matching pairs** in LIFO (Last-In First-Out) order.
- Stack Matching pattern.

---

## Important Clues

1. **"Open brackets must be closed by same type in correct order"**: LIFO matching.
2. **"Single pass O(N) requirement"**: Stack traversal.

---

## Example

### Input
`s = "([])"`

### Visual Step-by-Step Progression

```text
Processing string "([])":

ch = '(' -> Push '('    | ( |
ch = '[' -> Push '['    | [ | ( |
ch = ']' -> Match '['   | ( | (popped '[')
ch = ')' -> Match '('   Empty (popped '(')

Stack empty -> Output: true
```

---

## Alternative Solutions

### String Replacement Loop (Brute Force)
- Repeatedly replace `"()"`, `"{}"`, `"[]"` with `""` using `s.find()` and `s.erase()`.
- **Time Complexity**: $\mathcal{O}(N^2)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **Odd Length String**: `s = "(()"` (len 3) -> Returns `false` via fast-path check.
2. **Starts with Closing Bracket**: `s = ")("` -> Empty stack check returns `false`.
3. **Only Opening Brackets**: `s = "((("` -> Ends with non-empty stack $\implies$ `false`.

---

## Interview Tips

- **Explain Fast-Path Odd Length Guard**: State *"We check `if (s.length() % 2 != 0) return false` immediately, as a valid matching parenthesis expression MUST have an even total number of characters."*

---

## Similar Problems

1. [LeetCode #22: Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
2. [LeetCode #32: Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)
3. [LeetCode #150: Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

---

## Revision Notes

- Problem: Determine if parentheses string `s` is valid.
- Guard: `if (s.length() % 2 != 0) return false`.
- Pattern: Stack (`std::stack<char> st`).
- Loop `char ch` in `s`:
  - `if (opener) st.push(ch)`
  - `else`:
    - `if (st.empty()) return false`
    - `if (matches st.top()) st.pop()`
    - `else return false`
- Return `st.empty()`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(N)$.
