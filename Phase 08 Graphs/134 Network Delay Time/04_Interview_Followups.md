# 04 Interview Follow-ups & System Variations: Network Delay Time

The problem finds the time taken for all nodes to receive a signal from node $K$ on a directed weighted graph. The optimal solution uses **Dijkstra's Algorithm with a Min-Heap Priority Queue** in $\mathcal{O}((V + E) \log V)$ time and $\mathcal{O}(V + E)$ space.

In technical interviews, this problem is the launchpad for shortest path comparisons (Dijkstra, Bellman-Ford, Floyd-Warshall, A*).

---

## 1. Comprehensive Shortest Path Algorithm Comparison

| Algorithm | Edge Weights | Time Complexity | Space Complexity | Best Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **Dijkstra (Min-Heap)** | Non-Negative ($\ge 0$) | $\mathcal{O}((V + E) \log V)$ | $\mathcal{O}(V + E)$ | Single-Source Non-Negative |
| **0-1 BFS (Deque)** | Weights $\in \{0, 1\}$ | $\mathcal{O}(V + E)$ strictly | $\mathcal{O}(V)$ | Grid moves / Binary weights |
| **Bellman-Ford** | Negative allowed | $\mathcal{O}(V \cdot E)$ | $\mathcal{O}(V)$ | Detects Negative Weight Cycles |
| **SPFA (Queue Optimized)**| Negative allowed | $\mathcal{O}(E)$ avg / $\mathcal{O}(VE)$ worst | $\mathcal{O}(V)$ | Sparse graphs with negative edges |
| **Floyd-Warshall** | Negative allowed | $\mathcal{O}(V^3)$ | $\mathcal{O}(V^2)$ | All-Pairs Shortest Paths |
| **A* Search** | Non-Negative + Heuristic | $\mathcal{O}(E)$ directed | $\mathcal{O}(V)$ | Spatial Map Navigation (GPS) |

---

## 2. Dijkstra's Algorithm Implementation Template

```cpp
int networkDelayTime(vector<vector<int>>& times, int n, int k) {
    vector<vector<pair<int, int>>> adj(n + 1);
    for (auto& t : times) {
        adj[t[0]].push_back({t[1], t[2]}); // u -> {v, weight}
    }
    
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    vector<int> dist(n + 1, INT_MAX);
    
    dist[k] = 0;
    pq.push({0, k}); // {distance, node}
    
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue; // Stale heap entry optimization
        
        for (auto& [v, w] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    
    int max_time = 0;
    for (int i = 1; i <= n; i++) {
        if (dist[i] == INT_MAX) return -1;
        max_time = max(max_time, dist[i]);
    }
    return max_time;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Recommended Algorithm | Time | Space |
| :--- | :--- | :--- | :--- |
| **Non-Negative Weights** | Dijkstra (Min-Heap) | $\mathcal{O}((V + E) \log V)$ | $\mathcal{O}(V + E)$ |
| **Negative Weights Present** | Bellman-Ford / SPFA | $\mathcal{O}(V \cdot E)$ | $\mathcal{O}(V)$ |
| **All-Pairs Distances ($N \le 500$)**| Floyd-Warshall | $\mathcal{O}(V^3)$ | $\mathcal{O}(V^2)$ |
