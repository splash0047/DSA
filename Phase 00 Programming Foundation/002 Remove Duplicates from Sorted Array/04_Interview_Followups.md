# 04 Interview Follow-ups & System Variations: Remove Duplicates from Sorted Array

In standard interviews, the two-pointer technique (`write_idx` and `read_idx`) solves this problem in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ extra space. In senior/system-level interviews, interviewers use this problem to probe memory write bottlenecks, stream processing, hardware branch prediction, and multi-duplicate generalizations.

---

## 1. What if We Allow at Most $K$ Duplicates (e.g., LeetCode #80)?

### 🛑 The Scenario
Each unique element may appear at most $K$ times (e.g., $K = 2$) instead of just once.

### 💡 Generalized Two-Pointer Pattern
Instead of comparing `nums[read]` with `nums[read - 1]`, compare `nums[read]` against the element placed $K$ positions back at `nums[write - K]`:
```cpp
int removeDuplicatesK(vector<int>& nums, int k) {
    if (nums.size() <= k) return nums.size();
    int write = k;
    for (int read = k; read < nums.size(); read++) {
        if (nums[read] != nums[write - k]) {
            nums[write++] = nums[read];
        }
    }
    return write;
}
```
- **Why this works**: Because the array is sorted, if `nums[read] == nums[write - k]`, then the current value is already represented $K$ times in the valid prefix.
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(1)$.

---

## 2. What if There Are 1 Billion Elements ($N = 10^9$) on Disk / Storage?

### 🛑 The Bottleneck
- 1B 32-bit integers $\approx 4\text{ GB}$.
- Random in-place writes across a huge file can cause severe disk thrashing or flash wear.

### 💡 Streaming Chunk Processing (Single Sequential Pass)
- Since the array is already sorted, we **never need to look backward past the last emitted element**.
- Keep a single variable `last_emitted_val`.
- Stream chunk buffers (e.g., 64 MB blocks) from disk into RAM:
  - Process buffer sequentially: emit element only if `val != last_emitted_val`.
  - Stream unique items directly to an output stream / new file.
- **I/O Complexity**: Exactly 1 sequential read pass + 1 sequential write pass ($\mathcal{O}(N)$ disk bandwidth).

---

## 3. What if the Array is NOT Sorted?

### 💡 Follow-up Trade-offs
1. **Hash Set Preservation (Preserve Order of First Appearance)**:
   - Use an `unordered_set<int>` to track seen values.
   - Time: $\mathcal{O}(N)$ average, Space: $\mathcal{O}(U)$ where $U$ is the number of unique elements.
2. **Sort First (If Extra Space is Prohibited & Reordering is Allowed)**:
   - In-place sort in $\mathcal{O}(N \log N)$ (e.g., Heapsort), then run standard two-pointer deduplication.
   - Time: $\mathcal{O}(N \log N)$, Space: $\mathcal{O}(1)$.
3. **Bitset / Boolean Array (If Values Have Bounded Range $[-M, M]$)**:
   - Allocate direct bit array; mark bits in $\mathcal{O}(1)$ time.

---

## 4. What if the Input is an Infinite / Real-Time Sorted Stream?

### 💡 Streaming Generator Pattern
- You do not need to buffer historical data.
- Yield / forward elements only on value change:
  ```python
  def deduplicate_stream(stream):
      last = None
      for x in stream:
          if x != last:
              yield x
              last = x
  ```
- **Memory Overhead**: Strictly $\mathcal{O}(1)$ state storage regardless of stream duration.

---

## 5. Hardware & Low-Level Optimization: Minimizing Redundant Memory Writes

### 🛑 The Problem with Naive Two Pointers
In the standard loop:
```cpp
for (int read = 1; read < n; read++) {
    if (nums[read] != nums[write]) {
        nums[++write] = nums[read]; // Redundant write when all elements are unique!
    }
}
```
If the array has no duplicates (`[1, 2, 3, 4, 5]`), every element is overwritten with itself (`nums[i] = nums[i]`), generating unnecessary cache dirtiness and write-back traffic.

### 💡 Optimization (Skip Identity Writes)
```cpp
for (int read = 1; read < n; read++) {
    if (nums[read] != nums[write]) {
        write++;
        if (write != read) {
            nums[write] = nums[read]; // Only write when pointers have diverged
        }
    }
}
```

---

## 6. Distributed Deduplication Across Multiple Machines

### 🛑 Scenario
Data is partitioned across $M$ machines in sorted chunks (e.g., Machine 1 has $[1 \dots 100]$, Machine 2 has $[100 \dots 250]$).

### 💡 Edge Boundary Resolution
1. Each machine independently runs local deduplication on its partition.
2. Machines only need to communicate with adjacent partition neighbors:
   - Check if `Machine_i.max_element == Machine_{i+1}.min_element`.
   - If equal, drop the duplicate boundary value from `Machine_{i+1}`.
3. Communication cost: $\mathcal{O}(M)$ metadata messages instead of shuffling the entire dataset.

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Bottleneck | Strategy | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Standard Sorted** | Basic deduplication | Two Pointers (`write`, `read`) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **At Most $K$ Duplicates** | Generalizing window | Compare with `nums[write - K]` | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Unsorted + Preserve Order** | Unsorted duplicates | Hash Set (`seen`) | $\mathcal{O}(N)$ | $\mathcal{O}(U)$ |
| **Unsorted + $\mathcal{O}(1)$ Space** | Memory constraint | In-place Sort + Two Pointers | $\mathcal{O}(N \log N)$ | $\mathcal{O}(1)$ |
| **1B Items on Disk** | RAM capacity & Disk I/O | Block Streaming + Sequential Output | $\mathcal{O}(N)$ I/O | $\mathcal{O}(1)$ RAM |
| **Distributed Sorted Chunks** | Network communication | Local Dedup + Boundary Sync | $\mathcal{O}(N/M)$ parallel | $\mathcal{O}(1)$ |
