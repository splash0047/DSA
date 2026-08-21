# 04 Interview Follow-ups & System Variations: Implement Queue using Stacks

The problem implements a FIFO Queue using two LIFO Stacks (`in_stack` and `out_stack`). Pushes take $\mathcal{O}(1)$ and pops take $\mathcal{O}(1)$ amortized time with $\mathcal{O}(N)$ space.

In technical interviews, this problem tests amortized complexity proofs and multi-threaded lock decoupling.

---

## 1. Amortized $\mathcal{O}(1)$ Time Complexity Proof

### 💡 Lazy Transfer Invariant
- Elements are pushed directly to `in_stack` in $\mathcal{O}(1)$.
- When `pop()` or `peek()` is called:
  - If `out_stack` is not empty: Pop directly from `out_stack` in $\mathcal{O}(1)$.
  - If `out_stack` is empty: Transfer **all** elements from `in_stack` to `out_stack`.
- **Amortized Analysis**: Each element is pushed to `in_stack` once, transferred to `out_stack` once, and popped from `out_stack` once $\implies$ exactly 3 operations per element over its entire lifetime.
- Average cost per operation is $\mathcal{O}(1)$.

---

## 2. Thread-Safe Concurrency Optimization

### 💡 Lock Decoupling (Two Mutexes)
- Since `push()` only interacts with `in_stack` and `pop()` primarily interacts with `out_stack`, a producer thread and consumer thread can operate concurrently using separate locks on each stack without blocking each other (except during empty-transfer phase).

---

## Summary Matrix: Trade-offs at a Glance

| Operation | Amortized Time | Worst-Case Single Call | Space |
| :--- | :--- | :--- | :--- |
| `push(x)` | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ |
| `pop()` | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ auxiliary |
| `peek()` | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ auxiliary |
