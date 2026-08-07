# Problem Summary

Find all coordinates in an `m x n` grid where rain water can flow to **both** the Pacific (top/left) and Atlantic (bottom/right) oceans. Water flows to adjacent cells of equal or lower height. The optimal approach uses **Multi-Source Reverse Ocean DFS**:
- Instead of flowing downhill from every cell, flow water **uphill** from ocean borders into the island!
- Run DFS from Pacific borders (top/left) upward to higher/equal cells $\implies$ store in `pacific` matrix.
- Run DFS from Atlantic borders (bottom/right) upward to higher/equal cells $\implies$ store in `atlantic` matrix.
- Collect all cells where `pacific[r][c] && atlantic[r][c]` is `true`.
This finds all dual-flowing cells in $\mathcal{O}(M \times N)$ time and $\mathcal{O}(M \times N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find **cells that can reach multiple distinct boundaries**.
- Reverse Boundary DFS / Multi-Source Flood Fill pattern.

---

## Important Clues

1. **"Flows to both Pacific and Atlantic oceans"**: Dual boundary reachability.
2. **"Adjacent cell height <= current cell height"**: Uphill flow condition (`nextHeight >= prevHeight`) when starting from boundaries.

---

## Example

### Input
`heights = [[1, 2], [2, 1]]`

### Visual Step-by-Step Progression

```text
Pacific Reachable (from top/left):
[T, T]
[T, F]

Atlantic Reachable (from bottom/right):
[F, T]
[T, T]

Intersection (Pacific && Atlantic):
(0,1) and (1,0) are True in both!

Result: [[0,1], [1,0]]
```

---

## Alternative Solutions

### Top-Down DFS from Every Cell ($\mathcal{O}((M \times N)^2)$ Time)
- Run 2 separate DFS searches from every single cell to check if Pacific and Atlantic boundaries can be reached.

---

## Edge Cases

1. **$1 \times 1$ Grid**: `[[1]]` $\implies$ returns `[[0, 0]]` (corner touches both oceans).
2. **Single Row / Column Grid**: All cells touch at least one ocean border.
3. **Flat Grid (All elements equal)**: All cells reach both oceans.

---

## Interview Tips

- **Explain Reverse Flow Insight**: State *"Instead of running $M \times N$ searches flowing downhill to oceans, we reverse the perspective: start at the ocean borders and flow uphill to higher ground. This reduces total DFS runs to just 2, achieving optimal $\mathcal{O}(M \times N)$ time."*

---

## Similar Problems

1. [LeetCode #130: Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)
2. [LeetCode #200: Number of Islands](https://leetcode.com/problems/number-of-islands/)
3. [LeetCode #286: Walls and Gates](https://leetcode.com/problems/walls-and-gates/)

---

## Revision Notes

- Problem: Find cells where water can flow to both Pacific & Atlantic.
- Pattern: Multi-Source Reverse DFS from ocean borders.
- Condition: Flow uphill (`heights[r][c] >= prevHeight`).
- Result: Cells where `pacific[r][c] && atlantic[r][c]`.
- Optimal Complexity: Time $\mathcal{O}(M \times N)$, Space $\mathcal{O}(M \times N)$.
