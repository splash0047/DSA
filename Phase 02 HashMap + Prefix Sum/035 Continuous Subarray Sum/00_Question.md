# 035. Continuous Subarray Sum

- **Platform**: LeetCode
- **Problem Number**: #523
- **Difficulty**: Medium
- **URL**: [LeetCode #523 - Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)

---

## Problem Statement

Given an integer array `nums` and an integer `k`, return `true` *if `nums` has a **good subarray**, or `false` otherwise*.

A **good subarray** is a subarray where:
- Its length is **at least two**, and
- The sum of the elements of the subarray is a **multiple of `k`**.

Note that:
- A **subarray** is a contiguous part of the array.
- An integer `x` is a multiple of `k` if there exists an integer `n` such that $x = n \times k$. `0` is **always** a multiple of `k`.

---

## Examples

### Example 1
```text
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose sum is 6.
```

### Example 2
```text
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose sum is 42.
42 is a multiple of 6 because 42 = 7 * 6.
```

### Example 3
```text
Input: nums = [23,2,6,4,7], k = 13
Output: false
```

---

## Constraints

- $1 \le \text{nums.length} \le 10^5$
- $0 \le \text{nums}[i] \le 10^9$
- $0 \le \text{sum}(\text{nums}[i]) \le 2^{31} - 1$
- $1 \le k \le 2^{31} - 1$
