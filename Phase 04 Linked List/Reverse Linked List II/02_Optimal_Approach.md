# Reverse Linked List II - Optimal Approach (1-Pass Pointer Splicing)

- **Problem Number**: 92
- **Platform**: LeetCode #92
- **Difficulty**: Medium
- **Pattern**: Dummy Head + Head-Tail Reversal in 1 Pass ($\mathcal{O}(1)$ Space)

---

## Optimal Intuition

1. Create a `dummy` node before `head`.
2. Advance `prev` pointer to `left - 1`.
3. Repeatedly pull the node after `curr` and insert it immediately after `prev` for `right - left` iterations.

---

## Code

```cpp
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head || left == right) return head;

        ListNode dummy(0);
        dummy.next = head;
        ListNode* prev = &dummy;

        for (int i = 0; i < left - 1; i++) {
            prev = prev->next;
        }

        ListNode* curr = prev->next;
        for (int i = 0; i < right - left; i++) {
            ListNode* temp = curr->next;
            curr->next = temp->next;
            temp->next = prev->next;
            prev->next = temp;
        }

        return dummy.next;
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(N)$ strictly 1 pass.
- **Space Complexity**: strictly $\mathcal{O}(1)$ auxiliary space.
