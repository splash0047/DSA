# 04 Interview Follow-ups & System Variations: Number of 1 Bits

The problem counts the number of set bits (Hamming Weight) in a 32-bit unsigned integer. Optimal solutions include **Brian Kernighan's Algorithm** in $\mathcal{O}(	ext{set bits})$ and hardware `POPCNT` instructions in $\mathcal{O}(1)$.

In technical interviews, this problem tests low-level bit tricks, hardware CPU instructions, and parallel bit counting.

---

## 1. Brian Kernighan's Algorithm (`n &= (n - 1)`)

### 💡 The Lowest Set Bit Clear Trick
- `n - 1` flips all bits from the rightmost set bit downwards.
- `n & (n - 1)` clears the lowest set bit to 0 in a single operation.
- Loop runs in strictly $\mathcal{O}(K)$ steps where $K$ is the number of set bits (not 32 steps!).

---

## 2. Hardware Instruction: `POPCNT`

### 💡 1-Cycle Native CPU Execution
- Modern x86 / ARM processors have dedicated silicon for counting bits:
  ```cpp
  int count = __builtin_popcount(n); // In GCC / Clang (maps directly to POPCNT instruction)
  ```

---

## Summary Matrix: Trade-offs at a Glance

| Method | Steps | Time Complexity | Hardware Direct |
| :--- | :--- | :--- | :--- |
| **Brian Kernighan** | Number of set bits | $\mathcal{O}(	ext{Set Bits})$ | 0 extra space |
| **`__builtin_popcount`**| 1 CPU cycle | $\mathcal{O}(1)$ | **POPCNT instruction** |
| **Lookup Table (8-bit)**| 4 table lookups | $\mathcal{O}(1)$ | 256-byte static table |
