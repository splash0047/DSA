# 04 Interview Follow-ups & System Variations: Aggressive Cows

The problem places $C$ cows into $N$ stalls such that the minimum distance between any two cows is maximized. The optimal approach sorts the stall coordinates and uses **Binary Search on the Answer (Max-Min Distance)** in $\mathcal{O}(N \log(	ext{stalls}[N-1] - 	ext{stalls}[0]))$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is the foundational template for Maximize-the-Minimum placement constraints.

---

## 1. Why Sort Stalls First?

### 💡 Greedy Nearest-Neighbor Placement
- In an unsorted array of positions, checking distance feasibility requires combinatorial search.
- Once sorted, the optimal greedy strategy to place cows with at least distance $D$ is:
  1. Always place the 1st cow at `stalls[0]`.
  2. Place the next cow at the first stall `stalls[i]` where $	ext{stalls}[i] - 	ext{last\_stall} \ge D$.
  3. If $\ge C$ cows can be placed, distance $D$ is feasible.

---

## Summary Matrix: Trade-offs at a Glance

| Parameter | Value |
| :--- | :--- |
| **Search Space** | $[1, 	ext{stalls}[N-1] - 	ext{stalls}[0]]$ |
| **Feasibility Test** | Greedy placement from stall 0 in $\mathcal{O}(N)$ |
| **Time Complexity** | $\mathcal{O}(N \log N + N \log(	ext{Range}))$ |
| **Space Complexity** | $\mathcal{O}(1)$ / $\mathcal{O}(\log N)$ sort space |
