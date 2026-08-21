# 04 Interview Follow-ups & System Variations: Valid Palindrome

The standard problem checks if a string is a palindrome after removing non-alphanumeric characters and ignoring cases. The two-pointer approach (`left` and `right`) solves this in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem branches into error tolerance (deleting $1$ or $K$ characters), linked list palindrome detection without memory overhead, streaming forward-reverse rolling hashes, and Unicode normalization.

---

## 1. What if You Can Delete at Most One Character (Valid Palindrome II / LeetCode #680)?

### 💡 Branching Two-Pointer Technique
- Use standard two pointers `left = 0`, `right = n - 1`.
- When a mismatch occurs (`s[left] != s[right]`):
  - Check if the substring `s[left + 1 ... right]` is a palindrome **OR** `s[left ... right - 1]` is a palindrome.
  - If either is true, return `true`. Otherwise return `false`.
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(1)$ (only at most one branch split).

---

## 2. What if You Can Delete at Most $K$ Characters (Valid Palindrome III / LeetCode #1216)?

### 💡 Reduction to Longest Palindromic Subsequence (LPS)
- A string $S$ of length $N$ can become a palindrome with at most $K$ deletions if and only if its Longest Palindromic Subsequence has length:
  $$\text{LPS}(S) \ge N - K$$
- $\text{LPS}(S)$ equals the Longest Common Subsequence ($\text{LCS}$) between $S$ and $\text{reverse}(S)$.
- Using DP with space optimization:
  - **Time Complexity**: $\mathcal{O}(N^2)$ (or $\mathcal{O}(N \cdot K)$ with banded DP), **Space Complexity**: $\mathcal{O}(N)$.

---

## 3. What if the Input is a Singly Linked List (LeetCode #234)?

### 🛑 Constraints
Must achieve $\mathcal{O}(N)$ time and strictly $\mathcal{O}(1)$ auxiliary space without extra node arrays.

### 💡 4-Step In-Place Algorithm
1. **Find Middle**: Fast and slow pointers (`slow` moves 1 step, `fast` moves 2 steps).
2. **Reverse Second Half**: In-place reverse the linked list starting from `slow->next`.
3. **Compare**: Move pointer from `head` and pointer from `reversed_head` in lockstep.
4. **Restore (Good Engineering Practice)**: Re-reverse the second half back to original shape before returning.
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(1)$.

---

## 4. What if the String is an Infinite One-Way Stream (Cannot Seek Backwards)?

### 🛑 The Challenge
We can only read characters sequentially from left to right ($s[0], s[1], \dots, s[n-1]$). We cannot place a pointer at the end.

### 💡 Forward & Backward Rolling Hashing (Rabin-Karp Style)
Maintain two polynomial rolling hashes as characters $c$ arrive:
1. **Forward Hash**:
   $$H_{\text{forward}} = (H_{\text{forward}} \times B + c) \pmod M$$
2. **Backward Hash**:
   $$H_{\text{backward}} = (H_{\text{backward}} + c \times B^i) \pmod M$$
- At the end of the stream, if $H_{\text{forward}} == H_{\text{backward}}$, the string is a palindrome with high probability.
- Use **Double Hashing** (two coprime moduli $M_1, M_2$) to make collision probability negligible ($< 10^{-18}$).
- **Time Complexity**: $\mathcal{O}(N)$ single sequential pass, **Space Complexity**: $\mathcal{O}(1)$.

---

## 5. Unicode Case Folding Pitfalls

### 🛑 Real-World Gotcha
In Unicode, case conversion is not always 1-to-1:
- German lowercase `"ß"` capitalizes to `"SS"` (length changes from 1 to 2).
- Turkish `"I"` lowercases to dotless `"ı"` (`\u0131`), whereas `"i"` uppercases to `"İ"` (`\u0130`).
- Always clarify with the interviewer whether standard ASCII `tolower()` is assumed or if ICU Unicode Case Folding (NFKD) is expected.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Core Strategy | Time | Space |
| :--- | :--- | :--- | :--- |
| **Standard String** | Two Pointers from ends | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **At Most 1 Deletion** | Two Pointers + 1 Mismatch Branch | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **At Most $K$ Deletions** | LPS Dynamic Programming | $\mathcal{O}(N \cdot K)$ | $\mathcal{O}(N)$ |
| **Singly Linked List** | Slow/Fast + Reverse 2nd half | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **One-Way Stream** | Forward & Backward Rolling Hash | $\mathcal{O}(N)$ single pass | $\mathcal{O}(1)$ |
