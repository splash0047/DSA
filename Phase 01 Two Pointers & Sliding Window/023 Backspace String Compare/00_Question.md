# 023. Backspace String Compare

- **Platform**: LeetCode
- **Problem Number**: #844
- **Difficulty**: Easy
- **URL**: [LeetCode #844 - Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)

---

## Problem Statement

Given two strings `s` and `t`, return `true` *if they are equal when both are typed into empty text editors*. `'#'` means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

---

## Examples

### Example 1
```text
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
```

### Example 2
```text
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
```

### Example 3
```text
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
```

---

## Constraints

- $1 \le \text{s.length}, \text{t.length} \le 200$
- `s` and `t` consist of lowercase letters and `'#'` characters.

---

## Follow-up

Can you solve it in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space?
