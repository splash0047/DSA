# 04 Interview Follow-ups & System Variations: Merge k Sorted Lists

The problem merges $K$ sorted linked lists of total $N$ nodes. Optimal solutions include Min-Heap ($\mathcal{O}(N \log K)$ time, $\mathcal{O}(K)$ space) and Divide & Conquer Tournament Merge ($\mathcal{O}(N \log K)$ time, $\mathcal{O}(1)$ space).

In technical interviews, this is the prime template for external distributed merges, multi-way streaming, and priority queue tuning.

---

## 1. Min-Heap vs. Divide & Conquer Tournament Merge

| Metric | Min-Heap Priority Queue | Divide & Conquer (Pairwise) |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N \log K)$ | $\mathcal{O}(N \log K)$ |
| **Space Complexity** | $\mathcal{O}(K)$ Heap memory | $\mathcal{O}(1)$ iterative / $\mathcal{O}(\log K)$ stack |
| **Streaming Feasibility**| **Optimal for live streams** | Requires all lists upfront |
| **Hardware Cache** | Pointer heap hopping | Sequential linked list traversal |

---

## 2. Distributed Scale: Merging $K = 1,000$ Files from Disk / Cloud Storage

### 💡 External $K$-Way Merge Engine
- In database external sort (e.g., PostgreSQL / Apache Spark):
  - Open 1 stream buffer per file in RAM.
  - Maintain an in-memory Min-Heap of size $K$.
  - Pop smallest record, stream to output file, fetch next record from the corresponding stream buffer.
  - When a buffer empties, read the next 64KB block from disk.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Space Model | Best Used When |
| :--- | :--- | :--- |
| **Min-Heap (size $K$)** | $\mathcal{O}(K)$ | Dynamic real-time streams |
| **Divide & Conquer** | $\mathcal{O}(1)$ auxiliary | In-memory linked lists |
| **External $K$-Way Merge**| $\mathcal{O}(K 	imes 	ext{Buffer})$ | Multi-gigabyte disk files |
