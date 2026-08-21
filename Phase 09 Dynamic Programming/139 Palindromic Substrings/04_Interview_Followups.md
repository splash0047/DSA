# 04 Interview Follow-ups & System Variations: Palindromic Substrings

The problem counts the total number of palindromic substrings in $S$. Expand Around Center runs in $\mathcal{O}(N^2)$ time and $\mathcal{O}(1)$ space, and Manacher's Algorithm runs in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

In technical interviews, this problem is used to show how Manacher's radius array yields the total count in a single mathematical sum.

---

## 1. Counting Palindromes via Manacher's Radius Array in $\mathcal{O}(N)$

### 💡 Radius Sum Formula
- After running Manacher's Algorithm to compute radius array $P$:
  $$	ext{Total Palindromic Substrings} = \sum_{i=0}^{2N} \lfloor rac{P[i] + 1}{2} floor$$
- **Time Complexity**: $\mathcal{O}(N)$ single pass, **Space Complexity**: $\mathcal{O}(N)$.

---

## Summary Matrix: Trade-offs at a Glance

| Method | Time | Space | Complexity |
| :--- | :--- | :--- | :--- |
| **Expand Around Center** | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | $2N - 1$ centers |
| **Manacher's Radius Sum**| $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | 1 linear pass |
