# 057. Split Array Largest Sum

- **Platform**: LeetCode
- **Problem Number**: #410
- **Difficulty**: Hard
- **URL**: [LeetCode #410 - Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)

---

## Problem Statement

Given an integer array `nums` and an integer `k`, split `nums` into `k` non-empty subarrays such that the largest sum among these `k` subarrays is **minimized**.

Return *the minimized largest sum of the split*.

A **subarray** is a contiguous part of the array.

---

## Examples

### Example 1
```text
Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
```

### Example 2
```text
Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
```

---

## Constraints

- $1 \le \text{nums.length} \le 1000$
- $0 \le \text{nums}[i] \le 10^6$
- $1 \le k \le \min(50, \text{nums.length})$
