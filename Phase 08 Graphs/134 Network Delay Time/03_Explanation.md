# Problem Summary

Find the minimum time taken for a signal sent from node `k` to reach all `n` nodes in a weighted directed network. Return `-1` if any node is unreachable. The optimal approach uses **Dijkstra's Shortest Path Algorithm**:
- Build directed weighted adjacency list `adj`.
- `dist` array initialized to `INF`, `dist[k] = 0`.
- Min-Priority Queue `pq` storing `{dist, node}`, initialized with `{0, k}`.
- Pop `{d, u}`: relax edges `u -> v` with weight `w`. If `dist[u] + w < dist[v]`, update `dist[v]` and push to `pq`.
- Return `max(dist[1..n])` if all nodes reachable, else `-1`.
This finds network delay in $\mathcal{O}(E \log V)$ time and $\mathcal{O}(V + E)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need the **shortest path / minimum time in a non-negative weighted graph**.
- Single-Source Shortest Path (Dijkstra) pattern.

---

## Important Clues

1. **"Minimum time for all nodes to receive signal"**: Max of single-source shortest path distances.
2. **"Directed weighted edges with non-negative travel times"**: Canonical Dijkstra precondition.

---

## Example

### Input
`times = [[2,1,1],[2,3,1],[3,4,1]]`, `n = 4`, `k = 2`

### Visual Step-by-Step Progression

```text
       (1)
     1 <-- 2
           | (1)
           v
           3 --(1)--> 4

Signal from 2:
- Reaches Node 1: time 1
- Reaches Node 3: time 1
- Reaches Node 4: time 1+1 = 2

Max time to reach all = 2
```

---

## Alternative Solutions

### Bellman-Ford Algorithm ($\mathcal{O}(V \times E)$ Time, $\mathcal{O}(V)$ Space)
- Relax all edges $V - 1$ times.

---

## Edge Cases

1. **Disconnected Node**: At least 1 node remains `INF` $\implies$ returns `-1`.
2. **Single node network**: `n = 1`, `k = 1` $\implies$ returns `0`.
3. **Multiple outgoing edges**: Dijkstra picks minimum weight edge expansion first.

---

## Interview Tips

- **Explain Why Max Shortest Path Represents Delay**: State *"Because the signal travels along all outgoing paths simultaneously, all nodes receive the signal when the FARTHEST node gets it. Thus, network delay equals `max(dist[1..n])`."*

---

## Similar Problems

1. [LeetCode #787: Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
2. [LeetCode #1514: Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/)
3. [LeetCode #1631: Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)

---

## Revision Notes

- Problem: Min time for signal to reach all nodes from source `k`.
- Pattern: Dijkstra's Algorithm.
- Heap: `priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;`
- Relaxation: `if (dist[u] + w < dist[v]) { dist[v] = dist[u] + w; pq.push({dist[v], v}); }`
- Result: `max(dist[1..n])` or `-1` if any node `INF`.
- Optimal Complexity: Time $\mathcal{O}(E \log V)$, Space $\mathcal{O}(V + E)$.
