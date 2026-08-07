# Remove Nth Node From End of List

## Pattern Used

- **Pattern**: **Two Pointers (Fast & Slow Pointer Gap)**
- **Concept**: Maintain two pointers `fast` and `slow` separated by a gap of $n + 1$ nodes. When `fast` reaches `nullptr` at the end of the list, `slow` will point to the node **immediately preceding** the target node to be deleted.

---

## Observation

1. To delete a node in a singly linked list, we must position our pointer at the node **before** it (`prev->next = prev->next->next`).
2. If `fast` is advanced $n + 1$ steps ahead of `slow` starting from a `dummy` node, moving both pointers at equal speed will cause `slow` to stop right before the $n^{\text{th}}$ node from the end when `fast` hits `nullptr`.
3. Using a `dummy` node pointing to `head` cleanly eliminates edge cases where the node to be removed is the `head` itself!

---

## Intuition

1. Create a `dummy` node: `dummy->next = head`.
2. Set `fast = dummy` and `slow = dummy`.
3. Advance `fast` by $n + 1$ steps.
4. Move `fast` and `slow` together 1 step at a time until `fast == nullptr`.
5. Now `slow->next` is the target node! Bypass it: `slow->next = slow->next->next`.
6. Return `dummy->next`.

---

## Algorithm

1. Allocate `ListNode dummy(0)` with `dummy.next = head`.
2. Initialize `fast = &dummy`, `slow = &dummy`.
3. Loop $i$ from $0$ to $n$: `fast = fast->next`.
4. While `fast != nullptr`:
   - `fast = fast->next`
   - `slow = slow->next`
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
        ListNode dummy(0);
        dummy.next = head;
        
        ListNode* fast = &dummy;
        ListNode* slow = &dummy;
        
        // Step 1: Advance fast pointer n + 1 steps ahead
        for (int i = 0; i <= n; ++i) {
            fast = fast->next;
        }
        
        // Step 2: Move fast and slow together until fast reaches end
        while (fast != nullptr) {
            fast = fast->next;
            slow = slow->next;
        }
        
        // Step 3: Bypass and delete the target node
        ListNode* to_delete = slow->next;
        slow->next = slow->next->next;
        delete to_delete;
        
        return dummy.next;
    }
};
```

---

## Dry Run

### Input
- `head = [1, 2, 3, 4, 5]`, `n = 2`

### Execution Trace

| Step | State | `fast` Position | `slow` Position | Action |
| :--- | :--- | :--- | :--- | :--- |
| Start | `dummy -> 1 -> 2 -> 3 -> 4 -> 5` | `dummy` | `dummy` | Init pointers |
| 1 | Advance `fast` $n+1 = 3$ steps | `3` | `dummy` | `fast` is 3 steps ahead |
| 2 | Move together 1 step | `4` | `1` | `fast != null` |
| 3 | Move together 2 steps | `5` | `2` | `fast != null` |
| 4 | Move together 3 steps | `nullptr` | `3` | `fast == null` (Stop loop!) |
| 5 | Delete target node `slow->next` (`4`) | `nullptr` | `3` | `slow->next = 5`. List: `1->2->3->5` |

### Result
- Output: `[1, 2, 3, 5]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(L)$
  - Single pass through the list of length $L$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses stack dummy node and two pointer variables.

---

## Why This is Optimal

- Solves the problem in a **single pass** ($\mathcal{O}(L)$ time).
- Uses $\mathcal{O}(1)$ space.

---

## Common Mistakes

1. **Not Using a Dummy Node**: Removing the `head` node (when $n = L$) causes null pointer dereferences if no dummy node is used.
2. **Advancing `fast` $n$ steps instead of $n + 1$ steps**: If `fast` is advanced only $n$ steps, `slow` lands on the node to be deleted instead of the node *before* it.
