# 04 Interview Follow-ups & System Variations: Max Area of Island

The problem finds the maximum area of a connected island in a 2D binary matrix. Optimal solutions include **Recursive DFS** or **Iterative BFS** tracking component sizes in $\mathcal{O}(M 	imes N)$ time and $\mathcal{O}(M 	imes N)$ space.

In technical interviews, this problem tests call-stack safety in large connected components and component size tracking in Disjoint Set Union.

---

## 1. Preventing Stack Overflow on Massive Connected Continents

### 🛑 The Recursion Hazard
If the entire $1000 	imes 1000$ grid is a single giant island of $10^6$ land cells, recursive DFS will create $10^6$ call stack frames, causing a crash.

### 💡 Iterative BFS with Queue
```cpp
int bfsArea(vector<vector<int>>& grid, int r, int c) {
    int area = 0;
    queue<pair<int, int>> q;
    q.push({r, c});
    grid[r][c] = 0; // Mark visited immediately upon enqueue!
    
    int dirs[4][2] = {{-1,0}, {1,0}, {0,-1}, {0,1}};
    while (!q.empty()) {
        auto [cr, cc] = q.front(); q.pop();
        area++;
        
        for (auto& d : dirs) {
            int nr = cr + d[0], nc = cc + d[1];
            if (nr >= 0 && nr < grid.size() && nc >= 0 && nc < grid[0].size() && grid[nr][nc] == 1) {
                grid[nr][nc] = 0; // Prevent duplicate enqueues
                q.push({nr, nc});
            }
        }
    }
    return area;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Call Stack Safety | Time | Space |
| :--- | :--- | :--- | :--- |
| **Recursive DFS** | Unsafe on large islands | $\mathcal{O}(MN)$ | $\mathcal{O}(MN)$ stack |
| **Iterative BFS** | **Safe (Heap Queue)** | $\mathcal{O}(MN)$ | $\mathcal{O}(\min(M, N))$ queue |
| **Disjoint Set Union** | **Safe** | $\mathcal{O}(MN lpha(MN))$ | $\mathcal{O}(MN)$ array |
