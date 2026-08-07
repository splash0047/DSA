# Problem Summary

Find the length of the longest common subsequence (LCS) between two strings `text1` and `text2`. The optimal approach uses **Space-Optimized 2D DP (1D Double Buffering)**:
- Maintain two rows `prev` and `curr` of size $N + 1$.
- Outer loop `i` from `1` to `m`, inner loop `j` from `1` to `n`:
  - If `text1[i-1] == text2[j-1]`: `curr[j] = 1 + prev[j-1];` (match $\implies 1 + \text{diagonal}$).
  - Else: `curr[j] = max(prev[j], curr[j-1]);` (mismatch $\implies \max(\text{top}, \text{left})$).
  - `prev = curr;`
- Return `prev[n]`.
This evaluates LCS in $\mathcal{O}(M \times N)$ time and $\mathcal{O}(\min(M, N))$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need the **longest common subsequence / edit distance between two strings**.
- 2D Sequence Alignment DP pattern.

---

## Important Clues

1. **"Longest common subsequence of two strings"**: Classic 2D Grid DP.
2. **"Non-contiguous match allowed"**: Subsequence (not substring).

---

## Example

### Input
`text1 = "abcde"`, `text2 = "ace"`

### Visual Step-by-Step Progression

```text
       a  c  e
    0  0  0  0
a   0  1  1  1
b   0  1  1  1
c   0  1  2  2
d   0  1  2  2
e   0  1  2  3

Result: 3 ("ace")
```

---

## Alternative Solutions

### Full 2D DP Table ($\mathcal{O}(M \times N)$ Time, $\mathcal{O}(M \times N)$ Space)
- Maintain `dp[M+1][N+1]` table. Useful if reconstructing the actual LCS string.

---

## Edge Cases

1. **No common characters**: `text1 = "abc"`, `text2 = "def"` $\implies$ returns `0`.
2. **Identical strings**: `text1 = "abc"`, `text2 = "abc"` $\implies$ returns `3`.
3. **Single character match**: Returns `1`.

---

## Interview Tips

- **Explain Match vs Mismatch Transition**: State *"If `text1[i-1] == text2[j-1]`, both characters contribute 1 to the LCS, reducing subproblem to $1 + dp[i-1][j-1]$. If they mismatch, the LCS is the max between excluding character from `text1` ($dp[i-1][j]$) or excluding character from `text2` ($dp[i][j-1]$)."*

---

## Similar Problems

1. [LeetCode #516: Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)
2. [LeetCode #72: Edit Distance](https://leetcode.com/problems/edit-distance/)
3. [LeetCode #1092: Shortest Common Supersequence](https://leetcode.com/problems/shortest-common-supersequence/)

---

## Revision Notes

- Problem: Length of longest common subsequence between `text1` and `text2`.
- Pattern: 2D Sequence Alignment DP.
- Match: `curr[j] = 1 + prev[j-1];`
- Mismatch: `curr[j] = max(prev[j], curr[j-1]);`
- Space Optimization: Use two 1D rows `prev` and `curr`.
- Optimal Complexity: Time $\mathcal{O}(M \cdot N)$, Space $\mathcal{O}(\min(M, N))$.
