# 04 Interview Follow-ups & System Variations: Maximum Average Subarray I

The problem finds a contiguous subarray of fixed length $k$ that has the maximum average value. The optimal fixed-size sliding window approach computes the sum of the first $k$ elements, then slides the window by adding `nums[i]` and subtracting `nums[i - k]` in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem serves as the foundation for variable-length averages ($\ge k$), streaming numerical precision, and Welford's online statistics.

---

## 1. Floating-Point Precision: Sum First, Divide at the End

### 🛑 Precision Loss Pitfall
- If you maintain a running `double avg` and update `avg += (nums[i] - nums[i-k]) / (double)k` on every step, floating-point rounding errors accumulate over millions of steps.
- **Best Practice**: Accumulate pure integers using `long long max_sum` and perform exactly **one** floating-point division at the very end:
  $$\text{result} = \frac{\text{max\_sum}}{(double)k}$$

---

## 2. Generalization: Subarray Length $\ge k$ (Maximum Average Subarray II / LeetCode #644)

### 🛑 Why Sliding Window Fails When Length is Variable ($\ge k$)
A sliding window cannot greedily shrink or expand when the denominator is changing, because adding a smaller element might decrease the average, but enabling a much larger element ahead might increase it.

### 💡 Binary Search on the Answer (Guess the Average)
1. The target average $M$ must lie in range $[\min(\text{nums}), \max(\text{nums})]$.
2. **Check Condition**: Does there exist a subarray of length $\ge k$ with average $\ge M$?
   - Subtract $M$ from every element: $A'[i] = \text{nums}[i] - M$.
   - The question becomes: Is there a subarray of length $\ge k$ in $A'$ with sum $\ge 0$?
   - Maintain prefix sums of $A'$: $\text{sum}[i] - \min(\text{sum}[0 \dots i-k]) \ge 0$.
   - Check runs in $\mathcal{O}(N)$ time.
3. Binary search converges to precision $\epsilon = 10^{-5}$ in $\approx 30\text{–}40$ iterations.
- **Time Complexity**: $\mathcal{O}(N \log(\frac{\text{max} - \text{min}}{\epsilon}))$, **Space Complexity**: $\mathcal{O}(1)$.

---

## 3. Streaming Moving Average (Real-Time Sensors)

### 💡 Circular Buffer / Ring Queue
- To support `next(val)` queries in $\mathcal{O}(1)$ time with a sliding window of size $k$:
  - Maintain a circular array `buffer[k]` and `head_idx`.
  - Subtract overwritten value `buffer[head_idx]`, insert new value, advance `head_idx = (head_idx + 1) % k`.
  - Return `running_sum / count`.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Window Length | Optimal Approach | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Max Average I (#643)** | Exact $k$ | Fixed Sliding Window | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Max Average II (#644)** | Variable $\ge k$ | Binary Search on Answer + Prefix Sum | $\mathcal{O}(N \log(\text{Range}/\epsilon))$ | $\mathcal{O}(1)$ |
| **Streaming Moving Avg** | Real-time $k$ | Circular Ring Buffer | $\mathcal{O}(1)$ per tick | $\mathcal{O}(k)$ |
