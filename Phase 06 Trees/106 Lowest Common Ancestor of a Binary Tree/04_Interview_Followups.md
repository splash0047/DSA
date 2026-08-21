# 04 Interview Follow-ups & System Variations: Lowest Common Ancestor

The LCA problem finds the lowest common ancestor of two nodes $P$ and $Q$ in a binary tree. The standard post-order DFS runs in $\mathcal{O}(N)$ time and $\mathcal{O}(H)$ space.

In top-tier technical interviews, this is the prime problem for scaling to millions of offline/online queries (Binary Lifting, RMQ Euler Tour).

---

## 1. LCA in BST vs. Binary Tree vs. Nodes with Parent Pointers

| Tree Type | Optimal Algorithm | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Binary Search Tree (BST)**| Value comparison ($\mathcal{O}(H)$ path) | $\mathcal{O}(H)$ | $\mathcal{O}(1)$ iterative |
| **General Binary Tree** | Post-Order DFS Return | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| **With Parent Pointers** | Two Pointers (Intersection of Lists) | $\mathcal{O}(H)$ | $\mathcal{O}(1)$ |

---

## 2. Millions of LCA Queries on a Static Tree: Binary Lifting ($\mathcal{O}(\log N)$ per query)

### 💡 Binary Lifting Precomputation
- Precompute table `up[node][j]`: the $2^j$-th ancestor of `node`.
  $$	ext{up}[node][j] = 	ext{up}[	ext{up}[node][j-1]][j-1]$$
- **Preprocessing Time**: $\mathcal{O}(N \log N)$, **Space**: $\mathcal{O}(N \log N)$.
- **LCA Query**:
  1. Lift deeper node to the same depth as the shallower node using binary jumps in $\mathcal{O}(\log N)$.
  2. Jump both nodes upwards simultaneously in powers of 2 until their parents match in $\mathcal{O}(\log N)$.

---

## 3. Euler Tour + Sparse Table (RMQ) for $\mathcal{O}(1)$ Query Time

### 💡 Reduction to Range Minimum Query
- Record Euler Tour sequence of tree nodes (length $2N - 1$) with their depths.
- The LCA of $P$ and $Q$ is the node with the **minimum depth** between first occurrence of $P$ and first occurrence of $Q$ in the Euler tour!
- Using a Sparse Table for RMQ:
  - **Preprocessing**: $\mathcal{O}(N \log N)$, **Query Time**: strictly $\mathcal{O}(1)$.

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Preprocessing | Query Time | Space |
| :--- | :--- | :--- | :--- |
| **Single Query** | None ($\mathcal{O}(0)$) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| **Binary Lifting** | $\mathcal{O}(N \log N)$ | $\mathcal{O}(\log N)$ | $\mathcal{O}(N \log N)$ |
| **Euler Tour + RMQ** | $\mathcal{O}(N \log N)$ | **$\mathcal{O}(1)$** | $\mathcal{O}(N \log N)$ |
