# 04 Interview Follow-ups & System Variations: Pacific Atlantic Water Flow

The problem finds all grid coordinates where water can flow both to the Pacific Ocean (top/left) and Atlantic Ocean (bottom/right). The optimal solution runs **Reverse Graph Traversal** (flowing uphill from ocean boundaries) using 2 BFS/DFS passes in $\mathcal{O}(M 	imes N)$ time and $\mathcal{O}(M 	imes N)$ space.

In technical interviews, this problem is the prime demonstration of **Multi-Source Reverse Search** vs. naive forward simulation.

---

## 1. Why Forward Simulation is $\mathcal{O}(M^2 N^2)$ vs. Reverse Search $\mathcal{O}(MN)$

### 🛑 The Forward Simulation Pitfall
Testing water flow starting from every individual cell $(r, c)$ triggers $M 	imes N$ separate flood fills, taking $\mathcal{O}(M^2 N^2)$ worst-case time.

### 💡 Reverse Multi-Source Search (Uphill Flow)
- Water can only flow from $(r_1, c_1) 	o (r_2, c_2)$ if $	ext{height}_1 \ge 	ext{height}_2$.
- In reverse, water flows **uphill**: $(r_2, c_2) 	o (r_1, c_1)$ if $	ext{height}_1 \ge 	ext{height}_2$.
1. **Pacific Pass**: Start Multi-Source BFS from all Top and Left border cells. Mark reachable cells in `pacific_visited`.
2. **Atlantic Pass**: Start Multi-Source BFS from all Bottom and Right border cells. Mark reachable cells in `atlantic_visited`.
3. Cells where `pacific_visited[r][c] && atlantic_visited[r][c]` are the exact answer!
- **Time Complexity**: $2 	imes \mathcal{O}(MN) = \mathcal{O}(MN)$ strictly.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Traversal Direction | Number of Traversals | Time Complexity |
| :--- | :--- | :--- | :--- |
| **Forward Simulation** | Downhill from each cell | $M 	imes N$ individual searches | $\mathcal{O}(M^2 N^2)$ (Slow) |
| **Reverse Search (Optimal)**| Uphill from Oceans | Exactly 2 Multi-Source BFS | $\mathcal{O}(MN)$ (Optimal) |
