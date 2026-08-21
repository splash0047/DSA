# 04 Interview Follow-ups & System Variations: Two Sum II - Input Array Is Sorted

The classic problem finds two numbers in a 1-indexed sorted array that add up to `target`. The optimal two-pointer approach (`left = 0`, `right = n - 1`) runs in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is used to test binary search hybrids, exponential leaps for skewed targets, massive disk streams, and multi-threaded parallelization.

---

## 1. What if $N = 10^9$ Elements and the Solution Pair Lies Very Close to the Start?

### 🛑 The Inefficiency
If `target` is formed by `numbers[0] + numbers[1]`, the standard two-pointer loop will decrement `right` from index $10^9 - 1$ all the way down to $1$, taking $10^9$ unnecessary iterations.

### 💡 Hybrid Exponential Search / Binary Search Leaps
Instead of moving `right` by 1 step at a time:
1. **Binary Search Upper Bound**: Use `std::upper_bound` to find the largest element $\le \text{target} - \text{numbers}[0]$ in $\mathcal{O}(\log N)$ time and set `right` directly there.
2. **Exponential Leap Galloping**:
   - If `numbers[left] + numbers[right] > target`, probe backwards exponentially: `step = 1, 2, 4, 8...` until sum $\le \text{target}$, then binary search in that range.
- **Time Complexity**: $\mathcal{O}(\log N)$ instead of $\mathcal{O}(N)$ when targets are asymmetric.

---

## 2. What if Array is Stored in Block Storage on Disk (Cannot Randomly Seek)?

### 💡 Bidirectional Stream Reader
- Open two sequential disk file handles / block streams:
  - `Stream_A` reading forwards from the start (block $0, 1, 2...$).
  - `Stream_B` reading backwards from the end (block $M, M-1, ...$).
- Buffer 1 block in RAM for each stream.
- When `Stream_A` needs to advance, read next buffered element.
- When `Stream_B` needs to advance, read previous buffered element.
- When buffer is exhausted, load the next sequential block.
- **I/O Complexity**: Strictly sequential disk reads; total I/O bounded by data traversed ($\le 2$ passes).

---

## 3. What if Duplicates Exist and We Must Return ALL Unique Pairs?

### 💡 Two-Pointer Duplicate Skipping
```cpp
while (left < right) {
    int sum = numbers[left] + numbers[right];
    if (sum == target) {
        result.push_back({left + 1, right + 1});
        while (left < right && numbers[left] == numbers[left + 1]) left++;
        while (left < right && numbers[right] == numbers[right - 1]) right--;
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

## 4. What if We Want Closest Pair Sum to Target?

### 💡 Tracking Minimum Absolute Difference
- Maintain `min_diff = INT_MAX` and `best_pair`.
- In the two-pointer loop:
  - Update `diff = abs(target - sum)`.
  - If `diff < min_diff`, update `min_diff` and `best_pair`.
  - If `sum < target`, `left++`; else `right--`.

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Strategy | Time | Space |
| :--- | :--- | :--- | :--- |
| **Standard Two-Pointer** | Linear convergence from ends | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Skewed Target Location** | Exponential Leap + Binary Search | $\mathcal{O}(\log N)$ best | $\mathcal{O}(1)$ |
| **Closest Pair to Target** | Two-Pointer tracking `min_diff` | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Disk Block Stream** | Two Sequential Block Buffer Readers | $\mathcal{O}(N)$ sequential I/O | $\mathcal{O}(2 \times \text{BlockSize})$ |
