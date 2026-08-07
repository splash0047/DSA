# 028. Find All Anagrams in a String

- **Platform**: LeetCode
- **Problem Number**: #438
- **Difficulty**: Medium
- **URL**: [LeetCode #438 - Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

---

## Problem Statement

Given two strings `s` and `p`, return *an array of all the start indices of `p`'s anagrams in `s`*. You may return the answer in **any order**.

---

## Examples

### Example 1
```text
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

### Example 2
```text
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

---

## Constraints

- $1 \le \text{s.length}, \text{p.length} \le 3 \times 10^4$
- `s` and `p` consist of lowercase English letters.
