# 04 Interview Follow-ups & System Variations: Sliding Window Maximum

The problem finds the maximum element in each sliding window of size $k$ (Hard). The optimal solution uses a **Monotonic Decreasing Deque** in $\mathcal{O}(N)$ time and $\mathcal{O}(k)$ space.

In technical interviews, this problem is compared with Block Decomposition (Two-Pass Prefix/Suffix Max with $\mathcal{O}(1)$ space) and Sliding Window Median (Two Heaps).

---

## 1. Monotonic Deque Invariant ($\mathcal{O}(N)$ Strict)

### 💡 Deque Maintenance Rules
1. **Evict Out-of-Window Elements**: If `deque.front() <= i - k`, pop front.
2. **Maintain Monotonic Decreasing Order**: While `!deque.empty() && nums[deque.back()] <= nums[i]`, pop back.
3. Push current index `i` to back.
4. If $i \ge k - 1$, record maximum `nums[deque.front()]`.
- **Amortized Proof**: Each index is pushed and popped at most once $\implies \mathcal{O}(N)$ total operations.

---

## 2. Block Decomposition: Prefix/Suffix Max ($\mathcal{O}(1)$ Auxiliary Space)

### 💡 Two-Pass Array Method
1. Divide array into blocks of size $k$.
2. Precompute `left_max[i]` (max from start of block to $i$) and `right_max[i]` (max from end of block to $i$).
3. Sliding window max for range $[i, i + k - 1]$ is simply:
   $$\max\Big(	ext{right\_max}[i],\; 	ext{left\_max}[i + k - 1]\Big)$$
- **Query Time**: strictly $\mathcal{O}(1)$ with zero deques!

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Data Structure | Time | Space |
| :--- | :--- | :--- | :--- |
| **Monotonic Deque (Optimal)**| `std::deque<int>` | $\mathcal{O}(N)$ | $\mathcal{O}(k)$ |
| **Block Prefix/Suffix Max** | Flat arrays | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ or $\mathcal{O}(1)$ in-place |
| **Max-Heap (Priority Queue)**| `priority_queue<pair<int, int>>` | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ |
