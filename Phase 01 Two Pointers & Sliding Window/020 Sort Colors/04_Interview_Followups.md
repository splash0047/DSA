# 04 Interview Follow-ups & System Variations: Sort Colors

The standard problem sorts an array containing only `0`s (red), `1`s (white), and `2`s (blue) in-place in a single pass. The optimal solution is the **Dutch National Flag Algorithm** (invented by Edsger W. Dijkstra) in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is used to test precise loop invariant proofs, $K$-color generalizations, and stable partitioning.

---

## 1. Loop Invariant Proof & The `mid` Increment Gotcha

### 💡 The 4 Region Invariants
Throughout the loop, the array is partitioned into 4 distinct regions:
1. `[0 ... low - 1]`: strictly `0`s.
2. `[low ... mid - 1]`: strictly `1`s.
3. `[mid ... high]`: **unexamined / unknown elements**.
4. `[high + 1 ... n - 1]`: strictly `2`s.

### 🛑 Why We Increment `mid` on 0-Swap, but NOT on 2-Swap
```cpp
if (nums[mid] == 0) {
    swap(nums[low++], nums[mid++]); // BOTH low and mid increment
} else if (nums[mid] == 2) {
    swap(nums[mid], nums[high--]);  // ONLY high decrements; mid stays!
}
```
- **When swapping with `low`**: The element coming from `low` is guaranteed to be a `1` (because `low` tracks the boundary of the `1`s region). A `1` is valid at `mid`, so we can safely advance `mid++`.
- **When swapping with `high`**: The element coming from `high` was in the unexamined region. It could be a `0`, `1`, or `2`. We must evaluate this new element in the next iteration without advancing `mid`.

---

## 2. What if There Are $K$ Distinct Colors ($K > 3$)?

### 💡 Two Optimal Approaches
1. **Counting Sort (2-Pass)**:
   - Count frequencies of each color in an array of size $K$.
   - Overwrite array sequentially.
   - **Time Complexity**: $\mathcal{O}(N + K)$, **Space Complexity**: $\mathcal{O}(K)$.
2. **Generalized $K$-Way Partition (QuickSort 3-Way Extension)**:
   - If counting sort is disallowed and elements are arbitrary objects, run recursive 3-way QuickSort (Dual-Pivot / Multi-way partition).

---

## 3. What if Relative Order of Equal Elements Must Be Preserved (Stable Partition)?

### 🛑 Inherent Limitation of In-Place Swapping
The standard Dutch National Flag algorithm is **unstable** (swapping with `high` scrambles relative order of `2`s).

### 💡 Stable Multi-Pointer Queue / Buffer
- To make it stable in $\mathcal{O}(N)$ time, allocate 3 small bucket arrays / queues for `0`s, `1`s, and `2`s, or use a stable in-place block-merge with $\mathcal{O}(N \log N)$ time and $\mathcal{O}(1)$ space.

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Stability | Algorithm | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **3 Colors (In-Place)** | Unstable | Dutch National Flag (3-Pointer) | $\mathcal{O}(N)$ (1 pass) | $\mathcal{O}(1)$ |
| **$K$ Colors** | Stable | Counting Sort | $\mathcal{O}(N + K)$ (2 passes) | $\mathcal{O}(K)$ |
| **Stable 3 Colors** | Stable | 3-Queue / Multi-buffer | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
