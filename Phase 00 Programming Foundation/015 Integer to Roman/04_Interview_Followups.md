# 04 Interview Follow-ups & System Variations: Integer to Roman

The standard problem converts an integer in the range $[1, 3999]$ into a Roman numeral string. Standard solutions include Greedy Value-Symbol Subtraction ($\mathcal{O}(1)$ time, $\mathcal{O}(1)$ space) and Digit Place-Value Lookup ($\mathcal{O}(1)$ time, $\mathcal{O}(1)$ space).

In interviews, this problem is used to discuss static lookup tables vs. greedy reductions, zero-allocation memory formatting, and scaling conversions to high-throughput financial or archival systems.

---

## 1. Greedy Subtraction vs. Digit Place-Value Lookup: Which is Faster?

### 💡 Two Approaches Compared
1. **Greedy 13-Pair Subtraction**:
   - Loops through 13 predefined pairs: `(1000, "M"), (900, "CM"), ..., (1, "I")`.
   - Requires while-loops and repeated subtractions.
2. **Hardcoded 4-Array Direct Indexing (Fastest $\mathcal{O}(1)$)**:
   ```cpp
   string intToRoman(int num) {
       static const string M[] = {"", "M", "MM", "MMM"};
       static const string C[] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
       static const string X[] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
       static const string I[] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
       
       return M[num / 1000] + C[(num % 1000) / 100] + X[(num % 100) / 10] + I[num % 10];
   }
   ```
   - **Advantage**: Zero loops, zero branch mispredictions, pure direct table indexing in CPU L1 cache.

---

## 2. High-Throughput / Zero-Allocation Systems Optimization

### 🛑 Memory Allocation Overhead
In C++ or Java, returning `string` dynamically allocates heap memory for every single conversion call.

### 💡 Zero-Heap In-Place Buffer Formatting
- Pass a fixed stack buffer: `char buffer[16]`.
- The maximum Roman numeral length for $\le 3999$ is `"MMMDCCCLXXXVIII"` (15 characters).
- Fill buffer directly without dynamic memory allocations:
  ```cpp
  int intToRomanBuffer(int num, char* out_buf) {
      // Append string slices directly via memcpy into out_buf
      // Returns length of formatted string
  }
  ```

---

## 3. What if Numbers Exceed 3,999 (Vinculum / Multiplier Format)?

### 💡 Recursive / Modular Scaling
- Separate input into thousands chunks: $Q = \text{num} / 1000$, $R = \text{num} \pmod{1000}$.
- For values $\ge 4000$, format the quotient $Q$ with an overline indicator (e.g., `_V`, `_X`, `_L`) and concatenate with the Roman conversion of remainder $R$.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Latency | Memory Allocation | Best Used When |
| :--- | :--- | :--- | :--- |
| **Greedy Subtraction** | Very Low | Minimal | Quick implementation, clean code |
| **Digit Direct Table** | **Optimal (Fastest)** | Minimal | Production hot paths with high query volume |
| **Stack Buffer (`char[16]`)** | **Optimal** | **0 Heap Allocs** | Embedded systems, low-latency engines |
| **Vinculum Recursive** | Low | Low | Supporting numbers $> 4,000$ |
