# 04 Interview Follow-ups & System Variations: Intersection of Two Linked Lists

The problem finds the node where two singly linked lists intersect. The optimal two-pointer approach switches heads (`pA = (pA == nullptr) ? headB : pA->next`) in $\mathcal{O}(M + N)$ time and strictly $\mathcal{O}(1)$ space.

In technical interviews, this problem tests path length normalization proofs and intersection scenarios when cycles exist.

---

## 1. Mathematical Proof of the Head-Switch Traversal

### 💡 The Commutative Distance Invariant
- Let:
  - $a$ = length of non-shared prefix of List A.
  - $b$ = length of non-shared prefix of List B.
  - $c$ = length of shared intersection tail.
- Pointer A traverses: $a + c + b$.
- Pointer B traverses: $b + c + a$.
- Since $a + c + b = b + c + a$, both pointers traverse the exact same total distance!
- If the lists intersect, they will collide at the intersection node on the second pass.
- If the lists do not intersect ($c = 0$), both reach `nullptr` simultaneously ($a + b = b + a$) and terminate safely.

---

## 2. What if the Linked Lists May Contain CYCLES?

### 💡 3 Cycle Topology Scenarios
1. **Neither list has a cycle**: Standard intersection algorithm applies.
2. **Only one list has a cycle**: Mathematical impossibility for intersection; return `nullptr`.
3. **Both lists have cycles**:
   - Case 3A (Intersect before cycle): Intersection entrance found before cycle entry.
   - Case 3B (Intersect at cycle entrance / inside cycle): Pointers traverse the shared cycle; both loop entries are valid intersection points.
   - Case 3C (Disjoint cycles): Lists do not share the cycle; return `nullptr`.

---

## Summary Matrix: Trade-offs at a Glance

| Topology | Approach | Time | Space |
| :--- | :--- | :--- | :--- |
| **Acyclic Lists** | Head-switch Two Pointers | $\mathcal{O}(M+N)$ | $\mathcal{O}(1)$ |
| **Acyclic Lists (Length Diff)**| Compute lengths $\Delta = |M - N|$ | $\mathcal{O}(M+N)$ | $\mathcal{O}(1)$ |
| **Cyclic Lists** | Floyd's Cycle II + Topology Case Check | $\mathcal{O}(M+N)$ | $\mathcal{O}(1)$ |
