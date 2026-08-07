# Number of Connected Components in an Undirected Graph

## Pattern Used

- **Pattern**: **Disjoint Set Union (Union-Find Component Counter)**
- **Concept**:
  - Initially, assume every node is its own separate connected component $\implies$ `components = n`.
  - For each edge `[u, v]` in `edges`:
    - Union sets of `u` and `v`.
    - If `u` and `v` belonged to different components (`find(u) != find(v)`):
      - Merge components and decrement `components--`.
  - At the end of processing all edges, return `components`.

---

## Observation

1. Each successful union operation between two previously disconnected components reduces the total number of connected components by exactly 1.
2. Union-Find with Path Compression and Rank performs union operations in near-constant $\mathcal{O}(\alpha(N))$ time without requiring graph adjacency lists.

---

## Intuition

Start with $N$ isolated islands (components $= N$). Every time an edge connects two previously unconnected islands, they merge into 1 island, so the total count of distinct islands drops by 1.

---

## Algorithm

1. `components = n`.
2. Initialize DSU parent array `parent[i] = i`.
3. For each edge `[u, v]` in `edges`:
   - `rootU = find(u)`, `rootV = find(v)`.
   - If `rootU != rootV`:
     - `parent[rootU] = rootV`.
     - `components--`.
4. Return `components`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <numeric>

class UnionFind {
private:
    std::vector<int> parent;
    int count;

public:
    UnionFind(int n) : count(n) {
        parent.resize(n);
        std::iota(parent.begin(), parent.end(), 0);
    }
    
    int find(int i) {
        if (parent[i] == i)
            return i;
        return parent[i] = find(parent[i]); // Path Compression
    }
    
    void unionSets(int i, int j) {
        int rootI = find(i);
        int rootJ = find(j);
        
        if (rootI != rootJ) {
            parent[rootI] = rootJ;
            count--; // Merged two distinct components
        }
    }
    
    int getCount() const {
        return count;
    }
};

class Solution {
public:
    int countComponents(int n, std::vector<std::vector<int>>& edges) {
        UnionFind dsu(n);
        
        for (const auto& edge : edges) {
            dsu.unionSets(edge[0], edge[1]);
        }
        
        return dsu.getCount();
    }
};
```

---

## Dry Run

### Input
- `n = 5`, `edges = [[0,1],[1,2],[3,4]]`

### Execution Trace

1. `count = 5`.
2. Edge `[0, 1]`: `find(0) != find(1)` $\implies$ Union `0` & `1`. `count = 4`.
3. Edge `[1, 2]`: `find(1) != find(2)` $\implies$ Union `1` & `2`. `count = 3`.
4. Edge `[3, 4]`: `find(3) != find(4)` $\implies$ Union `3` & `4`. `count = 2`.

### Result
- Output: `2`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(V + E \cdot \alpha(V))$
  - Where $\alpha(V)$ is the inverse Ackermann function. DSU operations run in near-constant time per edge.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(V)$
  - Stores `parent` array of size $V$.

---

## Why This is Optimal

- Avoids building adjacency lists ($\mathcal{O}(E)$ allocation overhead).
- Operates in linear time $\mathcal{O}(V + E \cdot \alpha(V))$ with minimal auxiliary space.

---

## Common Mistakes

1. **Not Decrementing Count Only on New Unions**: Decrementing `count` even when `rootI == rootJ` (redundant edge within same component).
2. **Missing Path Compression**: Forgetting `parent[i] = find(parent[i])`.
