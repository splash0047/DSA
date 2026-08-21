# 04 Interview Follow-ups & System Variations: Merge Two Sorted Lists

The problem merges two sorted singly linked lists into one sorted list. The optimal approach uses a **Dummy Head Node** and iterative pointer splicing in $\mathcal{O}(M + N)$ time and $\mathcal{O}(1)$ auxiliary space.

In technical interviews, this problem is compared with recursive merges, array merges, and $K$-list extensions.

---

## 1. Why Iterative Pointer Splicing is Superior to Allocating New Nodes

### 🛑 Zero Memory Allocation Invariant
- Naive solutions create new `new ListNode(val)` nodes for the merged list.
- **Optimal Splicing**: Simply rewire existing `next` pointers from `list1` and `list2`.
- Zero heap allocation overhead; zero memory leaks.

---

## 2. Iterative vs. Recursive Merge

```cpp
// Iterative with Dummy Node: O(1) Space
ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    ListNode dummy(0);
    ListNode* tail = &dummy;
    while (l1 && l2) {
        if (l1->val <= l2->val) { tail->next = l1; l1 = l1->next; }
        else { tail->next = l2; l2 = l2->next; }
        tail = tail->next;
    }
    tail->next = l1 ? l1 : l2;
    return dummy.next;
}
```
- **Recursive Space**: $\mathcal{O}(M + N)$ stack frames $\implies$ risky for large lists.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Time | Space | Memory Allocation |
| :--- | :--- | :--- | :--- |
| **Iterative + Dummy Node** | $\mathcal{O}(M+N)$ | $\mathcal{O}(1)$ | **0 allocations (Rewires pointers)** |
| **Recursive** | $\mathcal{O}(M+N)$ | $\mathcal{O}(M+N)$ | Call stack allocations |
