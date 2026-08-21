# 04 Interview Follow-ups & System Variations: Minimum Size Subarray Sum

The problem finds the minimal length of a contiguous subarray of which the sum is $\ge \text{target}$ in an array of **positive integers**. The standard sliding window expands `right` and shrinks `left` whenever `sum >= target` in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, the interviewer's most famous follow-up is: **"What if the array can contain NEGATIVE numbers?"**

---

## 1. What if the Array Contains Negative Numbers (LeetCode #862)?

### 🛑 Why Sliding Window Breaks
The sliding window algorithm relies on the property that expanding the window always increases (or maintains) the sum, and shrinking the window always decreases the sum. With negative numbers, adding an element can reduce the sum and removing an element can increase the sum, completely breaking monotonicity.

### 💡 The Solution: Monotonic Deque of Prefix Sums
1. Compute prefix sums: $P[i] = \sum_{j=0}^{i-1} \text{nums}[j]$.
2. The condition $\text{sum}(j \dots i-1) \ge \text{target}$ translates to:
   $$P[i] - P[j] \ge \text{target} \iff P[j] \le P[i] - \text{target}$$
3. Maintain a **Monotonic Increasing Deque** of prefix sum indices:
   - **Optimization 1 (Valid Window Check)**: While $P[i] - P[\text{deque.front()}] \ge \text{target}$, update `min_len = min(min_len, i - deque.front())` and pop `deque.front()`. (Because any future $i' > i$ will have a larger distance $i' - j > i - j$, index $j$ can never produce a shorter valid subarray).
   - **Optimization 2 (Monotonicity Maintenance)**: While $P[i] \le P[\text{deque.back()}]$, pop `deque.back()`. (A smaller prefix sum occurring at a later index is always strictly superior to a larger prefix sum at an earlier index).
- **Time Complexity**: $\mathcal{O}(N)$ (each index pushed and popped at most once), **Space Complexity**: $\mathcal{O}(N)$.

---

## 2. When is the $\mathcal{O}(N \log N)$ Binary Search Approach Preferred?

### 💡 Binary Search on Subarray Length / Prefix Sums
- If $N$ is small or array is stored in immutable distributed chunks, we can binary search on the subarray length $L \in [1, N]$.
- For a fixed length $L$, verify if any sliding window of size $L$ has sum $\ge \text{target}$ in $\mathcal{O}(N)$ time.
- Highly useful in GPU / parallel implementations where uniform fixed-length window evaluations run synchronously across threads.

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Element Values | Optimal Technique | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **LeetCode #209** | Strictly Positive ($>0$) | Sliding Window (Two Pointers) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **LeetCode #862** | Positive & Negative | Monotonic Deque + Prefix Sums | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **Parallel / GPU** | Strictly Positive | Binary Search on Length $L$ | $\mathcal{O}(N \log N)$ | $\mathcal{O}(1)$ |
