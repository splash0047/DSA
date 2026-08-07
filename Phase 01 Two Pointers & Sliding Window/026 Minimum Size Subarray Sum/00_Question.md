# 026. Minimum Size Subarray Sum

- **Platform**: LeetCode
- **Problem Number**: #209
- **Difficulty**: Medium
- **URL**: [LeetCode #209 - Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

---

## Problem Statement

Given an array of positive integers `nums` and a positive integer `target`, return the **minimal length** of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

---

## Examples

### Example 1
```text
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```

### Example 2
```text
Input: target = 4, nums = [1,4,4]
Output: 1
```

### Example 3
```text
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

---

## Constraints

- $1 \le \text{target} \le 10^9$
- $1 \le \text{nums.length} \le 10^5$
- $1 \le \text{nums}[i] \le 10^5$

---

## Follow-up

If you have completed the $\mathcal{O}(N)$ time solution, try coding another solution of which the time complexity is $\mathcal{O}(N \log N)$.
