# 04 Interview Follow-ups & System Variations: House Robber

The problem finds the maximum money you can rob without robbing two adjacent houses. The standard optimal approach uses two variables (`rob1`, `rob2`) in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is extended to trees (House Robber III / Tree DP), circular streets (House Robber II), and bounded capacity constraints.

---

## 1. Generalization: House Robber on a Binary Tree (LeetCode #337 / House Robber III)

### 💡 Tree DP Tuple State: `(rob_this_node, skip_this_node)`
- For each tree node, return a pair:
  1. `rob_node = node.val + left.skip + right.skip`
  2. `skip_node = max(left.rob, left.skip) + max(right.rob, right.skip)`
- Post-order DFS traversal in $\mathcal{O}(N)$ time and $\mathcal{O}(H)$ stack space.

---

## Summary Matrix: Trade-offs at a Glance

| Topology | State Model | Time | Space |
| :--- | :--- | :--- | :--- |
| **1D Line (I)** | 2 scalars (`rob1`, `rob2`) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Circular Neighborhood (II)**| Split into 2 Linear passes | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Binary Tree (III)** | Post-order `(rob, skip)` pair | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
