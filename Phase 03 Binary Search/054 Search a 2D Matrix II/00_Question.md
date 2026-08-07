# 054. Search a 2D Matrix II

- **Platform**: LeetCode
- **Problem Number**: #240
- **Difficulty**: Medium
- **URL**: [LeetCode #240 - Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)

---

## Problem Statement

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix `matrix`. This matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

---

## Examples

### Example 1
```text
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
```

### Example 2
```text
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
```

---

## Constraints

- $m == \text{matrix.length}$
- $n == \text{matrix}[i].\text{length}$
- $1 \le n, m \le 300$
- $-10^9 \le \text{matrix}[i][j] \le 10^9$
- All elements in each row are sorted in ascending order.
- All elements in each column are sorted in ascending order.
- $-10^9 \le \text{target} \le 10^9$
