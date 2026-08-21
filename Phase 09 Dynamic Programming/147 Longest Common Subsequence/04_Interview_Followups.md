# 04 Interview Follow-ups & System Variations: Longest Common Subsequence

The problem finds the length of the longest common subsequence of two strings. Optimal solutions use **2-Row Rolling 1D DP** in $\mathcal{O}(M 	imes N)$ time and $\mathcal{O}(\min(M, N))$ space.

In technical interviews, this is the prime template for sequence alignment (Bioinformatics BLAST, Git Diff), and Hirschberg's linear-space string reconstruction algorithm.

---

## 1. Reconstructing the Exact LCS in $\mathcal{O}(\min(M, N))$ Space (Hirschberg's Algorithm)

### 🛑 The Memory Bottleneck of Standard Backtracking
Standard LCS reconstruction stores the full $M 	imes N$ matrix for pointer backtracking. For two DNA sequences of length $100,000$, this requires 40GB RAM.

### 💡 Hirschberg's Divide & Conquer Algorithm
- Split string $A$ in half at $mid = M / 2$.
- Compute forward LCS of $A[0 \dots mid]$ and $B$, and backward LCS of $A[mid+1 \dots M]$ and $reverse(B)$ using 2-row rolling DP in $\mathcal{O}(N)$ space.
- Find the split point in $B$ that maximizes the sum of forward and backward LCS.
- Recursively solve on the two smaller halves!
- **Time Complexity**: $\mathcal{O}(M 	imes N)$ (geometric series $1 + 1/2 + 1/4 \dots \le 2$), **Space Complexity**: strictly $\mathcal{O}(N)$!

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Purpose | Time | Space |
| :--- | :--- | :--- | :--- |
| **2-Row Rolling DP** | Length only | $\mathcal{O}(MN)$ | $\mathcal{O}(\min(M, N))$ |
| **Full 2D Matrix DP** | Length + String Reconstruction | $\mathcal{O}(MN)$ | $\mathcal{O}(MN)$ |
| **Hirschberg's Algorithm**| Length + String Reconstruction | $\mathcal{O}(MN)$ | $\mathcal{O}(\min(M, N))$ |
