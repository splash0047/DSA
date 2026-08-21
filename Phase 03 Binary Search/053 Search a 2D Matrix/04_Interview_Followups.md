# 04 Interview Follow-ups & System Variations: Search a 2D Matrix

The problem searches for `target` in an $M 	imes N$ matrix where each row is sorted and the first integer of each row is greater than the last integer of the previous row. Treating the 2D matrix as a virtual flattened 1D sorted array of size $M 	imes N$ runs in $\mathcal{O}(\log(M 	imes N))$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem tests virtual coordinate projection, preventing 32-bit index overflow, and cache layout analysis.

---

## 1. Virtual 1D-to-2D Coordinate Mapping

### 💡 The Mapping Formulas
- Total virtual elements: $T = M 	imes N$.
- Range: `left = 0`, `right = M * N - 1`.
- For any 1D index `mid`:
  $$	ext{row} = \lfloor 	ext{mid} / N floor, \quad 	ext{col} = 	ext{mid} \pmod N$$
- Access element: `matrix[row][col]`.

---

## 2. Integer Overflow Hazard on Virtual 1D Bounds

### 🛑 The Hazard
If $M = 50,000$ and $N = 50,000$, $M 	imes N = 2.5 	imes 10^9 > 2^{31} - 1$.
- `right = M * N - 1` overflows 32-bit signed `int`.
- **Solution**: Use `long long` for virtual pointers:
  ```cpp
  long long left = 0, right = (long long)m * n - 1;
  ```
- Or perform two 1D binary searches: First binary search to find the candidate row ($\mathcal{O}(\log M)$), second binary search inside that row ($\mathcal{O}(\log N)$).

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Pointers | Time | Space | Overflow Risk |
| :--- | :--- | :--- | :--- | :--- |
| **Virtual 1D Flatten** | `long long` 1D | $\mathcal{O}(\log(MN))$ | $\mathcal{O}(1)$ | Handled via 64-bit |
| **2-Step Binary Search** | Row BS $	o$ Col BS | $\mathcal{O}(\log M + \log N)$ | $\mathcal{O}(1)$ | Zero overflow risk |
