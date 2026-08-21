# 04 Interview Follow-ups & System Variations: Move Zeroes

The standard problem moves all `0`s to the end of an array while maintaining the relative order of non-zero elements in-place. The optimal solution uses two pointers (`read` and `write`) in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In system and senior engineering interviews, this problem is used to analyze write-amplification (SSD/Flash durability), stable vs. unstable partitioning, parallel stream compaction, and vectorization.

---

## 1. How to Minimize Total Number of Operations/Writes (Flash / SSD Optimization)?

### 🛑 The Problem
In NAND Flash storage or EEPROM, write operations wear out physical cells, whereas read operations are virtually free.

### 💡 Two Approaches Compared
1. **Standard Two-Pointer Swap**:
   ```cpp
   for (int read = 0; read < n; read++) {
       if (nums[read] != 0) {
           swap(nums[write++], nums[read]);
       }
   }
   ```
   - For an array of all non-zero elements (`[1, 2, 3, 4, 5]`), this executes $N$ swaps $\implies 2N$ or $3N$ unnecessary writes!
2. **Optimal Write-Minimizing Strategy**:
   ```cpp
   int write = 0;
   // Find the first zero index
   while (write < n && nums[write] != 0) write++;
   
   for (int read = write + 1; read < n; read++) {
       if (nums[read] != 0) {
           nums[write++] = nums[read];
           nums[read] = 0;
       }
   }
   ```
   - If there are zero zeroes, **0 writes** occur.
   - Total writes is strictly proportional to the number of non-zero elements after the first zero.

---

## 2. What if Relative Order Does NOT Need to Be Preserved?

### 💡 Two-Pointer End-Swap (Minimum Movement)
- Place `left = 0`, `right = n - 1`.
- If `nums[left] == 0`:
  - Swap `nums[left]` with `nums[right--]`.
- Else:
  - `left++`.
- **Advantage**: Elements are only moved if they need to be replaced. Non-zero elements already in the front are never touched.
- **Complexity**: $\mathcal{O}(N)$ time, $\mathcal{O}(1)$ space, but order is scrambled.

---

## 3. What if We Have 3 Distinct Classes (Move 0s to Front, 1s in Middle, 2s to End)?

### 💡 Dutch National Flag (3-Way Partitioning)
- Maintain 3 pointers: `low = 0`, `mid = 0`, `high = n - 1`.
- While `mid <= high`:
  - If `nums[mid] == 0`: `swap(nums[low++], nums[mid++])`.
  - If `nums[mid] == 1`: `mid++`.
  - If `nums[mid] == 2`: `swap(nums[mid], nums[high--])` *(note: do not increment `mid` here!)*.
- **Time Complexity**: $\mathcal{O}(N)$ single pass, $\mathcal{O}(1)$ space.

---

## 4. How to Parallelize Stream Compaction on GPU / Multi-core (Prefix Sum / Prefix Scan)?

### 🛑 The Challenge
How can $P$ threads compact non-zero elements into contiguous memory simultaneously without write race conditions?

### 💡 Parallel Stream Compaction Algorithm
1. **Predicate Mask**: Generate boolean array `mask[i] = (nums[i] != 0 ? 1 : 0)`.
2. **Parallel Prefix Sum (Exclusive Scan)**: Compute prefix sums of `mask` in $\mathcal{O}(\log N)$ parallel steps. The prefix sum value gives the exact target destination index `target_idx[i]` for every element.
3. **Scatter**: In parallel, each thread writes `if (mask[i] == 1) output[target_idx[i]] = nums[i]`.
4. Fill remaining indices with `0`.
- Used extensively in GPU computing (CUDA Thrust / OpenCL).

---

## Summary Matrix: Trade-offs at a Glance

| Goal | Relative Order Preserved? | Strategy | Write Complexity |
| :--- | :--- | :--- | :--- |
| **Standard Stable** | Yes | Two-Pointer (`write`, `read`) | $\mathcal{O}(N)$ |
| **SSD / Write-Optimized** | Yes | Skip initial non-zeros before writing | Minimized ($< N$ writes) |
| **Unstable Minimum Moves** | No | Bidirectional Two Pointers (`left`, `right`) | Strictly moves only misplaced items |
| **3 Categories (0, 1, 2)** | Partitioned | Dutch National Flag (3-Way) | Single pass, $\mathcal{O}(1)$ space |
| **GPU / Multi-threaded** | Yes | Prefix Scan + Scatter | $\mathcal{O}(\frac{N}{P} + \log N)$ parallel |
