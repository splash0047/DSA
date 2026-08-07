# Graph Valid Tree

## Pattern Used

- **Pattern**: **Disjoint Set Union (Union-Find with Path Compression)**
- **Concept**:
  - A graph is a valid tree if and only if:
    1. Number of edges is exactly `N - 1`.
    2. Adding each edge connects two previously disconnected components. If `find(u) == find(v)` when processing edge `[u, v]`, a **cycle** exists!
  - Using Union-Find:
    - Initialize DSU with `n` components.
    - If `edges.size() != n - 1`, return `false`.
    - For each edge `[u, v]`:
      - If `!unionSets(u, v)` (i.e. `u` and `v` already share the same root parent), return `false` (cycle!).
  - If all $N - 1$ edges are merged without cycles, return `true`.

---

## Observation

1. **Tree Theorem**: An undirected graph of $N$ nodes is a tree if and only if it has $N - 1$ edges and NO cycles.
2. Checking `edges.size() == n - 1` up front guarantees that if there are no cycles, the graph is automatically fully connected!

---

## Intuition

Start with $N$ isolated nodes (components $= N$). For each edge, try to union the two endpoints. If the two endpoints are ALREADY in the same connected component, adding this edge creates a cycle (invalid tree!). If all $N - 1$ edges successfully union distinct components without cycles, the graph is a valid tree.

---

## Algorithm

1. If `edges.size() != n - 1`, return `false`.
2. Class `UnionFind`:
   - `parent` array: `parent[i] = i`.
   - `find(i)`: returns root parent with path compression.
   - `unionSets(u, v)`:
     - `rootU = find(u)`, `rootV = find(v)`.
     - If `rootU == rootV`, return `false` (cycle!).
     - `parent[rootU] = rootV`, return `true`.
3. For each edge `[u, v]` in `edges`:
   - If `!dsu.unionSets(u, v)`, return `false`.
4. Return `true`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <numeric>

class UnionFind {
private:
    std::vector<int> parent;

public:
    UnionFind(int n) {
        parent.resize(n);
        std::iota(parent.begin(), parent.end(), 0);
    }
    
    int find(int i) {
        if (parent[i] == i)
            return i;
        return parent[i] = find(parent[i]); // Path Compression
    }
    
    bool unionSets(int i, int j) {
        int rootI = find(i);
        int rootJ = find(j);
        
        if (rootI == rootJ) {
            return false; // Cycle detected: i and j already connected
        }
        
        parent[rootI] = rootJ;
        return true;
    }
};

class Solution {
public:
    bool validTree(int n, std::vector<std::vector<int>>& edges) {
        // Fundamental Tree Property: A valid tree with n nodes must have exactly n - 1 edges
        if (edges.size() != n - 1) {
            return false;
        }
        
        UnionFind dsu(n);
        
        for (const auto& edge : edges) {
            if (!dsu.unionSets(edge[0], edge[1])) {
                return false; // Cycle detected
            }
        }
        
        return true;
    }
};
```

---

## Dry Run

### Input
- `n = 5`, `edges = [[0,1],[0,2],[0,3],[1,4]]`

### Execution Trace

1. `edges.size() = 4 == 5 - 1`. OK.
2. Edge `[0,1]`: Union `0` and `1` $\implies$ Success.
3. Edge `[0,2]`: Union `0` and `2` $\implies$ Success.
4. Edge `[0,3]`: Union `0` and `3` $\implies$ Success.
5. Edge `[1,4]`: Union `1` and `4` $\implies$ Success.
6. All 4 edges merged without cycles. Return `true`.

### Result
- Output: `true`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \cdot \alpha(N))$
  - Where $\alpha(N)$ is the inverse Ackermann function ($\approx \mathcal{O}(1)$ amortized per DSU operation).
  - Checking edge count takes $\mathcal{O}(1)$. Processing $N - 1$ edges takes nearly linear $\mathcal{O}(N)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - `parent` vector of size $N$.

---

## Why This is Optimal

- Leverages graph theory theorem (`edges.size() == n - 1`) to eliminate adjacency list construction.
- DSU with Path Compression detects cycles in near-constant $\mathcal{O}(\alpha(N))$ time per edge.

---

## Common Mistakes

1. **Forgetting `edges.size() == n - 1` Check**: Without checking edge count, DSU might declare a graph with $N - 2$ edges as non-cyclic without catching that it is disconnected!
2. **Missing Path Compression**: Omitting `parent[i] = find(parent[i])` degrades DSU time complexity to $\mathcal{O}(N)$.
