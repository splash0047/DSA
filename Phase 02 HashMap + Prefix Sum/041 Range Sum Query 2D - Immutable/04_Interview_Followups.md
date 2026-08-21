# 04 Interview Follow-ups & System Variations: Range Sum Query 2D - Immutable

The problem computes the sum of elements inside a 2D submatrix defined by top-left $(r_1, c_1)$ and bottom-right $(r_2, c_2)$ on an immutable matrix. Using a 2D Prefix Sum table and the **Inclusion-Exclusion Principle**, preprocessing takes $\mathcal{O}(R \times C)$ and each query runs in $\mathcal{O}(1)$ time with $\mathcal{O}(R \times C)$ space.

In technical interviews, this is extended to 2D Mutable Range Sums (2D Fenwick Tree), 2D Difference Matrices, 3D Spatial Tensors, and cache-friendly matrix flattening.

---

## 1. Mathematical Derivation of 2D Inclusion-Exclusion

### 💡 Preprocessing Formula
$$\text{Pref}[r+1][c+1] = \text{Matrix}[r][c] + \text{Pref}[r][c+1] + \text{Pref}[r+1][c] - \text{Pref}[r][c]$$

### 💡 Query Submatrix Formula
$$\text{Sum}(r_1, c_1 \dots r_2, c_2) = \text{Pref}[r_2+1][c_2+1] - \text{Pref}[r_1][c_2+1] - \text{Pref}[r_2+1][c_1] + \text{Pref}[r_1][c_1]$$

---

## 2. Generalization: 3D Tensor Range Sum Query

### 💡 8-Corner Inclusion-Exclusion Principle
In a 3D box bounded by $[x_1, x_2] \times [y_1, y_2] \times [z_1, z_2]$:
- Total sum uses 8 corner points with alternating signs:
  $$\text{Sum} = P(x_2, y_2, z_2) - [P(x_1, y_2, z_2) + P(x_2, y_1, z_2) + P(x_2, y_2, z_1)] + [P(x_1, y_1, z_2) + P(x_1, y_2, z_1) + P(x_2, y_1, z_1)] - P(x_1, y_1, z_1)$$
- Query time remains strictly $\mathcal{O}(1)$.

---

## 3. What if the 2D Matrix is MUTABLE (2D Fenwick Tree / 2D BIT)?

### 💡 2D Binary Indexed Tree
- Maintain a 2D BIT of size $(R+1) \times (C+1)$.
- Point update at $(r, c)$: Nested lowest-set-bit updates.
  - **Update Time**: $\mathcal{O}(\log R \times \log C)$
- Submatrix query: 4 prefix queries in 2D BIT.
  - **Query Time**: $\mathcal{O}(\log R \times \log C)$
  - **Space**: $\mathcal{O}(R \times C)$ flat array.

---

## 4. 2D Submatrix Range Updates: 2D Difference Array

### 💡 $\mathcal{O}(1)$ Range Update on Submatrix $[r_1, c_1] \dots [r_2, c_2]$
To add $V$ to all cells in a submatrix:
1. `diff[r1][c1] += V`
2. `diff[r1][c2 + 1] -= V`
3. `diff[r2 + 1][c1] -= V`
4. `diff[r2 + 1][c2 + 1] += V`
- Compute standard 2D prefix sums over `diff` at the end to reconstruct the final matrix in $\mathcal{O}(R \times C)$ time.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Mutability | Query Technique | Query Time | Update Time |
| :--- | :--- | :--- | :--- | :--- |
| **2D Immutable** | Immutable | 2D Prefix Sum (4 terms) | $\mathcal{O}(1)$ | N/A |
| **2D Point Mutable** | Mutable | 2D Fenwick Tree (BIT) | $\mathcal{O}(\log R \log C)$ | $\mathcal{O}(\log R \log C)$ |
| **2D Submatrix Update**| Batch updates | 2D Difference Matrix | $\mathcal{O}(R \times C)$ offline | $\mathcal{O}(1)$ |
| **3D Spatial Tensor** | Immutable | 3D Prefix Sum (8 terms) | $\mathcal{O}(1)$ | N/A |
