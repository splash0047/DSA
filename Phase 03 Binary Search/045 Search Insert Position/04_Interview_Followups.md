# 04 Interview Follow-ups & System Variations: Search Insert Position

The problem finds the index of `target` in a sorted array, or the index where it would be if inserted in order. The optimal binary search maintains `left <= right` and returns `left` in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is equivalent to implementing `std::lower_bound` in C++ or `bisect_left` in Python. Interviewers probe boundary invariants, dynamic insertion cost trade-offs, and multi-set duplicates.

---

## 1. Why Returning `left` is Guaranteed to Be the Exact Insertion Point

### 💡 Loop Termination Invariant
- The search space invariant is `[left, right]`.
- When the while loop `while (left <= right)` terminates:
  - `right = left - 1`.
  - All elements at indices $< left$ are strictly $< 	ext{target}$.
  - All elements at indices $\ge left$ are strictly $\ge 	ext{target}$.
- Therefore, `left` is always the first index whose value is $\ge 	ext{target}$ (the exact insertion position).

---

## 2. Lower Bound vs. Upper Bound (Bisect Left vs. Bisect Right)

| Function | Condition | Description |
| :--- | :--- | :--- |
| **`lower_bound` (`bisect_left`)** | `nums[mid] >= target` $	o$ `right = mid - 1` | First element $\ge 	ext{target}$ |
| **`upper_bound` (`bisect_right`)** | `nums[mid] > target` $	o$ `right = mid - 1` | First element strictly $> 	ext{target}$ |

- If target contains duplicates (`[1, 2, 2, 2, 3]`, target = 2):
  - `lower_bound` returns index 1 (start of duplicates).
  - `upper_bound` returns index 4 (one past end of duplicates).

---

## 3. Dynamic Array Insertion Bottlenecks: $\mathcal{O}(\log N)$ Search vs. $\mathcal{O}(N)$ Shift

### 🛑 The Memory Bottleneck
While binary search finds the insertion index in $\mathcal{O}(\log N)$, physically inserting an element into a dynamic array (like `std::vector` or Python `list`) requires shifting all subsequent elements to the right ($\mathcal{O}(N)$ memory move).

### 💡 Scalable Alternatives for Frequent Insertions
1. **Balanced Binary Search Tree (AVL / Red-Black Tree)**:
   - Search: $\mathcal{O}(\log N)$, Insert: $\mathcal{O}(\log N)$.
2. **B+ Tree / Skip List**:
   - Cache-friendly block insertions in $\mathcal{O}(\log N)$.

---

## Summary Matrix: Trade-offs at a Glance

| Goal | Operation | Time | Space |
| :--- | :--- | :--- | :--- |
| **Find Insertion Index** | Binary Search (`lower_bound`) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| **Physical Array Insert** | Binary Search + Memory Shift | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Dynamic Insert + Search** | Red-Black Tree / B-Tree | $\mathcal{O}(\log N)$ | $\mathcal{O}(N)$ |
