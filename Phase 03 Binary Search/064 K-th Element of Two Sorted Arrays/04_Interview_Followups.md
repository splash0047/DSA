# 04 Interview Follow-ups & System Variations: K-th Element of Two Sorted Arrays

The problem finds the $k$-th smallest element in two sorted arrays of sizes $M$ and $N$. The optimal approach uses Binary Search Partitioning in $\mathcal{O}(\log(\min(M, N)))$ or recursive $k/2$ elimination in $\mathcal{O}(\log k)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is the generalization of the Median problem.

---

## 1. Dual Partitioning with Target Rank $k$

### 💡 Search Space Bounds
- When searching for rank $k$, partition $P_1$ cannot exceed $k$ or $M$, and cannot be smaller than $\max(0, k - N)$:
  $$	ext{low} = \max(0, k - N), \quad 	ext{high} = \min(k, M)$$
  $$P_2 = k - P_1$$
- Invariant: $L_1 \le R_2$ and $L_2 \le R_1 \implies 	ext{Result} = \max(L_1, L_2)$.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Invariant | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Binary Search Partition** | $P_1 + P_2 = k$ | $\mathcal{O}(\log(\min(M, N)))$ | $\mathcal{O}(1)$ |
| **Recursive $k/2$ Elimination**| Compare $	ext{arr1}[k/2]$ vs $	ext{arr2}[k/2]$ | $\mathcal{O}(\log k)$ | $\mathcal{O}(\log k)$ stack |
