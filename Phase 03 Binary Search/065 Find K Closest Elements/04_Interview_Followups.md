# 04 Interview Follow-ups & System Variations: Find K Closest Elements

The problem finds the $k$ closest integers to $x$ in a sorted array. While Two Pointers from ends runs in $\mathcal{O}(N - k)$, the optimal Binary Search for the **starting index of the window** runs in $\mathcal{O}(\log(N - k) + k)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem tests comparing window edges (`x - arr[mid]` vs `arr[mid + k] - x`) to eliminate sliding window loops.

---

## 1. Binary Search for Window Start Index ($\mathcal{O}(\log(N - k))$)

### 💡 The Edge Comparison Trick
- The target window of size $k$ must start at some index in range $[0, N - k]$.
- Binary search `mid \in [0, N - k]`:
  - Compare the distance of the element just outside the window on the right `arr[mid + k]` with the element at the left boundary `arr[mid]`:
    $$	ext{if } (x - 	ext{arr}[mid] > 	ext{arr}[mid + k] - x) \implies 	ext{left} = 	ext{mid} + 1$$
    $$	ext{else} \implies 	ext{right} = 	ext{mid}$$
- **Result**: `left` is the optimal start index of the $k$-element window.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Strategy | Time Complexity | Space |
| :--- | :--- | :--- | :--- |
| **Two Pointers from Ends** | Shrink $N 	o k$ by removing farthest | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **BS for Window Start (Optimal)**| Compare `arr[mid]` vs `arr[mid + k]` | $\mathcal{O}(\log(N - k) + k)$ | $\mathcal{O}(1)$ |
