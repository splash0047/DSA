# 04 Interview Follow-ups & System Variations: Find Pivot Index

The problem finds the leftmost pivot index where the sum of numbers strictly to the left equals the sum of numbers strictly to the right. The optimal approach calculates `total_sum` in Pass 1, then maintains `left_sum` in Pass 2 checking `left_sum == total_sum - left_sum - nums[i]` in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem tests prefix balance equations, 2D matrix pivot extensions, integer overflow safeguards, and stream limitations.

---

## 1. Mathematical Derivation of the $\mathcal{O}(1)$ Space Balance Condition

### 💡 The Balance Equation
- Let `total_sum` be the sum of all elements in the array.
- For any candidate pivot index $i$:
  $$\text{RightSum} = \text{total\_sum} - \text{left\_sum} - \text{nums}[i]$$
- Equating $\text{LeftSum} = \text{RightSum}$:
  $$\text{left\_sum} = \text{total\_sum} - \text{left\_sum} - \text{nums}[i]$$
  $$2 \times \text{left\_sum} + \text{nums}[i] = \text{total\_sum}$$
- **Advantage**: Eliminates the need for any prefix or suffix array; requires only 2 scalar variables.

---

## 2. Integer Overflow Safeguard in 64-bit Systems

### 🛑 Potential Bug
If array contains $10^6$ elements of value $10^4$, `total_sum` reaches $10^{10}$, exceeding standard 32-bit signed integer limits ($2 \times 10^9$).
- **Rule**: Always accumulate `total_sum` and `left_sum` using `long long` in C++ or `long` in Java.

---

## 3. Generalization: 2D Matrix Pivot Row and Pivot Column

### 💡 2D Balance Analysis
1. **Pivot Row**: A row $r$ where sum of all elements in rows $0 \dots r-1$ equals sum of all elements in rows $r+1 \dots R-1$.
   - Precompute 1D array of row sums in $\mathcal{O}(R \times C)$ time.
   - Run 1D Pivot Index on the row sums array in $\mathcal{O}(R)$ time.
2. **Pivot Column**: A column $c$ where sum of columns to the left equals sum of columns to the right.
   - Compute column sums in $\mathcal{O}(R \times C)$ time; run 1D Pivot Index in $\mathcal{O}(C)$ time.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Space Model | Strategy | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **1D Array (Standard)** | Primitive Scalars | `total_sum` pass + `left_sum` pass | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **2D Matrix Pivot Row/Col**| 1D Array of sums | Row/Col sum compression $\to$ 1D Pivot | $\mathcal{O}(R \times C)$ | $\mathcal{O}(R + C)$ |
| **Unbounded Stream** | Streaming | Requires buffering / 2-pass disk | $\mathcal{O}(N)$ I/O | $\mathcal{O}(N)$ buffer |
