# Linked List Cycle

## Pattern Used

- **Pattern**: **Floyd's Cycle Detection (Tortoise and Hare Pointers)**
- **Concept**: Maintain two pointers `slow` and `fast` initialized at `head`.
  - `slow` moves 1 step at a time: `slow = slow->next`.
  - `fast` moves 2 steps at a time: `fast = fast->next->next`.
  - If a cycle exists, `fast` will eventually enter the cycle and catch up to `slow` (`slow == fast`).
  - If no cycle exists, `fast` will hit `nullptr`.

---

## Observation

1. Why does `fast` always meet `slow` if a cycle exists?
   - Once both pointers enter a cycle of length $C$, the relative distance between `fast` and `slow` decreases by 1 step in every iteration ($2 - 1 = 1$).
   - Therefore, `fast` is guaranteed to catch `slow` within at most $C$ iterations inside the loop!
2. If `fast == nullptr` or `fast->next == nullptr`, the list ends cleanly without a cycle.

---

## Intuition

Imagine two runners on a circular track: one runner running twice as fast as the other. The faster runner is mathematically bound to lap and catch the slower runner.

---

## Algorithm

1. `slow = head`, `fast = head`.
2. While `fast != nullptr` and `fast->next != nullptr`:
   a. `slow = slow->next`.
   b. `fast = fast->next->next`.
   c. If `slow == fast`: return `true`.
3. Return `false`.

---

## Clean C++17 Solution

```cpp
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == nullptr || head->next == nullptr) return false;
        
        ListNode* slow = head;
        ListNode* fast = head;
        
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
            
            if (slow == fast) {
                return true; // Fast pointer caught slow pointer -> Cycle detected!
            }
        }
        
        return false; // Fast reached end -> No cycle
    }
};
```

---

## Dry Run

### Input
- `head = [3 -> 2 -> 0 -> -4]` where `-4` points back to `2` (Cycle of length 3).

### Execution Trace

| Step | `slow` (val) | `fast` (val) | `slow == fast`? | Action |
| :--- | :--- | :--- | :--- | :--- |
| Init | `3` | `3` | - | - |
| 1 | `2` | `0` | No | Continue |
| 2 | `0` | `2` | No | Continue |
| 3 | `-4` | `-4` | **`slow == fast` (True!)** | **Return `true`** |

### Result
- Output: `true`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Non-cyclic list: `fast` reaches end in $N/2$ steps $\implies \mathcal{O}(N)$.
  - Cyclic list: `fast` catches `slow` in at most $K + C$ steps (where $K$ is non-cyclic length and $C$ is cycle length) $\implies \mathcal{O}(N)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space (only two pointer variables used).

---

## Why This is Optimal

- Detects cycle in $\mathcal{O}(N)$ time.
- Uses zero extra memory ($\mathcal{O}(1)$ space), satisfying the follow-up.

---

## Common Mistakes

1. **Comparing Pointer Values vs Memory Addresses**: Checking `slow->val == fast->val` instead of `slow == fast`. Multiple distinct nodes can share identical integer values! Compare node pointers (memory addresses).
2. **Missing Boundary Guard**: Forgetting `while (fast != nullptr && fast->next != nullptr)` resulting in null pointer exception on acyclic lists.
