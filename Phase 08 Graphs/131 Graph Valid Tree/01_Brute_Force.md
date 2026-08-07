# Graph Valid Tree

- **Problem Number**: 261
- **Platform**: LeetCode #261
- **Difficulty**: Medium
- **Pattern**: Undirected DFS Cycle & Connectivity Check

---

## Brute Force Intuition

A graph of $N$ nodes is a valid tree if and only if:
1. `edges.size() == n - 1` (a tree of $N$ nodes MUST have exactly $N - 1$ edges).
2. It contains no cycles and is fully connected.

We can run a DFS from node `0` tracking parent nodes to detect undirected cycles, while populating a `visited` set to ensure all $N$ nodes are connected.

---

## Algorithm

1. If `edges.size() != n - 1`, return `false` immediately.
2. Build undirected adjacency list `adj`.
3. `visited` boolean array initialized to `false`.
4. Run `hasCycle(0, -1, adj, visited)`:
   - If `hasCycle` returns `true`, return `false`.
5. Check if all nodes were visited: if any `visited[i] == false`, return `false`.
6. Return `true`.

---

## Code

```cpp
#include <vector>

class Solution {
private:
    bool hasCycle(int node, int parent, const std::vector<std::vector<int>>& adj, std::vector<bool>& visited) {
        visited[node] = true;
        
        for (int neighbor : adj[node]) {
            if (neighbor == parent) continue; // Skip immediate parent edge
            
            if (visited[neighbor]) {
                return true; // Cycle detected!
            }
            
            if (hasCycle(neighbor, node, adj, visited)) {
                return true;
            }
        }
        
        return false;
    }

public:
    bool validTree(int n, std::vector<std::vector<int>>& edges) {
        // Quick edge count check for tree property
        if (edges.size() != n - 1) return false;
        
        std::vector<std::vector<int>> adj(n);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        
        std::vector<bool> visited(n, false);
        
        if (hasCycle(0, -1, adj, visited)) {
            return false;
        }
        
        // Ensure all nodes belong to single connected component
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) return false;
        }
        
        return true;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(V + E)$
  - Edge count check takes $\mathcal{O}(1)$. DFS traversal visits all $V$ vertices and $E$ edges once.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(V + E)$
  - Adjacency list and call stack memory.

---

## Why This Approach Is Not Optimal

DFS works, but **Disjoint Set Union (DSU / Union-Find with Path Compression and Rank)** is the industry-standard optimal approach for dynamic graph cycle detection and component union without needing explicit adjacency lists!
