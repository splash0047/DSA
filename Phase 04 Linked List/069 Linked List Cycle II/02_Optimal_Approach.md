# Linked List Cycle II

## Pattern Used

- **Pattern**: **Floyd's Cycle Entry Finding (Mathematical Proof)**
- **Concept**:
  1. Detect cycle using `slow` and `fast` pointers (`slow` moves 1 step, `fast` moves 2 steps).
  2. Once `slow == fast` (collision point inside cycle), reset `entry = head`.
  3. Advance both `entry` and `slow` 1 step at a time (`entry = entry->next`, `slow = slow->next`).
  4. The node where `entry` and `slow` meet is mathematically proven to be the **cycle start node**!

---

## Proof of Optimality (Mathematical Derivation)

Let:
- $L_1$ = distance from `head` to cycle start node.
- $L_2$ = distance from cycle start node to collision point.
- $C$ = cycle length.

When `slow` and `fast` collide:
- Distance traveled by `slow` = $L_1 + L_2$.
- Distance traveled by `fast` = $L_1 + L_2 + k \cdot C$ (where $k \ge 1$ is full loop rounds).

Since `fast` travels twice as fast as `slow`:
$$2 \cdot (L_1 + L_2) = L_1 + L_2 + k \cdot C$$
$$L_1 + L_2 = k \cdot C \implies L_1 = k \cdot C - L_2$$

This equation states that **the distance from `head` to cycle start ($L_1$) equals the remaining distance from collision point to cycle start ($k \cdot C - L_2$)**!

Thus, advancing `entry` from `head` and `slow` from collision point 1 step at a time causes them to meet exactly at the cycle start node!

---

## Intuition

After detecting the collision point, reset one pointer to `head`. Moving both pointers at single speed makes them collide at the entry door of the cycle.

---

## Algorithm

1. `slow = head`, `fast = head`.
2. While `fast != nullptr` and `fast->next != nullptr`:
   a. `slow = slow->next`.
   b. `fast = fast->next->next`.
   c. If `slow == fast`:
      - `entry = head`.
      - While `entry != slow`:
        - `entry = entry->next`.
        - `slow = slow->next`.
      - Return `entry`.
3. Return `nullptr`.

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
    ListNode *detectCycle(ListNode *head) {
        if (head == nullptr || head->next == nullptr) return nullptr;
        
        ListNode* slow = head;
        ListNode* fast = head;
        
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
            
            if (slow == fast) {
                // Cycle detected! Reset entry pointer to head
                ListNode* entry = head;
                while (entry != slow) {
                    entry = entry->next;
                    slow = slow->next;
                }
                return entry; // Cycle start node!
            }
        }
        
        return nullptr; // No cycle
    }
};
```

---

## Dry Run

### Input
- `head = [3 -> 2 -> 0 -> -4]` (tail `-4` points back to `2`, so cycle start is node `2`).

### Execution Trace

1. **Collision Phase**: `slow` and `fast` collide at node `-4`.
2. **Entry Phase**:
   - `entry = 3` (head), `slow = -4` (collision).
   - Step 1: `entry = 2`, `slow = 2` (`entry == slow` **Match!**)
3. Return node `2`.

### Result
- Output Node: `2`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Collision detection takes $\le N$ steps; entry phase takes $\le N$ steps.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This is Optimal

- Solves cycle entry detection in $\mathcal{O}(N)$ time.
- Uses zero extra memory ($\mathcal{O}(1)$ space).

---

## Common Mistakes

1. **Incorrect Single Step Increments in Entry Phase**: Moving `slow` by 2 steps during the second phase instead of 1 step (`slow = slow->next`).
2. **Missing `nullptr` Check**: Failing to check `fast != nullptr && fast->next != nullptr` before Phase 1.
