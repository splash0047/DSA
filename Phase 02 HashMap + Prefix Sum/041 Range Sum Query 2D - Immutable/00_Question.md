# 041. Range Sum Query 2D - Immutable

- **Platform**: LeetCode
- **Problem Number**: #304
- **Difficulty**: Medium
- **URL**: [LeetCode #304 - Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)

---

## Problem Statement

Given a 2D matrix `matrix`, handle multiple queries of the following type:

1. Calculate the **sum** of the elements of `matrix` inside the rectangle defined by its **upper left corner** `(row1, col1)` and **lower right corner** `(row2, col2)`.

Implement the `NumMatrix` class:

- `NumMatrix(int[][] matrix)` Initializes the object with the integer matrix `matrix`.
- `int sumRegion(int row1, int col1, int row2, int col2)` Returns the sum of the elements of `matrix` inside the rectangle defined by its upper left corner `(row1, col1)` and lower right corner `(row2, col2)`.

---

## Examples

### Example 1
```text
Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8
numMatrix.sumRegion(1, 1, 2, 2); // return 11
numMatrix.sumRegion(1, 2, 2, 4); // return 12
```

---

## Constraints

- $m == \text{matrix.length}$
- $n == \text{matrix}[i].\text{length}$
- $1 \le m, n \le 200$
- $-10^4 \le \text{matrix}[i][j] \le 10^4$
- $0 \le \text{row1} \le \text{row2} < m$
- $0 \le \text{col1} \le \text{col2} < n$
- At most $10^4$ calls will be made to `sumRegion`.
