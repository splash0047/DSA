# Course Schedule

## Pattern Used

- **Pattern**: **Kahn's Algorithm (BFS Topological Sort / Indegree Tracking)**
- **Concept**:
  - Represent dependencies as a Directed Graph: Edge `b -> a` means course `b` must be completed before course `a`.
  - Calculate `indegree[i]` (number of prerequisites remaining) for every course `i`.
  - Enqueue all courses with `indegree[i] == 0` (courses with zero prerequisites).
  - While `!q.empty()`:
    - Pop `curr` course, increment `processedCourses++`.
    - For each course `nextCourse` dependent on `curr`:
      - Decrement `indegree[nextCourse]--`.
      - If `indegree[nextCourse] == 0`, push `nextCourse` into `q`.
  - If `processedCourses == numCourses`, return `true` (all courses completed!). Otherwise return `false` (cycle detected).

---

## Observation

1. Directed Acyclic Graphs (DAGs) always contain at least one node with indegree 0.
2. If a graph contains a directed cycle, nodes within the cycle will NEVER reach an indegree of 0, leaving `processedCourses < numCourses`.

---

## Intuition

Start with the courses that have NO prerequisites. Once you finish a course, remove it as a requirement for all courses that depend on it. If any dependent course now has 0 remaining requirements, take it next. If you manage to finish all courses, you succeed; if you get stuck with unfulfilled prerequisites, a circular dependency (cycle) exists.

---

## Algorithm

1. Build `adj` list and compute `indegree` array for all courses.
2. `queue<int> q`.
3. Push all course `i` with `indegree[i] == 0` into `q`.
4. `count = 0`.
5. While `!q.empty()`:
   a. `curr = q.front(); q.pop();`
   b. `count++`.
   c. For `neighbor` in `adj[curr]`:
      - `indegree[neighbor]--`.
      - If `indegree[neighbor] == 0`: `q.push(neighbor)`.
6. Return `count == numCourses`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <queue>

class Solution {
public:
    bool canFinish(int numCourses, std::vector<std::vector<int>>& prerequisites) {
        std::vector<std::vector<int>> adj(numCourses);
        std::vector<int> indegree(numCourses, 0);
        
        // Build adjacency list and compute indegrees (b -> a)
        for (const auto& req : prerequisites) {
            int course = req[0];
            int prereq = req[1];
            adj[prereq].push_back(course);
            indegree[course]++;
        }
        
        // Push all courses with 0 prerequisites to queue
        std::queue<int> q;
        for (int i = 0; i < numCourses; ++i) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }
        
        int completedCourses = 0;
        
        // Kahn's BFS Process
        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            completedCourses++;
            
            for (int neighbor : adj[curr]) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        
        return completedCourses == numCourses;
    }
};
```

---

## Dry Run

### Input
- `numCourses = 2`, `prerequisites = [[1, 0]]` (0 $\rightarrow$ 1)

### Execution Trace

1. `adj[0] = [1]`, `indegree = [0, 1]`.
2. Initial queue: `q = [0]` (`indegree[0] == 0`).
3. Loop 1: Pop `0`. `completedCourses = 1`.
   - Neighbor `1`: `indegree[1]` decremented to `0` $\implies$ Push `1`. `q = [1]`.
4. Loop 2: Pop `1`. `completedCourses = 2`. `adj[1]` empty.
5. Queue empty. `completedCourses (2) == numCourses (2)`.

### Result
- Output: `true`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(V + E)$
  - Where $V = \text{numCourses}$ and $E = \text{prerequisites.length}$.
  - Building graph takes $\mathcal{O}(V + E)$; BFS visits each node and edge once.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(V + E)$
  - Adjacency list stores $E$ edges across $V$ vertices. Queue and indegree array take $\mathcal{O}(V)$ memory.

---

## Why This is Optimal

- Detects directed graph cycles and calculates course feasibility in single-pass linear time $\mathcal{O}(V + E)$.

---

## Common Mistakes

1. **Reversing Edge Direction**: Mapping `a -> b` instead of `b -> a` alters indegree calculations.
2. **Missing Disconnected Components**: Initial loop MUST scan all nodes `0` to `numCourses - 1` to push all initial 0-indegree nodes.
