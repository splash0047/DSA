# 033. Subarray Sum Equals K

- **Platform**: LeetCode
- **Problem Number**: #560
- **Difficulty**: Medium
- **URL**: [LeetCode #560 - Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

---

## Problem Statement

Given an array of integers `nums` and an integer `k`, return *the total number of subarrays whose sum equals to `k`*.

A subarray is a contiguous non-empty sequence of elements within an array.

---

## Examples

### Example 1
```text
Input: nums = [1,1,1], k = 2
Output: 2
Explanation: Subarrays [1,1] starting at index 0 and index 1 sum up to 2.
```

### Example 2
```text
Input: nums = [1,2,3], k = 3
Output: 2
Explanation: Subarrays [1,2] and [3] sum up to 3.
```

---

## Constraints

- $1 \le \text{nums.length} \le 2 \times 10^4$
- $-1000 \le \text{nums}[i] \le 1000$
- $-10^7 \le k \le 10^7$
