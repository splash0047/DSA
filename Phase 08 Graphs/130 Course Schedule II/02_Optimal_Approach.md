# Course Schedule II

## Pattern Used

- **Pattern**: **Kahn's Algorithm (BFS Topological Sort / Topological Ordering Array)**
- **Concept**:
  - Model prerequisite pairs `[a, b]` as directed edges $b \rightarrow a$ (taking course $b$ unlocks course $a$).
  - Calculate `indegree` (number of incoming prerequisite edges) for all courses.
  - Enqueue all courses with `indegree == 0` into `queue<int> q`.
  - While `!q.empty()`:
    - Pop `curr` course and append to `order` vector.
    - For each `neighbor` course depending on `curr`:
      - Decrement `indegree[neighbor]--`.
      - If `indegree[neighbor] == 0`, push `neighbor` into `q`.
  - If `order.size() == numCourses`, return `order`. Else return `{}` (cycle exists!).

---

## Observation

1. In a Directed Acyclic Graph (DAG), popping nodes with indegree 0 sequentially produces a valid **Topological Sort Order**.
2. If the graph contains a cycle, nodes within the cycle will never reach 0 indegree, so `order.size()` will be less than `numCourses`.

---

## Intuition

Start by adding all courses that have NO prerequisites to your course schedule. As each course is completed, remove it from the prerequisite requirements of its dependent courses. Whenever a dependent course has zero remaining prerequisites, append it to your schedule.

---

## Algorithm

1. Build `adj` list ($b \rightarrow a$) and `indegree` array.
2. `queue<int> q`, `vector<int> order`.
3. Push all course `i` with `indegree[i] == 0` into `q`.
4. While `!q.empty()`:
   a. `curr = q.front(); q.pop();`
   b. `order.push_back(curr);`
   c. For `neighbor` in `adj[curr]`:
      - `indegree[neighbor]--`.
      - If `indegree[neighbor] == 0`: `q.push(neighbor)`.
5. Return `order.size() == numCourses ? order : vector<int>{}`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <queue>

class Solution {
public:
    std::vector<int> findOrder(int numCourses, std::vector<std::vector<int>>& prerequisites) {
        std::vector<std::vector<int>> adj(numCourses);
        std::vector<int> indegree(numCourses, 0);
        
        // Build graph: prereq -> course
        for (const auto& req : prerequisites) {
            int course = req[0];
            int prereq = req[1];
            adj[prereq].push_back(course);
            indegree[course]++;
        }
        
        // Enqueue courses with zero prerequisites
        std::queue<int> q;
        for (int i = 0; i < numCourses; ++i) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }
        
        std::vector<int> order;
        order.reserve(numCourses);
        
        // BFS Topological Sort
        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            order.push_back(curr);
            
            for (int neighbor : adj[curr]) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        
        // Return order if all courses can be taken, else return empty vector
        if (order.size() == numCourses) {
            return order;
        }
        return {};
    }
};
```

---

## Dry Run

### Input
- `numCourses = 4`, `prerequisites = [[1,0],[2,0],[3,1],[3,2]]`

### Execution Trace

1. `adj`: `0 -> [1, 2]`, `1 -> [3]`, `2 -> [3]`.
2. `indegree`: `[0:0, 1:1, 2:1, 3:2]`.
3. Initial Queue: `q = [0]`. `order = []`.
4. Pop `0`: `order = [0]`. Decrement indegree: `indegree[1]=0`, `indegree[2]=0`. `q = [1, 2]`.
5. Pop `1`: `order = [0, 1]`. Decrement indegree: `indegree[3]=1`.
6. Pop `2`: `order = [0, 1, 2]`. Decrement indegree: `indegree[3]=0` $\implies$ `q = [3]`.
7. Pop `3`: `order = [0, 1, 2, 3]`.
8. `order.size() == 4 == numCourses`.

### Result
- Output: `[0, 1, 2, 3]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(V + E)$
  - Building adjacency list and computing indegrees takes $\mathcal{O}(V + E)$. BFS visits every vertex and edge once.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(V + E)$
  - Adjacency list stores $E$ edges across $V$ vertices. Queue and result array take $\mathcal{O}(V)$ memory.

---

## Why This is Optimal

- Computes a valid topological course sequence in optimal single-pass linear time $\mathcal{O}(V + E)$.

---

## Common Mistakes

1. **Returning Partial Order on Cycle**: Returning incomplete `order` array instead of `{}` when a cycle exists.
2. **Pushing Courses with Non-Zero Indegree**: Enqueuing courses before their indegree reaches `0`.
