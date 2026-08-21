# 04 Interview Follow-ups & System Variations: Coin Change

The problem finds the fewest coins needed to make up a given amount (Unbounded Knapsack). The optimal bottom-up DP runs in $\mathcal{O}(	ext{amount} 	imes C)$ time and $\mathcal{O}(	ext{amount})$ space, or BFS for shortest unweighted path.

In technical interviews, interviewers test why greedy fails on non-canonical currency systems and integer linear programming at scale.

---

## 1. Why Greedy Fails on Arbitrary Coin Systems (Canonical Coin Systems)

### 🛑 The Greedy Counter-Example
Suppose coins are `[1, 3, 4]` and target amount is `6`:
- **Greedy Choice**: Picks largest coin $4$, leaving remainder $2 \implies 4 + 1 + 1 = 3	ext{ coins}$.
- **Optimal Choice**: $3 + 3 = 2	ext{ coins}$.
- **Insight**: Greedy is only optimal for **Canonical Coin Systems** (like US/Euro currency: 1, 5, 10, 25, 100). For arbitrary integer denominations, Dynamic Programming is mandatory.

---

## 2. Dynamic Programming vs. Breadth-First Search (BFS)

| Method | Best Scenario | Time | Space |
| :--- | :--- | :--- | :--- |
| **Bottom-Up DP** | Computing all amounts $\le A$ | $\mathcal{O}(A 	imes C)$ | $\mathcal{O}(A)$ array |
| **BFS Shortest Path** | Small answer (e.g., amount reached in 3 coins) | $\mathcal{O}(C^{	ext{depth}})$ | $\mathcal{O}(A)$ visited |

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Space Model | Time | Space |
| :--- | :--- | :--- | :--- |
| **Bottom-Up 1D DP** | Tabulation | $\mathcal{O}(	ext{Amount} 	imes C)$ | $\mathcal{O}(	ext{Amount})$ |
| **BFS Shortest Path** | Queue of states | $\mathcal{O}(	ext{Amount} 	imes C)$ | $\mathcal{O}(	ext{Amount})$ |
