# 04 Interview Follow-ups & System Variations: Edit Distance

The problem finds the minimum operations (insert, delete, replace) to convert `word1` to `word2`. Optimal solutions use 2-Row Rolling 1D DP in $\mathcal{O}(M 	imes N)$ time and $\mathcal{O}(\min(M, N))$ space.

In technical interviews, this is the benchmark Levenshtein Distance problem. Interviewers probe Ukkonen's Banded Algorithm ($K$-bounded distance) and asymmetric operation costs.

---

## 1. Ukkonen's Banded Algorithm for Small Edit Distance $K$

### 🛑 The Inefficiency
If two strings have length $100,000$ and we only want to check if their edit distance is $\le 3$, computing full $10^{10}$ cells is wasteful.

### 💡 Banded Diagonal DP
- Only compute cells within distance $K$ of the main diagonal: $|i - j| \le K$.
- **Time Complexity**: $\mathcal{O}(K 	imes \min(M, N))$ instead of $\mathcal{O}(M 	imes N)$!

---

## Summary Matrix: Trade-offs at a Glance

| Variant | Strategy | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Standard Levenshtein** | 2-Row Rolling DP | $\mathcal{O}(MN)$ | $\mathcal{O}(\min(M, N))$ |
| **Bounded Edit Distance ($K$)**| Ukkonen's Diagonal Band | $\mathcal{O}(K \cdot \min(M, N))$ | $\mathcal{O}(K)$ |
