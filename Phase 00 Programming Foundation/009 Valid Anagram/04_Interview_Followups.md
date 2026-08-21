# 04 Interview Follow-ups & System Variations: Valid Anagram

The basic problem tests whether two strings $S$ and $T$ are anagrams. Standard approaches include Sorting ($\mathcal{O}(N \log N)$ time, $\mathcal{O}(1)$ or $\mathcal{O}(N)$ space) and a Fixed 26-element Frequency Array ($\mathcal{O}(N)$ time, $\mathcal{O}(1)$ space).

In interviews, this quickly expands to UTF-8/Unicode character handling, streaming sliding windows, large-scale grouping (Group Anagrams), and order-independent rolling hashing.

---

## 1. What if Strings Contain Unicode / UTF-8 Characters (e.g., Chinese, Arabic, Emojis)?

### 🛑 Why `int count[26]` Fails
UTF-8 is a variable-length encoding (1 to 4 bytes per code point). A standard fixed 26 or 256 array will index out of bounds or corrupt character boundaries.

### 💡 The Solution
1. **Decode to 32-bit Code Points (Runes / `char32_t`)**:
   - Parse UTF-8 bytes into standard Unicode scalar values.
2. **Dynamic Hash Table**:
   - Use `unordered_map<char32_t, int>` or `unordered_map<int, int>`.
   - Increment on string $S$, decrement on string $T$.
   - Verify that all counts return to zero.
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(U)$ where $U$ is the number of distinct Unicode characters.

---

## 2. How to Group Anagrams at Scale Across 10 Million Words (LeetCode #49)?

### 💡 Two Key Hashing Strategies Compared
1. **Sorted String as Hash Map Key**:
   - For each word $W$, `key = sort(W)`.
   - Map: `unordered_map<string, vector<string>> groups`.
   - Key generation time: $\mathcal{O}(L \log L)$ where $L$ is word length.
2. **Frequency Count Signature as Key (Faster for long strings)**:
   - Construct a formatted string key from counts: `"#1#0#2#0...#0"`.
   - Key generation time: $\mathcal{O}(L + \Sigma)$ where $\Sigma = 26$.
3. **Prime Number Product Hashing (Careful with Overflow)**:
   - Assign each character 'a' through 'z' a unique prime number: $p_a = 2, p_b = 3, p_c = 5, \dots$
   - $\text{Hash}(W) = \prod_{c \in W} p_c$.
   - By the Fundamental Theorem of Arithmetic, two words have the exact same product if and only if they are anagrams.
   - *Limitation*: Can overflow 64-bit integers for words longer than 15–20 characters; requires BigInt or modular arithmetic with multiple coprime moduli.

---

## 3. What if We Need to Find All Anagrams of Pattern $P$ in a Long Text $S$ (LeetCode #438)?

### 🛑 The Scenario
Pattern $P$ has length $M$, text $S$ has length $N$. Find all starting indices of anagrams of $P$ in $S$.

### 💡 Fixed-Size Sliding Window with Match Counter
- Maintain a window of size $M$.
- Instead of comparing entire 26-element arrays every step ($\mathcal{O}(26 \cdot N)$), maintain a single scalar `matches`:
  - `matches` counts how many of the 26 character slots currently have matching frequencies between the window and $P$.
  - Slide window by 1: adjust only the entering character and leaving character. If any character count hits the target frequency, `matches++`; if it leaves the target frequency, `matches--`.
  - When `matches == 26`, an anagram is found.
- **Time Complexity**: Strictly $\mathcal{O}(N)$ with $\mathcal{O}(1)$ operations per character slide.

---

## 4. Hardware & SIMD Acceleration for Frequency Comparisons

### 💡 Vectorized 256-bit AVX2 Compare
- In modern C++ compilers / high-performance systems, two 16-element or 32-element `int8_t` frequency vectors can be loaded into an AVX register (`__m256i`).
- A single instruction (`_mm256_cmpeq_epi8` followed by `_mm256_testz_si256`) compares all 26 character counts simultaneously in **1 CPU clock cycle**.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Character Set | Recommended Approach | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Standard ASCII** | a–z (26 chars) | Direct `int count[26]` | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Unicode / Emojis** | Full UTF-8 code points | `unordered_map<char32_t, int>` | $\mathcal{O}(N)$ | $\mathcal{O}(U)$ |
| **Group Anagrams (Short)** | ASCII | Sort each word as map key | $\mathcal{O}(N \cdot L \log L)$ | $\mathcal{O}(N \cdot L)$ |
| **Group Anagrams (Long)** | ASCII | Count Signature string key | $\mathcal{O}(N \cdot (L + \Sigma))$ | $\mathcal{O}(N \cdot L)$ |
| **Sliding Window Search** | Length $M$ in $N$ | Sliding Window + `matches` scalar | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
