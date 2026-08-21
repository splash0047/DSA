# 04 Interview Follow-ups & System Variations: Rotting Oranges

The problem finds the minimum number of minutes until no fresh orange remains in a grid. The optimal solution uses **Multi-Source BFS with Level Barriers** in $\mathcal{O}(M 	imes N)$ time and $\mathcal{O}(M 	imes N)$ space.

In technical interviews, this problem is the gold standard for Multi-Source BFS. Interviewers test why DFS fails here, unreachable island detection, and 3D warehouse extensions.

---

## 1. Why DFS Cannot Solve Rotting Oranges Directly

### 🛑 The Simulation Asymmetry
- All rotten oranges rot their adjacent fresh oranges **simultaneously in parallel** on each minute tick.
- DFS explores one single path deeply first, requiring expensive repeated minimum timestamp updates across all overlapping paths ($\mathcal{O}(MN)$ per branch).
- **Multi-Source BFS** naturally expands all rotting fronts uniformly outward in concentric 1-minute layers, guaranteeing the earliest rotting time for every orange in a single pass.

---

## 2. Multi-Source BFS Implementation Pattern

```cpp
int orangesRotting(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    queue<pair<int, int>> q;
    int fresh_count = 0;
    
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            if (grid[r][c] == 2) q.push({r, c}); // Seed all initial rotten oranges
            else if (grid[r][c] == 1) fresh_count++;
        }
    }
    
    if (fresh_count == 0) return 0;
    
    int minutes = -1;
    int dirs[4][2] = {{-1,0}, {1,0}, {0,-1}, {0,1}};
    
    while (!q.empty()) {
        int sz = q.size();
        minutes++;
        for (int i = 0; i < sz; i++) {
            auto [cr, cc] = q.front(); q.pop();
            for (auto& d : dirs) {
                int nr = cr + d[0], nc = cc + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                    grid[nr][nc] = 2; // Rot the fresh orange
                    fresh_count--;
                    q.push({nr, nc});
                }
            }
        }
    }
    return (fresh_count == 0) ? minutes : -1;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Algorithm | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **2D Grid** | Multi-Source BFS | $\mathcal{O}(MN)$ | $\mathcal{O}(MN)$ |
| **3D Grid ($R 	imes C 	imes H$)**| 6-Neighbor 3D BFS | $\mathcal{O}(R \cdot C \cdot H)$ | $\mathcal{O}(R \cdot C \cdot H)$ |
