# 030. Longest Repeating Character Replacement

- **Platform**: LeetCode
- **Problem Number**: #424
- **Difficulty**: Medium
- **URL**: [LeetCode #424 - Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

---

## Problem Statement

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return *the length of the longest substring containing the same letter you can get after performing the above operations*.

---

## Examples

### Example 1
```text
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

### Example 2
```text
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'B' in the middle with 'A' to form "AAAA".
The substring "AAAA" has the longest length of 4.
There may exists other ways to achieve this answer too.
```

---

## Constraints

- $1 \le \text{s.length} \le 10^5$
- `s` consists of only uppercase English letters.
- $0 \le k \le \text{s.length}$
