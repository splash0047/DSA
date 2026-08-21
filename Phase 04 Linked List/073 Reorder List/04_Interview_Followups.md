# 04 Interview Follow-ups & System Variations: Reorder List

The problem reorders a singly linked list from $L_0 	o L_1 	o \dots 	o L_{n-1} 	o L_n$ into $L_0 	o L_n 	o L_1 	o L_{n-1} 	o L_2 \dots$ in-place. The optimal approach uses a 3-step pipeline in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this is the ultimate composite linked list problem, combining middle-finding, list reversal, and two-way list interleaving.

---

## 1. The 3-Step Pipeline ($\mathcal{O}(N)$ Time, $\mathcal{O}(1)$ Space)

### 💡 Step-by-Step Architecture
1. **Find First Middle**:
   - `while (fast->next && fast->next->next)`
   - Disconnect halves: `ListNode* second = slow->next; slow->next = nullptr;`.
2. **Reverse the Second Half**:
   - In-place reversal of `second` to produce reversed list `l2`.
3. **Interleave / Merge Alternate Nodes**:
   ```cpp
   ListNode* l1 = head;
   while (l2) {
       ListNode* next1 = l1->next;
       ListNode* next2 = l2->next;
       
       l1->next = l2;
       l2->next = next1;
       
       l1 = next1;
       l2 = next2;
   }
   ```

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Space Model | Time | Extra Memory |
| :--- | :--- | :--- | :--- |
| **Array of Pointers** | Buffer all nodes | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ extra space |
| **3-Step In-Place Splicing**| Pure pointer rewiring | $\mathcal{O}(N)$ | strictly $\mathcal{O}(1)$ |
