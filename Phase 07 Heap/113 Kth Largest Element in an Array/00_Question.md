# 113. Kth Largest Element in an Array

- **Platform**: LeetCode
- **Problem Number**: #215
- **Difficulty**: Medium
- **URL**: [LeetCode #215 - Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

---

## Problem Statement

Given an integer array `nums` and an integer `k`, return *the* $k^{th}$ *largest element in the array*.

Note that it is the $k^{th}$ largest element in the sorted order, not the $k^{th}$ distinct element.

Can you solve it without sorting?

---

## Examples

### Example 1
```text
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

### Example 2
```text
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

---

## Constraints

- $1 \le k \le \text{nums.length} \le 10^5$
- $-10^4 \le \text{nums}[i] \le 10^4$
