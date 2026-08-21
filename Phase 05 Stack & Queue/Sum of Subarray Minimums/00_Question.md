# Sum of Subarray Minimums

- **Platform**: LeetCode
- **Problem Number**: #907
- **Difficulty**: Medium
- **URL**: [LeetCode #907 - Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/)

---

## Problem Statement

Given an array of integers `arr`, find the sum of `min(b)`, where `b` ranges over every (contiguous) subarray of `arr`. Since the answer may be large, return the answer **modulo $10^9 + 7$**.

---

## Examples

### Example 1
```text
Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
```

---

## Constraints

- $1 \le \text{arr.length} \le 3 \times 10^4$
- $1 \le \text{arr}[i] \le 3 \times 10^4$
