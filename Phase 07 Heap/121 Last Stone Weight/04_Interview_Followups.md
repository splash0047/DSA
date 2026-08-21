# 04 Interview Follow-ups & System Variations: Last Stone Weight

The problem simulates smashing the two heaviest stones until at most 1 stone remains. The optimal solution uses a **Max-Heap** in $\mathcal{O}(N \log N)$ time and $\mathcal{O}(N)$ space.

In technical interviews, this problem is contrasted with **Last Stone Weight II** (0-1 Knapsack DP).

---

## 1. Last Stone Weight I vs. Last Stone Weight II (LeetCode #1049)

| Problem | Stone Choice Rule | Problem Reduction | Optimal Strategy | Time |
| :--- | :--- | :--- | :--- | :--- |
| **Stone Weight I (#1046)**| Greedily smash 2 heaviest | Simulation | Max-Heap | $\mathcal{O}(N \log N)$ |
| **Stone Weight II (#1049)**| Choose arbitrary order to minimize final stone | Partition into two sets $S_1, S_2$ with min difference $|S_1 - S_2|$ | 0-1 Knapsack Dynamic Programming | $\mathcal{O}(N 	imes \sum W)$ |

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Core Technique | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Greedy Smashing (I)** | Max-Heap Simulation | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ |
| **Optimal Minimal (II)** | 0-1 Knapsack Subset Sum DP | $\mathcal{O}(N 	imes 	ext{Sum})$ | $\mathcal{O}(	ext{Sum})$ |
