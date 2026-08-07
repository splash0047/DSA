# Network Delay Time

## Pattern Used

- **Pattern**: **Dijkstra's Algorithm (Min-Priority Queue Shortest Path)**
- **Concept**:
  - Build directed weighted adjacency list `adj[u]` storing `{v, weight}`.
  - Maintain a `dist` array initialized to `INF` with `dist[k] = 0`.
  - Use a Min-Priority Queue `std::priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq` storing `{current_dist, node}`.
  - Push `{0, k}` into `pq`.
  - While `!pq.empty()`:
    - Pop `{d, u}`. If `d > dist[u]`, continue (stale entry).
    - For each `{v, weight}` in `adj[u]`:
      - If `dist[u] + weight < dist[v]`:
        - `dist[v] = dist[u] + weight`.
        - Push `{dist[v], v}` into `pq`.
  - Return `max(dist[1..n])` if no `INF` remains, else `-1`.

---

## Observation

1. All travel times are non-negative ($w \ge 0$), satisfying Dijkstra's greedy edge expansion requirement.
2. The total time for all nodes to receive the signal is equal to the **maximum shortest path distance** from source node `k` among all $n$ nodes.

---

## Intuition

Send the signal from source `k`. Use a Min-Heap to always expand the node currently receiving the signal earliest. As the signal spreads through network links, record the arrival time at each node. After all reachable nodes receive the signal, the arrival time at the last node is the overall network delay.

---

## Algorithm

1. Build `adj` list: `adj[u].push_back({v, w})`.
2. `dist` array of size `n + 1` filled with `INF`. `dist[k] = 0`.
3. Min-Heap `pq` storing `{dist, node}`. Push `{0, k}`.
4. While `!pq.empty()`:
   a. Pop `{d, u}`.
   b. If `d > dist[u]`: continue.
   c. For each `{v, w}` in `adj[u]`:
      - If `dist[u] + w < dist[v]`:
        - `dist[v] = dist[u] + w`.
        - Push `{dist[v], v}` to `pq`.
5. Find max distance among `dist[1..n]`. Return `-1` if any node has `INF`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <queue>
#include <algorithm>

class Solution {
public:
    int networkDelayTime(std::vector<std::vector<int>>& times, int n, int k) {
        // Adjacency list: u -> list of pair<v, weight>
        std::vector<std::vector<std::pair<int, int>>> adj(n + 1);
        for (const auto& edge : times) {
            adj[edge[0]].push_back({edge[1], edge[2]});
        }
        
        const int INF = 1e9;
        std::vector<int> dist(n + 1, INF);
        dist[k] = 0;
        
        // Min-heap storing pair<distance, node>
        using Pair = std::pair<int, int>;
        std::priority_queue<Pair, std::vector<Pair>, std::greater<Pair>> pq;
        pq.push({0, k});
        
        // Dijkstra's Shortest Path Algorithm
        while (!pq.empty()) {
            auto [d, u] = pq.top();
            pq.pop();
            
            if (d > dist[u]) continue;
            
            for (const auto& [v, weight] : adj[u]) {
                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                    pq.push({dist[v], v});
                }
            }
        }
        
        // Find maximum delay time among all nodes
        int maxTime = 0;
        for (int i = 1; i <= n; ++i) {
            if (dist[i] == INF) return -1; // Unreachable node
            maxTime = std::max(maxTime, dist[i]);
        }
        
        return maxTime;
    }
};
```

---

## Dry Run

### Input
- `times = [[2,1,1],[2,3,1],[3,4,1]]`, `n = 4`, `k = 2`

### Execution Trace

1. `adj`: `2 -> [{1,1}, {3,1}]`, `3 -> [{4,1}]`. `dist = [INF, INF, 0, INF, INF]`.
2. Push `{0, 2}` to `pq`.
3. Pop `{0, 2}`:
   - Relax `(2 -> 1)`: `dist[1] = 1`. Push `{1, 1}`.
   - Relax `(2 -> 3)`: `dist[3] = 1`. Push `{1, 3}`.
4. Pop `{1, 1}`: No outgoing edges.
5. Pop `{1, 3}`:
   - Relax `(3 -> 4)`: `dist[4] = 2`. Push `{2, 4}`.
6. Pop `{2, 4}`: No outgoing edges.
7. `dist` array = `[0, 1, 0, 1, 2]`. Max distance among `dist[1..4]` is `max(1, 0, 1, 2) = 2`.

### Result
- Output: `2`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(E \log V)$
  - Priority queue operations take $\mathcal{O}(\log V)$ per edge insertion/extraction.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(V + E)$
  - Adjacency list stores $E$ edges. Priority queue and `dist` vector store up to $V$ nodes.

---

## Why This is Optimal

- Dijkstra's algorithm computes single-source shortest paths on non-negative weighted graphs in optimal $\mathcal{O}(E \log V)$ time.

---

## Common Mistakes

1. **Missing Stale Entry Check**: Omitting `if (d > dist[u]) continue;` causes unnecessary processing of outdated distance pairs.
2. **1-Based vs 0-Based Indexing**: Node labels are 1-based (`1` to `n`); allocating `dist` array of size `n` leads to out-of-bounds access.
