# 04 Interview Follow-ups & System Variations: Split Array Largest Sum

The problem splits `nums` into $k$ contiguous subarrays such that the largest subarray sum is minimized. While 2D Dynamic Programming solves this in $\mathcal{O}(k \cdot N^2)$, the optimal Binary Search on the Answer achieves $\mathcal{O}(N \log(\sum 	ext{nums}))$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem tests DP vs. Binary Search trade-offs and fractional relaxations.

---

## 1. Binary Search on Answer ($\mathcal{O}(N \log S)$) vs. Dynamic Programming ($\mathcal{O}(k N^2)$)

| Approach | Recurrence / State | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Dynamic Programming** | $DP[i][j] = \min_{p} \max(DP[p][j-1], 	ext{sum}(p \dots i))$ | $\mathcal{O}(k \cdot N^2)$ | $\mathcal{O}(k \cdot N)$ |
| **Binary Search on Answer** | Guess max sum $M \in [\max(A), \sum A]$ | $\mathcal{O}(N \log(\sum A))$ | $\mathcal{O}(1)$ |

- **Takeaway**: Always recognize when a minimax/maximin optimization problem has a monotonic feasibility predicate, allowing an exponential speedup from $\mathcal{O}(k N^2) 	o \mathcal{O}(N \log S)$.

---

## Summary Matrix: Trade-offs at a Glance

| Dimension | Min Value | Max Value | Optimal Algorithm |
| :--- | :--- | :--- | :--- |
| **Search Range** | $\max(	ext{nums})$ | $\sum 	ext{nums}$ | Binary Search on Max Subarray Sum |
| **Feasibility Pass**| Subarrays needed $\le k$ | Greedy contiguous accumulator | $\mathcal{O}(N)$ time, $\mathcal{O}(1)$ space |
