# 04 Interview Follow-ups & System Variations: Number of Islands

The problem counts the number of disconnected islands in a 2D binary grid. Optimal solutions include **DFS Flood Fill** / **BFS** in $\mathcal{O}(M 	imes N)$ time and $\mathcal{O}(M 	imes N)$ space (or in-place cell mutation for $\mathcal{O}(1)$ auxiliary space), or **Disjoint Set Union (DSU)**.

In top-tier technical interviews, this is the archetypal grid connectivity problem. Interviewers probe massive grid streaming (1B cells), dynamic land additions (Number of Islands II), and distributed MapReduce graph partitioning.

---

## 1. What if the Grid Has 1 Billion Cells ($10^5 	imes 10^5$) and Cannot Fit in RAM?

### 🛑 Memory Bottleneck
A $10^5 	imes 10^5$ grid takes 10 GB of raw memory; in-memory DFS or BFS will trigger Out-Of-Memory (OOM).

### 💡 Row-by-Row Disjoint Set Streaming
- You only need to keep **2 rows** in memory at any given time (the `previous_row` and `current_row`).
- Maintain a **Disjoint Set Union (Union-Find)** structure for the active active land boundaries.
- As `current_row` streams in:
  - Union adjacent horizontal land cells in `current_row`.
  - Union vertical connections with `previous_row`.
  - When moving to the next row, discard nodes from the row above that have no downward connections.
- **RAM Overhead**: Strictly $\mathcal{O}(	ext{Column Width})$ instead of $\mathcal{O}(R 	imes C)$.

---

## 2. Dynamic Land Additions: Number of Islands II (LeetCode #305)

### 🛑 The Scenario
Start with an empty $M 	imes N$ ocean grid. Land positions are added one by one dynamically; return the island count after each addition.

### 💡 Disjoint Set with Path Compression & Union by Rank
- Each cell $(r, c)$ has a 1D ID: $	ext{id} = r 	imes N + c$.
- When a new land cell $(r, c)$ is added:
  - Increment `count++`.
  - Check 4 cardinal neighbors. If a neighbor is land:
    - Perform `Union(current_id, neighbor_id)`.
    - If they were in different sets, decrement `count--`.
- **Time Complexity**: $\mathcal{O}(K 	imes lpha(M 	imes N))$ where $K$ is number of additions and $lpha$ is the Inverse Ackermann function ($pprox \mathcal{O}(1)$).

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Grid Model | Optimal Algorithm | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Static Grid** | In-Memory | DFS / BFS Flood Fill | $\mathcal{O}(MN)$ | $\mathcal{O}(MN)$ stack / queue |
| **Massive Grid** | 2-Row Stream | 2-Row Disjoint Set (DSU) | $\mathcal{O}(MN lpha(N))$ | $\mathcal{O}(N)$ RAM |
| **Dynamic Land (#305)**| Point Additions | Disjoint Set with Path Compression | $\mathcal{O}(K lpha(MN))$ | $\mathcal{O}(MN)$ DSU |
