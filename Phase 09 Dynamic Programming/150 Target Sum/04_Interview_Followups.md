# 04 Interview Follow-ups & System Variations: Target Sum

The problem assigns `+` and `-` signs to array elements to equal `target`. By algebraic reformulation, this transforms into **0-1 Knapsack Subset Sum** for $P = (	ext{target} + 	ext{sum}) / 2$ in $\mathcal{O}(N 	imes P)$ time and $\mathcal{O}(P)$ space.

In technical interviews, this problem tests problem inversion into standard DP models.

---

## 1. Algebraic Reduction to Subset Sum

### 💡 Mathematical Derivation
- Let $P$ be the subset of numbers with `+` sign, and $N$ be the subset with `-` sign:
  $$	ext{Sum}(P) - 	ext{Sum}(N) = 	ext{target}$$
  $$	ext{Sum}(P) + 	ext{Sum}(N) = 	ext{total\_sum}$$
- Adding the two equations:
  $$2 	imes 	ext{Sum}(P) = 	ext{target} + 	ext{total\_sum} \implies 	ext{Sum}(P) = rac{	ext{target} + 	ext{total\_sum}}{2}$$
- **Impossibility Checks**:
  1. `(target + total_sum)` must be non-negative and even.
  2. `abs(target) <= total_sum`.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Problem Form | Time | Space |
| :--- | :--- | :--- | :--- |
| **Subset Sum DP (Optimal)**| Find subsets summing to $P$ | $\mathcal{O}(N \cdot P)$ | $\mathcal{O}(P)$ |
| **Recursion with Memo** | 2D `(index, current_sum)` | $\mathcal{O}(N \cdot 	ext{Sum})$ | $\mathcal{O}(N \cdot 	ext{Sum})$ |
