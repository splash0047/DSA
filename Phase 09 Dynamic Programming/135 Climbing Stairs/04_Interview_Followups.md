# 04 Interview Follow-ups & System Variations: Climbing Stairs

The problem finds the number of distinct ways to climb $N$ stairs (taking 1 or 2 steps). Standard approaches include 1D DP / 2-variable Fibonacci iteration in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In top-tier technical interviews, this problem is the gateway to **Matrix Exponentiation for $N = 10^9$**, variable step generalizations ($K$ steps), and closed-form Binet equations.

---

## 1. What if $N = 10^{18}$ (Scaling to Billions with Matrix Exponentiation)?

### 🛑 Why Linear $\mathcal{O}(N)$ Fails
If $N = 10^{18}$, looping $N$ times takes hundreds of years of CPU time.

### 💡 $\mathcal{O}(\log N)$ Matrix Fast Power
- Formulate the recurrence as a matrix transition:
  $$egin{pmatrix} F(n+1) \ F(n) \end{pmatrix} = egin{pmatrix} 1 & 1 \ 1 & 0 \end{pmatrix} egin{pmatrix} F(n) \ F(n-1) \end{pmatrix} \implies egin{pmatrix} F(n+1) \ F(n) \end{pmatrix} = egin{pmatrix} 1 & 1 \ 1 & 0 \end{pmatrix}^N egin{pmatrix} F(1) \ F(0) \end{pmatrix}$$
- Compute the $N$-th power of the $2 	imes 2$ matrix using **Binary Exponentiation** (Repeated Squaring) in $\mathcal{O}(\log N)$ multiplications.
- Supports answers modulo $10^9 + 7$.

---

## 2. Generalization: Climbing Stairs with $K$ Steps (1 to $K$ Steps per Leap)

### 💡 Sliding Window DP ($\mathcal{O}(N)$ Time)
- Recurrence: $DP[i] = \sum_{j=1}^K DP[i - j]$.
- Instead of summing $K$ elements every step ($\mathcal{O}(N \cdot K)$):
  - Maintain a running `window_sum`.
  - $DP[i] = 	ext{window\_sum}$.
  - Slide window: `window_sum += DP[i] - DP[i - K]`.
- **Time Complexity**: strictly $\mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(K)$.

---

## Summary Matrix: Trade-offs at a Glance

| Constraint / Scale | Optimal Approach | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Standard $N \le 10^5$** | 2-Variable Fibonacci State | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Massive $N = 10^{18}$** | Matrix Exponentiation | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| **$K$ Variable Steps** | Sliding Window DP Accumulator | $\mathcal{O}(N)$ | $\mathcal{O}(K)$ |
