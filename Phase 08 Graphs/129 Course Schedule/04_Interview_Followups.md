# 04 Interview Follow-ups & System Variations: Course Schedule

The problem determines if all courses can be finished given prerequisite pairs. This is equivalent to **Cycle Detection in a Directed Graph**. Optimal solutions include **Kahn's Algorithm (BFS with In-degrees)** or **DFS 3-Coloring** in $\mathcal{O}(V + E)$ time and $\mathcal{O}(V + E)$ space.

In technical interviews, this problem is the foundation of DAG topological sorting, package dependency managers (npm, pip), and build systems.

---

## 1. Kahn's Algorithm (BFS In-Degree) vs. DFS 3-Coloring

| Feature | Kahn's Algorithm (BFS) | DFS 3-Coloring |
| :--- | :--- | :--- |
| **Core Mechanism** | Track `in_degree[u]` for each node | Track node states (`UNVISITED`, `VISITING`, `VISITED`) |
| **Cycle Detection** | `processed_count < num_courses` | Finding an edge to a `VISITING` (Gray) node |
| **Queue / Stack** | Enqueue nodes with `in_degree == 0` | Standard recursion call stack |
| **Topological Order**| Natural forward order | Reverse of post-order finishing times |

---

## 2. DFS 3-Coloring Cycle Detection Template

```cpp
bool hasCycle(int u, vector<vector<int>>& adj, vector<int>& state) {
    state[u] = 1; // 1 = VISITING (Gray node on current recursion path)
    for (int v : adj[u]) {
        if (state[v] == 1) return true; // Back-edge detected -> CYCLE!
        if (state[v] == 0 && hasCycle(v, adj, state)) return true;
    }
    state[u] = 2; // 2 = VISITED (Black node completely evaluated)
    return false;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Approach | In-Degree Array Needed? | Time | Space |
| :--- | :--- | :--- | :--- |
| **Kahn's BFS (Optimal)** | Yes (`in_degree[V]`) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ |
| **DFS 3-Coloring** | No (State array `0, 1, 2`) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ |
