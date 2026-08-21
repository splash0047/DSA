# 04 Interview Follow-ups & System Variations: 4Sum

The 4Sum problem finds all unique quadruplets $[a, b, c, d]$ in an array summing to `target`. The standard optimal approach sorts the array, nests two outer loops, and uses two pointers for the inner pair in $\mathcal{O}(N^3)$ time and $\mathcal{O}(1)$ extra space.

In interviews, this problem is a classic comparison between single-array 4Sum vs. 4-array 4Sum II, 64-bit integer overflow protection, and aggressive branch pruning.

---

## 1. 4Sum (LeetCode #18) vs. 4Sum II (LeetCode #454)

### 🛑 Crucial Architectural Difference
| Problem | Input Source | Optimal Approach | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **4Sum (#18)** | 1 single array (unique quadruplets) | Sort + Two Pointers | $\mathcal{O}(N^3)$ | $\mathcal{O}(1)$ |
| **4Sum II (#454)** | 4 distinct arrays $A, B, C, D$ | Hash Map of Pair Sums | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ |

### 💡 Why Hash Map Pair Sums Fails on 4Sum (#18)
In 4Sum II, elements come from separate arrays, so indices never conflict. In 4Sum (#18), a pair sum hash map `Map<sum, list<pair<int, int>>>` requires complex index-overlap checks and expensive duplicate quadruplet elimination, often running slower with high $\mathcal{O}(N^2)$ memory overhead compared to pruned $\mathcal{O}(N^3)$ two pointers.

---

## 2. Integer Overflow Safeguard (32-bit vs. 64-bit)

### 🛑 Real-World Bug
Summing four 32-bit signed integers ($4 \times 10^9 = 4 \times 10^9 > 2^{31}-1$) can overflow `int` and cause undefined behavior or wrong results.
- **Rule**: Always cast intermediate sums to `long long` in C++ or `long` in Java:
  ```cpp
  long long sum = (long long)nums[i] + nums[j] + nums[left] + nums[right];
  ```

---

## 3. High-Efficiency 2-Level Pruning

### 💡 Pruning Both Loops ($i$ and $j$)
```cpp
for (int i = 0; i < n - 3; i++) {
    if (i > 0 && nums[i] == nums[i - 1]) continue;
    if ((long long)nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target) break;
    if ((long long)nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target) continue;

    for (int j = i + 1; j < n - 2; j++) {
        if (j > i + 1 && nums[j] == nums[j - 1]) continue;
        if ((long long)nums[i] + nums[j] + nums[j+1] + nums[j+2] > target) break;
        if ((long long)nums[i] + nums[j] + nums[n-2] + nums[n-1] < target) continue;

        // Two-pointer inner loop
    }
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Input | Technique | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **4Sum (Unique Quads)** | 1 Array | Sort + 2-Level Pruning + Two Pointers | $\mathcal{O}(N^3)$ | $\mathcal{O}(1)$ |
| **4Sum II (Count Combos)** | 4 Arrays | Hash Map of $(A+B)$ lookup $-(C+D)$ | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ |
