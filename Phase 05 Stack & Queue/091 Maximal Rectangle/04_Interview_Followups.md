# 04 Interview Follow-ups & System Variations: Maximal Rectangle

The problem finds the largest rectangle containing only `1`s in a 2D binary matrix (Hard). The optimal approach transforms the matrix row-by-row into a dynamic Histogram and runs the **Largest Rectangle in Histogram** algorithm on each row in $\mathcal{O}(R 	imes C)$ time and $\mathcal{O}(C)$ space.

In technical interviews, this problem is compared with Maximal Square and 2D Dynamic Programming.

---

## 1. 2D-to-1D Histogram Row Reduction

### 💡 Row-by-Row Height Accumulation
- Maintain a 1D array `heights[C]`.
- For each row $r \in [0, R - 1]$:
  - For each column $c$: `heights[c] = (matrix[r][c] == '1') ? heights[c] + 1 : 0;`
  - Compute largest rectangle for `heights` in $\mathcal{O}(C)$ using Monotonic Stack.
- **Total Time Complexity**: $R 	imes \mathcal{O}(C) = \mathcal{O}(R 	imes C)$.
- **Total Space Complexity**: $\mathcal{O}(C)$.

---

## 2. Maximal Rectangle vs. Maximal Square (LeetCode #221)

| Problem | Shape Constraint | Optimal Technique | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Maximal Rectangle (#85)**| Arbitrary width/height | Row Histogram + Monotonic Stack | $\mathcal{O}(R 	imes C)$ | $\mathcal{O}(C)$ |
| **Maximal Square (#221)** | Width == Height | 2D DP: $DP[i][j] = 1 + \min(top, left, diag)$ | $\mathcal{O}(R 	imes C)$ | $\mathcal{O}(C)$ |

---

## Summary Matrix: Trade-offs at a Glance

| Dimension | Strategy | Time | Space |
| :--- | :--- | :--- | :--- |
| **Maximal Rectangle** | Row-wise Histogram + Monotonic Stack | $\mathcal{O}(R 	imes C)$ | $\mathcal{O}(C)$ |
| **Dynamic Programming**| Track `left`, `right`, `height` per cell | $\mathcal{O}(R 	imes C)$ | $\mathcal{O}(C)$ |
