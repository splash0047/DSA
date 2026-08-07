# 065. Find K Closest Elements

- **Platform**: LeetCode
- **Problem Number**: #658
- **Difficulty**: Medium
- **URL**: [LeetCode #658 - Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)

---

## Problem Statement

Given a **sorted** integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order.

An integer `a` is closer to `x` than an integer `b` if:
- `|a - x| < |b - x|`, or
- `|a - x| == |b - x|` and `a < b`

---

## Examples

### Example 1
```text
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
```

### Example 2
```text
Input: arr = [1,1,2,3,4,5], k = 4, x = -1
Output: [1,1,2,3]
```

---

## Constraints

- $1 \le k \le \text{arr.length}$
- $1 \le \text{arr.length} \le 10^4$
- `arr` is sorted in **ascending** order.
- $-10^4 \le \text{arr}[i], x \le 10^4$
