# 037. Maximum Size Subarray Sum Equals k

- **Platform**: LeetCode / GeeksforGeeks
- **Problem Number**: LeetCode #325 (Premium) / GFG "Longest Sub-Array with Sum K"
- **Difficulty**: Medium
- **URL**: [LeetCode #325 - Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/)

---

## Problem Statement

Given an integer array `nums` and an integer `k`, return the **maximum length** of a subarray that sums to `k`. If there is not one, return `0` instead.

---

## Examples

### Example 1
```text
Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest (length 4).
```

### Example 2
```text
Input: nums = [-2, -1, 2, 1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest (length 2).
```

---

## Constraints

- $1 \le \text{nums.length} \le 2 \times 10^5$
- $-10^4 \le \text{nums}[i] \le 10^4$
- $-10^9 \le k \le 10^9$
