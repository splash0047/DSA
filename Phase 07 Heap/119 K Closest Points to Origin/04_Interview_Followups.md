# 04 Interview Follow-ups & System Variations: K Closest Points to Origin

The problem finds the $k$ closest points to the origin $(0, 0)$ on a 2D plane. Optimal approaches include **Max-Heap of size $K$** ($\mathcal{O}(N \log K)$ time, $\mathcal{O}(K)$ space) and **QuickSelect** ($\mathcal{O}(N)$ average time, $\mathcal{O}(1)$ space).

In technical interviews, this problem tests Euclidean distance optimizations without square roots, and KD-Trees for 2D spatial indexing.

---

## 1. Low-Level Optimization: Avoiding `sqrt()` Calls

### 💡 Monotonic Distance Equivalence
- Distance $D = \sqrt{x^2 + y^2}$.
- Because the square root function is strictly monotonically increasing for non-negative numbers:
  $$D_1 < D_2 \iff x_1^2 + y_1^2 < x_2^2 + y_2^2$$
- Computing raw integer Euclidean norm $x^2 + y^2$ eliminates expensive floating-point `sqrt()` CPU instructions.

---

## 2. Generalization: Spatial Indexing with KD-Tree

### 💡 Dynamic $K$-Nearest Neighbors (KNN)
- If points are fixed and millions of `findKClosest(point)` queries arrive dynamically:
  - Construct a 2D **KD-Tree** (alternating X and Y axis splits) in $\mathcal{O}(N \log N)$ preprocessing.
  - Each KNN query runs in $\mathcal{O}(\log N)$ average time.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Best Scenario | Time | Space |
| :--- | :--- | :--- | :--- |
| **QuickSelect** | 1-time static query | $\mathcal{O}(N)$ avg | $\mathcal{O}(1)$ |
| **Max-Heap of size $K$** | Streaming points | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| **KD-Tree** | Repeated dynamic queries | $\mathcal{O}(\log N)$ / query | $\mathcal{O}(N)$ tree |
