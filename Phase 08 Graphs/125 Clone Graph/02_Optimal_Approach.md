# Clone Graph

## Pattern Used

- **Pattern**: **Single-Pass DFS with Hash Map Memoization**
- **Concept**:
  - Maintain a hash map `unordered_map<Node*, Node*> copies` mapping `original_node -> cloned_node`.
  - Recursive helper `cloneDFS(node)`:
    - Base Case 1: `if (node == nullptr) return nullptr;`
    - Base Case 2: `if (copies.count(node)) return copies[node];` (already cloned $\implies$ return memoized clone pointer).
    - Create new node `Node* copy = new Node(node->val)`.
    - Memoize `copies[node] = copy`.
    - For each `neighbor` in `node->neighbors`:
      - `copy->neighbors.push_back(cloneDFS(neighbor));`
    - Return `copy`.

---

## Observation

1. Undirected graphs contain cycles. Without memoizing created nodes, DFS traversal would fall into infinite recursion loops.
2. Registering `copies[node] = copy` BEFORE recursing into neighbors guarantees that cycle references resolve to the existing clone instance seamlessly!

---

## Intuition

As you explore each node in the graph during DFS, immediately create a twin (clone) and record the relationship in your memory map `copies[original] = twin`. When linking twin neighbors, ask: "Has the neighbor been cloned yet?" If yes, return the existing twin. If no, recursively clone it.

---

## Algorithm

1. `unordered_map<Node*, Node*> copies`.
2. `cloneGraph(node)`:
   - If `node == nullptr`, return `nullptr`.
   - If `copies.find(node) != copies.end()`, return `copies[node]`.
   - `copy = new Node(node->val)`.
   - `copies[node] = copy`.
   - For `neighbor` in `node->neighbors`:
     - `copy->neighbors.push_back(cloneGraph(neighbor))`.
   - Return `copy`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <unordered_map>

class Node {
public:
    int val;
    std::vector<Node*> neighbors;
    Node() : val(0), neighbors(std::vector<Node*>()) {}
    Node(int _val) : val(_val), neighbors(std::vector<Node*>()) {}
    Node(int _val, std::vector<Node*> _neighbors) : val(_val), neighbors(_neighbors) {}
};

class Solution {
private:
    std::unordered_map<Node*, Node*> copies;

public:
    Node* cloneGraph(Node* node) {
        if (node == nullptr) {
            return nullptr;
        }
        
        // Return existing clone if node was already visited/cloned
        if (copies.find(node) != copies.end()) {
            return copies[node];
        }
        
        // Instantiate deep copy of current node
        Node* copy = new Node(node->val);
        copies[node] = copy;
        
        // Recursively clone and connect all neighbors
        for (Node* neighbor : node->neighbors) {
            copy->neighbors.push_back(cloneGraph(neighbor));
        }
        
        return copy;
    }
};
```

---

## Dry Run

### Input
- Graph with 2 connected nodes: `1 <-> 2`

### Execution Trace

1. Call `cloneGraph(1)`:
   - `1` not in `copies`. Create `copy1 = new Node(1)`. `copies[1] = copy1`.
   - Neighbor of 1 is `2`. Call `cloneGraph(2)`:
     - `2` not in `copies`. Create `copy2 = new Node(2)`. `copies[2] = copy2`.
     - Neighbor of 2 is `1`. Call `cloneGraph(1)`:
       - `1` IS in `copies` $\implies$ Returns `copy1` immediately!
     - `copy2->neighbors` gets `copy1`.
     - Return `copy2`.
   - `copy1->neighbors` gets `copy2`.
   - Return `copy1`.

### Result
- Deep copy of graph `1 <-> 2` successfully returned.

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(V + E)$
  - Every vertex $V$ and edge $E$ in the graph is visited exactly once.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(V)$
  - Hash map `copies` stores $V$ entries, and recursion stack depth is bounded by $V$.

---

## Why This is Optimal

- Creates a deep copy of the connected graph in optimal single-pass linear time $\mathcal{O}(V + E)$.
- Prevents infinite cycles and duplicate node creation using $\mathcal{O}(V)$ hash map memoization.

---

## Common Mistakes

1. **Memoizing After Recursion**: Inserting `copies[node] = copy` AFTER the neighbor loop causes infinite recursion cycles in undirected graphs.
2. **Shallow Copy**: Returning existing pointers without allocating `new Node(...)`.
