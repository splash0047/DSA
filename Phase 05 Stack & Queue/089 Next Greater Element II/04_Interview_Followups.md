# 04 Interview Follow-ups & System Variations: Next Greater Element II

The problem finds the next greater element in a **Circular Array**. The optimal approach iterates through the array twice ($2N$ steps) using modulo indexing `i % n` with a Monotonic Decreasing Stack in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

In technical interviews, this problem tests virtual array unrolling and circular boundary invariants.

---

## 1. The $2N$ Virtual Unrolling Pattern

### 💡 Why $2N - 1$ Steps Suffice
- In a circular array of size $N$, every element can look ahead at most $N - 1$ positions.
- Looping $i$ from $0$ to $2N - 1$ simulates traversing the array concatenated with itself `nums + nums`.
- Only push to stack during the first pass ($i < N$); the second pass serves only to resolve unresolved elements remaining in the stack.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Traversal Range | Time | Space |
| :--- | :--- | :--- | :--- |
| **Linear Array (I)** | $0 \dots N-1$ | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **Circular Array (II)**| $0 \dots 2N-1$ via `i % n` | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
