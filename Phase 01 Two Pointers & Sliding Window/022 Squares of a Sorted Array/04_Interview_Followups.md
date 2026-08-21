# 04 Interview Follow-ups & System Variations: Squares of a Sorted Array

The problem squares each element in a sorted integer array and returns the squares in sorted order. The optimal two-pointer approach starts from both ends (`left = 0`, `right = n - 1`) and populates the result array **from right to left** in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ output space.

In technical interviews, this problem tests parabola geometry, quadratic transformations ($ax^2 + bx + c$), outwards vs. inwards merging, and vectorization.

---

## 1. Why Populate Right-to-Left Instead of Inward-to-Outward?

### 💡 Two Approaches Compared
1. **Inwards from Ends (Right-to-Left Fill - Optimal)**:
   - The largest square is guaranteed to be at either `nums[left]^2` (extreme negative) or `nums[right]^2` (extreme positive).
   - Requires zero search to find the start; simply compare the ends and write backwards from index $N-1$ down to $0$.
2. **Outwards from Center (Left-to-Right Fill)**:
   - Find the partition point where numbers transition from negative to positive via Binary Search in $\mathcal{O}(\log N)$.
   - Move two pointers outwards towards the ends.
   - *Downside*: Extra code complexity and edge cases when all numbers are negative or all positive.

---

## 2. Generalization: Sort Transformed Array ($f(x) = ax^2 + bx + c$ / LeetCode #360)

### 🛑 The Scenario
Transform sorted array `nums` by a quadratic function $f(x) = ax^2 + bx + c$ and return the result in sorted order.

### 💡 Parabolic Convexity Analysis
The shape of a parabola depends strictly on the coefficient $a$:
1. **If $a > 0$ (U-shaped / Upward Parabola)**:
   - The maximum values lie at the **outer extremes** (far left or far right).
   - Use Two Pointers from ends moving inward, filling result **from right to left**.
2. **If $a < 0$ (Inverted U-shape / Downward Parabola)**:
   - The minimum values lie at the **outer extremes**.
   - Use Two Pointers from ends moving inward, filling result **from left to right**.
3. **If $a == 0$ (Linear Function $bx + c$)**:
   - If $b \ge 0$: already sorted in non-decreasing order.
   - If $b < 0$: sorted in reverse; simply reverse the transformed array.

---

## 3. What if $N = 10^9$ Elements on Disk?

### 💡 External Bidirectional Stream Reader
- Open two read cursors on disk (one at byte 0, one at the end of the file).
- Buffer blocks into RAM.
- Write output blocks sequentially backwards to a target file.
- Single sequential pass with $\mathcal{O}(1)$ working memory.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Function Form | Strategy | Direction Filled |
| :--- | :--- | :--- | :--- |
| **Squares of Array** | $f(x) = x^2$ | Two Pointers from ends | Right to Left (max to min) |
| **Quadratic ($a > 0$)** | $f(x) = ax^2+bx+c$ | Two Pointers from ends | Right to Left |
| **Quadratic ($a < 0$)** | $f(x) = ax^2+bx+c$ | Two Pointers from ends | Left to Right |
| **Linear ($a = 0, b < 0$)** | $f(x) = bx + c$ | Direct transform + Reverse | Linear scan |
