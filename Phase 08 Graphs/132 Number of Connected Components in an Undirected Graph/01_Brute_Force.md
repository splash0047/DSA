# Number of Connected Components in an Undirected Graph

- **Problem Number**: 323
- **Platform**: LeetCode #323
- **Difficulty**: Medium
- **Pattern**: Adjacency List DFS / BFS Traversal

---

## Brute Force Intuition

Build an undirected adjacency list `adj` for the graph. Maintain a `visited` boolean array initialized to `false`. Iterate through all nodes `0` to `n - 1`. Whenever an unvisited node `i` is encountered:
- Increment `components++`.
- Launch a recursive DFS from node `i` to mark all reachable nodes in `visited`.

---

## Algorithm

1. Build `adj` list for all undirected edges `[u, v]`.
2. `visited` boolean array of size `n` initialized to `false`.
3. `components = 0`.
4. For `i` from `0` to `n - 1`:
   - If `!visited[i]`:
     - `components++`.
     - `dfs(i, adj, visited)`.
5. `dfs(node)`:
   - `visited[node] = true`.
   - For `neighbor` in `adj[node]`:
     - If `!visited[neighbor]`: `dfs(neighbor)`.
6. Return `components`.

---

## Code

```cpp
#include <vector>

class Solution {
private:
    void dfs(int node, const std::vector<std::vector<int>>& adj, std::vector<bool>& visited) {
        visited[node] = true;
        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                dfs(neighbor, adj, visited);
            }
        }
    }

public:
    int countComponents(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<int>> adj(n);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        
        std::vector<bool> visited(n, false);
        int components = 0;
        
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                components++;
                dfs(i, adj, visited);
            }
        }
        
        return components;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(V + E)$
  - Building adjacency list takes $\mathcal{O}(V + E)$. DFS visits each vertex and edge once.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(V + E)$
  - Adjacency list and `visited` array take $\mathcal{O}(V + E)$ memory.

---

## Why This Approach Is Not Optimal

DFS works well, but allocating explicit adjacency lists and call stack memory takes extra space. Using **Disjoint Set Union (Union-Find)**, we can count components dynamically in near-constant $\mathcal{O}(E \cdot \alpha(V))$ time without building adjacency lists!
