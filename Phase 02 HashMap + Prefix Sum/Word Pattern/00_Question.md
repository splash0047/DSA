# Word Pattern

- **Platform**: LeetCode
- **Problem Number**: #290
- **Difficulty**: Easy
- **URL**: [LeetCode #290 - Word Pattern](https://leetcode.com/problems/word-pattern/)

---

## Problem Statement

Given a `pattern` and a string `s`, find if `s` follows the same pattern.

Here **follow** means a full match, such that there is a bijection between a letter in `pattern` and a **non-empty** word in `s`.

---

## Examples

### Example 1
```text
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
```

### Example 2
```text
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
```

### Example 3
```text
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
```

---

## Constraints

- $1 \le \text{pattern.length} \le 300$
- `pattern` contains only lower-case English letters.
- $1 \le \text{s.length} \le 3000$
- `s` contains only lowercase English letters and spaces `' '`.
- `s` does not contain any leading or trailing spaces.
- All the words in `s` are separated by a single space.
