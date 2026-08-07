# Course Schedule

- **Problem Number**: 207
- **Platform**: LeetCode #207
- **Difficulty**: Medium
- **Pattern**: Unmemoized Cycle Detection Search

---

## Brute Force Intuition

Model course prerequisites as a Directed Graph where an edge `b -> a` exists if course `b` is a prerequisite for course `a`. The problem of determining whether all courses can be finished is equivalent to checking if the directed graph has **NO directed cycles**.

A naive brute force approach runs a full DFS path traversal from every course node to see if any path loops back to an already visited node in the current traversal path.

---

## Algorithm

1. Build adjacency list `adj` for directed graph ($b \rightarrow a$).
2. For each course `i` from `0` to `numCourses - 1`:
   - `visited` set for current path traversal.
   - `if (hasCycle(i, adj, visited)) return false;`
3. Return `true`.

---

## Code

```cpp
#include <vector>
#include <unordered_set>

class Solution {
private:
    bool hasCycle(int node, const std::vector<std::vector<int>>& adj, std::unordered_set<int>& path) {
        if (path.count(node)) return true; // Cycle detected!
        
        path.insert(node);
        for (int neighbor : adj[node]) {
            if (hasCycle(neighbor, adj, path)) {
                return true;
            }
        }
        path.erase(node); // Backtrack
        
        return false;
    }

public:
    bool canFinish(int numCourses, std::vector<std::vector<int>>& prerequisites) {
        std::vector<std::vector<int>> adj(numCourses);
        for (const auto& req : prerequisites) {
            adj[req[1]].push_back(req[0]);
        }
        
        for (int i = 0; i < numCourses; ++i) {
            std::unordered_set<int> path;
            if (hasCycle(i, adj, path)) {
                return false;
            }
        }
        
        return true;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(V \times (V + E))$
  - Running unmemoized cycle search from every vertex leads to quadratic/exponential time complexity in dense graphs.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(V + E)$
  - Adjacency list and path set memory.

---

## Why This Approach Is Not Optimal

Re-traversing previously verified cycle-free subgraphs takes quadratic time. Using **Kahn's Algorithm (Kahn's BFS Topological Sort)** or **3-State DFS (Visited Array)**, we can detect cycles in linear $\mathcal{O}(V + E)$ time!
