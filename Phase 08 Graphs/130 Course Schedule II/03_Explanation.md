# Problem Summary

Return a valid ordering of courses to complete all `numCourses` given prerequisite pairs `[a, b]` (take `b` before `a`). Return `{}` if impossible (cycle exists). The optimal approach uses **Kahn's Algorithm (BFS Topological Sort)**:
- Build directed graph `b -> a` and compute `indegree` for every course.
- Push all 0-indegree courses into a `queue<int> q`.
- While `!q.empty()`:
  - Pop `curr`, append to `order`.
  - Decrement `indegree` of all neighbors `neighbor`. If `indegree[neighbor] == 0`, push to `q`.
- Return `order.size() == numCourses ? order : vector<int>{}`.
This computes topological ordering in $\mathcal{O}(V + E)$ time and $\mathcal{O}(V + E)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **find a valid execution order / topological sequence** for dependent tasks.
- Topological Sort Ordering pattern.

---

## Important Clues

1. **"Return ordering of courses you should take"**: Topological Sort.
2. **"Return empty array if impossible"**: Cycle detection check `order.size() == numCourses`.

---

## Example

### Input
`numCourses = 4`, `prerequisites = [[1,0],[2,0],[3,1],[3,2]]`

### Visual Step-by-Step Progression

```text
Dependencies:
0 -> 1 -> 3
0 -> 2 -> 3

BFS Order:
- 0 has indegree 0 -> Take 0 -> Order: [0]
- 1 & 2 now have indegree 0 -> Take 1, 2 -> Order: [0, 1, 2]
- 3 now has indegree 0 -> Take 3 -> Order: [0, 1, 2, 3]

Result: [0, 1, 2, 3]
```

---

## Alternative Solutions

### Post-Order DFS with Stack reversing ($\mathcal{O}(V + E)$ Time, $\mathcal{O}(V + E)$ Space)
- Perform DFS with 3-state cycle detection. Push nodes to a stack upon exiting recursion, then reverse/pop stack.

---

## Edge Cases

1. **No prerequisites**: `prerequisites = []` $\implies$ returns `[0, 1, ..., numCourses - 1]`.
2. **Circular dependency**: `prerequisites = [[1, 0], [0, 1]]` $\implies$ returns `[]`.
3. **Disconnected components**: Independent prerequisite trees merged into valid total order.

---

## Interview Tips

- **Compare Course Schedule I vs II**: State *"Course Schedule I only requires returning a boolean indicating if a topological sort is possible (`count == numCourses`), whereas Course Schedule II asks for the actual topological ordering vector produced during BFS."*

---

## Similar Problems

1. [LeetCode #207: Course Schedule](https://leetcode.com/problems/course-schedule/)
2. [LeetCode #269: Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)
3. [LeetCode #1203: Sort Items by Groups Respecting Dependencies](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/)

---

## Revision Notes

- Problem: Find valid topological course ordering.
- Pattern: Kahn's BFS Topological Sort.
- Queue Init: Enqueue 0-indegree courses.
- Loop: `curr = q.front(); q.pop(); order.push_back(curr); for (n) { if (--indegree[n] == 0) q.push(n); }`
- Result: `return order.size() == numCourses ? order : {};`
- Optimal Complexity: Time $\mathcal{O}(V + E)$, Space $\mathcal{O}(V + E)$.
