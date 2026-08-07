# 126. Pacific Atlantic Water Flow

- **Platform**: LeetCode
- **Problem Number**: #417
- **Difficulty**: Medium
- **URL**: [LeetCode #417 - Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)

---

## Problem Statement

There is an `m x n` rectangular island that borders both the **Pacific Ocean** and **Atlantic Ocean**. The **Pacific Ocean** touches the island's left and top edges, and the **Atlantic Ocean** touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the height above sea level of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is **less than or equal to** the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return *a 2D list of grid coordinates* `result` *where* `result[i] = [ri, ci]` *denotes that rain water can flow from cell* `(ri, ci)` *to **both** the Pacific and Atlantic oceans*.

---

## Examples

### Example 1
```text
Input: heights = [
  [1,2,2,3,5],
  [3,2,3,4,4],
  [2,4,5,3,1],
  [6,7,1,4,5],
  [5,1,1,2,4]
]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to both the Pacific and Atlantic oceans:
- [0,4]: height 5 -> Pacific (top) and Atlantic (right)
- [1,3]: height 4 -> Pacific (top) and Atlantic (right)
- [1,4]: height 4 -> Pacific (top) and Atlantic (right)
- [2,2]: height 5 -> Pacific (top/left) and Atlantic (right/bottom)
- [3,0]: height 6 -> Pacific (left) and Atlantic (bottom)
- [3,1]: height 7 -> Pacific (left) and Atlantic (bottom)
- [4,0]: height 5 -> Pacific (left) and Atlantic (bottom)
```

### Example 2
```text
Input: heights = [[1]]
Output: [[0,0]]
```

---

## Constraints

- $m == \text{heights.length}$
- $n == \text{heights}[r].\text{length}$
- $1 \le m, n \le 200$
- $0 \le \text{heights}[r][c] \le 10^5$
