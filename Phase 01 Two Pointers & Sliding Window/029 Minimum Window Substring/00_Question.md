# 029. Minimum Window Substring

- **Platform**: LeetCode
- **Problem Number**: #76
- **Difficulty**: Hard
- **URL**: [LeetCode #76 - Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

---

## Problem Statement

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is **unique**.

---

## Examples

### Example 1
```text
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

### Example 2
```text
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

### Example 3
```text
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return "".
```

---

## Constraints

- $m == \text{s.length}$
- $n == \text{t.length}$
- $1 \le m, n \le 10^5$
- `s` and `t` consist of uppercase and lowercase English letters.

---

## Follow-up

Could you find an algorithm that runs in $\mathcal{O}(m + n)$ time?
