# Remove Nth Node From End of List

## Pattern Used

- **Pattern**: **Two-Pointer Fixed Gap (Fast & Slow Pointers)**
- **Concept**: Maintain a dummy node `dummy` pointing to `head`. Initialize `fast = &dummy` and `slow = &dummy`.
  1. Advance `fast` pointer $n + 1$ steps forward.
  2. Advance both `fast` and `slow` 1 step at a time until `fast == nullptr`.
  3. Now `slow` sits exactly at the node **preceding** the target node to delete!
  4. Perform deletion: `slow->next = slow->next->next`.

---

## Observation

1. Why maintain a gap of $n + 1$ steps between `fast` and `slow`?
   - When `fast` reaches `nullptr` (past the last node), `slow` will sit at position $(SZ + 1) - (n + 1) = SZ - n$ (the node right before the $N^{\text{th}}$ node from the end).
2. Using `dummy` sentinel node cleanly handles the edge case where the $N^{\text{th}}$ node from the end is the **head of the list** ($n = SZ$).

---

## Intuition

Place two pointers $n + 1$ steps apart. Slide both pointers forward together like a rigid measuring ruler until the front pointer hits the end. The rear pointer will automatically point to the node right before the target.

---

## Algorithm

1. `dummy = ListNode(0, head)`.
2. `fast = &dummy`, `slow = &dummy`.
3. For `i` from `0` to `n`:
   - `fast = fast->next`.
4. While `fast != nullptr`:
   a. `slow = slow->next`.
   b. `fast = fast->next`.
5. `to_delete = slow->next`.
6. `slow->next = slow->next->next`.
7. `delete to_delete`.
8. Return `dummy.next`.

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy(0, head);
        ListNode* fast = &dummy;
        ListNode* slow = &dummy;
        
        // Advance fast pointer n + 1 steps to create gap
        for (int i = 0; i <= n; ++i) {
            fast = fast->next;
        }
        
        // Slide both pointers until fast reaches nullptr
        while (fast != nullptr) {
            slow = slow->next;
            fast = fast->next;
        }
        
        // Delete target node
        ListNode* to_delete = slow->next;
        slow->next = slow->next->next;
        delete to_delete;
        
        return dummy.next;
    }
};


          slow
            ↓
dummy → [0] → [1] → [2] → [3] → [4] → [5] → NULL
            ↑
           fast
```

---

## Dry Run

### Input
- `head = [1 -> 2 -> 3 -> 4 -> 5]`, `n = 2`

### Execution Trace

- `dummy = [0 -> 1 -> 2 -> 3 -> 4 -> 5]`
- Advance `fast` $n + 1 = 3$ steps: `fast` points to node `3`.

| Step | `slow` (val) | `fast` (val) | `fast == nullptr`? |
| :--- | :--- | :--- | :--- |
| Init | `0` (dummy) | `3` | False |
| 1 | `1` | `4` | False |
| 2 | `2` | `5` | False |
| 3 | `3` | `nullptr` | **True (Stop!)** |

- Target node: `slow->next` (Node `4`).
- Delete Node `4`: `slow->next = slow->next->next` (`3->next = 5`).

### Result
- Output List: `1 -> 2 -> 3 -> 5`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass over $N$ nodes.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This is Optimal

- Meets the follow-up requirement for a **single pass** $\mathcal{O}(N)$ algorithm.
- Uses zero extra memory.

---

## Common Mistakes

1. **Advancing `fast` $n$ steps instead of $n + 1$**: Advancing `fast` only $n$ steps leaves `slow` pointing to the target node itself rather than the node *before* it, making deletion cumbersome.
2. **Missing Dummy Sentinel**: Failing to use `dummy` node causes segment fault when $n$ equals list size (deleting head node).
