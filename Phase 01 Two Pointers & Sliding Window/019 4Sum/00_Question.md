# 019. 4Sum

- **Platform**: LeetCode
- **Problem Number**: #18
- **Difficulty**: Medium
- **URL**: [LeetCode #18 - 4Sum](https://leetcode.com/problems/4sum/)

---

## Problem Statement

Given an array `nums` of `n` integers, return an array of all the **unique** quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:

- $0 \le a, b, c, d < n$
- $a, b, c,$ and $d$ are **distinct**.
- $\text{nums}[a] + \text{nums}[b] + \text{nums}[c] + \text{nums}[d] == \text{target}$

You may return the answer in **any order**.

---

## Examples

### Example 1
```text
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

### Example 2
```text
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
```

---

## Constraints

- $1 \le \text{nums.length} \le 200$
- $-10^9 \le \text{nums}[i] \le 10^9$
- $-10^9 \le \text{target} \le 10^9$
