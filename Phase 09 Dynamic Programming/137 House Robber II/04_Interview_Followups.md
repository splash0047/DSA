# 04 Interview Follow-ups & System Variations: House Robber II

The problem extends House Robber to a circular street (first and last house are neighbors). The optimal approach breaks the circular dependency into two linear sub-problems in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem demonstrates the standard paradigm for **Linearizing Circular Dynamic Programming**.

---

## 1. The 2-Pass Linearization Architecture

### 💡 Mutual Exclusion of First and Last Houses
- You can either rob House $0$ OR House $N-1$, but never both.
- **Subproblem 1**: Rob from House $0$ to $N - 2$ (excludes last house).
- **Subproblem 2**: Rob from House $1$ to $N - 1$ (excludes first house).
- **Result**: $\max(	ext{Solve}(0 \dots N-2),\; 	ext{Solve}(1 \dots N-1))$.

---

## Summary Matrix: Trade-offs at a Glance

| Topology | Strategy | Time Complexity | Extra Space |
| :--- | :--- | :--- | :--- |
| **Circular Street** | $\max(	ext{Line}(0 \dots N-2), 	ext{Line}(1 \dots N-1))$ | $\mathcal{O}(N)$ (2 passes) | $\mathcal{O}(1)$ |
