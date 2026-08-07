# 042. Grid Game

- **Platform**: LeetCode
- **Problem Number**: #2017
- **Difficulty**: Medium
- **URL**: [LeetCode #2017 - Grid Game](https://leetcode.com/problems/grid-game/)

---

## Problem Statement

You are given a **0-indexed** 2D array `grid` of size `2 x n`, where `grid[r][c]` represents the number of points at cell `(r, c)`. Two robots are playing a game on this grid.

Both robots start at `(0, 0)` and want to reach `(1, n - 1)`. Each robot may only move to the **right** (`(r, c + 1)`) and **down** (`(r + 1, c)`).

- The **first robot** wants to **minimize** the number of points collected by the second robot.
- The **second robot** wants to **maximize** the number of points it collects.

When the first robot moves through a cell, that cell's points are set to `0`. Then the second robot makes its move.

Return *the **number of points** collected by the second robot if both robots play optimally*.

---

## Examples

### Example 1
```text
Input: grid = [[2,5,4],[1,5,1]]
Output: 4
Explanation: The optimal path taken by the first robot is shown in red:
[2, 5, 4]
[1, 5, 1]
After the first robot's path, the grid becomes:
[0, 0, 0]
[1, 5, 0]
The second robot can collect at most 4 points by taking the path shown in blue:
[0, 0, 0]
[1, 5, 0]
```

### Example 2
```text
Input: grid = [[3,3,1],[8,5,2]]
Output: 4
```

### Example 3
```text
Input: grid = [[1,3,1,15],[1,3,3,1]]
Output: 7
```

---

## Constraints

- `grid.length == 2`
- $n == \text{grid}[0].\text{length}$
- $1 \le n \le 5 \times 10^4$
- $1 \le \text{grid}[r][c] \le 10^5$
