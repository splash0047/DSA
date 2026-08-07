# 116. Sort Array by Increasing Frequency

- **Platform**: LeetCode
- **Problem Number**: #1636
- **Difficulty**: Easy
- **URL**: [LeetCode #1636 - Sort Array by Increasing Frequency](https://leetcode.com/problems/sort-array-by-increasing-frequency/)

---

## Problem Statement

Given an array of integers `nums`, sort the array in **increasing** order based on the frequency of the values. If multiple values have the same frequency, sort them in **decreasing** order.

Return the *sorted array*.

---

## Examples

### Example 1
```text
Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation:
'3' has frequency 1.
'1' has frequency 2.
'2' has frequency 3.
So values are sorted by frequency: 3 (freq 1), 1 (freq 2), 2 (freq 3).
```

### Example 2
```text
Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation:
'1' has frequency 1.
'2' and '3' both have frequency 2.
For same frequency (2), sort in decreasing order of value: 3 comes before 2.
```

### Example 3
```text
Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]
```

---

## Constraints

- $1 \le \text{nums.length} \le 100$
- $-100 \le \text{nums}[i] \le 100$
