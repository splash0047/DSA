# Problem Summary

Given a reference to a node in a connected undirected graph, return a deep copy (clone) of the graph. The optimal approach uses **Single-Pass DFS with Hash Map Memoization**:
- Maintain `unordered_map<Node*, Node*> copies` mapping `{orig_node -> clone_node}`.
- Helper `cloneGraph(node)`:
  - Base case 1: `if (!node) return nullptr;`
  - Base case 2: `if (copies.count(node)) return copies[node];`
  - Create `copy = new Node(node->val)`, store `copies[node] = copy`.
  - Recurse neighbors: `copy->neighbors.push_back(cloneGraph(neighbor));`
  - Return `copy`.
This clones the graph in $\mathcal{O}(V + E)$ time and $\mathcal{O}(V)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **deep copy / clone a graph or complex pointer structure with cycles** (e.g. Copy List with Random Pointer).
- Memoized Graph DFS/BFS pattern.

---

## Important Clues

1. **"Deep copy of undirected graph"**: Must allocate new node instances.
2. **"Undirected graph / cycles present"**: Must use hash map memoization to prevent infinite loop cycles.

---

## Example

### Input
`1 <-> 2`

### Visual Step-by-Step Progression

```text
DFS Call Stack:
1. Visit Node 1:
   - Create Copy(1)
   - Store copies[1] = Copy(1)
   - Recurse neighbor Node 2

2. Visit Node 2:
   - Create Copy(2)
   - Store copies[2] = Copy(2)
   - Recurse neighbor Node 1 -> copies[1] exists! Returns Copy(1)
   - Copy(2)->neighbors = [Copy(1)]

3. Unwind back to Node 1:
   - Copy(1)->neighbors = [Copy(2)]

Return Copy(1)
```

---

## Alternative Solutions

### Queue-Based BFS with Memoization ($\mathcal{O}(V + E)$ Time, $\mathcal{O}(V)$ Space)
- Use `std::queue<Node*>` and map `copies` to clone nodes level-by-level in BFS order.

---

## Edge Cases

1. **Empty graph**: `node = nullptr` $\implies$ returns `nullptr`.
2. **Single node without neighbors**: Returns cloned single node.
3. **Graph with self-loops or double edges**: Handled automatically by `copies` map lookups.

---

## Interview Tips

- **Explain Early Map Registration**: State *"Registering `copies[node] = copy` BEFORE recursing into neighbor calls is critical because it breaks cycles in undirected graphs. If a neighbor points back to `node`, `copies[node]` is returned immediately."*

---

## Similar Problems

1. [LeetCode #138: Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)
2. [LeetCode #1490: Clone N-ary Tree](https://leetcode.com/problems/clone-n-ary-tree/)
3. [LeetCode #1485: Clone Binary Tree With Random Pointer](https://leetcode.com/problems/clone-binary-tree-with-random-pointer/)

---

## Revision Notes

- Problem: Deep copy of undirected graph.
- Pattern: DFS with `unordered_map<Node*, Node*> copies`.
- Logic: `if (copies.count(node)) return copies[node]; copy = new Node(val); copies[node] = copy; for (n : node->neighbors) copy->neighbors.push_back(cloneGraph(n));`
- Crucial step: Store in map BEFORE entering loop.
- Optimal Complexity: Time $\mathcal{O}(V + E)$, Space $\mathcal{O}(V)$.
