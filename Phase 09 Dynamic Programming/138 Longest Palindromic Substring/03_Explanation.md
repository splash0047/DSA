# Problem Summary

Find the longest palindromic substring in a string `s`. The optimal approach uses **Expand Around Center**:
- A palindrome mirrors symmetrically around its center ($2N - 1$ possible centers).
- Loop `i` from `0` to `n - 1`:
  - Expand odd-length palindrome centered at `(i, i)`.
  - Expand even-length palindrome centered at `(i, i + 1)`.
- Track `start` index and `maxLen`. Return `s.substr(start, maxLen)`.
This computes the longest palindromic substring in $\mathcal{O}(N^2)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find **palindromic substrings / sub-sequences**.
- Expand Around Center / Interval DP pattern.

---

## Important Clues

1. **"Longest palindromic substring"**: Substring must be contiguous and symmetric.
2. **"O(N^2) time with O(1) space requirement"**: Expand around center.

---

## Example

### Input
`s = "babad"`

### Visual Step-by-Step Progression

```text
Center at index 1 ('a'):
  b [a] b a d
 <-  ^  ->
  s[0] == s[2] ('b' == 'b') -> Palindrome "bab" (length 3)

Result: "bab" (or "aba")
```

---

## Alternative Solutions

### 1. 2D Dynamic Programming ($\mathcal{O}(N^2)$ Time, $\mathcal{O}(N^2)$ Space)
- Maintain boolean table `dp[i][j]` storing if `s[i...j]` is a palindrome.

### 2. Manacher's Algorithm ($\mathcal{O}(N)$ Time, $\mathcal{O}(N)$ Space)
- Uses pre-calculated palindrome radius array to skip redundant comparisons, achieving true linear time.

---

## Edge Cases

1. **Single character**: `s = "a"` $\implies$ returns `"a"`.
2. **Even length palindrome**: `s = "cbbd"` $\implies$ returns `"bb"`.
3. **All identical characters**: `s = "aaaa"` $\implies$ returns `"aaaa"`.

---

## Interview Tips

- **Explain Why Center Expansion Beats 2D DP**: State *"While both 2D DP and Expand Around Center take $\mathcal{O}(N^2)$ time, Expand Around Center uses $\mathcal{O}(1)$ space compared to 2D DP's $\mathcal{O}(N^2)$ table space."*

---

## Similar Problems

1. [LeetCode #647: Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
2. [LeetCode #516: Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)
3. [LeetCode #214: Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/)

---

## Revision Notes

- Problem: Find longest palindromic substring in `s`.
- Pattern: Expand Around Center.
- Centers: `(i, i)` for odd length, `(i, i+1)` for even length.
- Expansion: `while (left >= 0 && right < n && s[left] == s[right]) { left--; right++; }`
- Range length: `len = right - left - 1`. `start = left + 1`.
- Optimal Complexity: Time $\mathcal{O}(N^2)$, Space $\mathcal{O}(1)$.
