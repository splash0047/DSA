# Network Delay Time

- **Problem Number**: 743
- **Platform**: LeetCode #743
- **Difficulty**: Medium
- **Pattern**: Bellman-Ford / Edge Relaxation Iterations

---

## Brute Force Intuition

Use the Bellman-Ford algorithm to find shortest path distances from source node `k` to all other $n - 1$ nodes.
- Initialize `dist[i] = INF` for all nodes $1 \le i \le n$, and `dist[k] = 0`.
- Relax all $E$ edges $n - 1$ times.
- The minimum time required for all nodes to receive the signal is `max(dist[1], dist[2], ..., dist[n])`. If any node remains `INF`, return `-1`.

---

## Algorithm

1. `dist` array of size `n + 1` filled with `INF`. `dist[k] = 0`.
2. Repeat `n - 1` times:
   - For each `[u, v, w]` in `times`:
     - If `dist[u] != INF` and `dist[u] + w < dist[v]`:
       - `dist[v] = dist[u] + w`.
3. `maxTime = 0`.
4. For `i` from `1` to `n`:
   - If `dist[i] == INF`, return `-1`.
   - `maxTime = max(maxTime, dist[i])`.
5. Return `maxTime`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int networkDelayTime(std::vector<std::vector<int>>& times, int n, int k) {
        const int INF = 1e9;
        std::vector<int> dist(n + 1, INF);
        dist[k] = 0;
        
        // Bellman-Ford: Relax all edges V - 1 times
        for (int i = 1; i <= n - 1; ++i) {
            for (const auto& edge : times) {
                int u = edge[0];
                int v = edge[1];
                int w = edge[2];
                
                if (dist[u] != INF && dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                }
            }
        }
        
        int maxTime = 0;
        for (int i = 1; i <= n; ++i) {
            if (dist[i] == INF) return -1;
            maxTime = std::max(maxTime, dist[i]);
        }
        
        return maxTime;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(V \times E)$
  - Where $V = n$ and $E = \text{times.length}$. Relaxing all $E$ edges $V - 1$ times takes $\mathcal{O}(V \times E)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(V)$
  - Vector storage for `dist` array.

---

## Why This Approach Is Not Optimal

Bellman-Ford relaxes all edges $V - 1$ times indiscriminately, taking $\mathcal{O}(V \times E)$ time. Because all edge weights $w_i \ge 0$ are non-negative, using **Dijkstra's Priority Queue Algorithm**, we compute single-source shortest paths in optimal $\mathcal{O}(E \log V)$ time!
