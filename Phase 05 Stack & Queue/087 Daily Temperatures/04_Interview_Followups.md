# 04 Interview Follow-ups & System Variations: Daily Temperatures

The problem finds the number of days you have to wait after the $i$-th day to get a warmer temperature. The optimal approach uses a **Monotonic Decreasing Stack** in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

In technical interviews, this problem is the foundational entry point to Monotonic Stack patterns, eliminating dynamic stack memory allocations, and streaming temperatures.

---

## 1. High-Performance Optimization: Array-Backed Stack

### 🛑 `std::stack` Deque Overhead
In C++, `std::stack<int>` wraps `std::deque`, causing block allocations.

### 💡 Flat Array Stack
```cpp
vector<int> dailyTemperatures(vector<int>& temperatures) {
    int n = temperatures.size();
    vector<int> ans(n, 0);
    vector<int> stk(n);
    int top = -1;
    
    for (int i = 0; i < n; i++) {
        while (top >= 0 && temperatures[i] > temperatures[stk[top]]) {
            int prev_idx = stk[top--];
            ans[prev_idx] = i - prev_idx;
        }
        stk[++top] = i;
    }
    return ans;
}
```
- **Performance**: Runs in pure contiguous memory with 0 heap fragmentations.

---

## 2. 1-Billion Temperature Readings Stream on Disk

### 💡 Chunked Monotonic Spill Stack
- As temperature records stream from disk, maintain the monotonic stack in RAM.
- Stack entries only persist until their warmer day arrives; in typical weather patterns, stack size stays small ($< 100$ entries).

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Data Structure | Time Complexity | Cache Locality |
| :--- | :--- | :--- | :--- |
| **Standard Stack** | `std::stack<int>` | $\mathcal{O}(N)$ | Moderate |
| **Flat Array Stack**| `vector<int>` with `top` index | $\mathcal{O}(N)$ | **Optimal (L1 Cache)** |
