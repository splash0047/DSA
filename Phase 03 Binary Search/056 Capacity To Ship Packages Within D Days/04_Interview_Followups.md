# 04 Interview Follow-ups & System Variations: Capacity To Ship Packages Within D Days

The problem finds the least ship capacity to transport all packages within $D$ days in contiguous conveyor order. Using Binary Search on the Answer in range $[\max(	ext{weights}), \sum 	ext{weights}]$, the optimal approach runs in $\mathcal{O}(N \log(\sum W))$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is structurally identical to Book Allocation Problem and Split Array Largest Sum.

---

## 1. Search Space Boundary Invariants

### 💡 Why `left = max(weights)` and `right = sum(weights)`
1. **Lower Bound (`left = max(weights)`)**: The ship MUST be capable of carrying the single heaviest package. Any capacity $< \max(W)$ can never ship that package.
2. **Upper Bound (`right = sum(weights)`)**: A ship with capacity $\sum W$ can ship all packages in exactly 1 day.

---

## 2. Equivalence Trinity in Computer Science Interviews

These 3 classic problems share the **exact same code and mathematical reduction**:
1. **Capacity to Ship Packages Within D Days (LeetCode #1011)**
2. **Split Array Largest Sum (LeetCode #410)**
3. **Book Allocation Problem / Painter's Partition Problem**

---

## Summary Matrix: Trade-offs at a Glance

| Parameter | Value |
| :--- | :--- |
| **Search Range** | $[\max(weights), \sum weights]$ |
| **Check Monotonicity** | Larger capacity $\implies$ fewer or equal days needed |
| **Time Complexity** | $\mathcal{O}(N \log(\sum W))$ |
| **Space Complexity** | $\mathcal{O}(1)$ |
