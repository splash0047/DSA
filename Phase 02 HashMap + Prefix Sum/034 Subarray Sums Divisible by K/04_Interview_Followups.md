# 04 Interview Follow-ups & System Variations: Subarray Sums Divisible by K

The problem counts non-empty subarrays whose sum is divisible by $k$. Using modular prefix sums and a remainder frequency array, the optimal solution runs in $\mathcal{O}(N + K)$ time and $\mathcal{O}(K)$ space.

In technical interviews, this problem is used to test modular arithmetic edge cases (negative modulo behavior), combinatorial prefix counting, and memory allocation trade-offs when $K \ll N$ vs. $K \gg N$.

---

## 1. The Negative Modulo Bug Across Languages (C++, Java vs. Python)

### 🛑 The Hazard
In C++ and Java, the `%` operator is the **remainder** operator, which retains the sign of the numerator:
- `-7 % 5 = -2` in C++ / Java.
- However, in modular arithmetic, $-2 \equiv 3 \pmod 5$.
- If you use `-2` as an array index, you cause an `OutOfBoundsException` / memory corruption.

### 💡 The Universal Positive Modulo Formula
Always normalize remainders into the range $[0, K - 1]$:
```cpp
int rem = ((running_sum % k) + k) % k;
```

---

## 2. Array vs. Hash Map: When to Use Which?

### 💡 Memory Optimization Rules
1. **When $K \le 10^5$ (e.g., $K \ll N$)**:
   - Use a direct fixed array: `int count[K] = {0}; count[0] = 1;`.
   - **Advantage**: $\mathcal{O}(K)$ direct L1-cache memory, 0 hashing collisions, zero heap allocations.
2. **When $K$ is Massive (e.g., $K = 10^9$)**:
   - Storing an array of size $10^9$ requires 4GB RAM.
   - Switch back to `unordered_map<int, int> count;` which only allocates entries for actual remainders encountered ($\le \min(N, K)$ entries).

---

## 3. Two Counting Equivalences: Running Accumulator vs. Combination Formula

### 💡 Why Both Formulas Yield the Exact Same Answer
- **Approach A (Online Accumulator)**:
  - For each element, `ans += count[rem]; count[rem]++;`.
- **Approach B (Combinatorial Batch)**:
  - Populate frequency array `count[rem]` for all elements.
  - Compute total pairs for each remainder:
    $$\text{Total} = \sum_{r=0}^{K-1} \frac{\text{count}[r] \times (\text{count}[r] - 1)}{2}$$
- Both are mathematically identical since $\sum_{i=1}^{m-1} i = \frac{m(m-1)}{2}$.

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | $K$ Magnitude | Data Structure | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Small $K$ ($K \le 10^5$)** | $K \ll N$ | Fixed Array `int count[k]` | $\mathcal{O}(N + K)$ | $\mathcal{O}(K)$ cache-friendly |
| **Massive $K$ ($K = 10^9$)** | $K \gg N$ | Hash Map `unordered_map` | $\mathcal{O}(N)$ | $\mathcal{O}(\min(N, K))$ |
| **Negative Numbers Present** | Any | Normalize via `((sum % k) + k) % k` | $\mathcal{O}(N)$ | $\mathcal{O}(K)$ |
