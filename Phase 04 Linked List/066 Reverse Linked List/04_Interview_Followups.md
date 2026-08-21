# 04 Interview Follow-ups & System Variations: Reverse Linked List

The problem reverses a singly linked list. The optimal iterative approach uses 3 pointers (`prev`, `curr`, `next`) running in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this is the launchpad for questions on stack overflow hazards in recursion, sublist reversals, doubly linked list variants, and cache memory layout.

---

## 1. Iterative vs. Recursive Reversal

| Dimension | Iterative (3-Pointer) | Recursive |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **Space Complexity** | $\mathcal{O}(1)$ strictly | $\mathcal{O}(N)$ Call Stack Frames |
| **Stack Overflow Risk**| Zero risk (processes $10^9$ nodes) | **Crashes** for $N > 10^4$ (OS stack limit) |
| **Production Use** | **Industry Standard** | Avoid in systems code |

---

## 2. Generalization: Reverse a Sublist Between Positions $L$ and $R$ (LeetCode #92)

### 💡 1-Pass Head-Insertion Technique
- Navigate to node at position $L - 1$ (`pre`).
- Set `curr = pre->next`.
- For $R - L$ iterations:
  - Detach `next_node = curr->next`.
  - Splice `next_node` directly after `pre`:
    ```cpp
    curr->next = next_node->next;
    next_node->next = pre->next;
    pre->next = next_node;
    ```
- **Time Complexity**: $\mathcal{O}(N)$ 1-pass, **Space Complexity**: $\mathcal{O}(1)$.

---

## 3. Hardware Architecture: Linked List Cache Misses vs. Arrays

### 🛑 The Memory Fragmentation Reality
- Array elements are contiguous in physical RAM; hardware prefetchers load full 64-byte cache lines.
- Linked list nodes are allocated on the heap at arbitrary memory addresses.
- Every `curr = curr->next` pointer chase triggers a CPU L1/L2 cache miss.
- **System Insight**: In high-performance software, contiguous array-backed lists (or Unrolled Linked Lists) are preferred over classic pointer-based linked lists.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Technique | Time | Space |
| :--- | :--- | :--- | :--- |
| **Full Reverse** | Iterative 3-Pointer (`prev`, `curr`, `next`) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Sublist ($L \dots R$)** | 1-Pass Splice Head-Insertion | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Doubly Linked List** | Swap `curr->prev` and `curr->next` | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
