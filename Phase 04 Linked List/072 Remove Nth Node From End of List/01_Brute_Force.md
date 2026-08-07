# Remove Nth Node From End of List

- **Problem Number**: 19
- **Platform**: LeetCode #19
- **Difficulty**: Medium
- **Pattern**: Two-Pass Length Count

---

## Brute Force Intuition

Pass 1: Count total number of nodes `sz` in the linked list.
Pass 2: The node to remove is at index `sz - n` from the front. Advance `curr` pointer to index `sz - n - 1` (node preceding the target) and delete `curr->next`.

---

## Algorithm

1. `sz = 0`, `curr = head`.
2. While `curr != nullptr`:
   a. `sz++`.
   b. `curr = curr->next`.
3. If `sz == n`: return `head->next` (removing original head node).
4. `target_idx = sz - n`.
5. `curr = head`.
6. For `i` from `0` to `target_idx - 2`:
   a. `curr = curr->next`.
7. `to_delete = curr->next`.
8. `curr->next = curr->next->next`.
9. `delete to_delete`.
10. Return `head`.

---

## Code

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
        int sz = 0;
        ListNode* curr = head;
        while (curr != nullptr) {
            sz++;
            curr = curr->next;
        }
        
        if (sz == n) {
            ListNode* new_head = head->next;
            delete head;
            return new_head;
        }
        
        curr = head;
        for (int i = 0; i < sz - n - 1; ++i) {
            curr = curr->next;
        }
        
        ListNode* to_delete = curr->next;
        curr->next = curr->next->next;
        delete to_delete;
        
        return head;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Two passes over the linked list.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

Requires **two passes** over the linked list. Using **Two Pointers with Fixed Gap (Fast/Slow)**, we can locate and remove the $N^{\text{th}}$ node from the end in a **single pass**.
