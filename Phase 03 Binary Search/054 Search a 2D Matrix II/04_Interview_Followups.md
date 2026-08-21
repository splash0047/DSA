# 04 Interview Follow-ups & System Variations: Search a 2D Matrix II

The problem searches for `target` in an $M 	imes N$ matrix where rows and columns are independently sorted in ascending order. The optimal **Saddleback Search** starts at the top-right corner $(0, N - 1)$ or bottom-left corner in $\mathcal{O}(M + N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is used to compare Saddleback elimination against Quad-Tree Divide & Conquer and row-wise binary search.

---

## 1. Why Start at the Top-Right (or Bottom-Left) Corner?

### 💡 The Asymmetric Decision Property
- **Top-Left $(0, 0)$**: Both right and down increase $\implies$ ambiguous decision when `target > matrix[0][0]`.
- **Bottom-Right $(M-1, N-1)$**: Both left and up decrease $\implies$ ambiguous decision when `target < matrix[M-1][N-1]`.
- **Top-Right $(0, N-1)$ (Optimal Saddle Point)**:
  - Moving **Left** strictly decreases value.
  - Moving **Down** strictly increases value.
  - If `matrix[r][c] == target`: return `true`.
  - If `matrix[r][c] > target`: eliminate current column (`c--`).
  - If `matrix[r][c] < target`: eliminate current row (`r++`).
- **Time Complexity**: At most $M + N$ steps.

---

## 2. 3 Algorithmic Approaches Compared

| Approach | Strategy | Time Complexity | Best Scenario |
| :--- | :--- | :--- | :--- |
| **Row-wise Binary Search** | Binary search all $M$ rows | $\mathcal{O}(M \log N)$ | $M \ll N$ (e.g., $2 	imes 10^6$) |
| **Saddleback Search** | Step from Top-Right corner | $\mathcal{O}(M + N)$ | Square matrices ($M pprox N$) |
| **Quad-Tree Divide & Conquer**| Split into 4 submatrices | $\mathcal{O}((MN)^{\log_4 3}) pprox \mathcal{O}(N^{1.58})$ | Extremely large sparse matrices |

---

## Summary Matrix: Trade-offs at a Glance

| Matrix Shape | Recommended Algorithm | Time Complexity | Space |
| :--- | :--- | :--- | :--- |
| **Square ($M pprox N$)** | Top-Right Saddleback | $\mathcal{O}(M + N)$ | $\mathcal{O}(1)$ |
| **Wide ($M \ll N$)** | Binary Search on each Row | $\mathcal{O}(M \log N)$ | $\mathcal{O}(1)$ |
| **Tall ($M \gg N$)** | Binary Search on each Col | $\mathcal{O}(N \log M)$ | $\mathcal{O}(1)$ |
