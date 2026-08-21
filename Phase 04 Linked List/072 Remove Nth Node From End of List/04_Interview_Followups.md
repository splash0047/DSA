# 04 Interview Follow-ups & System Variations: Remove Nth Node From End of List

The problem deletes the $N$-th node from the end of a linked list in a single pass using two pointers separated by $N$ steps and a dummy head in $\mathcal{O}(L)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem tests boundary dummy invariants, manual memory deallocation, and concurrent deletions.

---

## 1. Single-Pass Pointer Separation Invariant

```cpp
ListNode* removeNthFromEnd(ListNode* head, int n) {
    ListNode dummy(0, head);
    ListNode* fast = &dummy;
    ListNode* slow = &dummy;
    
    for (int i = 0; i <= n; i++) {
        fast = fast->next;
    }
    while (fast != nullptr) {
        fast = fast->next;
        slow = slow->next;
    }
    ListNode* to_delete = slow->next;
    slow->next = slow->next->next;
    delete to_delete; // Free memory in C++
    return dummy.next;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Strategy | Time | Space |
| :--- | :--- | :--- | :--- |
| **Delete Head Node** | Handled by Dummy Head | $\mathcal{O}(L)$ | $\mathcal{O}(1)$ |
| **C++ Heap Deallocation** | Explicit `delete` | $\mathcal{O}(L)$ | $\mathcal{O}(1)$ |
