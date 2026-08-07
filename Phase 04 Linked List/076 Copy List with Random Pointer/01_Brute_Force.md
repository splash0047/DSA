# Copy List with Random Pointer

- **Problem Number**: 138
- **Platform**: LeetCode #138
- **Difficulty**: Medium
- **Pattern**: Hash Map Mapping

---

## Brute Force Intuition

Use a Hash Map `unordered_map<Node*, Node*> old_to_new` mapping each original node pointer to its newly instantiated clone node pointer.
1. Pass 1: Traverse the list and instantiate a new clone node for every original node, populating `old_to_new[curr] = new Node(curr->val)`.
2. Pass 2: Traverse the list again and wire the `next` and `random` pointers of each cloned node using the Hash Map lookups:
   - `old_to_new[curr]->next = old_to_new[curr->next]`
   - `old_to_new[curr]->random = old_to_new[curr->random]`

---

## Algorithm

1. If `head == nullptr`, return `nullptr`.
2. `old_to_new = unordered_map<Node*, Node*>()`.
3. `curr = head`.
4. Pass 1: While `curr != nullptr`:
   - `old_to_new[curr] = new Node(curr->val)`.
   - `curr = curr->next`.
5. `curr = head`.
6. Pass 2: While `curr != nullptr`:
   - `old_to_new[curr]->next = old_to_new[curr->next]`.
   - `old_to_new[curr]->random = old_to_new[curr->random]`.
   - `curr = curr->next`.
7. Return `old_to_new[head]`.

---

## Code

```cpp
#include <unordered_map>

class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = nullptr;
        random = nullptr;
    }
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == nullptr) return nullptr;
        
        std::unordered_map<Node*, Node*> old_to_new;
        
        // Pass 1: Create all new nodes and map old -> new
        Node* curr = head;
        while (curr != nullptr) {
            old_to_new[curr] = new Node(curr->val);
            curr = curr->next;
        }
        
        // Pass 2: Wire next and random pointers
        curr = head;
        while (curr != nullptr) {
            old_to_new[curr]->next = old_to_new[curr->next];
            old_to_new[curr]->random = old_to_new[curr->random];
            curr = curr->next;
        }
        
        return old_to_new[head];
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Two passes over $N$ nodes; Hash Map lookups take $\mathcal{O}(1)$ average time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Hash Map stores $N$ pointer pairs.

---

## Why This Approach Is Not Optimal

Using a Hash Map requires $\mathcal{O}(N)$ auxiliary space. By using **Interleaved Node Weaving (Node Cloning In-Place)**, we can achieve deep copy in $\mathcal{O}(N)$ time with $\mathcal{O}(1)$ auxiliary space.
