# 127. Surrounded Regions

- **Platform**: LeetCode
- **Problem Number**: #130
- **Difficulty**: Medium
- **URL**: [LeetCode #130 - Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)

---

## Problem Statement

Given an `m x n` matrix `board` containing `'X'` and `'O'`, **capture all regions that are 4-directionally surrounded by** `'X'`.

A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region.

Notice that an `'O'` on the border of the board is **not** surrounded by `'X'`. Any `'O'` that is not on the border and it is not connected to an `'O'` on the border will be captured.

---

## Examples

### Example 1
```text
Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]
Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]
Explanation:
Notice that an 'O' on the border is not surrounded.
The 'O' at (3, 1) is on the border, so it is not flipped.
All other 'O's are surrounded by 'X's, so they are flipped to 'X'.
```

### Example 2
```text
Input: board = [["X"]]
Output: [["X"]]
```

---

## Constraints

- $m == \text{board.length}$
- $n == \text{board}[i].\text{length}$
- $1 \le m, n \le 200$
- `board[i][j]` is `'X'` or `'O'`.
