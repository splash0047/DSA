# Add Two Numbers

## Pattern Used

- **Pattern**: **Single-Pass Digit Addition with Carry (Dummy Sentinel)**
- **Concept**: Maintain `carry = 0`. Iterate through `l1` and `l2` simultaneously. At each step:
  - `sum = val1 + val2 + carry`.
  - `carry = sum / 10`.
  - Append new node `ListNode(sum % 10)` to the result list.

---

## Observation

1. Digits are stored in **reverse order** (Least Significant Digit at head). This means adding node-by-node from left to right mirrors standard elementary school addition!
2. Loop continuation condition: `while (l1 != nullptr || l2 != nullptr || carry > 0)`.
3. If one list is shorter than the other, treat missing node values as `0`.
4. If `carry > 0` after exhausting both lists, append a final node `ListNode(carry)`.

---

## Intuition

Simulate elementary column-by-column addition from right to left (head to tail). Accumulate the carry into the next position.

---

## Algorithm

1. `dummy = ListNode(0)`, `curr = &dummy`, `carry = 0`.
2. While `l1 != nullptr` or `l2 != nullptr` or `carry > 0`:
   a. `val1 = (l1 != nullptr) ? l1->val : 0`.
   b. `val2 = (l2 != nullptr) ? l2->val : 0`.
   c. `sum = val1 + val2 + carry`.
   d. `carry = sum / 10`.
   e. `curr->next = new ListNode(sum % 10)`.
   f. `curr = curr->next`.
   g. If `l1 != nullptr`: `l1 = l1->next`.
   h. If `l2 != nullptr`: `l2 = l2->next`.
3. Return `dummy.next`.

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy(0);
        ListNode* curr = &dummy;
        int carry = 0;
        
        while (l1 != nullptr || l2 != nullptr || carry > 0) {
            int val1 = (l1 != nullptr) ? l1->val : 0;
            int val2 = (l2 != nullptr) ? l2->val : 0;
            
            int sum = val1 + val2 + carry;
            carry = sum / 10;
            
            curr->next = new ListNode(sum % 10);
            curr = curr->next;
            
            if (l1 != nullptr) l1 = l1->next;
            if (l2 != nullptr) l2 = l2->next;
        }
        
        return dummy.next;
    }
};
```

---

## Dry Run

### Input
- `l1 = [2 -> 4 -> 3]`, `l2 = [5 -> 6 -> 4]`

### Execution Trace

| Step | `l1->val` | `l2->val` | `carry` in | `sum = val1+val2+carry` | `carry` out | Created Node (`sum % 10`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `2` | `5` | `0` | `2 + 5 + 0 = 7` | `0` | `7` |
| 2 | `4` | `6` | `0` | `4 + 6 + 0 = 10` | `1` | `0` |
| 3 | `3` | `4` | `1` | `3 + 4 + 1 = 8` | `0` | `8` |
| End | `nullptr` | `nullptr` | `0` | Loop terminates | - | - |

### Result
- Output List: `7 -> 0 -> 8` (807)

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(\max(N, M))$
  - Single pass over the maximum length of `l1` ($N$) and `l2` ($M$).

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(\max(N, M))$
  - Result linked list requires $\max(N, M) + 1$ new nodes.

---

## Why This is Optimal

- Computes sum in a single pass in $\mathcal{O}(\max(N, M))$ time.
- Uses zero extra memory beyond the required output list structure.

---

## Common Mistakes

1. **Forgetting Final Carry**: Omitting `carry > 0` in the loop condition, causing `99 + 1 = 00` instead of `001` (100).
2. **Null Pointer Access on Unequal Lengths**: Accessing `l1->val` when `l1` is `nullptr`. Always use ternary guard `(l1 != nullptr) ? l1->val : 0`.
