# Problem Summary

Find the number of connected components in an undirected graph with `n` nodes and `edges`. The optimal approach uses **Disjoint Set Union (Union-Find Component Counter)**:
- Initialize `components = n`.
- For each edge `[u, v]`:
  - `if (dsu.unionSets(u, v))` decrements `components--` when merging two distinct components.
- Return `components`.
This counts connected components in $\mathcal{O}(V + E \cdot \alpha(V))$ time and $\mathcal{O}(V)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to count or track **connected components dynamically** as edges are added.
- Union-Find (DSU) Component Counting pattern.

---

## Important Clues

1. **"Number of connected components in undirected graph"**: Standard DSU problem.
2. **"List of edges"**: DSU edge processing.

---

## Example

### Input
`n = 5`, `edges = [[0,1],[1,2],[3,4]]`

### Visual Step-by-Step Progression

```text
Initial Components: [0], [1], [2], [3], [4] (count = 5)

1. Edge [0,1] -> Union(0,1) -> count = 4
2. Edge [1,2] -> Union(1,2) -> count = 3
3. Edge [3,4] -> Union(3,4) -> count = 2

Components remaining: {0,1,2} and {3,4} -> Result: 2
```

---

## Alternative Solutions

### Adjacency List DFS / BFS ($\mathcal{O}(V + E)$ Time, $\mathcal{O}(V + E)$ Space)
- Build adjacency list and run DFS from unvisited nodes, incrementing component count for each unvisited search trigger.

---

## Edge Cases

1. **No edges**: `edges = []` $\implies$ returns `n` (all nodes isolated).
2. **Fully connected graph**: Returns `1`.
3. **Graph with redundant cycles**: DSU ignores edges within same component (`rootI == rootJ`).

---

## Interview Tips

- **Explain DSU Component Counting Trick**: State *"Initializing `count = n` and decrementing `count--` ONLY when `unionSets` connects two different component roots allows tracking connected components in $\mathcal{O}(\alpha(N))$ per edge without building adjacency lists."*

---

## Similar Problems

1. [LeetCode #547: Number of Provinces](https://leetcode.com/problems/number-of-provinces/)
2. [LeetCode #261: Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)
3. [LeetCode #684: Redundant Connection](https://leetcode.com/problems/redundant-connection/)

---

## Revision Notes

- Problem: Count connected components in undirected graph.
- Pattern: Union-Find with `count = n`.
- Logic: `dsu.unionSets(u, v)` decrements `count--` on valid component merge.
- Result: `return dsu.getCount();`
- Optimal Complexity: Time $\mathcal{O}(V + E \cdot \alpha(V))$, Space $\mathcal{O}(V)$.
