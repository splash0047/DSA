# Decode String

- **Platform**: LeetCode
- **Problem Number**: #394
- **Difficulty**: Medium
- **URL**: [LeetCode #394 - Decode String](https://leetcode.com/problems/decode-string/)

---

## Problem Statement

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

---

## Examples

### Example 1
```text
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
```

### Example 2
```text
Input: s = "3[a2[c]]"
Output: "accaccacc"
```

### Example 3
```text
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

---

## Constraints

- $1 \le \text{s.length} \le 30$
- `s` consists of lowercase English letters, digits, and square brackets `'['`, `']'`.
- `s` is guaranteed to be **a valid input**.
