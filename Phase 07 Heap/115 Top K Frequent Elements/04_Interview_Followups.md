# 04 Interview Follow-ups & System Variations: Top K Frequent Elements

The problem returns the $k$ most frequent elements. While a Min-Heap achieves $\mathcal{O}(N \log K)$, the optimal **Bucket Sort (Frequency Buckets)** runs in strictly $\mathcal{O}(N)$ linear time and $\mathcal{O}(N)$ space.

In technical interviews, this problem tests linear bucket sorting and distributed heavy hitters (Count-Min Sketch, Space-Saving algorithm).

---

## 1. Bucket Sort for Guaranteed $\mathcal{O}(N)$ Linear Time

### 💡 Frequency Array of Lists
1. Compute frequency map `unordered_map<int, int> count`.
2. Allocate bucket array of size $N + 1$: `vector<vector<int>> buckets(n + 1)`.
3. Place each unique number into `buckets[count[x]]`.
4. Scan `buckets` from right to left ($N$ down to $1$) and gather the first $K$ numbers.
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(N)$.

---

## 2. Distributed Scale: Heavy Hitters in Real-Time Web Traffic

### 🛑 The Problem
Finding the top 100 most trending URLs across 100 million requests/sec on Twitter/Cloudflare without storing every URL in memory.

### 💡 Count-Min Sketch + Space-Saving Algorithm
- Stream URLs into a 2D matrix of hash counters (**Count-Min Sketch**).
- Maintain a bounded Min-Heap / list of $K$ candidate heavy hitters.
- When an item's estimated frequency exceeds the minimum in the heap, promote it.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Time Complexity | Space Complexity | Best Used When |
| :--- | :--- | :--- | :--- |
| **Bucket Sort** | $\mathcal{O}(N)$ strictly | $\mathcal{O}(N)$ | Max frequency $\le N$ |
| **Min-Heap (size $K$)** | $\mathcal{O}(N \log K)$ | $\mathcal{O}(U)$ unique | $K \ll N$ |
| **Count-Min Sketch** | $\mathcal{O}(1)$ / event | $\mathcal{O}(K + rac{1}{\epsilon})$ | Unbounded terabyte streams |
