# 04 Interview Follow-ups & System Variations: Contiguous Array

The problem finds the maximum length of a contiguous subarray with an equal number of `0`s and `1`s. By transforming `0` into `-1`, the problem reduces to **Longest Subarray with Sum Equals 0**. Storing the earliest index of each prefix sum in a Hash Map achieves $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

In technical interviews, this problem tests state transformation, 3-class balance generalizations (0s, 1s, and 2s), and memory optimization using direct bounded arrays.

---

## 1. Low-Level Memory Optimization: Fixed Array Instead of Hash Map

### 🛑 Hash Map Overhead
`unordered_map<int, int>` incurs dynamic memory allocation and hash collision overhead.

### 💡 Bounded Range Offset Array ($\mathcal{O}(1)$ Lookup Time)
- The running sum using $-1$ and $+1$ can only range between $-N$ and $+N$ (at most $2N + 1$ possible values).
- Allocate a flat array `int first_seen[2 * N + 1]` initialized to $-2$:
  ```cpp
  int findMaxLength(vector<int>& nums) {
      int n = nums.size();
      vector<int> first_seen(2 * n + 1, -2);
      first_seen[0 + n] = -1; // Base case: prefix sum 0 at index -1
      
      int sum = 0, max_len = 0;
      for (int i = 0; i < n; i++) {
          sum += (nums[i] == 1 ? 1 : -1);
          if (first_seen[sum + n] >= -1) {
              max_len = max(max_len, i - first_seen[sum + n]);
          } else {
              first_seen[sum + n] = i;
          }
      }
      return max_len;
  }
  ```
- **Performance**: $3\text{–}5\times$ faster in runtime; 0 hash lookups, zero dynamic heap overhead.

---

## 2. Generalization: Equal Number of 0s, 1s, and 2s (3 Distinct Categories)

### 🛑 The Challenge
Find the longest contiguous subarray with an equal number of `0`s, `1`s, and `2`s.

### 💡 2D Differential State Tuple Hashing
- Let $c_0, c_1, c_2$ be the running counts of 0, 1, and 2.
- An equal count requires: $c_1 - c_0 = \Delta_1$ and $c_2 - c_0 = \Delta_2$.
- Maintain a Hash Map storing the earliest index for the 2D tuple key:
  $$\text{State}(i) = (\Delta_1, \Delta_2) = (c_1 - c_0,\; c_2 - c_0)$$
- When $(\Delta_1, \Delta_2)$ repeats at index $j$, the subarray $(first\_seen \dots j]$ has an equal count of 0s, 1s, and 2s!
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(N)$.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Categories | State Representation | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **0s and 1s (Map)** | 2 | Single integer `sum` in `unordered_map` | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ heap |
| **0s and 1s (Array)** | 2 | Direct array `first_seen[sum + N]` | $\mathcal{O}(N)$ | $\mathcal{O}(2N)$ cache |
| **0s, 1s, and 2s** | 3 | Pair tuple key `(c1 - c0, c2 - c0)` | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
