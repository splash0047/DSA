# 04 Interview Follow-ups & System Variations: Longest Palindromic Substring

The problem finds the longest palindromic substring in $S$. While Expand Around Center runs in $\mathcal{O}(N^2)$ time and $\mathcal{O}(1)$ space, the optimal **Manacher's Algorithm** achieves strictly $\mathcal{O}(N)$ linear time and $\mathcal{O}(N)$ space.

In technical interviews, this problem is the gold standard for linear string algorithms and palindromic radius symmetry.

---

## 1. Manacher's Algorithm ($\mathcal{O}(N)$ Linear Time)

### 💡 Virtual Character Insertion & Symmetry Radius
1. Preprocess string with `#` delimiters (e.g., `"aba"` $	o$ `"#a#b#a#"` of length $2N + 1$) so all even and odd palindromes have odd lengths.
2. Maintain `center` $C$ and right boundary $R$.
3. For each index $i$:
   - Let mirror index be $i' = 2C - i$.
   - If $i < R$, initialize radius $P[i] = \min(R - i, P[i'])$.
   - Expand palindrome radius around $i$ while characters match.
   - If $i + P[i] > R$, update new center $C = i$ and boundary $R = i + P[i]$.
- **Time Complexity**: $\mathcal{O}(N)$ strictly (each right expansion advances $R$ forward).

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Time Complexity | Space Complexity | Best Used When |
| :--- | :--- | :--- | :--- |
| **Expand Around Center** | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | Short strings / Simple code |
| **2D Dynamic Programming**| $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | Substring range queries |
| **Manacher's Algorithm** | **$\mathcal{O}(N)$ (Optimal)** | $\mathcal{O}(N)$ | Production string matching |
