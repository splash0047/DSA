# Middle of the Linked List

## Pattern Used

- **Pattern**: **Fast & Slow Pointers (Floyd's Tortoise and Hare)**
- **Concept**: Initialize two pointers `slow` and `fast` at `head`. Advance `slow` by 1 step (`slow = slow->next`) and `fast` by 2 steps (`fast = fast->next->next`). When `fast` reaches the end of the list (`nullptr` or `fast->next == nullptr`), `slow` sits exactly at the middle node!

---

## Observation

1. Speed Ratio: `fast` moves twice as fast as `slow` ($2v$ vs $v$).
2. When `fast` covers the entire length $N$, `slow` covers exactly $\lfloor N / 2 \rfloor$ steps.
3. Behavior on Even vs Odd lengths:
   - Odd length ($N = 5$): `fast->next == nullptr` at termination $\implies$ `slow` points to node 3 (exact middle).
   - Even length ($N = 6$): `fast == nullptr` at termination $\implies$ `slow` points to node 4 (second middle node).

---

## Intuition

Race two runners along the list: one moving at double speed. When the fast runner crosses the finish line, the slow runner is right at the midpoint.

---

## Algorithm

1. `slow = head`, `fast = head`.
2. While `fast != nullptr` and `fast->next != nullptr`:
   a. `slow = slow->next`.
   b. `fast = fast->next->next`.
3. Return `slow`.

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
    ListNode* middleNode(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        return slow;
    }
};
```

---

## Dry Run

### Input 1 (Odd Length)
- `head = [1 -> 2 -> 3 -> 4 -> 5]`

| Step | `slow` (val) | `fast` (val) | Loop Condition (`fast && fast->next`) |
| :--- | :--- | :--- | :--- |
| Init | `1` | `1` | True |
| 1 | `2` | `3` | True |
| 2 | `3` | `5` | `fast->next == nullptr` (Stop) |

- Return `slow` = Node `3`

### Input 2 (Even Length)
- `head = [1 -> 2 -> 3 -> 4 -> 5 -> 6]`

| Step | `slow` (val) | `fast` (val) | Loop Condition (`fast && fast->next`) |
| :--- | :--- | :--- | :--- |
| Init | `1` | `1` | True |
| 1 | `2` | `3` | True |
| 2 | `3` | `5` | True |
| 3 | `4` | `nullptr` | `fast == nullptr` (Stop) |

- Return `slow` = Node `4` (Second Middle Node)

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

- Computes middle node in a single pass in $\mathcal{O}(N)$ time.
- Uses zero extra memory.

---

## Common Mistakes

1. **Null Pointer Dereference**: Writing `while (fast->next != nullptr)` without checking `while (fast != nullptr)`. If list length is even, `fast` becomes `nullptr` at the last step, causing a null pointer crash on `fast->next`.
2. **First vs Second Middle Node**: Misunderstanding `fast != nullptr && fast->next != nullptr` vs `fast->next != nullptr && fast->next->next != nullptr`. The former returns the **second** middle for even lengths (as required by LeetCode #876).
