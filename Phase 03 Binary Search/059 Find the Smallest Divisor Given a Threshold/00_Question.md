# 059. Find the Smallest Divisor Given a Threshold

- **Platform**: LeetCode
- **Problem Number**: #1283
- **Difficulty**: Medium
- **URL**: [LeetCode #1283 - Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/)

---

## Problem Statement

Given an array of integers `nums` and an integer `threshold`, we will choose a positive integer `divisor`, divide all the array by it, and sum the division's result. Find the **smallest** `divisor` such that the result mentioned above is less than or equal to `threshold`.

Each result of division is rounded to the nearest integer greater than or equal to that element. (For example: $7/3 = 3$ and $10/2 = 5$).

The test cases are generated such that there will be an answer.

---

## Examples

### Example 1
```text
Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to be 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum of 7 (1+1+2+3). 
If the divisor is 5 the sum will be 5 (1+1+1+2). 
```

### Example 2
```text
Input: nums = [44,22,33,11,1], threshold = 5
Output: 44
```

---

## Constraints

- $1 \le \text{nums.length} \le 5 \times 10^4$
- $1 \le \text{nums}[i] \le 10^6$
- $\text{nums.length} \le \text{threshold} \le 10^6$
