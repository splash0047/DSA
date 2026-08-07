# Problem Summary

Find the minimum number of operations (Insert, Delete, Replace) to convert `word1` into `word2`. The optimal approach uses **Levenshtein Distance 2D Grid DP (Space-Optimized 1D Double Buffering)**:
- Maintain two rows `prev` and `curr` of size $N + 1$.
- Base case: `prev[j] = j` for $0 \le j \le n$.
- Outer loop `i` from `1` to `m`:
  - `curr[0] = i;`
  - Inner loop `j` from `1` to `n`:
    - If `word1[i-1] == word2[j-1]`: `curr[j] = prev[j-1];`
    - Else: `curr[j] = 1 + min({prev[j], curr[j-1], prev[j-1]});`
  - `prev = curr;`
- Return `prev[n]`.
This computes Edit Distance in $\mathcal{O}(M \times N)$ time and $\mathcal{O}(\min(M, N))$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need the **minimum edit / transformation operations between two strings or sequences**.
- Levenshtein Edit Distance DP pattern.

---

## Important Clues

1. **"Minimum operations to convert word1 to word2"**: Edit Distance pattern.
2. **"Insert, Delete, Replace"**: 3-branch grid DP transitions.

---

## Example

### Input
`word1 = "horse"`, `word2 = "ros"`

### Visual Step-by-Step Progression

```text
       r  o  s
    0  1  2  3
h   1  1  2  3
o   2  2  1  2
r   3  2  2  2
s   4  3  3  2
e   5  4  3  3

Result: 3
```

---

## Alternative Solutions

### Full 2D Table DP ($\mathcal{O}(M \times N)$ Time, $\mathcal{O}(M \times N)$ Space)
- Maintain `dp[M+1][N+1]` table. Useful if reconstructing the exact sequence of edit operations.

---

## Edge Cases

1. **Empty string conversion**: `word1 = ""`, `word2 = "abc"` $\implies$ returns `3` (3 insertions).
2. **Identical strings**: `word1 = "abc"`, `word2 = "abc"` $\implies$ returns `0`.
3. **Single character difference**: `word1 = "a"`, `word2 = "b"` $\implies$ returns `1` (1 replacement).

---

## Interview Tips

- **Explain 3-Operation Transition Mapping**: State *"In Levenshtein Distance, `prev[j]` represents Deleting a character from `word1`, `curr[j-1]` represents Inserting a character into `word1`, and `prev[j-1]` represents Replacing a character. Taking $1 + \min(\text{Delete}, \text{Insert}, \text{Replace})$ ensures optimal edit choices at every cell."*

---

## Similar Problems

1. [LeetCode #1143: Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
2. [LeetCode #583: Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/)
3. [LeetCode #712: Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/)

---

## Revision Notes

- Problem: Min operations (Insert, Delete, Replace) to convert `word1` to `word2`.
- Pattern: Levenshtein Distance Grid DP.
- Match: `curr[j] = prev[j-1];`
- Mismatch: `curr[j] = 1 + min({prev[j], curr[j-1], prev[j-1]});`
- Operations: `prev[j]` = Delete, `curr[j-1]` = Insert, `prev[j-1]` = Replace.
- Optimal Complexity: Time $\mathcal{O}(M \cdot N)$, Space $\mathcal{O}(\min(M, N))$.
