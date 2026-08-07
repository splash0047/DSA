# 038. Product of Array Except Self

- **Platform**: LeetCode
- **Problem Number**: #238
- **Difficulty**: Medium
- **URL**: [LeetCode #238 - Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

---

## Problem Statement

Given an integer array `nums`, return *an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`*.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in $\mathcal{O}(n)$ time and without using the division operation.

---

## Examples

### Example 1
```text
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

### Example 2
```text
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

---

## Constraints

- $2 \le \text{nums.length} \le 10^5$
- $-30 \le \text{nums}[i] \le 30$
- The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

---

## Follow-up

Can you solve the problem in $\mathcal{O}(1)$ extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)
