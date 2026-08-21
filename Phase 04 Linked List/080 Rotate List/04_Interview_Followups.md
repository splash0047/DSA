# 04 Interview Follow-ups & System Variations: Rotate List

The problem rotates a linked list to the right by $k$ places. The optimal approach computes length $L$, forms a circular ring by connecting tail to head, and breaks the ring at $(L - (k \pmod L) - 1)$ in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem tests modular rotation normalization, circular list manipulation, and pointer decoupling.

---

## 1. Circular Ring Algorithm

```cpp
ListNode* rotateRight(ListNode* head, int k) {
    if (!head || !head->next || k == 0) return head;
    
    // 1. Compute length and find tail
    int len = 1;
    ListNode* tail = head;
    while (tail->next) {
        tail = tail->next;
        len++;
    }
    
    // 2. Connect tail to head (form ring)
    tail->next = head;
    
    // 3. Find new tail at (len - (k % len) - 1)
    k = k % len;
    int steps_to_new_tail = len - k - 1;
    ListNode* new_tail = head;
    for (int i = 0; i < steps_to_new_tail; i++) {
        new_tail = new_tail->next;
    }
    
    // 4. Break the ring
    ListNode* new_head = new_tail->next;
    new_tail->next = nullptr;
    
    return new_head;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Parameter | Value |
| :--- | :--- |
| **Length Normalization** | $k_{	ext{eff}} = k \pmod L$ |
| **Time Complexity** | $\mathcal{O}(N)$ (At most 2 passes) |
| **Space Complexity** | Strictly $\mathcal{O}(1)$ |
