# 04 Interview Follow-ups & System Variations: Reverse Words in a String

The standard problem reverses words in a sentence while cleaning multiple spaces and leading/trailing whitespace. The standard two-pointer in-place approach operates in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ extra space (or $\mathcal{O}(N)$ space in languages with immutable strings).

In top-tier interviews, this tests multi-pass in-place compaction, streaming word tokenization, and delimiter handling.

---

## 1. How to Handle Multiple Spaces & In-Place Compaction in $\mathcal{O}(1)$ Space (C++ / Mutable Buffer)?

### 💡 3-Step In-Place Algorithm
1. **Space Compaction (Two Pointers)**:
   - Use `write = 0`, `read = 0`.
   - Skip leading spaces: `while (read < n && s[read] == ' ') read++;`
   - For each word, copy characters to `s[write++]`.
   - If there are subsequent words, insert a single space `' '` before copying the next word.
   - Resize string to `write`.
2. **Reverse the Entire Compacted String**:
   - `reverse(s.begin(), s.end());`
3. **Reverse Each Individual Word Back to Normal**:
   - Scan for space delimiters and reverse each word range `[start, end - 1]`.
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: strictly $\mathcal{O}(1)$.

---

## 2. What if Input is an Infinite Stream of Characters (Cannot Reverse Backward)?

### 🛑 The Scenario
Characters arrive one by one. You cannot buffer the entire 10GB text stream in memory to reverse it from the end.

### 💡 Disk / Block-Level Reversal (External Memory Stack)
- Stream words into an in-memory buffer.
- When buffer fills (e.g., 64 MB), write the chunk of words to a temporary spill file on disk.
- Push file references onto an external **LIFO Stack**.
- To output: Read chunks from the stack in reverse order, reversing words within each chunk during emission.
- **RAM Overhead**: $\mathcal{O}(B)$ buffer size regardless of stream size.

---

## 3. What if Word Order Must Stay the Same, but Characters in Each Word Reversed (LeetCode #557)?

### 💡 Single-Pass Token Reversal
- Iterate through the string; locate `start` and `end` of each word.
- Reverse each individual word in-place without reversing the whole string:
  ```cpp
  int start = 0;
  for (int i = 0; i <= s.size(); i++) {
      if (i == s.size() || s[i] == ' ') {
          reverse(s.begin() + start, s.begin() + i);
          start = i + 1;
      }
  }
  ```
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(1)$.

---

## 4. What if Punctuation and Special Delimiters Must Retain Their Positions?

### 🛑 Example
`"hello, world!"` $\to$ `"world, hello!"` (words swapped, punctuation `,` and `!` stay in place).

### 💡 Two-Pointer Word Swap with State Extraction
1. Extract word tokens and their corresponding bounding indices $[L_i, R_i]$.
2. Two pointers on word list: swap words between left and right tokens while leaving punctuation delimiters untouched in the underlying array.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Space Model | Strategy | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **LeetCode #151 (With Extra Spaces)** | Mutable `string` | Space Compact $\to$ Reverse All $\to$ Reverse Words | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **LeetCode #186 (Single Space In-Place)** | Mutable `char[]` | Reverse All $\to$ Reverse Words | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Reverse Characters in Words (#557)** | Mutable `string` | Reverse each word individually | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **External Huge Stream** | Unbounded stream | Chunked Disk Spill + LIFO Block Reader | $\mathcal{O}(N)$ I/O | $\mathcal{O}(B)$ buffer |
