# 04 Interview Follow-ups & System Variations: Subarray Sum Equals K

The problem counts the total number of continuous subarrays whose sum equals $k$. The optimal solution uses a running Prefix Sum and a Hash Map storing frequency counts of past prefix sums (`prefix_counts[current_sum - k]`) in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

In technical interviews, this problem is the cornerstone of prefix-sum hashing. Interviewers probe why sliding window fails here, how to scale to 1B elements, and how to generalize to 2D matrices and trees.

---

## 1. Why Can't We Use Sliding Window / Two Pointers Here?

### 🛑 The Non-Monotonicity of General Arrays
- A sliding window relies on the property that expanding the right pointer monotonically increases the sum, and shrinking the left pointer monotonically decreases the sum.
- Because `nums` can contain **negative numbers** and **zeros**, the running sum can fluctuate unpredictably.
- Adding an element might decrease the sum, and removing an element might increase it.
- **Rule**: If array contains negative numbers and asks for exact sum $k$, Prefix Sum + Hash Map is the standard optimal approach. (If all numbers are strictly positive, Two Pointers works in $\mathcal{O}(1)$ space).

---

## 2. Why Initialize `prefix_counts[0] = 1`?

### 💡 The Mathematical Invariant
- A subarray sum from index $i$ to $j$ is calculated as:
  $$\text{Sum}(i \dots j) = \text{PrefixSum}[j] - \text{PrefixSum}[i - 1] = k$$
- When a valid subarray starts at the very beginning of the array ($i = 0$), its sum is simply $\text{PrefixSum}[j] = k$.
- To find this subarray, we lookup `PrefixSum[j] - k = 0` in our map.
- The entry `{0: 1}` represents the empty prefix before the array begins, ensuring prefixes starting at index 0 are counted.

---

## 3. What if $N = 10^9$ Elements on Disk (Memory Bottleneck)?

### 🛑 The Problem
Storing prefix sum frequencies for 1 billion numbers in a hash map requires gigabytes of RAM.

### 💡 Sort-Based External Reduction
1. Stream through numbers sequentially and write the sequence of prefix sum pairs $(P[i], i)$ to disk.
2. Sort the prefix sums on disk using **External Merge Sort** by value $P[i]$.
3. Use two pointers / binary search over the sorted prefix list to find all pairs where $P[j] - P[i] = k$ and $j > i$.
- **I/O Complexity**: $\mathcal{O}(N \log N)$ disk stream I/O, $\mathcal{O}(1)$ RAM.

---

## 4. Generalization: Subarray Sum in a Binary Tree (Path Sum III / LeetCode #437)

### 💡 Prefix Sum + Backtracking on Tree DFS
- Maintain the same prefix sum hash map during tree traversal.
- As you visit `node`:
  - `current_sum += node->val`
  - `total_paths += map[current_sum - k]`
  - `map[current_sum]++`
  - Recurse on left and right children.
  - **Backtracking Step**: `map[current_sum]--` before returning to parent node so paths in sibling subtrees do not interfere.
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(H)$ where $H$ is tree height.

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Element Constraints | Optimal Strategy | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **General Array** | Positive, Negative, Zeros | Prefix Sum + Hash Map | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **Strictly Positive** | $nums[i] > 0$ | Sliding Window (Two Pointers) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Binary Tree (#437)** | Tree Node Paths | Prefix Map + DFS Backtracking | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| **1B Items on Disk** | Massive stream | External Sort on Prefix Pairs | $\mathcal{O}(N \log N)$ I/O | $\mathcal{O}(1)$ RAM |
