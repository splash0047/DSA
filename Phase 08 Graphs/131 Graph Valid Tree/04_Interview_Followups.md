# 04 Interview Follow-ups & System Variations: Graph Valid Tree

The problem checks if an undirected graph of $N$ nodes and a list of edges forms a valid tree. Optimal solutions verify the **2 Fundamental Tree Invariants** in $\mathcal{O}(V + E)$ time and $\mathcal{O}(V)$ space.

In technical interviews, this problem tests minimal graph invariants and Disjoint Set Union cycle detection.

---

## 1. The 2 Fundamental Tree Theorems

An undirected graph with $N$ vertices is a valid tree **IF AND ONLY IF**:
1. **Edge Count Invariant**: Exactly $N - 1$ edges ($E = N - 1$).
2. **Connectivity Invariant**: The graph is fully connected (has exactly 1 connected component).

### 💡 The Fast-Exit Optimization
```cpp
bool validTree(int n, vector<vector<int>>& edges) {
    if (edges.size() != n - 1) return false; // Immediate fast exit!
    
    // Run DSU or BFS to verify full connectivity in 1 pass
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Edge Check | Connectivity Check | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **DSU (Union-Find)** | `edges.size() == n - 1` | Detect cycle on union | $\mathcal{O}(N lpha(N))$ | $\mathcal{O}(N)$ |
| **BFS / DFS** | `edges.size() == n - 1` | Visited count $== N$ | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
