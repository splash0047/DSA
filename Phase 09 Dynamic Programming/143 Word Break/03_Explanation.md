# Problem Summary

Determine if string `s` can be segmented into a sequence of dictionary words from `wordDict`. The optimal approach uses **1D Substring Partitioning DP**:
- Store dictionary in `unordered_set<string> wordSet`.
- `dp[i]` indicates if prefix `s[0...i-1]` is validly segmentable. Base case `dp[0] = true`.
- For `i` from `1` to `n`, for `j` from `0` to `i-1`:
  - `if (dp[j] && wordSet.count(s.substr(j, i - j))) { dp[i] = true; break; }`
- Return `dp[n]`.
This checks string segmentation in $\mathcal{O}(N^2 \cdot L)$ time and $\mathcal{O}(N + W)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to determine if a **string can be partitioned into valid substrings from a dictionary**.
- 1D Substring Partitioning DP pattern.

---

## Important Clues

1. **"Segmented into space-separated sequence of dictionary words"**: Substring partition DP.
2. **"Words can be reused multiple times"**: Unbounded dictionary word matching.

---

## Example

### Input
`s = "leetcode"`, `wordDict = ["leet", "code"]`

### Visual Step-by-Step Progression

```text
s = "l e e t c o d e"
dp: T F F F T F F F T
    ^       ^       ^
   [0]     [4]     [8]

- dp[0] = T (empty)
- dp[4] = T ("leet" matches, dp[0]=T)
- dp[8] = T ("code" matches, dp[4]=T)

Result: true
```

---

## Alternative Solutions

### Top-Down Memoization Recursion ($\mathcal{O}(N^2 \cdot L)$ Time, $\mathcal{O}(N + W)$ Space)
- Recurse with `memo[start]` boolean array storing whether suffix from `start` can be segmented.

---

## Edge Cases

1. **Entire string is single dictionary word**: `s = "apple"`, `wordDict = ["apple"]` $\implies$ returns `true`.
2. **Single character mismatch**: `s = "catsandog"`, `wordDict = ["cats", "dog", "sand", "and", "cat"]` $\implies$ returns `false`.
3. **Repeated words**: `s = "aaaaaaa"`, `wordDict = ["aaaa", "aaa"]` $\implies$ returns `true`.

---

## Interview Tips

- **Explain Substring Split Condition**: State *"Prefix `s[0...i-1]` is valid if we can find ANY split point `j` such that the prefix up to `j` (`dp[j]`) is valid, AND the remaining substring `s[j...i-1]` exists in `wordDict`."*

---

## Similar Problems

1. [LeetCode #140: Word Break II](https://leetcode.com/problems/word-break-ii/)
2. [LeetCode #472: Concatenated Words](https://leetcode.com/problems/concatenated-words/)
3. [LeetCode #139: Extra Characters in a String](https://leetcode.com/problems/extra-characters-in-a-string/)

---

## Revision Notes

- Problem: Can string `s` be segmented into dictionary words?
- Pattern: 1D Substring Partitioning DP.
- Table: `vector<bool> dp(n + 1, false); dp[0] = true;`
- Transition: `for (i = 1..n) for (j = 0..i-1) if (dp[j] && wordSet.count(s.substr(j, i-j))) { dp[i] = true; break; }`
- Optimal Complexity: Time $\mathcal{O}(N^2 \cdot L)$, Space $\mathcal{O}(N + W)$.
