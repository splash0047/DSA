# 04 Interview Follow-ups & System Variations: Longest Increasing Subsequence

The problem finds the length of the longest strictly increasing subsequence. While standard DP runs in $\mathcal{O}(N^2)$, the optimal **Patience Sorting (Greedy + Binary Search)** achieves $\mathcal{O}(N \log N)$ time and $\mathcal{O}(N)$ space.

In top-tier technical interviews, this is the premier example of replacing $\mathcal{O}(N^2)$ DP with binary search patience piles.

---

## 1. Patience Sorting with Binary Search ($\mathcal{O}(N \log N)$ Optimal)

### 💡 The `tails` Array Invariant
- Maintain an array `tails` where `tails[i]` stores the **smallest tail of all increasing subsequences of length $i + 1$** found so far.
- For each $x \in 	ext{nums}$:
  - Find first element in `tails` $\ge x$ using `std::lower_bound` in $\mathcal{O}(\log L)$.
  - If $x$ is greater than all elements: append $x$ to `tails`.
  - Else: overwrite `tails[idx] = x` (greedily lowers the bar for future extensions).
- **Result**: Length of LIS is `tails.size()`.

---

## 2. Generalization: 2D Russian Doll Envelopes (LeetCode #354 / Hard)

### 💡 2D Sort + 1D LIS Reduction
1. Sort envelopes by: **Width ASCENDING, and Height DESCENDING for ties**.
2. Run standard 1D LIS on the heights!
- *Why Height Descending?* Sorting heights in descending order ensures two envelopes with the exact same width can never be nested inside one another.
- **Time Complexity**: $\mathcal{O}(N \log N)$, **Space Complexity**: $\mathcal{O}(N)$.

---

## Summary Matrix: Trade-offs at a Glance

| Problem | Algorithm | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **1D LIS (#300)** | Patience Sorting + Binary Search | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ |
| **Russian Dolls (#354)**| 2D Sort + 1D Patience Sort | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ |
| **Dynamic LIS** | Fenwick Tree / Segment Tree | $\mathcal{O}(\log N)$ / insert | $\mathcal{O}(N)$ |
