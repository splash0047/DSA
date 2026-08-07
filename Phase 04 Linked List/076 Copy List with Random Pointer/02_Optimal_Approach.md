# Copy List with Random Pointer

## Pattern Used

- **Pattern**: **Interleaved Node Weaving (In-Place Pointer Modification)**
- **Concept**:
  1. **Pass 1 (Interleave Clones)**: Create cloned nodes and insert each cloned node directly after its original node ($A \rightarrow A' \rightarrow B \rightarrow B' \rightarrow C \rightarrow C'$).
  2. **Pass 2 (Wire Random Pointers)**: For each original node `curr`, set `curr->next->random = (curr->random) ? curr->random->next : nullptr`.
  3. **Pass 3 (Separate Lists)**: Separate the interleaved list back into original list and copied cloned list.

---

## Observation

1. Interleaving each cloned node $A'$ immediately after original node $A$ creates an implicit $\mathcal{O}(1)$ mapping!
2. The cloned node $A'$ is simply $A \rightarrow \text{next}$.
3. The cloned target of $A \rightarrow \text{random}$ is simply $A \rightarrow \text{random} \rightarrow \text{next}$!
4. This completely eliminates the need for an external Hash Map.

---

## Intuition

Weave new clone nodes directly alongside original nodes inside the linked list. Copy random pointer references through this woven connection, then unweave/unzip the lists apart.

---

## Algorithm

1. If `head == nullptr`, return `nullptr`.
2. **Pass 1: Weave Clones**:
   - `curr = head`.
   - While `curr != nullptr`:
     - `copy = new Node(curr->val)`.
     - `copy->next = curr->next`.
     - `curr->next = copy`.
     - `curr = copy->next`.
3. **Pass 2: Connect Random Pointers**:
   - `curr = head`.
   - While `curr != nullptr`:
     - If `curr->random != nullptr`:
       - `curr->next->random = curr->random->next`.
     - `curr = curr->next->next`.
4. **Pass 3: Separate Lists**:
   - `curr = head`.
   - `cloned_head = head->next`.
   - `copy_curr = cloned_head`.
   - While `curr != nullptr`:
     - `curr->next = curr->next->next`.
     - `copy_curr->next = (copy_curr->next) ? copy_curr->next->next : nullptr`.
     - `curr = curr->next`.
     - `copy_curr = copy_curr->next`.
5. Return `cloned_head`.

---

## Clean C++17 Solution

```cpp
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
        
        // Step 1: Interleave cloned nodes after original nodes
        Node* curr = head;
        while (curr != nullptr) {
            Node* copy = new Node(curr->val);
            copy->next = curr->next;
            curr->next = copy;
            curr = copy->next;
        }
        
        // Step 2: Assign random pointers for cloned nodes
        curr = head;
        while (curr != nullptr) {
            if (curr->random != nullptr) {
                curr->next->random = curr->random->next;
            }
            curr = curr->next->next;
        }
        
        // Step 3: Unweave/Separate original and copied lists
        curr = head;
        Node* cloned_head = head->next;
        Node* copy_curr = cloned_head;
        
        while (curr != nullptr) {
            curr->next = curr->next->next;
            copy_curr->next = (copy_curr->next != nullptr) ? copy_curr->next->next : nullptr;
            
            curr = curr->next;
            copy_curr = copy_curr->next;
        }
        
        return cloned_head;
    }
};
```

---

## Dry Run

### Input
- `head = [A -> B]` where `A->random = B`, `B->random = A`.

### Execution Trace

1. **Pass 1 (Weave)**:
   - `A -> A' -> B -> B' -> nullptr`
2. **Pass 2 (Random)**:
   - `A'->random = A->random->next` $\implies B'$
   - `B'->random = B->random->next` $\implies A'$
3. **Pass 3 (Separate)**:
   - Original: `A -> B -> nullptr`
   - Cloned: `A' -> B' -> nullptr`

### Result
- Output Head: `A'`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Three linear passes over $N$ nodes.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space (excluding memory for newly created deep copy nodes).

---

## Why This is Optimal

- Performs deep copy in linear $\mathcal{O}(N)$ time.
- Uses zero extra Hash Map memory ($\mathcal{O}(1)$ auxiliary space).

---

## Common Mistakes

1. **Null Pointer Dereference on Random**: Writing `curr->next->random = curr->random->next` without checking `if (curr->random != nullptr)`.
2. **Corrupting Original List Links**: Failing to properly restore `curr->next = curr->next->next` during Pass 3, leaving the original list modified.
