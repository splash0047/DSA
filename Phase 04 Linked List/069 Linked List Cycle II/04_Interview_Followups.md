# 04 Interview Follow-ups & System Variations: Linked List Cycle II

The problem finds the exact node where a cycle begins in a singly linked list. Floyd's Cycle Algorithm combined with a second phase of pointers moving from `head` and `meeting_point` finds the entrance in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this is the standard mathematical derivation test in pointer algorithms.

---

## 1. Mathematical Derivation of Cycle Entrance Equality

### 💡 The Distance Equation
- Let:
  - $L$ = distance from `head` to cycle entrance.
  - $C$ = circumference (length) of the cycle.
  - $x$ = distance from cycle entrance to meeting point inside the cycle.
- Total distance traveled by `slow` when they meet:
  $$D_{	ext{slow}} = L + x$$
- Total distance traveled by `fast` when they meet (with $k$ full cycle loops):
  $$D_{	ext{fast}} = L + k \cdot C + x$$
- Because `fast` travels at twice the speed of `slow`:
  $$D_{	ext{fast}} = 2 \cdot D_{	ext{slow}}$$
  $$L + k \cdot C + x = 2(L + x)$$
  $$L + k \cdot C + x = 2L + 2x$$
  $$L = k \cdot C - x = (k - 1) \cdot C + (C - x)$$
- **Conclusion**: The distance from `head` to the cycle entrance ($L$) is mathematically identical to the distance from the `meeting_point` to the cycle entrance ($C - x$) plus $(k - 1)$ full cycle loops.
- **Algorithm Phase 2**: Reset `p1 = head`, keep `p2 = meeting_point`. Advance both 1 step at a time; they will collide precisely at the cycle entrance!

---

## 2. Calculating the Exact Length of the Cycle $C$

### 💡 Simple Pointer Loop
- After finding `meeting_point`:
  - Keep `curr = meeting_point->next`, `length = 1`.
  - While `curr != meeting_point`: `curr = curr->next; length++;`.
- Returns exact number of nodes in the cycle in $\mathcal{O}(C)$ time.

---

## Summary Matrix: Trade-offs at a Glance

| Phase | Purpose | Pointers | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 1** | Detect collision | `slow` (1x), `fast` (2x) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Phase 2** | Find entrance | `head` (1x), `meeting` (1x)| $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Cycle Length** | Count nodes in cycle | Advance until return to meeting | $\mathcal{O}(C)$ | $\mathcal{O}(1)$ |
