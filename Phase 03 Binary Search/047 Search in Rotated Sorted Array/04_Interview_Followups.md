# 04 Interview Follow-ups & System Variations: Search in Rotated Sorted Array

The problem searches for `target` in an array of distinct integers rotated at an unknown pivot. The optimal approach identifies which half (`[left...mid]` or `[mid...right]`) is sorted and discards the other half in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is a classic test of partitioned search space invariants and edge cases in rotated topologies.

---

## 1. The Core Sorted-Half Decision Tree

### 💡 The Fundamental Invariant
In any rotated sorted array with distinct elements, splitting at `mid` **always results in at least one half being strictly sorted**:
1. **If `nums[left] <= nums[mid]` (Left Half is Sorted)**:
   - If `nums[left] <= target && target < nums[mid]`: target is in the left half $\implies$ `right = mid - 1`.
   - Else: target must be in the right half $\implies$ `left = mid + 1`.
2. **Else (`nums[mid] < nums[right]`, Right Half is Sorted)**:
   - If `nums[mid] < target && target <= nums[right]`: target is in the right half $\implies$ `left = mid + 1`.
   - Else: target must be in the left half $\implies$ `right = mid - 1`.

---

## 2. 2-Pass Approach vs. 1-Pass Approach

### 💡 Comparison
1. **2-Pass Approach**:
   - Pass 1: Find the pivot index (minimum element) using binary search in $\mathcal{O}(\log N)$.
   - Pass 2: Binary search either the left segment `[0 ... pivot-1]` or right segment `[pivot ... N-1]`.
2. **1-Pass Approach (Optimal)**:
   - Determine the sorted half on the fly in a single while-loop.
   - Requires fewer lines of code and fewer comparison operations.

---

## 3. What if Array is Rotated by $0$ (Not Rotated at All)?

### 💡 Natural Compatibility
- If array is not rotated, `nums[left] <= nums[mid]` is always true for the left half.
- The algorithm seamlessly degenerates into standard classic binary search without needing special-case checks.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Passes | Time | Space | Edge Cases |
| :--- | :--- | :--- | :--- | :--- |
| **1-Pass Sorted Half** | 1 | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ | Clean single loop |
| **2-Pass (Find Min First)**| 2 | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ | Extra boundary conditionals |
