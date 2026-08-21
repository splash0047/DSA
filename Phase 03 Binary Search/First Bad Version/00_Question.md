# First Bad Version

- **Platform**: LeetCode
- **Problem Number**: #278
- **Difficulty**: Easy
- **URL**: [LeetCode #278 - First Bad Version](https://leetcode.com/problems/first-bad-version/)

---

## Problem Statement

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

---

## Examples

### Example 1
```text
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
```

---

## Constraints

- $1 \le \text{bad} \le n \le 2^{31} - 1$
