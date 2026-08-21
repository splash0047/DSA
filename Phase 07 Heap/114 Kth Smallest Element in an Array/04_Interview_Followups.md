# 04 Interview Follow-ups & System Variations: Kth Smallest Element in an Array

The problem finds the $k$-th smallest element in an unsorted array. Optimal approaches include QuickSelect ($\mathcal{O}(N)$ average) or a **Max-Heap of size $K$** ($\mathcal{O}(N \log K)$ time, $\mathcal{O}(K)$ space).

In technical interviews, this problem is extended to 2D Sorted Matrices (LeetCode #378) and $K$-th smallest sums.

---

## 1. Generalization: K-th Smallest Element in a Sorted Matrix (LeetCode #378)

### 🛑 The Challenge
Given an $N 	imes N$ matrix where each row and column is sorted in ascending order, find the $k$-th smallest element.

### 💡 Two Optimal Approaches
1. **Min-Heap of Row Pointers ($\mathcal{O}(K \log N)$)**:
   - Push first element of each row `(matrix[r][0], r, 0)` into a Min-Heap of size $N$.
   - Pop minimum $K$ times and insert next element from the popped row.
2. **Binary Search on the Value Range ($\mathcal{O}(N \log(	ext{max} - 	ext{min}))$ Optimal)**:
   - Search space: $[	ext{matrix}[0][0], 	ext{matrix}[N-1][N-1]]$.
   - For a candidate value $M$, count how many elements in the matrix are $\le M$ using Saddleback search from top-right in $\mathcal{O}(N)$ time.
   - **Space Complexity**: strictly $\mathcal{O}(1)$!

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Strategy | Time | Space |
| :--- | :--- | :--- | :--- |
| **1D Array** | QuickSelect / Max-Heap | $\mathcal{O}(N)$ avg / $\mathcal{O}(N \log K)$ | $\mathcal{O}(1)$ / $\mathcal{O}(K)$ |
| **2D Sorted Matrix** | Binary Search on Range + Saddleback | $\mathcal{O}(N \log(	ext{Range}))$ | strictly $\mathcal{O}(1)$ |
