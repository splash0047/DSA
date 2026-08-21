# 04 Interview Follow-ups & System Variations: Binary Search

The classic binary search locates a target value in a sorted array in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space. 

In top-tier technical interviews, this is the foundational problem used to probe low-level CPU branch prediction, 64-bit integer overflow, searching unbounded streams (Galloping Search), and disk-based external search.

---

## 1. The Famous Midpoint Integer Overflow Bug

### 🛑 The Problem
```cpp
int mid = (left + right) / 2; // Dangerous!
```
- If `left` and `right` are large positive integers (e.g., in a 2-billion element array where `left = 1.5 * 10^9` and `right = 2 * 10^9`), their sum exceeds $2^{31} - 1 = 2,147,483,647$.
- This results in a negative integer overflow and crashes with `IndexOutOfBounds`.

### 💡 The Production Solutions
1. **Subtraction Safe Formula**:
   ```cpp
   int mid = left + (right - left) / 2;
   ```
2. **Unsigned Bitwise Shift**:
   ```cpp
   int mid = (left + right) >> 1; // In languages with unsigned ints / uint
   // Or in Java: int mid = (left + right) >>> 1;
   ```

---

## 2. What if $N = 10^9$ Elements on Disk / Storage?

### 🛑 Memory Bottleneck
- An array of $10^9$ 64-bit integers takes 8 GB.
- If storage is on SSD / HDD, every `nums[mid]` probe triggers a random sector read.

### 💡 Disk-Optimized B-Trees & Block Probing
- A standard binary search takes $\log_2(10^9) pprox 30$ random disk seeks (slow on spinning disks).
- **Optimization (B-Tree / Multi-way Search)**:
  - Read disk blocks of size 4KB (containing 512 integers).
  - Perform 512-way branching per disk read.
  - Reduces disk I/O from 30 seeks to $\log_{512}(10^9) pprox 3	ext{--}4$ block reads.

---

## 3. What if the Array Length is UNKNOWN or INFINITE (Stream / Unbounded)?

### 💡 Exponential / Galloping Search
- Start with `bound = 1`.
- While `array[bound] < target`:
  - `bound *= 2` (check $1, 2, 4, 8, 16 \dots$).
- Once `array[bound] >= target` (or out of bounds exception occurs), binary search within the range `[bound / 2, bound]`.
- **Time Complexity**: $\mathcal{O}(\log P)$ where $P$ is the target's actual position in the stream.

---

## 4. Hardware Optimization: Branchless Binary Search (Eytzinger Layout)

### 🛑 CPU Branch Mispredictions
Standard binary search causes frequent CPU branch mispredictions because the comparison `nums[mid] < target` is unpredictable (~50% probability).

### 💡 Branchless Ternary Step
```cpp
while (len > 1) {
    int half = len / 2;
    left += (nums[left + half] < target) * half;
    len -= half;
}
return (nums[left] == target) ? left : -1;
```
- Uses conditional move instructions (`CMOV`) without branching, maximizing CPU instruction pipeline throughput.

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Challenge | Technique | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Standard Array** | Basic search | Left + (Right - Left)/2 | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| **Unbounded / Stream** | Unknown $N$ | Exponential Galloping Search | $\mathcal{O}(\log P)$ | $\mathcal{O}(1)$ |
| **Disk Block Storage** | High seek latency | B-Tree / Multi-way branching | $\mathcal{O}(\log_B N)$ I/O | $\mathcal{O}(B)$ |
| **High Frequency CPU** | Branch stall | Branchless CMOV Step | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
