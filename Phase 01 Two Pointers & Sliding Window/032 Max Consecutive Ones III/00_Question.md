# 032. Max Consecutive Ones III

- **Platform**: LeetCode
- **Problem Number**: #1004
- **Difficulty**: Medium
- **URL**: [LeetCode #1004 - Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)

---

## Problem Statement

Given a binary array `nums` and an integer `k`, return *the maximum number of consecutive `1`s in the array if you can flip at most `k` `0`s*.

---

## Examples

### Example 1
```text
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bold numbers were flipped from 0 to 1. The longest subarray is underlined.
Max length = 6.
```

### Example 2
```text
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bold numbers were flipped from 0 to 1. The longest subarray is underlined.
Max length = 10.
```

---

## Constraints

- $1 \le \text{nums.length} \le 10^5$
- `nums[i]` is either `0` or `1`.
- $0 \le k \le \text{nums.length}$
