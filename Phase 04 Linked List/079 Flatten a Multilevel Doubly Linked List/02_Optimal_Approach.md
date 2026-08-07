# Flatten a Multilevel Doubly Linked List

## Pattern Used

- **Pattern**: **In-Place Iterative Splice Re-linking**
- **Concept**: Traverse the list node-by-node. When a node `curr` has a `child` pointer:
  1. Find the tail `child_tail` of the child linked list by walking to its end.
  2. If `curr->next != nullptr`, connect `child_tail->next = curr->next` and `curr->next->prev = child_tail`.
  3. Connect `curr->next = curr->child` and `curr->child->prev = curr`.
  4. Nullify `curr->child = nullptr`.

---

## Observation

1. Flattening inserts the child list directly between `curr` and `curr->next`.
2. Splicing steps:
   - `curr` $\rightarrow$ `child_head` $\dots$ `child_tail` $\rightarrow$ `original_next`.
3. After splicing, advance `curr = curr->next`. If the inserted child list itself contained sub-children, the loop will encounter them seamlessly as it traverses forward!

---

## Intuition

Whenever you hit a node with a child branch, splice the entire child list inline between the current node and its next node. Then resume walking forward.

---

## Algorithm

1. `curr = head`.
2. While `curr != nullptr`:
   a. If `curr->child != nullptr`:
      - `child_head = curr->child`.
      - Find tail of child list: `child_tail = child_head`. While `child_tail->next != nullptr`: `child_tail = child_tail->next`.
      - If `curr->next != nullptr`:
        - `child_tail->next = curr->next`.
        - `curr->next->prev = child_tail`.
      - `curr->next = child_head`.
      - `child_head->prev = curr`.
      - `curr->child = nullptr`.
   b. `curr = curr->next`.
3. Return `head`.

---

## Clean C++17 Solution

```cpp
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
        
        Node* curr = head;
        
        while (curr != nullptr) {
            if (curr->child != nullptr) {
                Node* child_head = curr->child;
                Node* child_tail = child_head;
                
                // Find the tail of the child branch
                while (child_tail->next != nullptr) {
                    child_tail = child_tail->next;
                }
                
                // Splice child_tail to curr->next
                if (curr->next != nullptr) {
                    child_tail->next = curr->next;
                    curr->next->prev = child_tail;
                }
                
                // Splice curr to child_head
                curr->next = child_head;
                child_head->prev = curr;
                curr->child = nullptr; // Clear child pointer
            }
            
            curr = curr->next;
        }
        
        return head;
    }
};
```

---

## Dry Run

### Input
- `1 <-> 2 <-> 3 <-> 4` where `3` has child `7 <-> 8`.

### Execution Trace

1. `curr` at `1`: no child. `curr = 2`.
2. `curr` at `2`: no child. `curr = 3`.
3. `curr` at `3`: HAS CHILD `7 <-> 8`!
   - `child_tail` at `8`.
   - Connect `8->next = 4`, `4->prev = 8`.
   - Connect `3->next = 7`, `7->prev = 3`.
   - Clear `3->child = nullptr`.
   - List state: `1 <-> 2 <-> 3 <-> 7 <-> 8 <-> 4`.
4. `curr` continues to `7`, `8`, `4`.

### Result
- Flattened List: `1 <-> 2 <-> 3 <-> 7 <-> 8 <-> 4`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Each node is visited at most twice (once by `curr`, once by `child_tail` search).

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - In-place pointer modifications with zero extra memory allocation.

---

## Why This is Optimal

- Flattens multilevel list in linear $\mathcal{O}(N)$ time.
- Uses zero extra memory ($\mathcal{O}(1)$ space).

---

## Common Mistakes

1. **Forgetting `curr->child = nullptr`**: Leaving non-null child pointers causes invalid list state.
2. **Null Pointer Check on `curr->next`**: Forgetting to check `if (curr->next != nullptr)` before accessing `curr->next->prev`.
