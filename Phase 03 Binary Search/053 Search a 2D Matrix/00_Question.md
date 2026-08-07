# 053. Search a 2D Matrix

- **Platform**: LeetCode
- **Problem Number**: #74
- **Difficulty**: Medium
- **URL**: [LeetCode #74 - Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

---

## Problem Statement

You are given an `m x n` integer matrix `matrix` with the following two properties:

1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` *if `target` is in `matrix` or `false` otherwise*.

You must write a solution in $\mathcal{O}(\log(m \times n))$ time complexity.

---

## Examples

### Example 1
```text
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
```

### Example 2
```text
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```

---

## Constraints

- $m == \text{matrix.length}$
- $n == \text{matrix}[i].\text{length}$
- $1 \le m, n \le 100$
- $-10^4 \le \text{matrix}[i][j], \text{target} \le 10^4$
