# 04 Interview Follow-ups & System Variations: Path Sum II

The problem finds all root-to-leaf paths where the sum of node values equals `targetSum`. The optimal solution uses **DFS with a Backtracking Path Buffer** in $\mathcal{O}(N)$ time (plus path copying) and $\mathcal{O}(H)$ auxiliary space.

In technical interviews, this problem tests backtracking buffer management and copy-cost amortized analysis.

---

## 1. Backtracking Path Buffer Management

### 💡 Single Shared Buffer Pattern
- Maintain a single `vector<int> current_path`.
- When visiting `node`: `current_path.push_back(node->val)`.
- When backtracking to parent: `current_path.pop_back()`.
- Avoids allocating and cloning vectors on every branch traversal.
- **Copy Cost**: Path vector is only cloned into the result list when a valid leaf match is found.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Vector Allocation | Time | Auxiliary Space |
| :--- | :--- | :--- | :--- |
| **Single Backtracking Vector** | 1 Shared Vector | $\mathcal{O}(N + K \cdot H)$ | $\mathcal{O}(H)$ |
| **Pass-by-Value Vector** | Cloned per recursion frame | $\mathcal{O}(N \cdot H)$ | $\mathcal{O}(H^2)$ |
