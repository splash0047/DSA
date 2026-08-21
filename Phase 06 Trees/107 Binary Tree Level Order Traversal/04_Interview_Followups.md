# 04 Interview Follow-ups & System Variations: Level Order Traversal

The problem returns the level-by-level values of a binary tree. The optimal approach uses **Breadth-First Search (BFS) with Level Size Snapshot** in $\mathcal{O}(N)$ time and $\mathcal{O}(W)$ space.

In technical interviews, this problem is compared with recursive DFS level indexing and serialization.

---

## 1. BFS Queue Snapshot vs. Recursive DFS with Level Index

### 💡 Two Approaches Compared
1. **Iterative BFS Queue**:
   - `int sz = q.size()` captures the exact number of nodes at the current level.
   - Natural left-to-right order.
2. **Recursive DFS**:
   - Pass `depth` parameter:
     ```cpp
     if (depth == res.size()) res.push_back({});
     res[depth].push_back(node->val);
     ```
   - **Time**: $\mathcal{O}(N)$, **Space**: $\mathcal{O}(H)$ stack space (lower memory than BFS if tree is wide).

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Memory Dominant Case | Time | Space |
| :--- | :--- | :--- | :--- |
| **BFS Queue Snapshot** | Wide trees ($W = N/2$) | $\mathcal{O}(N)$ | $\mathcal{O}(W)$ |
| **DFS Level Index** | Skewed trees ($H = N$) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
