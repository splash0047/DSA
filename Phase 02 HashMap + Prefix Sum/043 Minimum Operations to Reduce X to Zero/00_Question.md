# 043. Minimum Operations to Reduce X to Zero

- **Platform**: LeetCode
- **Problem Number**: #1658
- **Difficulty**: Medium
- **URL**: [LeetCode #1658 - Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/)

---

## Problem Statement

You are given an integer array `nums` and an integer `x`. In one operation, you can remove either the **leftmost** or the **rightmost** element from the array `nums` and subtract its value from `x`. Note that this modifies the array for future operations.

Return *the **minimum number of operations** required to reduce `x` to **exactly** `0` if it is possible, otherwise, return `-1`*.

---

## Examples

### Example 1
```text
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to 0 (3 then 2).
Number of operations = 2.
```

### Example 2
```text
Input: nums = [5,6,7,8,9], x = 4
Output: -1
```

### Example 3
```text
Input: nums = [3,2,2,0,4,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and first two elements (3, 4, 0, then 3, 2).
Total operations = 5.
```

---

## Constraints

- $1 \le \text{nums.length} \le 10^5$
- $1 \le \text{nums}[i] \le 10^4$
- $1 \le x \le 10^9$
