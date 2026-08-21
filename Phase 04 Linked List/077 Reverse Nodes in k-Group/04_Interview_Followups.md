# 04 Interview Follow-ups & System Variations: Reverse Nodes in k-Group

The problem reverses nodes of a singly linked list $k$ at a time (Hard). If the number of nodes is not a multiple of $k$, left-out nodes remain as they are. The optimal solution runs in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this is the most notorious pointer-manipulation question. Interviewers test boundary counting, head splicing, and remainder handling variations.

---

## 1. Iterative Pointer Splicing Template

```cpp
ListNode* reverseKGroup(ListNode* head, int k) {
    ListNode dummy(0, head);
    ListNode* group_prev = &dummy;
    
    while (true) {
        // 1. Check if k nodes exist in current group
        ListNode* kth = group_prev;
        for (int i = 0; i < k && kth != nullptr; i++) {
            kth = kth->next;
        }
        if (kth == nullptr) break; // Less than k nodes remain
        
        ListNode* group_next = kth->next;
        
        // 2. Reverse current k nodes
        ListNode* prev = group_next;
        ListNode* curr = group_prev->next;
        while (curr != group_next) {
            ListNode* tmp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = tmp;
        }
        
        // 3. Connect previous group to new group head
        ListNode* tmp = group_prev->next;
        group_prev->next = kth;
        group_prev = tmp;
    }
    return dummy.next;
}
```

---

## 2. Variation: What if Leftover Nodes $(< k)$ MUST ALSO Be Reversed?

### 💡 Reversal Without Pre-Counting Check
- In this variation, we simply reverse nodes as they come without breaking on incomplete groups.
- If $N = 7, k = 3$: groups are reversed as $[3, 2, 1], [6, 5, 4], [7]$.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Space Model | Time | Extra Memory |
| :--- | :--- | :--- | :--- |
| **Iterative Splicing** | Pointer Rewiring | $\mathcal{O}(N)$ | strictly $\mathcal{O}(1)$ |
| **Recursive** | Call Stack | $\mathcal{O}(N)$ | $\mathcal{O}(N/k)$ stack |
