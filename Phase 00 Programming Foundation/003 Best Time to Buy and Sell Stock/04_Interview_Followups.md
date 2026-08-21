# 04 Interview Follow-ups & System Variations: Best Time to Buy and Sell Stock

The standard problem asks for a single transaction (1 buy, 1 sell) maximizing profit in an unsorted array of daily prices. The greedy/Kadane-like approach tracks `min_price_so_far` and updates `max_profit = max(max_profit, price - min_price_so_far)` in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In advanced interviews, this problem is a stepping stone to state machines, dynamic programming extensions, high-frequency streaming, and distributed parallel processing.

---

## 1. How to Parallelize This for 1 Billion Stock Ticks (Distributed MapReduce / Fork-Join)?

### 🛑 The Challenge
Can we compute the global maximum single-transaction profit across $M$ machines in parallel without processing the whole array sequentially on a single core?

### 💡 Associative Chunk Reduction (Parallel Divide & Conquer)
Represent each price chunk $C$ as a summary tuple of 3 values:
$$\text{Tuple}(C) = \{\text{min\_val}, \text{max\_val}, \text{max\_profit}\}$$

For two adjacent contiguous chunks $L$ (Left) and $R$ (Right), combine them associatively:
1. $\text{min\_val}_{\text{combined}} = \min(L.\text{min\_val}, R.\text{min\_val})$
2. $\text{max\_val}_{\text{combined}} = \max(L.\text{max\_val}, R.\text{max\_val})$
3. $\text{max\_profit}_{\text{combined}} = \max\Big(L.\text{max\_profit},\; R.\text{max\_profit},\; R.\text{max\_val} - L.\text{min\_val}\Big)$

- **Significance**: Because merge operation is strictly associative, this can be implemented in **SIMD/AVX vectorization**, **OpenMP multi-threading**, or **MapReduce / Apache Spark TreeAggregate** running in $\mathcal{O}(\frac{N}{P} + \log P)$ time across $P$ processors.

---

## 2. What if Unlimited Transactions Are Allowed (LeetCode #122: Stock II)?

### 💡 Greedy Local Monotonicity
- Buy on every local dip and sell on every local rise.
- Sum up every positive adjacent difference:
  $$\text{Total Profit} = \sum_{i=1}^{N-1} \max(0, \text{prices}[i] - \text{prices}[i-1])$$
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(1)$.

---

## 3. What if at Most $K$ Transactions Are Allowed (LeetCode #188: Stock IV)?

### 💡 Dynamic Programming & Memory Optimization
1. If $K \ge \frac{N}{2}$, it degenerates to unlimited transactions (Greedy Stock II) in $\mathcal{O}(N)$ time.
2. Otherwise, maintain two arrays of size $K + 1$:
   - `buy[j]`: maximum profit achievable with at most $j$ transactions currently holding a stock.
   - `sell[j]`: maximum profit achievable with at most $j$ transactions not holding stock.
   - Transitions for each price $P$:
     $$\text{buy}[j] = \max(\text{buy}[j],\; \text{sell}[j-1] - P)$$
     $$\text{sell}[j] = \max(\text{sell}[j],\; \text{buy}[j] + P)$$
- **Time Complexity**: $\mathcal{O}(N \cdot K)$, **Space Complexity**: $\mathcal{O}(K)$ (reduced from $\mathcal{O}(N \cdot K)$).

---

## 4. What if There is a Transaction Fee or Cooldown Period?

### 💡 2-State / 3-State Machine
- **With Fixed Fee $F$**:
  - `buy = max(buy, sell - price)`
  - `sell = max(sell, buy + price - fee)`
- **With 1-Day Cooldown (LeetCode #309)**:
  - `held = max(held, rest - price)`
  - `sold = held + price`
  - `rest = max(rest, prev_sold)`

---

## 5. What if the Prices Come as an Infinite Real-Time Stream (Sliding Window of Size $W$)?

### 🛑 The Scenario
We want to continuously report the maximum profit possible within the most recent $W$ seconds/ticks.

### 💡 Data Structure: Monotonic Deques & Segment Tree
- In a sliding window of size $W$, $L.\text{min\_val}$ and $R.\text{max\_val}$ must respect temporal ordering ($i_{\text{buy}} \le i_{\text{sell}}$ within window $W$).
- **Segment Tree / Range Maximum Query**:
  - Maintain a dynamic segment tree of current window elements storing the associative tuple $\{\text{min}, \text{max}, \text{profit}\}$.
  - Point updates and window shifts take $\mathcal{O}(\log W)$ time per incoming tick.

---

## 6. What if Short-Selling is Allowed?

### 💡 Bidirectional Profit
- Standard Long Trade: Buy low, sell high $\implies \max(P_{\text{sell}} - P_{\text{buy}})$ where $\text{index}_{\text{buy}} < \text{index}_{\text{sell}}$.
- Short Trade: Sell high, buy back low $\implies \max(P_{\text{short}} - P_{\text{cover}})$ where $\text{index}_{\text{short}} < \text{index}_{\text{cover}}$.
- Track both `min_so_far` and `max_so_far` in a single pass to find optimal long and short trades simultaneously.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Core Strategy | Time | Space |
| :--- | :--- | :--- | :--- |
| **Stock I (1 Transaction)** | Greedy `min_price_so_far` | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Stock II (Unlimited)** | Sum all positive slope increments | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Stock III ($K = 2$)** | 4-variable state machine | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Stock IV ($K$ Transactions)** | 1D DP arrays (`buy[k]`, `sell[k]`) | $\mathcal{O}(N \cdot K)$ | $\mathcal{O}(K)$ |
| **Stock with Cooldown** | 3-State Finite State Machine | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **1B Ticks Parallelized** | Associative Tuple Merge Reduction | $\mathcal{O}(N/P + \log P)$ | $\mathcal{O}(P)$ |
| **Sliding Window Stream** | Dynamic Segment Tree on window $W$ | $\mathcal{O}(\log W)$ / tick | $\mathcal{O}(W)$ |
