# 04 Interview Follow-ups & System Variations: Max Consecutive Ones III

The problem finds the maximum number of consecutive `1`s in a binary array if you can flip at most $k$ `0`s. The optimal solution uses a non-shrinking sliding window in $\mathcal{O}(N)$ time and strictly $\mathcal{O}(1)$ space.

In technical interviews, this problem is used to compare sliding windows vs. zero-index queues, run-length compression (RLC), and infinite stream processing.

---

## 1. Non-Shrinking Sliding Window ($\mathcal{O}(N)$ Optimal)

### 💡 The Cleanest Template
```cpp
int longestOnes(vector<int>& nums, int k) {
    int left = 0, right;
    for (right = 0; right < nums.size(); right++) {
        if (nums[right] == 0) k--;
        if (k < 0) {
            // When budget is exhausted, slide left forward by 1
            if (nums[left] == 0) k++;
            left++;
        }
    }
    return right - left;
}
```
- **Time Complexity**: $\mathcal{O}(N)$ strictly (each element visited once, 0 inner loops).
- **Space Complexity**: $\mathcal{O}(1)$.

---

## 2. What if Input is an Infinite Stream and $k$ is Small (e.g., $k = 1$ or $k = 10$)?

### 🛑 The Scenario
You cannot store historical `nums` in an array; elements stream in real time.

### 💡 Queue of Zero Indices
- Maintain a `queue<int> zero_indices` of size at most $k$.
- When a `0` arrives at timestamp $t$:
  - If `zero_indices.size() == k`, the new left boundary becomes `zero_indices.front() + 1`; pop `zero_indices.front()`.
  - Push $t$ to `zero_indices`.
- **Memory Overhead**: $\mathcal{O}(k)$ instead of buffering the whole stream.

---

## 3. What if $N = 10^9$ Stored via Run-Length Encoding (RLE)?

### 🛑 The Scenario
Sparse binary array compressed as pairs: `[(1, 1000000), (0, 3), (1, 500000), ...]`.

### 💡 Two Pointers on Compressed Blocks
- Instead of iterating $10^9$ bits, maintain two pointers across the array of run-length tuples.
- Expand `right_block`: accumulate total length and subtract zero counts from budget $k$.
- Shrink `left_block`: restore zero budget from outgoing zero runs.
- **Time Complexity**: $\mathcal{O}(B)$ where $B$ is the number of compressed runs ($B \ll N$).

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Constraint / Model | Optimal Approach | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Max Consecutive Ones I (#485)** | $k = 0$ | Single-pass streak counter | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Max Consecutive Ones II (#487)** | $k = 1$ | 2-Variable streak tracker | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Max Consecutive Ones III (#1004)**| Arbitrary $k$ | Non-Shrinking Sliding Window | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Infinite Stream** | Small $k$ | Queue of $k$ zero indices | $\mathcal{O}(1)$ / bit | $\mathcal{O}(k)$ |
| **Run-Length Encoded (RLE)** | Compressed $10^9$ bits | Sliding Window on Run Blocks | $\mathcal{O}(B)$ | $\mathcal{O}(1)$ |
