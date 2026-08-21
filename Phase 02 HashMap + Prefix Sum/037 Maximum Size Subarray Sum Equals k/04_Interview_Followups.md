# 04 Interview Follow-ups & System Variations: Maximum Size Subarray Sum Equals k

The problem finds the maximum length of a subarray that sums to $k$. The optimal solution stores the **earliest index** of each prefix sum in a Hash Map (`first_seen[sum] = index`) and queries `first_seen[current_sum - k]` in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

In technical interviews, this problem is compared directly with Minimum Size Subarray Sum, strictly positive sliding window trade-offs, and 2D matrix maximal subgrid problems.

---

## 1. Max Size vs. Min Size vs. Count of Subarrays Equals $k$

| Problem Goal | Hash Map Value Stored | Map Update Strategy |
| :--- | :--- | :--- |
| **Max Size Equals $k$** | **Earliest Index** | Insert **only if key NOT present** (preserve earliest $j$) |
| **Min Size Equals $k$** | **Latest Index** | Always **overwrite** key with current index $i$ |
| **Total Count Equals $k$** | **Frequency Count** | Increment frequency on every visit (`count[sum]++`) |

---

## 2. What if All Elements Are Strictly Positive ($nums[i] > 0$)?

### 💡 Pivot to Two Pointers / Sliding Window ($\mathcal{O}(1)$ Memory)
- Because all elements are positive, prefix sums are strictly monotonic.
- Maintain `left = 0`, `current_sum = 0`.
- Expand `right`: `current_sum += nums[right]`.
- Shrink `left` while `current_sum > k`: `current_sum -= nums[left++]`.
- If `current_sum == k`, update `max_len = max(max_len, right - left + 1)`.
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: strictly $\mathcal{O}(1)$.

---

## 3. Generalization: 2D Matrix - Largest Submatrix with Sum Equals $k$

### 💡 2D to 1D Row Compression
1. Fix top row $r_1$ and bottom row $r_2$ (at most $\mathcal{O}(R^2)$ pairs).
2. Compress columns between $r_1$ and $r_2$ into a 1D array of column sums.
3. Run the 1D Max Subarray Sum Equals $k$ algorithm using a Hash Map on the column sums.
- **Time Complexity**: $\mathcal{O}(R^2 \times C)$, **Space Complexity**: $\mathcal{O}(C)$.

---

## Summary Matrix: Trade-offs at a Glance

| Goal | Elements | Strategy | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Max Size ($\text{sum} = k$)** | Pos/Neg/0 | Hash Map of Earliest Indices | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **Max Size ($\text{sum} = k$)** | Strictly Positive | Sliding Window (Two Pointers) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **2D Largest Submatrix** | Matrix | Row-pair compression + 1D Hash Map | $\mathcal{O}(R^2 C)$ | $\mathcal{O}(C)$ |
