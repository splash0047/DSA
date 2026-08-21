# 04 Interview Follow-ups & System Variations: Contains Duplicate

The basic problem checks if any integer appears at least twice in an unsorted array. The standard solutions are Hash Set ($\mathcal{O}(N)$ time, $\mathcal{O}(N)$ space) or Sorting ($\mathcal{O}(N \log N)$ time, $\mathcal{O}(1)$ extra space).

In interviews, this is the launchpad for questions on spatial/temporal proximity constraints, streaming frequency estimation, and massive-scale external deduplication.

---

## 1. What if Duplicates Must Be Within Distance $K$ (Contains Duplicate II)?

### 🛑 The Scenario
Return `true` if there exist indices $i \neq j$ such that `nums[i] == nums[j]` and $|i - j| \le k$.

### 💡 Sliding Window Hash Set
Maintain a Hash Set of size at most $k$:
- As index $i$ advances, check if `nums[i]` is in the set.
- Add `nums[i]` to the set.
- If the set size exceeds $k$, remove `nums[i - k]`.
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(\min(N, k))$.

---

## 2. What if Values Are Close ($\le t$) AND Indices Are Close ($\le k$) (Contains Duplicate III)?

### 🛑 The Scenario
Find indices $i \neq j$ such that $|nums[i] - nums[j]| \le t$ and $|i - j| \le k$.

### 💡 Two Optimal Approaches
1. **Balanced Binary Search Tree (`std::set` in C++ / `TreeSet` in Java)**:
   - For each element $x$, check `set.lower_bound(x - t)`. If it exists and is $\le x + t$, return `true`.
   - Maintain sliding window of size $k$.
   - **Time Complexity**: $\mathcal{O}(N \log k)$, **Space Complexity**: $\mathcal{O}(k)$.
2. **Bucket Sort / Hashing (Fastest $\mathcal{O}(N)$ approach)**:
   - Partition numbers into buckets of width $w = t + 1$.
   - A bucket $B = \lfloor x / w \rfloor$ can contain at most 1 number (if 2 fall in the same bucket, difference $< w \implies \le t$).
   - Check current bucket $B$, left neighbor $B - 1$, and right neighbor $B + 1$.
   - **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(k)$.

---

## 3. What if $N = 10^9$ and Data Does Not Fit in Memory?

### 💡 System Architectures
1. **Bloom Filter (Fast Probabilistic Early-Exit)**:
   - If the goal is rapid detection and duplicates are frequent, pass elements through an in-memory Bloom Filter.
   - If Bloom Filter returns "Definitely NOT present", insert it.
   - If it returns "Maybe present", verify via disk/SSD storage.
   - Drastically cuts down disk I/O.
2. **External Merge Sort / Disk Hash Sharding**:
   - Hash partition the 1 billion numbers across $P$ partition files: `file_id = hash(x) % P`.
   - All duplicate values are guaranteed to hash into the same partition file.
   - Process each small partition file individually in RAM using a standard hash set.

---

## 4. What if Numbers are in Range $[1, N]$ with Exact 1 Duplicate (LeetCode #287)?

### 💡 Cycle Detection & Bit Manipulation
- Treat array values as pointers: $i \to nums[i]$.
- Because a duplicate value has multiple incoming pointers, a cycle must exist.
- **Floyd's Tortoise and Hare (Cycle Detection)**:
  - Phase 1: `slow = nums[slow]`, `fast = nums[nums[fast]]` until they meet.
  - Phase 2: Reset `slow = 0`; move both 1 step at a time until they meet at the cycle entrance (the duplicate value).
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: strictly $\mathcal{O}(1)$ without modifying the array.

---

## 5. What if the Input is an Unbounded Real-Time Stream?

### 💡 Probabilistic Frequency Sketches (Count-Min Sketch)
- If we cannot store all historical keys, use a **Count-Min Sketch** (2D array of counters with $d$ hash functions).
- For each incoming element $x$:
  - Increment $d$ counters.
  - Estimated frequency = $\min_{j=1}^d (\text{count}[j][h_j(x)])$.
  - If estimated frequency $\ge 2$, flag as duplicate.
- Uses sublinear memory $\mathcal{O}(\frac{1}{\epsilon} \ln \frac{1}{\delta})$ with bounded error.

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Bottleneck | Technique | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Contains Duplicate I** | Basic lookup | Hash Set / Sort | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ or $\mathcal{O}(1)$ |
| **Within Window $k$ (II)** | Spatial window | Sliding Window Hash Set | $\mathcal{O}(N)$ | $\mathcal{O}(k)$ |
| **Value Diff $\le t$, Index Diff $\le k$ (III)** | Value proximity | Bucket Hashing ($\text{width} = t + 1$) | $\mathcal{O}(N)$ | $\mathcal{O}(k)$ |
| **Range $[1, N]$ Immutable** | No extra space | Floyd's Cycle Detection | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **1B Items (Disk bound)** | RAM constraint | Hash Sharding into Partitions | $\mathcal{O}(N)$ I/O | $\mathcal{O}(N/P)$ RAM |
| **Streaming / Sketching** | Unbounded stream | Count-Min Sketch / Bloom Filter | $\mathcal{O}(1)$ / item | $\mathcal{O}(1)$ bounded |
