# Problem Summary

Determine if it is possible to complete all `numCourses` given prerequisite constraints `[a, b]` (must take `b` before `a`). This is equivalent to checking if a directed graph contains NO cycles. The optimal approach uses **Kahn's Algorithm (BFS Topological Sort)**:
- Build directed graph `b -> a` and compute `indegree` for every course.
- Push all courses with `indegree == 0` into a `queue<int> q`.
- While `!q.empty()`:
  - Pop `curr`, increment `completedCourses++`.
  - Decrement `indegree` of all neighbors `b`. If `indegree[b] == 0`, push `b`.
- Return `completedCourses == numCourses`.
This evaluates course completion feasibility in $\mathcal{O}(V + E)$ time and $\mathcal{O}(V + E)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to process tasks with **prerequisite dependencies / ordering constraints**.
- Topological Sort / Cycle Detection pattern in Directed Graphs.

---

## Important Clues

1. **"Must take course B before course A"**: Directed edge $B \rightarrow A$.
2. **"Can you finish all courses?"**: Check if directed graph is a DAG (no cycles).

---

## Example

### Input
`numCourses = 2`, `prerequisites = [[1,0]]` (0 -> 1)

### Visual Step-by-Step Progression

```text
Graph: 0 -> 1
Indegrees: [0: 0, 1: 1]

Queue Init: [0]
1. Pop 0 -> completed = 1 -> Decrement indegree[1] to 0 -> Push 1
2. Pop 1 -> completed = 2

completed (2) == numCourses (2) -> TRUE
```

---

## Alternative Solutions

### 3-State DFS Cycle Detection ($\mathcal{O}(V + E)$ Time, $\mathcal{O}(V + E)$ Space)
- Use node states: `0` (Unvisited), `1` (Visiting/In current recursion stack), `2` (Visited/Verified safe). If DFS hits state `1`, a cycle exists.

---

## Edge Cases

1. **No prerequisites**: `prerequisites = []` $\implies$ returns `true`.
2. **Self-cycle**: `prerequisites = [[0, 0]]` $\implies$ returns `false`.
3. **Disconnected Components**: Multiple independent prerequisite chains.

---

## Interview Tips

- **Explain Kahn's Algorithm Logic**: State *"Kahn's BFS processes nodes with 0 indegree (zero remaining prerequisites). If a cycle exists, nodes in the cycle never reach 0 indegree, so `completedCourses` will be strictly less than `numCourses`."*

---

## Similar Problems

1. [LeetCode #210: Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
2. [LeetCode #269: Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)
3. [LeetCode #310: Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/)

---

## Revision Notes

- Problem: Check if course prerequisites form a valid DAG (no cycles).
- Pattern: Kahn's BFS Topological Sort.
- Steps: Compute `indegree`, queue 0-indegree nodes, pop & decrement neighbors, push new 0-indegrees, count popped.
- Condition: `return completedCourses == numCourses;`
- Optimal Complexity: Time $\mathcal{O}(V + E)$, Space $\mathcal{O}(V + E)$.
