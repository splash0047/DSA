# 04 Interview Follow-ups & System Variations: Add Two Numbers

The problem adds two numbers represented by linked lists in reverse order (Least Significant Digit first). The optimal single-pass approach uses a `carry` accumulator and dummy head in $\mathcal{O}(\max(M, N))$ time and $\mathcal{O}(\max(M, N))$ output space.

In technical interviews, this problem is extended to MSB-first addition (Add Two Numbers II) and database BigInt arithmetic engines.

---

## 1. What if Digits Are Stored in Forward Order (MSB First / LeetCode #445)?

### 💡 Two Optimal Solutions
1. **Stack-Based Evaluation**:
   - Push digits of List 1 onto `Stack1` and List 2 onto `Stack2`.
   - Pop from stacks to add least significant digits first.
   - Build result linked list **backwards** using head-insertions (`newNode->next = head; head = newNode;`).
   - **Time**: $\mathcal{O}(M + N)$, **Space**: $\mathcal{O}(M + N)$.
2. **Reverse Lists First (if mutation is permitted)**:
   - In-place reverse both input lists in $\mathcal{O}(1)$ space.
   - Run standard Add Two Numbers.
   - Reverse inputs and output back to original order.
   - **Time**: $\mathcal{O}(M + N)$, **Space**: $\mathcal{O}(1)$ extra space.

---

## 2. Long Carry Propagation Chains (`9999 + 1`)

### 🛑 Potential Inefficiency
When adding 1 to a chain of 9s, the carry propagates all the way to the end, creating a new leading node (`10000`).
- The loop condition `while (l1 || l2 || carry)` handles this edge case without special post-loop conditionals.

---

## Summary Matrix: Trade-offs at a Glance

| Digit Order | Permitted Actions | Strategy | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **LSB First (#2)** | Output allocation | Single-pass pointer traverse | $\mathcal{O}(\max(M, N))$ | $\mathcal{O}(1)$ auxiliary |
| **MSB First (#445)**| Cannot modify input| 2 Stacks + Head insertion | $\mathcal{O}(M+N)$ | $\mathcal{O}(M+N)$ |
| **MSB First (#445)**| Can modify input | Reverse $	o$ Add $	o$ Reverse | $\mathcal{O}(M+N)$ | $\mathcal{O}(1)$ auxiliary |
