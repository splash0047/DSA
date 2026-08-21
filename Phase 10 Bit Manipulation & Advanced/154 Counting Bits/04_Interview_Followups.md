# 04 Interview Follow-ups & System Variations: Counting Bits

The problem returns an array of the number of 1 bits for every integer from $0$ to $N$. Optimal Bit Manipulation DP calculates the result in strictly $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ output space.

In technical interviews, this problem tests bitwise DP state transitions.

---

## 1. Two Bitwise Dynamic Programming Recurrences

### 💡 Recurrence A: Right-Shift (Even/Odd Transition)
$$	ext{ans}[i] = 	ext{ans}[i \gg 1] + (i \ \& \ 1)$$
- Every right-shifted number $i \gg 1$ has already been computed. Add 1 if the last bit is set.

### 💡 Recurrence B: Brian Kernighan's Step
$$	ext{ans}[i] = 	ext{ans}[i \ \& \ (i - 1)] + 1$$
- $i \ \& \ (i - 1)$ has strictly 1 fewer set bit than $i$.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Formula | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Right-Shift DP** | `ans[i >> 1] + (i & 1)` | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ auxiliary |
| **Lowest-Bit DP** | `ans[i & (i - 1)] + 1` | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ auxiliary |
| **Naive Popcount** | Call popcount on each $i$ | $\mathcal{O}(N \log N)$ | $\mathcal{O}(1)$ auxiliary |
