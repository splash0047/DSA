# 04 Interview Follow-ups & System Variations: Find Median from Data Stream

The problem designs a data structure supporting `addNum(num)` and `findMedian()` in real time. The optimal **Dual-Heap Algorithm** (Max-Heap for lower half, Min-Heap for upper half) achieves $\mathcal{O}(\log N)$ insertion and $\mathcal{O}(1)$ median queries with $\mathcal{O}(N)$ space.

In top-tier technical interviews, this is the absolute classic streaming challenge. Interviewers probe sliding window medians, P99 percentile latency monitors, and T-Digest quantile sketches.

---

## 1. The Dual-Heap Invariant & Balance Rules

### 💡 The Structural Invariants
1. **Order Invariant**: Every element in `max_heap` (lower half) $\le$ every element in `min_heap` (upper half):
   $$\max(	ext{lower}) \le \min(	ext{upper})$$
2. **Size Invariant**: Either `max_heap.size() == min_heap.size()` OR `max_heap.size() == min_heap.size() + 1`.

### 💡 Insertion Workflow (`addNum`)
```cpp
void addNum(int num) {
    max_heap.push(num);
    min_heap.push(max_heap.top());
    max_heap.pop();
    
    if (max_heap.size() < min_heap.size()) {
        max_heap.push(min_heap.top());
        min_heap.pop();
    }
}

double findMedian() {
    if (max_heap.size() > min_heap.size()) return max_heap.top();
    return (max_heap.top() + min_heap.top()) / 2.0;
}
```

---

## 2. Follow-up: Monitoring P99 Latency (99th Percentile Stream)

### 💡 Asymmetric Dual-Heap
- To support finding the **99th Percentile**:
  - `max_heap` holds $99\%$ of all data points.
  - `min_heap` holds top $1\%$ of all data points.
  - Balance condition: $	ext{min\_heap.size()} = \lceil 0.01 	imes N ceil$.

---

## 3. Approximate Streaming Quantiles: T-Digest / GK-Sketch

### 🛑 Memory Bound on 1 Billion Requests
Storing 1 billion floats across heaps requires 8GB RAM.
- **T-Digest**: Compresses stream into dynamic cluster centroids. Computes P50, P90, P99 within 0.1% relative error using only **a few kilobytes of RAM**.

---

## Summary Matrix: Trade-offs at a Glance

| Percentile Metric | Data Structure | `addNum` Time | Query Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Exact Median (P50)**| 50:50 Dual Heap | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ |
| **Exact P99 Latency** | 99:1 Dual Heap | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ |
| **Approx Percentile** | T-Digest / GK-Quantiles | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ bounded |
