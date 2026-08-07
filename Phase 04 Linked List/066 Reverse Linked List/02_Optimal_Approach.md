# Reverse Linked List

## Pattern Used

- **Pattern**: **Iterative 3-Pointer Link Reversal**
- **Concept**: Maintain three pointers `prev`, `curr`, and `next_node`. At each node, store `next_node = curr->next`, redirect `curr->next = prev`, then advance `prev = curr` and `curr = next_node`.

---

## Observation

1. To reverse a linked list node pointer $A \rightarrow B$ into $A \leftarrow B$, we must modify `curr->next` to point to `prev`.
2. Modifying `curr->next` destroys the link to the rest of the list!
3. Solution: Store `next_node = curr->next` *before* overwriting `curr->next`.
4. When `curr` reaches `nullptr`, `prev` points to the new head of the reversed list.

---

## Intuition

Walk through the list sequentially, flipping each node's `next` arrow to point backward to `prev`.

---

## Algorithm

1. `prev = nullptr`, `curr = head`.
2. While `curr != nullptr`:
   a. `next_node = curr->next`.
   b. `curr->next = prev`.
   c. `prev = curr`.
   d. `curr = next_node`.
3. Return `prev`.

---

## Clean C++17 Solution

```cpp
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        
        while (curr != nullptr) {
            ListNode* next_node = curr->next; // Save next node
            curr->next = prev;                // Reverse current link
            prev = curr;                      // Move prev forward
            curr = next_node;                 // Move curr forward
        }
        
        return prev; // New head of reversed list
    }
};
```

---

## Recursive Alternative ($\mathcal{O}(N)$ Time, $\mathcal{O}(N)$ Stack Space)

```cpp
class SolutionRecursive {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }
        ListNode* new_head = reverseList(head->next);
        head->next->next = head;
        head->next = nullptr;
        return new_head;
    }
};
```

---

## Dry Run

### Input
- `head = [1 -> 2 -> 3 -> nullptr]`

### Execution Trace

| Step | `prev` | `curr` | `next_node` | Action (`curr->next = prev`) | New State |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Init | `nullptr` | `1` | - | - | `nullptr <- 1` |
| 1 | `1` | `2` | `3` | `2->next = 1` | `nullptr <- 1 <- 2` |
| 2 | `2` | `3` | `nullptr` | `3->next = 2` | `nullptr <- 1 <- 2 <- 3` |
| 3 | `3` | `nullptr` | - | `curr == nullptr` (Stop) | Return `prev = 3` |

### Result
- Output Head: `3 -> 2 -> 1 -> nullptr`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass through $N$ nodes.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Iterative approach uses constant auxiliary space.

---

## Why This is Optimal

- Reverses pointers in a single pass $\mathcal{O}(N)$ time.
- Uses zero extra memory ($\mathcal{O}(1)$ space).

---

## Common Mistakes

1. **Losing Next Node Reference**: Overwriting `curr->next = prev` before storing `next_node = curr->next`, breaking list traversal.
2. **Returning `curr` instead of `prev`**: At loop termination, `curr` is `nullptr`. Return `prev` (the new head).
