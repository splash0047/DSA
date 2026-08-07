# Clone Graph

- **Problem Number**: 133
- **Platform**: LeetCode #133
- **Difficulty**: Medium
- **Pattern**: Two-Pass Graph Copy (Create Nodes then Copy Edges)

---

## Brute Force Intuition

1. Perform a First-Pass DFS/BFS traversal to visit every node in the graph, creating a new cloned node `new Node(node->val)` for every original node and storing the mapping in an `unordered_map<Node*, Node*> copies`.
2. Perform a Second-Pass traversal over all original nodes, and for each neighbor of an original node, append `copies[neighbor]` to `copies[original_node]->neighbors`.

---

## Algorithm

1. `unordered_map<Node*, Node*> copies`.
2. First Pass: Traverse original graph (using BFS/DFS) and store `copies[node] = new Node(node->val)`.
3. Second Pass: For each `[origNode, cloneNode]` in `copies`:
   - For each `neighbor` in `origNode->neighbors`:
     - `cloneNode->neighbors.push_back(copies[neighbor])`.
4. Return `copies[node]`.

---

## Code

```cpp
#include <vector>
#include <unordered_map>
#include <queue>

class Node {
public:
    int val;
    std::vector<Node*> neighbors;
    Node() : val(0), neighbors(std::vector<Node*>()) {}
    Node(int _val) : val(_val), neighbors(std::vector<Node*>()) {}
    Node(int _val, std::vector<Node*> _neighbors) : val(_val), neighbors(_neighbors) {}
};

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (node == nullptr) return nullptr;
        
        std::unordered_map<Node*, Node*> copies;
        std::queue<Node*> q;
        
        // Pass 1: Create all node copies
        q.push(node);
        copies[node] = new Node(node->val);
        
        while (!q.empty()) {
            Node* curr = q.front();
            q.pop();
            
            for (Node* neighbor : curr->neighbors) {
                if (copies.find(neighbor) == copies.end()) {
                    copies[neighbor] = new Node(neighbor->val);
                    q.push(neighbor);
                }
            }
        }
        
        // Pass 2: Connect neighbor pointers
        for (const auto& [origNode, cloneNode] : copies) {
            for (Node* neighbor : origNode->neighbors) {
                cloneNode->neighbors.push_back(copies[neighbor]);
            }
        }
        
        return copies[node];
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(V + E)$
  - First pass visits all $V$ nodes and $E$ edges; second pass connects all $E$ edges. Total time $= \mathcal{O}(V + E)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(V)$
  - Hash map and queue store all $V$ nodes.

---

## Why This Approach Is Not Optimal

Doing two separate passes requires redundant iteration over all nodes and edges. Using **Single-Pass DFS / BFS with Memoization**, we can clone nodes and connect neighbor pointers simultaneously in a single pass!
