# 04 Interview Follow-ups & System Variations: Largest Rectangle in Histogram

The problem finds the area of the largest rectangle in a histogram (Hard). The optimal solution uses a **Monotonic Increasing Stack** in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

In top-tier technical interviews, this is considered a premier algorithmic challenge. Interviewers probe boundary sentinels, width calculation derivations, and Divide & Conquer Segment Tree alternatives.

---

## 1. Derivation of Width: Why `i - stack.top() - 1`?

### 💡 The Geometric Invariant
- When a bar at `stack.top()` is popped because `heights[i] < heights[popped]`:
  - `heights[i]` is the **Right Smaller Boundary** (first bar to the right shorter than `heights[popped]`).
  - The new `stack.top()` (after popping) is the **Left Smaller Boundary** (first bar to the left shorter than `heights[popped]`).
- The rectangle bounded by `heights[popped]` extends between `left_boundary` and `right_boundary`:
  $$	ext{Width} = (	ext{right} - 1) - (	ext{left}) = i - 	ext{stack.top()} - 1$$
- If stack is empty after popping: The popped bar is the smallest bar seen so far $\implies 	ext{Width} = i$.

---

## 2. Clean Sentinel Flush Optimization

### 💡 Adding a Trailing `0` Height
- By appending a sentinel height `0` to the histogram, all remaining bars in the stack are automatically popped and evaluated without needing post-loop cleanup code.

---

## 3. Alternative: Divide & Conquer with Segment Tree (RMQ)

### 💡 Range Minimum Query Approach
- The largest rectangle in range $[L, R]$ is:
  $$\max\Big(	ext{height}[min\_idx] 	imes (R - L + 1),\; 	ext{Solve}(L, min\_idx - 1),\; 	ext{Solve}(min\_idx + 1, R)\Big)$$
- Precomputing Range Minimum Query via Segment Tree: $\mathcal{O}(N \log N)$ average time, $\mathcal{O}(N^2)$ worst case on skewed histograms.
- Monotonic stack is strictly superior ($\mathcal{O}(N)$ worst case).

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Worst-Case Time | Space | Complexity |
| :--- | :--- | :--- | :--- |
| **Monotonic Stack (Optimal)**| $\mathcal{O}(N)$ strictly | $\mathcal{O}(N)$ | 1 linear pass |
| **Segment Tree RMQ** | $\mathcal{O}(N^2)$ worst / $\mathcal{O}(N \log N)$ avg | $\mathcal{O}(N)$ | Tree construction |
