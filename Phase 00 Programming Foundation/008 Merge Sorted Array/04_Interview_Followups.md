# 04 Interview Follow-ups & System Variations: Merge Sorted Array

The classic problem merges `nums2` of size $N$ into `nums1` of size $M + N$ in-place. The optimal approach uses three pointers moving **backwards from the end** (`p1 = m - 1`, `p2 = n - 1`, `p = m + n - 1`) in $\mathcal{O}(M + N)$ time and $\mathcal{O}(1)$ space.

In top-tier interviews, this problem scales into $K$-way merging, in-place merging without extra buffer (The Gap Method), asymmetric array merges ($M \gg N$), and parallel multi-core merging.

---

## 1. Why is Backwards Merging Guaranteed Never to Overwrite Unread Elements in `nums1`?

### 💡 Invariant Proof
- At any step, the total number of empty slots at the end of `nums1` is $N$.
- The write pointer `p` starts at $M + N - 1$.
- The number of elements written so far is $(M + N - 1) - p$.
- For `p` to overwrite `p1`, we would need:
  $$p \le p1$$
  $$(M + N - 1) - \text{items\_written} \le p1$$
- But since at most $N$ items could have been pulled from `nums2`, the write pointer `p` is always strictly ahead of or aligned with `p1`. Overwrite of unread data is mathematically impossible.

---

## 2. What if `nums1` Has NO Extra Buffer ($\mathcal{O}(1)$ In-Place Merge without Extra Space)?

### 🛑 The Challenge
Merge `nums1` (size $M$) and `nums2` (size $N$) such that `nums1` contains the first $M$ smallest elements and `nums2` contains the remaining $N$ elements, strictly in-place.

### 💡 The Gap Method (Derived from Shell Sort)
1. Initialize gap: $\text{gap} = \lceil (M + N) / 2 \rceil$.
2. Compare and swap elements separated by `gap` distance across both arrays:
   - Case 1: Both pointers in `nums1`.
   - Case 2: Left pointer in `nums1`, right pointer in `nums2`.
   - Case 3: Both pointers in `nums2`.
3. Reduce gap: $\text{gap} = \lceil \text{gap} / 2 \rceil$ until $\text{gap} = 0$.
- **Time Complexity**: $\mathcal{O}((M + N) \log(M + N))$, **Space Complexity**: strictly $\mathcal{O}(1)$.

---

## 3. What if $M \gg N$ (e.g., $M = 10^9$ and $N = 10$)?

### 🛑 The Inefficiency
Sequential $\mathcal{O}(M + N)$ scanning will iterate over all 1 billion elements of `nums1` just to insert 10 elements.

### 💡 Binary Search Insertion Points + Block Memory Moves
- For each element in `nums2`, find its exact insertion position in `nums1` using `std::upper_bound` (Binary Search) in $\mathcal{O}(\log M)$ time.
- Move entire blocks of memory using `memmove()` / DMA transfers rather than element-by-element comparisons.
- **Time Complexity**: $\mathcal{O}(N \log M + M)$ memory bandwidth.

---

## 4. How to Merge $K$ Sorted Streams / Arrays of Total Size $N$ (LeetCode #23)?

### 💡 Two Optimal Strategies
1. **Min-Heap / Priority Queue of Size $K$**:
   - Push the head element of each of the $K$ arrays into a Min-Heap.
   - Pop the minimum element, write to output, and push the next element from that same array.
   - **Time Complexity**: $\mathcal{O}(N \log K)$, **Space Complexity**: $\mathcal{O}(K)$ heap memory.
2. **Divide & Conquer (Tournament Merge)**:
   - Pairwise merge arrays: Array 0 with Array 1, Array 2 with Array 3...
   - Reduces $K \to K/2 \to K/4 \dots \to 1$ in $\log K$ merge levels.
   - **Time Complexity**: $\mathcal{O}(N \log K)$, **Space Complexity**: $\mathcal{O}(1)$ auxiliary if using linked lists.

---

## 5. How to Merge Two Massive Sorted Arrays in Parallel Across $P$ CPU Cores?

### 💡 Independent Sub-range Partitioning (Finding Median / $K$-th Element)
1. Split the output into $P$ equal segments of size $(M + N)/P$.
2. For each thread $i \in [0, P-1]$, calculate the target partition rank $R_i = i \times \frac{M + N}{P}$.
3. Find the cut-points $(C_{1, i}, C_{2, i})$ in `nums1` and `nums2` such that $C_{1, i} + C_{2, i} = R_i$ using **Binary Search for $K$-th element** in $\mathcal{O}(\log(\min(M, N)))$ time.
4. Each thread independently merges its own assigned slices without locks or communication.
- **Time Complexity**: $\mathcal{O}\left(\frac{M + N}{P} + \log(\min(M, N))\right)$.

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Constraint / Setup | Optimal Strategy | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Standard with Buffer** | `nums1` has $M+N$ capacity | 3 Pointers from End | $\mathcal{O}(M+N)$ | $\mathcal{O}(1)$ |
| **No Extra Buffer** | Strictly in-place | Gap Method (Shell Sort) | $\mathcal{O}((M+N)\log(M+N))$ | $\mathcal{O}(1)$ |
| **Asymmetric ($M \gg N$)** | $M$ massive, $N$ small | Binary Search + Block Move | $\mathcal{O}(N \log M)$ | $\mathcal{O}(1)$ |
| **$K$ Sorted Streams** | $K$ streams of total $N$ | Min-Heap of size $K$ | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| **$P$-Core Parallel Merge** | Multi-threaded | Binary Search Split + Slice Merge | $\mathcal{O}(\frac{M+N}{P})$ | $\mathcal{O}(P)$ |
