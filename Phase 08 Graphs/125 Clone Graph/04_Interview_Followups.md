# 04 Interview Follow-ups & System Variations: Clone Graph

The problem creates a deep copy of a connected undirected graph where each node contains an integer value and a list of neighbor pointers. Optimal approaches include **DFS** or **BFS** with a `visited` Hash Map mapping `Node* -> Node*` in $\mathcal{O}(V + E)$ time and $\mathcal{O}(V)$ space.

In technical interviews, this problem is extended to distributed graph processing (Apache Giraph / GraphX Pregel model) and massive graph serialization.

---

## 1. Graph Cloning Template with Visited Map

```cpp
unordered_map<Node*, Node*> visited;

Node* cloneGraph(Node* node) {
    if (!node) return nullptr;
    if (visited.count(node)) return visited[node];
    
    Node* clone = new Node(node->val);
    visited[node] = clone;
    
    for (Node* neighbor : node->neighbors) {
        clone->neighbors.push_back(cloneGraph(neighbor));
    }
    return clone;
}
```

---

## 2. Distributed Scale: Cloning Graphs with 1 Billion Vertices (Pregel / Bulk Synchronous Parallel)

### 🛑 Memory & Pointer Limitations
A graph with $10^9$ vertices and $10^{11}$ edges cannot fit in a single server's RAM; pointer-based object graphs cannot cross machine boundaries.

### 💡 Vertex-Centric Message Passing (Bulk Synchronous Parallel)
1. Vertices are partitioned across cluster nodes by `hash(vertex_id) % NUM_MACHINES`.
2. **Superstep 1**: Each machine clones local vertices and broadcasts adjacency requests to remote neighbor hosts.
3. **Superstep 2**: Remote machines reply with newly minted cloned node IDs.
4. **Superstep 3**: Stitch remote edge IDs into adjacency lists without pointers.

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Strategy | Time | Space |
| :--- | :--- | :--- | :--- |
| **In-Memory Graph** | DFS / BFS with Hash Map | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| **Distributed Graph** | Pregel Vertex-Centric Message Passing | $\mathcal{O}(rac{V+E}{M})$ | $\mathcal{O}(rac{V+E}{M})$ / node |
