# 04 Interview Follow-ups & System Variations: Unique Paths

The problem finds the number of unique paths from top-left to bottom-right of an $M 	imes N$ grid. Optimal solutions include **Combinatorics** in $\mathcal{O}(\min(M, N))$ time and $\mathcal{O}(1)$ space, or **1D DP**.

In technical interviews, this problem tests combinatorics vs. DP trade-offs and obstacle handling (Unique Paths II).

---

## 1. Closed-Form Combinatorics Formula ($\mathcal{O}(1)$ Space)

### 💡 Mathematical Derivation
- To reach bottom-right from $(0, 0)$, you must take exactly:
  - $M - 1$ downward moves ($D$).
  - $N - 1$ rightward moves ($R$).
- Total moves: $(M - 1) + (N - 1) = M + N - 2$.
- Number of unique combinations to choose the downward moves:
  $$	ext{Total Paths} = inom{M + N - 2}{M - 1} = rac{(M + N - 2)!}{(M - 1)! (N - 1)!}$$
- Calculate multiplicatively in $\mathcal{O}(\min(M, N))$ time with zero overflow:
  ```cpp
  int uniquePaths(int m, int n) {
      long long ans = 1;
      int total_steps = m + n - 2;
      int k = min(m - 1, n - 1);
      for (int i = 1; i <= k; i++) {
          ans = ans * (total_steps - k + i) / i;
      }
      return (int)ans;
  }
  ```

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Grid Model | Optimal Strategy | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **No Obstacles (I)** | Empty Grid | Combinatorics $inom{m+n-2}{m-1}$ | $\mathcal{O}(\min(M, N))$ | $\mathcal{O}(1)$ |
| **With Obstacles (II)**| Grid with Obstacles | 1D Dynamic Programming | $\mathcal{O}(MN)$ | $\mathcal{O}(N)$ |
