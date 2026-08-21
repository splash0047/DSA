# 04 Interview Follow-ups & System Variations: Reverse String

The classic problem reverses an array of characters in-place using two pointers (`left = 0`, `right = n - 1`) in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is a test of low-level character encodings (UTF-8 byte corruption vs. Grapheme Clusters), language-specific memory models (string immutability), and hardware SIMD vectorization.

---

## 1. What if the String Contains Multi-Byte UTF-8 or Emojis (Grapheme Clusters)?

### 🛑 The Dangerous Bug with Naive Reversal
If you reverse bytes or 16-bit `char` units directly on UTF-8 / UTF-16 strings:
1. **Multi-byte code points get corrupted**: A 4-byte emoji (e.g., `🎉` = `F0 9F 8E 89`) reversed becomes `89 8E 9F F0`, which is invalid UTF-8 and crashes decoders.
2. **Grapheme Clusters get mangled**: A character with a combining accent mark (`e` + `\u0301` = `é`) reversed becomes `\u0301` + `e`, attaching the accent to whatever preceding character was swapped next to it.
3. **Compound Emojis (ZWJ sequences)**: `👨‍👩‍👧‍👦` (Family emoji) consists of 7 Unicode code points glued by Zero-Width Joiners (`\u200D`). Simple reversal breaks it into separate disconnected glyphs.

### 💡 The Solution (Grapheme Segmentation)
1. Segment the string into user-perceived characters (**Extended Grapheme Clusters**) using the Unicode UAX #29 standard.
2. Reverse the array of grapheme clusters as whole atomic units without reversing bytes inside a cluster.

---

## 2. What if Strings Are Immutable in Your Language (Java, Python, C#)?

### 💡 Language Internals & Allocation Strategy
- In Java/Python, strings are immutable arrays under the hood. Any in-place modification creates a new object.
- **Python**: `s[::-1]` creates a new string in $\mathcal{O}(N)$ time using optimized C-level `memcpy` internally.
- **Java**: `new StringBuilder(s).reverse().toString()` allocates a mutable `char[]` buffer, reverses in-place, and constructs a new `String`.
- **System Takeaway**: Mention to the interviewer that if memory allocation is strictly prohibited in an embedded/low-memory system, the API must accept a mutable character buffer (`char[]` in Java or `bytearray` in Python).

---

## 3. How to Vectorize String Reversal with SIMD (AVX-512 / NEON)?

### 💡 Byte Shuffling in CPU Registers
- Modern CPUs provide byte shuffle instructions (e.g., `_mm256_shuffle_epi8` in AVX2, or `_mm512_shuffle_epi8` in AVX-512).
- Load 32 or 64 bytes into a vector register.
- Apply a reversal mask vector: `[31, 30, 29, ..., 0]`.
- Write the reversed 32/64 bytes to the opposite end of the destination buffer.
- Reverses gigabytes of text per second at native memory bus speed.

---

## 4. Problem Variations

### 1. Reverse Every $2k$ Characters (LeetCode #541)
- Iterate in chunks of $2k$: `for (int i = 0; i < n; i += 2 * k)`.
- Reverse the sub-range `[i, min(i + k - 1, n - 1)]`.
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(1)$.

### 2. Reverse Only Vowels (LeetCode #345)
- Two pointers `left = 0`, `right = n - 1`.
- Advance `left` until it hits a vowel (`a, e, i, o, u, A, E, I, O, U`), decrement `right` until it hits a vowel, then swap.
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(1)$.

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Input Type | Strategy | Memory / Safety |
| :--- | :--- | :--- | :--- |
| **Plain ASCII** | `vector<char>&` | Two-Pointer In-Place Swap | $\mathcal{O}(1)$ space, perfectly safe |
| **Unicode UTF-8** | UTF-8 String | Grapheme Cluster Segmentation | $\mathcal{O}(N)$ space to preserve glyphs |
| **Immutable Strings** | Java `String` / Python `str` | `StringBuilder` / Bytearray slice | $\mathcal{O}(N)$ allocation required |
| **High Throughput** | 100MB+ buffer | SIMD AVX-256 Byte Shuffle | Up to 10–20 GB/s bandwidth |
