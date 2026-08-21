# 04 Interview Follow-ups & System Variations: Course Schedule II

The problem returns a valid ordering of courses you should take to finish all courses (Topological Sort). Optimal approaches include **Kahn's BFS Algorithm** appending nodes to an `order` list in $\mathcal{O}(V + E)$ time and $\mathcal{O}(V + E)$ space.

In technical interviews, this problem is compared with parallel compilation job graphs (Make, Ninja, Bazel) and detecting all valid orderings.

---

## 1. Build Systems & Multi-Core Parallel Job Compilation (Ninja / Bazel)

### 💡 Parallel Topological Execution
- When building large software codebases (like Linux or Chrome):
  - Every source file is a vertex; dependencies are directed edges.
  - All nodes with `in_degree == 0` can be compiled **simultaneously in parallel across multiple CPU cores**!
  - As a file finishes compiling, decrement in-degrees of dependent files; when any hits 0, push to the thread pool work queue.

---

## Summary Matrix: Trade-offs at a Glance

| Output Goal | Algorithm | Time | Space |
| :--- | :--- | :--- | :--- |
| **Boolean Check (I)** | Kahn's count check | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ |
| **1 Valid Order (II)** | Kahn's `order` vector append | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ |
| **All Valid Orders** | Backtracking DFS with In-degrees | $\mathcal{O}(V!)$ | $\mathcal{O}(V)$ |
