# Problem Summary

Return the total number of palindromic substrings in string `s`. The optimal approach uses **Expand Around Center**:
- A string of length $N$ has $2N - 1$ possible centers.
- Loop `i` from `0` to `n - 1`:
  - `total += expand(i, i)` (Odd-length centers).
  - `total += expand(i, i + 1)` (Even-length centers).
- `expand(left, right)` increments count every time `s[left] == s[right]` matches while stepping outward (`left--`, `right++`).
This counts all palindromic substrings in $\mathcal{O}(N^2)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **count all valid palindromic substrings**.
- Center Expansion Counting pattern.

---

## Important Clues

1. **"Number of palindromic substrings"**: Substrings must be contiguous and palindromic.
2. **"Different indices count as different substrings"**: Every matching center expansion step is 1 valid substring.

---

## Example

### Input
`s = "aaa"`

### Visual Step-by-Step Progression

```text
Indices: 0('a'), 1('a'), 2('a')

Single character centers (3):
- "a" at index 0
- "a" at index 1
- "a" at index 2

Pair centers (2):
- "aa" at (0,1)
- "aa" at (1,2)

Triple center (1):
- "aaa" at (0,2)

Total = 3 + 2 + 1 = 6
```

---

## Alternative Solutions

### 1. 2D Dynamic Programming ($\mathcal{O}(N^2)$ Time, $\mathcal{O}(N^2)$ Space)
- Maintain `dp[i][j]` storing if `s[i...j]` is a palindrome.

### 2. Manacher's Algorithm ($\mathcal{O}(N)$ Time, $\mathcal{O}(N)$ Space)
- Computes palindrome radius array in linear time.

---

## Edge Cases

1. **Single character**: `s = "a"` $\implies$ returns `1`.
2. **All distinct characters**: `s = "abc"` $\implies$ returns `3` (each single char is a palindrome).
3. **All identical characters**: `s = "aaaa"` $\implies$ returns `10`.

---

## Interview Tips

- **Explain Why Each Step Adds 1**: State *"Each successful step outward where `s[left] == s[right]` forms a NEW, longer valid palindrome substring `s[left...right]`, so incrementing `count` by 1 per step counts all valid palindromic substrings accurately."*

---

## Similar Problems

1. [LeetCode #5: Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
2. [LeetCode #516: Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)
3. [LeetCode #132: Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/)

---

## Revision Notes

- Problem: Count total number of palindromic substrings in `s`.
- Pattern: Expand Around Center.
- Centers: `(i, i)` and `(i, i+1)`.
- Expansion logic: `while (left >= 0 && right < n && s[left] == s[right]) { count++; left--; right++; }`
- Total: Sum counts from all $2N - 1$ centers.
- Optimal Complexity: Time $\mathcal{O}(N^2)$, Space $\mathcal{O}(1)$.
