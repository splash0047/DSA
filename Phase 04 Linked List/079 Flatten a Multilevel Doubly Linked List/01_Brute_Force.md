# Flatten a Multilevel Doubly Linked List

- **Problem Number**: 430
- **Platform**: LeetCode #430
- **Difficulty**: Medium
- **Pattern**: Stack DFS Preorder Traversal

---

## Brute Force Intuition

Treat the multilevel doubly linked list as a tree where `child` is the left branch and `next` is the right branch. Perform Preorder DFS using an explicit Stack to collect all nodes into a linear list, then reconstruct `next`, `prev`, and `child = nullptr` connections.

---

## Algorithm

1. If `head == nullptr`, return `nullptr`.
2. Push `head` onto a stack `st`.
3. Collect all nodes in preorder sequence into `vector<Node*> nodes`.
4. While `st` is not empty:
   a. `curr = st.top()`, `st.pop()`.
   b. `nodes.push_back(curr)`.
   c. If `curr->next != nullptr`, push `curr->next`.
   d. If `curr->child != nullptr`, push `curr->child`.
5. Re-link doubly linked list:
   - For `i` from `0` to `nodes.size() - 2`:
     - `nodes[i]->next = nodes[i + 1]`.
     - `nodes[i + 1]->prev = nodes[i]`.
     - `nodes[i]->child = nullptr`.
   - `nodes.back()->child = nullptr`.
   - `nodes.back()->next = nullptr`.
6. Return `nodes[0]`.

---

## Code

```cpp
#include <vector>
#include <stack>

class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};

class Solution {
public:
    Node* flatten(Node* head) {
        if (head == nullptr) return nullptr;
        
        std::stack<Node*> st;
        std::vector<Node*> nodes;
        st.push(head);
        
        while (!st.empty()) {
            Node* curr = st.top();
            st.pop();
            nodes.push_back(curr);
            
            if (curr->next != nullptr) st.push(curr->next);
            if (curr->child != nullptr) st.push(curr->child);
        }
        
        for (size_t i = 0; i < nodes.size() - 1; ++i) {
            nodes[i]->next = nodes[i + 1];
            nodes[i + 1]->prev = nodes[i];
            nodes[i]->child = nullptr;
        }
        nodes.back()->child = nullptr;
        nodes.back()->next = nullptr;
        
        return nodes[0];
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Stack traversal and vector re-stitching take $\mathcal{O}(N)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Stack and vector store $N$ node pointers.

---

## Why This Approach Is Not Optimal

Using a vector requires $\mathcal{O}(N)$ auxiliary memory. By using **In-Place Iterative Splice Re-linking**, we can flatten the multilevel list directly in-place with $\mathcal{O}(1)$ auxiliary space.
