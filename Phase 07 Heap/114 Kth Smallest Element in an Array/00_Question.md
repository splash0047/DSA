# 114. Kth Smallest Element in an Array

- **Platform**: GeeksForGeeks / LeetCode
- **Difficulty**: Medium
- **URL**: [GeeksForGeeks - Kth Smallest Element](https://www.geeksforgeeks.org/problems/kth-smallest-element5615/1)

---

## Problem Statement

Given an array `arr[]` and an integer `k` where `k` is smaller than the size of the array, the task is to find the $k^{th}$ **smallest** element in the given array.

It is given that all array elements are distinct.

---

## Examples

### Example 1
```text
Input: arr = [7, 10, 4, 3, 20, 15], k = 3
Output: 7
Explanation: 3rd smallest element is 7 (sorted order: 3, 4, 7, 10, 15, 20).
```

### Example 2
```text
Input: arr = [7, 10, 4, 20, 15], k = 4
Output: 15
Explanation: 4th smallest element is 15.
```

---

## Constraints

- $1 \le k \le \text{arr.length} \le 10^5$
- $1 \le \text{arr}[i] \le 10^5$
- All elements are distinct.
