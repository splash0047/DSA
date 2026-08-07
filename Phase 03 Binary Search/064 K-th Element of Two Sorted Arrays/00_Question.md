# 064. K-th Element of Two Sorted Arrays

- **Platform**: GeeksforGeeks
- **Problem Number**: GFG "K-th Element of Two Sorted Arrays"
- **Difficulty**: Medium
- **URL**: [GeeksforGeeks - K-th Element of Two Sorted Arrays](https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-arrays1370/1)

---

## Problem Statement

Given two sorted arrays `a` and `b` of size `n` and `m` respectively and an element `k`. The task is to find the element that would be at the $k^{\text{th}}$ position of the combined sorted array.

The overall run time complexity should be $\mathcal{O}(\log(n + m))$.

---

## Examples

### Example 1
```text
Input: a = [2, 3, 6, 7, 9], b = [1, 4, 8, 10], k = 5
Output: 6
Explanation: The final combined sorted array would be [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element of this array is 6.
```

### Example 2
```text
Input: a = [100, 112, 256, 349, 770], b = [72, 86, 113, 119, 265, 445, 892], k = 7
Output: 256
Explanation: Combined sorted array = [72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892]. The 7th element is 256.
```

---

## Constraints

- $1 \le a.\text{length}, b.\text{length} \le 10^6$
- $1 \le a[i], b[i] \le 10^9$
- $1 \le k \le a.\text{length} + b.\text{length}$
