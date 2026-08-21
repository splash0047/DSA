# 04 Interview Follow-ups & System Variations: Find Peak Element

The problem finds a peak element (an element strictly greater than its neighbors) in an unsorted array. The optimal binary search follows the discrete upward gradient in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is a classic demonstration of binary search on unsorted arrays, 2D matrix peak finding, and hill-climbing optimization.

---

## 1. Why Binary Search Works on an UNSORTED Array

### 💡 The Gradient Ascent Invariant
- Even though the array is unsorted, compare `nums[mid]` with `nums[mid + 1]`:
  1. **If `nums[mid] < nums[mid + 1]`**:
     - The slope is rising to the right.
     - Because `nums[n] = -\infty`, the slope must eventually decline. Therefore, **at least one peak is guaranteed to exist in the right half `[mid + 1 ... right]`**.
  2. **If `nums[mid] > nums[mid + 1]`**:
     - The slope is declining to the right (or rising to the left).
     - A peak is guaranteed to exist in the left half `[left ... mid]`.
- Always moving towards the ascending slope guarantees converging to a local maximum in $\mathcal{O}(\log N)$.

---

## 2. Generalization: 2D Matrix Peak Finding (LeetCode #1901)

### 🛑 The Challenge
Find a peak in an $R 	imes C$ matrix where a peak is greater than its top, bottom, left, and right neighbors.

### 💡 Divide & Conquer on Matrix Columns
1. Select middle column `mid_col = C / 2`.
2. Find the global maximum element in this column at row $r_{\max}$ in $\mathcal{O}(R)$ time.
3. Compare `matrix[r_max][mid_col]` with its horizontal neighbors `mid_col - 1` and `mid_col + 1`:
   - If greater than both: found a 2D peak!
   - If `matrix[r_max][mid_col + 1] > matrix[r_max][mid_col]`: recurse on right sub-matrix.
   - Else: recurse on left sub-matrix.
- **Time Complexity**: $\mathcal{O}(R \log C)$, **Space Complexity**: $\mathcal{O}(1)$.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Dimension | Optimal Strategy | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **1D Array Peak** | 1D | Gradient Binary Search | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| **2D Matrix Peak (#1901)** | 2D ($R 	imes C$) | Column Max + Binary Search | $\mathcal{O}(R \log C)$ | $\mathcal{O}(1)$ |
