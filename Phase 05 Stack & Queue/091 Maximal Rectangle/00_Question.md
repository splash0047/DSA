# 091. Maximal Rectangle

- **Platform**: LeetCode
- **Problem Number**: #85
- **Difficulty**: Hard
- **URL**: [LeetCode #85 - Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)

---

## Problem Statement

Given a `rows x cols` binary `matrix` filled with `0`'s and `1`'s, find the largest rectangle containing only `1`'s and return *its area*.

---

## Examples

### Example 1
```text
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the 2nd and 3rd rows with columns 2, 3, 4 (area = 6).
```

### Example 2
```text
Input: matrix = [["0"]]
Output: 0
```

### Example 3
```text
Input: matrix = [["1"]]
Output: 1
```

---

## Constraints

- $rows == \text{matrix.length}$
- $cols == \text{matrix}[i].\text{length}$
- $1 \le rows, cols \le 200$
- `matrix[i][j]` is `'0'` or `'1'`.
