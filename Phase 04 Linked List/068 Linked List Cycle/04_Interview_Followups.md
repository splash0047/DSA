# 04 Interview Follow-ups & System Variations: Linked List Cycle

The problem detects whether a linked list contains a cycle. Floyd's **Tortoise and Hare Algorithm** (`slow` moves 1 step, `fast` moves 2 steps) achieves $\mathcal{O}(N)$ time and strictly $\mathcal{O}(1)$ space.

In technical interviews, interviewers test mathematical convergence proofs, Hash Set trade-offs, and non-destructive node marking.

---

## 1. Mathematical Proof: Why `fast` is Guaranteed to Catch `slow`

### 💡 The Relative Speed Invariant
- Let the cycle length be $C$.
- Once both `slow` and `fast` are inside the cycle, let the distance between them (measuring clockwise from `slow` to `fast`) be $d$.
- In each step:
  - `slow` moves 1 step clockwise: $+1$.
  - `fast` moves 2 steps clockwise: $+2$.
  - Relative distance increases by $+1$ each step: $(d + 1) \pmod C$.
- Therefore, the remaining gap $C - (d + 1)$ decreases by strictly $1$ on every iteration.
- Because the gap decreases by 1 integer step each time, `fast` cannot "hop over" `slow` without landing on the exact same node. The gap reaches 0 in at most $C$ steps.

---

## 2. Floyd's Algorithm vs. Hash Set vs. Node Modification

| Method | Time | Space | Modifies List? |
| :--- | :--- | :--- | :--- |
| **Floyd's Tortoise & Hare** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | **No (Safe & Optimal)** |
| **Hash Set of Addresses** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | No |
| **Node Value Sentinel Tag** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Destructive (Corrupts data) |
| **Reversing Pointers Visited**| $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Destructive |

---

## Summary Matrix: Trade-offs at a Glance

| Parameter | Value |
| :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N + C)$ where $N$ is tail length and $C$ is cycle size |
| **Space Complexity** | Strictly $\mathcal{O}(1)$ |
| **Cycle Entrance Found?** | No (Only detects boolean presence; use Cycle II for node) |
