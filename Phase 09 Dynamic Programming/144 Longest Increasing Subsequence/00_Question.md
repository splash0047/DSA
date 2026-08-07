# 144. Longest Increasing Subsequence

- **Platform**: LeetCode
- **Problem Number**: #300
- **Difficulty**: Medium
- **URL**: [LeetCode #300 - Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

---

## Problem Statement

Given an integer array `nums`, return *the length of the longest **strictly increasing subsequence***.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

---

## Examples

### Example 1
```text
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

### Example 2
```text
Input: nums = [0,1,0,3,2,3]
Output: 4
```

### Example 3
```text
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

---

## Constraints

- $1 \le \text{nums.length} \le 2500$
- $-10^4 \le \text{nums}[i] \le 10^4$

---

## Follow-up

Can you come up with an algorithm that runs in $\mathcal{O}(N \log N)$ time complexity?
