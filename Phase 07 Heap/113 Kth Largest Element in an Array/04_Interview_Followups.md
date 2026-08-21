# 04 Interview Follow-ups & System Variations: Kth Largest Element in an Array

The problem finds the $k$-th largest element in an unsorted array. Optimal approaches include **QuickSelect** ($\mathcal{O}(N)$ average time, $\mathcal{O}(1)$ space) and a **Min-Heap of size $K$** ($\mathcal{O}(N \log K)$ time, $\mathcal{O}(K)$ space).

In top-tier technical interviews, this is the benchmark for selection algorithms. Interviewers probe QuickSelect worst-case guarantees (Median-of-Medians), memory stream bottlenecks, and distributed top-$K$ map-reduce.

---

## 1. QuickSelect vs. Min-Heap of Size $K$

| Metric | QuickSelect (Hoare's Selection) | Min-Heap of Size $K$ |
| :--- | :--- | :--- |
| **Average Time** | **$\mathcal{O}(N)$ (Linear)** | $\mathcal{O}(N \log K)$ |
| **Worst-Case Time** | $\mathcal{O}(N^2)$ (Avoidable via random pivot)| **$\mathcal{O}(N \log K)$ (Guaranteed)** |
| **Space Complexity**| $\mathcal{O}(1)$ auxiliary | $\mathcal{O}(K)$ memory |
| **Streaming Suitability**| Fails (requires random array access) | **Optimal for infinite stream** |

---

## 2. Guaranteed $\mathcal{O}(N)$ Worst-Case: Median-of-Medians (BFPRT Algorithm)

### 💡 Deterministic Good Pivot Selection
- Group elements into blocks of 5.
- Find the median of each 5-element block.
- Recursively find the median of the $\lceil N/5 ceil$ medians ($M$).
- Use $M$ as the partition pivot.
- **Recurrence**:
  $$T(N) \le T(N/5) + T(7N/10) + \mathcal{O}(N) \implies T(N) = \mathcal{O}(N) 	ext{ strictly}$$

---

## 3. What if $N = 10^9$ Elements on Distributed Cluster (MapReduce)?

### 💡 MapReduce Top-$K$ Pipeline
1. **Mapper Phase**: Each of the $M$ worker nodes processes its local partition using an in-memory Min-Heap of size $K$ and outputs its local top-$K$ candidates.
2. **Reducer Phase**: The single reducer receives $M 	imes K$ total candidate elements and merges them in a final Min-Heap of size $K$.
- **Network Traffic**: Transmits only $M 	imes K$ scalars instead of shuffling $10^9$ raw numbers!

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Recommended Approach | Time | Space |
| :--- | :--- | :--- | :--- |
| **Static In-Memory** | Randomized QuickSelect | $\mathcal{O}(N)$ avg | $\mathcal{O}(1)$ |
| **Live Stream** | Min-Heap of size $K$ | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| **Distributed Cluster**| Local Min-Heap $	o$ Global Reducer Merge | $\mathcal{O}(rac{N}{M} \log K)$ | $\mathcal{O}(K)$ / node |
