# 04 Interview Follow-ups & System Variations: Minimum Window Substring

The Minimum Window Substring problem (Hard) finds the shortest substring in $S$ that contains all characters of $T$ (including duplicates). The optimal approach uses a variable-size sliding window with a frequency map and a `formed` character counter in $\mathcal{O}(|S| + |T|)$ time and $\mathcal{O}(\Sigma)$ space.

In top-tier technical interviews, this is the gold standard sliding window question. Interviewers test sparse character optimization, $K$-list range reductions, and streaming stream buffers.

---

## 1. High-Performance Optimization: Filtered String Indexing ($|S| \gg |T|$)

### 🛑 The Scenario
Suppose $S$ is a 10MB document, but $T$ consists of only 3 characters (`"XYZ"`). 99.9% of characters in $S$ are irrelevant text (`a-w`).

### 💡 Filtered Sparse Array of Target Characters
1. Pre-process $S$ into a compressed array containing **only characters present in $T$ alongside their original indices**:
   ```cpp
   vector<pair<int, char>> filtered_s;
   for (int i = 0; i < s.size(); i++) {
       if (target_map.count(s[i])) {
           filtered_s.push_back({i, s[i]});
       }
   }
   ```
2. Run the sliding window **only on `filtered_s`**!
3. **Speedup**: If `filtered_s` has size $M \ll |S|$, the sliding window loop executes in $\mathcal{O}(M)$ steps instead of $\mathcal{O}(|S|)$ steps, speeding up execution by up to $100\times$.

---

## 2. Generalization: Smallest Range Covering Elements from $K$ Lists (LeetCode #632)

### 💡 Reduction to Minimum Window Substring
- Given $K$ sorted lists, find the smallest range $[a, b]$ containing at least 1 number from each of the $K$ lists.
- **Approach 1 (Flatten + Minimum Window Substring)**:
  - Tag each number with its list ID: $(val, list\_id)$.
  - Combine and sort all numbers.
  - Now the problem is identical to finding the minimum window substring that contains all list IDs $0 \dots K-1$!
- **Approach 2 (Min-Heap of size $K$)**:
  - Push first element of each list into Min-Heap while tracking `current_max`.
  - Pop min element, update range $[min, max]$, and insert next element from the popped list.
  - Time: $\mathcal{O}(N \log K)$, Space: $\mathcal{O}(K)$.

---

## 3. Streaming Log Monitor (Detecting Signature Within Minimal Time)

### 💡 Bounded Deque Window
- When characters/log events arrive continuously over network sockets, maintain a bounded deque of relevant event timestamps.
- When all required events in $T$ are present, record latency window `now - deque.front().timestamp` and evict front events.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Optimal Strategy | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Standard Minimum Window** | Sliding Window + `formed` scalar | $\mathcal{O}(\|S\| + \|T\|)$ | $\mathcal{O}(\Sigma)$ |
| **Sparse Target Chars ($|S| \gg |T|$)** | Filtered Index Array + Sliding Window | $\mathcal{O}(\|S\| + M)$ | $\mathcal{O}(M)$ |
| **Smallest Range in $K$ Lists (#632)**| Tagged Merge + Sliding Window / Min-Heap | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
