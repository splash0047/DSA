# 04 Interview Follow-ups & System Variations: Median of Two Sorted Arrays

The problem finds the median of two sorted arrays of sizes $M$ and $N$ in $\mathcal{O}(\log(\min(M, N)))$ time and $\mathcal{O}(1)$ space.

In top-tier technical interviews (FAANG Hard), this is considered the definitive binary search mastery test. Interviewers probe partition equations, infinite boundary guards, and distributed multi-machine medians.

---

## 1. The Dual Partitioning Equation

### 💡 The Balance Invariant
- Let the total combined elements in the left half be:
  $$	ext{left\_half\_size} = rac{M + N + 1}{2}$$
- Binary search for partition point $P_1 \in [0, M]$ in the smaller array `nums1`.
- The partition point $P_2$ in `nums2` is strictly determined:
  $$P_2 = 	ext{left\_half\_size} - P_1$$
- Define the 4 boundary elements:
  - $L_1 = (P_1 == 0) \;?\; -\infty : 	ext{nums1}[P_1 - 1]$
  - $R_1 = (P_1 == M) \;?\; +\infty : 	ext{nums1}[P_1]$
  - $L_2 = (P_2 == 0) \;?\; -\infty : 	ext{nums2}[P_2 - 1]$
  - $R_2 = (P_2 == N) \;?\; +\infty : 	ext{nums2}[P_2]$
- **Valid Partition Condition**:
  $$L_1 \le R_2 \quad 	ext{AND} \quad L_2 \le R_1$$
- **Median Formula**:
  - If $(M + N)$ is odd: $	ext{Median} = \max(L_1, L_2)$.
  - If $(M + N)$ is even: $	ext{Median} = rac{\max(L_1, L_2) + \min(R_1, R_2)}{2.0}$.

---

## 2. Why Always Binary Search on the SMALLER Array?

### 💡 2 Critical Benefits
1. **Guaranteed Valid $P_2$ Bounds**: Because $M \le N$, $P_2 = rac{M + N + 1}{2} - P_1$ is guaranteed to stay within valid range $[0, N]$.
2. **Minimal Time Complexity**: $\mathcal{O}(\log(\min(M, N)))$. If $M = 10$ and $N = 10^9$, the search finishes in $\log_2(10) pprox 4$ iterations!

---

## Summary Matrix: Trade-offs at a Glance

| Array Sizes | Binary Search Target | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| $M \le N$ | Smaller array ($M$) | $\mathcal{O}(\log(\min(M, N)))$ | $\mathcal{O}(1)$ |
| $M \gg N$ | Swap arrays $\implies$ Search $N$ | $\mathcal{O}(\log(\min(M, N)))$ | $\mathcal{O}(1)$ |
