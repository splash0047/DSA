# Problem Summary

Determine if an undirected graph of `n` nodes and `edges` forms a valid tree. A graph is a valid tree if it is fully connected and contains no cycles. The optimal approach uses **Union-Find (DSU with Path Compression)**:
- First, check fundamental tree theorem: `if (edges.size() != n - 1) return false;`
- Initialize DSU for `n` nodes.
- For each edge `[u, v]`:
  - `if (!dsu.unionSets(u, v)) return false;` (cycle detected!).
- If all $N - 1$ edges are merged safely, return `true`.
This verifies valid tree properties in $\mathcal{O}(N \cdot \alpha(N))$ time and $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to determine if a **graph is a valid tree / acyclic connected component**.
- Tree Theorem + Union-Find (DSU) pattern.

---

## Important Clues

1. **"Valid tree of n nodes"**: Must have $N - 1$ edges + no cycles + 1 connected component.
2. **"Undirected edges"**: Union-Find `unionSets(u, v)`.

---

## Example

### Input
`n = 5`, `edges = [[0,1],[0,2],[0,3],[1,4]]`

### Visual Step-by-Step Progression

```text
        0
      / | \
     1  2  3
    /
   4

1. edges.size() = 4 == 5 - 1 -> OK
2. Union [0,1] -> OK
3. Union [0,2] -> OK
4. Union [0,3] -> OK
5. Union [1,4] -> OK

Result: true
```

---

## Alternative Solutions

### DFS Cycle & Connectivity Check ($\mathcal{O}(V + E)$ Time, $\mathcal{O}(V + E)$ Space)
- Build adjacency list, run DFS from node 0 with parent tracking to detect cycles, then verify `visited.size() == n`.

---

## Edge Cases

1. **Disconnected graph with $N - 1$ edges**: Impossible if no cycles exist.
2. **Graph with redundant cycle edge**: `edges.size() != n - 1` catches it immediately.
3. **Single node graph**: `n = 1`, `edges = []` $\implies$ returns `true`.

---

## Interview Tips

- **Highlight the Tree Theorem**: State *"A graph with $N$ nodes is a tree if and only if it has $N - 1$ edges and no cycles. Checking `edges.size() == n - 1` up front means cycle freedom guarantees complete connectivity."*

---

## Similar Problems

1. [LeetCode #323: Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)
2. [LeetCode #684: Redundant Connection](https://leetcode.com/problems/redundant-connection/)
3. [LeetCode #547: Number of Provinces](https://leetcode.com/problems/number-of-provinces/)

---

## Revision Notes

- Problem: Check if undirected graph forms a valid tree.
- Pattern: Tree Theorem (`edges.size() == n - 1`) + Union-Find.
- Property 1: `if (edges.size() != n - 1) return false;`
- Property 2: `for (edge) if (!dsu.unionSets(u, v)) return false;`
- Return `true`.
- Optimal Complexity: Time $\mathcal{O}(N \cdot \alpha(N))$, Space $\mathcal{O}(N)$.
