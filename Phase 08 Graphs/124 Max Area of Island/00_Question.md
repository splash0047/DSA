# 124. Max Area of Island

- **Platform**: LeetCode
- **Problem Number**: #695
- **Difficulty**: Medium
- **URL**: [LeetCode #695 - Max Area of Island](https://leetcode.com/problems/max-area-of-island/)

---

## Problem Statement

You are given an `m x n` binary matrix `grid`. An island is a group of `1`s (representing land) connected **4-directionally** (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

The **area** of an island is the number of cells with a value `1` in the island.

Return *the maximum **area** of an island in* `grid`. If there is no island, return `0`.

---

## Examples

### Example 1
```text
Input: grid = [
  [0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
Output: 6
Explanation: The answer is not 11, because the island must be 4-directionally connected.
```

### Example 2
```text
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
```

---

## Constraints

- $m == \text{grid.length}$
- $n == \text{grid}[i].\text{length}$
- $1 \le m, n \le 50$
- `grid[i][j]` is `0` or `1`.
