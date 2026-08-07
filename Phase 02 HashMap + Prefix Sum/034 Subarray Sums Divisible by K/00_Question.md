# 034. Subarray Sums Divisible by K

- **Platform**: LeetCode
- **Problem Number**: #974
- **Difficulty**: Medium
- **URL**: [LeetCode #974 - Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/)

---

## Problem Statement

Given an integer array `nums` and an integer `k`, return *the number of non-empty subarrays that have a sum divisible by `k`*.

A **subarray** is a contiguous part of an array.

---

## Examples

### Example 1
```text
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays having a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
```

### Example 2
```text
Input: nums = [5], k = 9
Output: 0
```

---

## Constraints

- $1 \le \text{nums.length} \le 3 \times 10^4$
- $-10^4 \le \text{nums}[i] \le 10^4$
- $2 \le k \le 10^4$
