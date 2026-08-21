# 04 Interview Follow-ups & System Variations: Range Sum Query - Immutable

The problem processes multiple range sum queries on an immutable array. By precomputing a Prefix Sum array of size $N + 1$, preprocessing takes $\mathcal{O}(N)$ time and each `sumRange(left, right)` query runs in $\mathcal{O}(1)$ time with $\mathcal{O}(N)$ space.

In technical interviews, this problem is the launchpad for questions on **Mutable Arrays**, Fenwick Trees (Binary Indexed Trees), Segment Trees, and Difference Arrays.

---

## 1. What if the Array is MUTABLE (Point Updates Allowed / LeetCode #307)?

### 🛑 Why Prefix Sum Fails on Mutable Arrays
Updating a single element at `nums[i]` requires rebuilding the prefix sum array from index $i$ to $N$, costing $\mathcal{O}(N)$ time per update.

### 💡 Two Optimal Dynamic Data Structures
1. **Binary Indexed Tree / Fenwick Tree (BIT)**:
   - Uses lowest set bit extraction `(i & -i)` to balance range queries and point updates.
   - **Update Time**: $\mathcal{O}(\log N)$
   - **Query Time**: $\mathcal{O}(\log N)$
   - **Space**: $\mathcal{O}(N)$ (compact flat array, 0 pointers).
2. **Segment Tree**:
   - Binary tree where each node represents a range $[L, R]$.
   - **Update Time**: $\mathcal{O}(\log N)$
   - **Query Time**: $\mathcal{O}(\log N)$
   - **Space**: $\mathcal{O}(4N)$ array.

---

## 2. What if We Have Massive RANGE UPDATES + Few Offline Point Queries?

### 💡 The Difference Array Pattern
- To add a constant value $V$ to all elements in range $[L, R]$:
  - `diff[L] += V`
  - `diff[R + 1] -= V`
  - **Update Time**: strictly $\mathcal{O}(1)$ per range update!
- **Reconstruction**: Run a single prefix sum pass on `diff` to recover the final array values in $\mathcal{O}(N)$ time.

---

## 3. What if BOTH Range Updates AND Range Queries Are Required?

### 💡 Segment Tree with Lazy Propagation
- When updating a range $[L, R]$, mark tree nodes with a `lazy` tag without recursing down to leaf nodes immediately.
- Push lazy values down to children only when a query explicitly traverses that node.
- **Range Update Time**: $\mathcal{O}(\log N)$
- **Range Query Time**: $\mathcal{O}(\log N)$

---

## Summary Matrix: Trade-offs at a Glance

| Use Case | Updates | Queries | Optimal Data Structure |
| :--- | :--- | :--- | :--- |
| **Immutable Array** | None ($\mathcal{O}(0)$) | Range Sum $\mathcal{O}(1)$ | Prefix Sum Array |
| **Point Updates + Range Queries** | Point $\mathcal{O}(\log N)$ | Range Sum $\mathcal{O}(\log N)$ | Fenwick Tree (BIT) / Segment Tree |
| **Range Updates + Offline Queries**| Range $\mathcal{O}(1)$ | Offline $\mathcal{O}(N)$ | Difference Array |
| **Range Updates + Online Range Queries**| Range $\mathcal{O}(\log N)$ | Range $\mathcal{O}(\log N)$ | Segment Tree + Lazy Propagation |
