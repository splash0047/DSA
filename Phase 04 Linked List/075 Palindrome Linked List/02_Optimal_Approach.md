# Palindrome Linked List

## Pattern Used

- **Pattern**: **Find Mid + Reverse Second Half + Compare**
- **Concept**:
  1. **Find Middle**: Use Fast & Slow pointers (`slow`, `fast`) to reach the middle node.
  2. **Reverse Second Half**: Reverse the linked list starting from `slow`.
  3. **Compare**: Compare values node-by-node starting from `head` and the head of the reversed second half `second`.
  4. **Restore (Optional)**: Reverse second half back to restore original list structure.

---

## Observation

1. A sequence is a palindrome if reading forward from start matches reading backward from end.
2. Reversing the second half of a linked list allows comparing forward from `head` and forward from `second` simultaneously!
3. Reversing in-place requires zero auxiliary memory.

---

## Intuition

Find the midpoint of the list, reverse the second half so pointers point backward, then walk two pointers side-by-side to verify matching values.

---

## Algorithm

1. If `head == nullptr || head->next == nullptr`, return `true`.
2. **Find Mid**:
   - `slow = head`, `fast = head`.
   - While `fast != nullptr` and `fast->next != nullptr`:
     - `slow = slow->next`.
     - `fast = fast->next->next`.
3. **Reverse Second Half**:
   - `prev = nullptr`, `curr = slow`.
   - While `curr != nullptr`:
     - `next_node = curr->next`.
     - `curr->next = prev`.
     - `prev = curr`.
     - `curr = next_node`.
4. **Compare**:
   - `first = head`, `second = prev`.
   - `is_pal = true`.
   - While `second != nullptr`:
     - If `first->val != second->val`:
       - `is_pal = false`; break;
     - `first = first->next`.
     - `second = second->next`.
5. Return `is_pal`.

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
private:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while (curr != nullptr) {
            ListNode* next_node = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next_node;
        }
        return prev;
    }
public:
    bool isPalindrome(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return true;
        
        // Step 1: Find middle node using Fast/Slow pointers
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        // Step 2: Reverse second half starting from slow
        ListNode* second = reverseList(slow);
        ListNode* first = head;
        ListNode* second_copy = second; // Keep reference to restore list if needed
        
        // Step 3: Compare first half and reversed second half
        bool is_pal = true;
        while (second != nullptr) {
            if (first->val != second->val) {
                is_pal = false;
                break;
            }
            first = first->next;
            second = second->next;
        }
        
        // Step 4: Restore original list structure
        reverseList(second_copy);
        
        return is_pal;
    }
};
```

---

## Dry Run

### Input
- `head = [1 -> 2 -> 2 -> 1]`

### Execution Trace

1. **Find Mid**: `slow` stops at Node `2` (index 2).
2. **Reverse Second Half**:
   - First Half: `1 -> 2 ...`
   - Reversed Second Half: `1 -> 2 -> nullptr`
3. **Compare**:
   - Iteration 1: `first->val (1) == second->val (1)`
   - Iteration 2: `first->val (2) == second->val (2)`
   - `second` hits `nullptr`. Loop ends.

### Result
- Output: `true`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Mid search: $N/2$ steps. Reversal: $N/2$ steps. Comparison: $N/2$ steps. Restoration: $N/2$ steps. Total $\mathcal{O}(N)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This is Optimal

- Solves Palindrome check in linear $\mathcal{O}(N)$ time.
- Uses zero extra memory ($\mathcal{O}(1)$ space), satisfying the follow-up.

---

## Common Mistakes

1. **Not Restoring List Structure**: Leaving the linked list corrupted/reversed when returning, which may fail strict system design requirements.
2. **Odd Length Termination**: When $N$ is odd, `slow` lands on exact middle node; reversing from `slow` includes middle node in `second` half, which compares safely!
