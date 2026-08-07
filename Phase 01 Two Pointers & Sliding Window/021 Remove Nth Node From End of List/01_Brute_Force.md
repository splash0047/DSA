# Remove Nth Node From End of List

- **Problem Number**: 19
- **Platform**: LeetCode #19
- **Difficulty**: Medium
- **Pattern**: Two-Pass Length Calculation

---

## Brute Force Intuition

To remove the $n^{\text{th}}$ node from the end of a linked list, we can first make a full pass to calculate the total length `L` of the list. The $n^{\text{th}}$ node from the end corresponds to the $(L - n + 1)^{\text{th}}$ node from the beginning. In a second pass, we traverse to the node right before it (the $(L - n)^{\text{th}}$ node) and update its `next` pointer.

---

## Algorithm

1. Pass 1: Traverse the linked list and calculate length `L`.
2. If `n == L`, the node to remove is the `head`. Return `head->next`.
3. Pass 2: Traverse to node at position `L - n` (0-indexed).
4. Update `curr->next = curr->next->next`.
5. Return `head`.

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
        int length = 0;
        ListNode* curr = head;
        
        while (curr != nullptr) {
            length++;
            curr = curr->next;
        }
        
        if (n == length) {
            ListNode* new_head = head->next;
            delete head;
            return new_head;
        }
        
        curr = head;
        for (int i = 0; i < length - n - 1; ++i) {
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

- **Time Complexity**: $\mathcal{O}(L)$
  - Requires two passes over the linked list of length $L$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses constant extra space.

---

## Why This Approach Is Not Optimal

This approach requires two passes over the linked list. The follow-up challenge asks to solve the problem in a **single pass** using **Two Pointers (Fast & Slow Gap of N)**.
