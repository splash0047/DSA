# 04 Interview Follow-ups & System Variations: Two Sum

In technical interviews (especially for L4/L5+ or FAANG/top-tier tech companies), solving the standard problem with a Hash Map in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space is just the baseline. The real interview begins with follow-up scenarios testing system constraints, memory bottlenecks, streaming, and scalability.

---

## 1. What if the array contains 1 Billion Elements ($N = 10^9$)?

### 🛑 The Bottleneck
- 1 billion 32-bit integers require $\approx 4\text{ GB}$ of raw storage.
- A hash table (`std::unordered_map` or Python `dict`) has significant pointer and bucket overhead (typically $24\text{–}32\text{ bytes}$ per entry), requiring $\approx 24\text{–}32\text{ GB}$ of RAM.
- A single-machine in-memory hash map may exceed available RAM or cause thrashing.

### 💡 Optimal Follow-up Strategy
1. **External Sort & Two Pointers**:
   - If memory is strictly constrained (e.g., < 4 GB available), perform an **External Merge Sort** to chunk, sort on disk, and merge.
   - Once sorted across external files/streams, apply the **Two-Pointer technique** with one pointer reading from the start and another from the end.
   - Space complexity drops to $\mathcal{O}(1)$ working memory (plus buffer blocks).
2. **Distributed / Sharded Hash Table (MapReduce / Spark)**:
   - Partition elements across a cluster using consistent hashing: `partition_id = hash(val) % NUM_NODES`.
   - For every element $x$, check if the node responsible for `target - x` has seen its complement.
   - Communication pattern: Shuffle phase routes numbers to their respective complement buckets.

---

## 2. What if the Input Data Comes as an Infinite / Real-time Stream?

### 🛑 The Scenario
Numbers arrive continuously one by one over time, and we must detect or report if any incoming number pairs with a previously seen number to equal `target`.

### 💡 Strategy & Trade-offs
1. **Unbounded Stream**:
   - Storing all historical values will eventually lead to Out-Of-Memory (OOM).
2. **Sliding Window Stream (Last $K$ elements / Last $T$ minutes)**:
   - Maintain a sliding window using a combination of a `Queue` / `Deque` and a `Hash Map` with frequency counts.
   - As $x_{new}$ arrives:
     - Check if `target - x_new` exists in the hash map.
     - Add $x_{new}$ to queue and map.
     - When window exceeds limit $K$, evict $x_{old}$ from queue and decrement its frequency in the map.
3. **Probabilistic Membership (Bloom Filter)**:
   - If space is strictly capped and false positives are tolerable, use a Counting Bloom Filter to check complement existence before reading from cold storage.

---

## 3. What if You Cannot Use Extra Space ($\mathcal{O}(1)$ Memory Allowed)?

### 🛑 The Constraint
Memory overhead must be strictly $\mathcal{O}(1)$.

### 💡 Solutions Depending on Permissions
1. **If Input Array Can Be Modified**:
   - In-place Sort the array in $\mathcal{O}(N \log N)$ (e.g., Heapsort or introsort).
   - Use Two Pointers from both ends ($\mathcal{O}(N)$ pass).
   - *Note on Indices*: If original indices are required, modifying the original array loses them unless indices are packed into the numbers (e.g., bitwise packing if numbers are small) or paired into a struct (which requires $\mathcal{O}(N)$ space).
2. **If Array is Immutable & No Extra Space Allowed**:
   - The only possible approach is the nested loops Brute Force: $\mathcal{O}(N^2)$ time, $\mathcal{O}(1)$ space.

---

## 4. What if the Array is Already Sorted?

### 💡 Immediate Transition
- Immediately switch from Hash Map ($\mathcal{O}(N)$ space) to **Two Pointers** ($\mathcal{O}(1)$ space).
- Time Complexity: $\mathcal{O}(N)$.
- Space Complexity: $\mathcal{O}(1)$.
- If $N$ is massive and target pairs are near the ends, two pointers converge quickly.

---

## 5. What if the Query Operation is Performed Millions of Times on a Static Array?

### 🛑 The Scenario
The array `nums` is static (fixed once), but we receive millions of `twoSum(target)` queries with varying `target` values.

### 💡 Preprocessing Strategies
1. **Sorted Array + Binary Search / Two-Pointer per query**:
   - Sort once in $\mathcal{O}(N \log N)$.
   - Each query runs in $\mathcal{O}(N)$ or $\mathcal{O}(K)$ (where $K$ is number of matches).
2. **All-Pairs Precomputation (if $N$ is small, queries are massive)**:
   - Precompute all possible pairwise sums: `Map<sum, list<pair<int, int>>>`.
   - Precomputation: $\mathcal{O}(N^2)$ time and space.
   - Query time: $\mathcal{O}(1)$ instantaneous lookup.
3. **Bitset / Fast Fourier Transform (FFT) for Polynomial Convolution**:
   - If values are bounded integers in range $[0, M]$, represent the array as a polynomial/bitset $P(x)$.
   - $P(x) \times P(x)$ via FFT computes all possible pair sums in $\mathcal{O}(M \log M)$ time.

---

## 6. What if Duplicates Exist and We Must Return ALL Unique Pairs?

### 💡 Nuances & Pitfalls
- A standard single-pass map may return duplicate pairs or need complicated visited sets.
- **Sorted + Two Pointers** is the standard and cleanest way:
  ```cpp
  while (left < right) {
      int sum = nums[left] + nums[right];
      if (sum == target) {
          result.push_back({nums[left], nums[right]});
          while (left < right && nums[left] == nums[left + 1]) left++;
          while (left < right && nums[right] == nums[right - 1]) right--;
          left++;
          right--;
      } else if (sum < target) {
          left++;
      } else {
          right--;
      }
  }
  ```

---

## 7. What Real-World System Failures & Edge Cases Can Occur?

1. **Integer Overflow on Sum**:
   - If `nums[i] + nums[j]` can exceed standard 32-bit signed limits (`INT_MAX` / `INT_MIN`), calculate `target - nums[i]` rather than adding `nums[i] + nums[j]`.
2. **Hash Table Worst-Case Denial of Service (Anti-Hash Tests)**:
   - In languages using standard non-randomized hash functions (e.g., `std::unordered_map` in C++), crafted inputs can force all keys into a single bucket, degrading lookup from $\mathcal{O}(1)$ average to $\mathcal{O}(N)$ worst case (total time $\mathcal{O}(N^2)$).
   - *Fix*: Use a custom hash function with a randomized seed (e.g., `splitmix64` / `gp_hash_table`).

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Primary Bottleneck | Recommended Technique | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Standard In-Memory** | Lookup speed | Hash Table (Single Pass) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **Sorted Input** | Extra memory waste | Two Pointers | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Strict $\mathcal{O}(1)$ Space** | Memory limit | In-place Sort + Two Pointers | $\mathcal{O}(N \log N)$ | $\mathcal{O}(1)$ |
| **1B Items (Disk/RAM)** | Memory / RAM capacity | External Sort + Two Pointers | $\mathcal{O}(N \log N)$ IO | $\mathcal{O}(1)$ RAM |
| **Infinite Stream** | Unbounded memory growth | Sliding Window (Queue + Map) | $\mathcal{O}(1)$ / element | $\mathcal{O}(K)$ window |
| **Repeated Queries** | Latency per query | Precomputed Pair Sums / Binary Search | $\mathcal{O}(1)$ or $\mathcal{O}(N)$ | $\mathcal{O}(N^2)$ or $\mathcal{O}(N)$ |
