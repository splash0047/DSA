# Problem Summary

Given an array of strings `strs`, find the longest common prefix shared by all strings. **Vertical Scanning** checks character column by column across all strings, returning `strs[0].substr(0, i)` at the very first column mismatch or string end. This takes $\mathcal{O}(S)$ time (where $S$ is total character count) and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find common leading elements across multiple sequences.
- Column-wise matrix traversal allows early termination.

---

## Important Clues

1. **"Common prefix"**: Characters must match starting from index 0.
2. **"Return empty string if no common prefix"**: Mismatch at index 0 returns `""`.

---

## Example

### Input
`strs = ["flower", "flow", "flight"]`

### Visual Step-by-Step Progression

```text
Col 0  Col 1  Col 2
  f      l      o    w  e  r
  f      l      o    w
  f      l      i    g  h  t
  |      |      |
  v      v      x (Mismatch: 'o' vs 'i')

Result: "fl" (Length 2)
```

---

## Alternative Solutions

### Sorting First
1. Sort the vector `strs` alphabetically in $\mathcal{O}(N \cdot L \log N)$ time (where $L$ is max string length).
2. The longest common prefix of the entire array must equal the common prefix between the **first string** `strs[0]` and **last string** `strs[N-1]`.
3. Compare characters of `strs[0]` and `strs[N-1]`.
- **Time Complexity**: $\mathcal{O}(N \cdot L \log N)$.
- **Space Complexity**: $\mathcal{O}(1)$ or $\mathcal{O}(\log N)$.

---

## Edge Cases

1. **Empty Vector**: `strs = []` -> Returns `""`.
2. **Single String**: `strs = ["a"]` -> Returns `"a"`.
3. **No Common Prefix**: `strs = ["dog", "racecar"]` -> Returns `""`.
4. **Empty String in Vector**: `strs = ["", "b"]` -> Returns `""`.

---

## Interview Tips

- **Compare Horizontal vs Vertical Scanning**: Explain why vertical scanning is preferred because it stops early if a mismatch is at index 0 of the last string.
- **Mention Trie Alternative**: Note that a Trie (Prefix Tree) could also solve this in $\mathcal{O}(S)$ time, but vertical scanning achieves the same bound with $\mathcal{O}(1)$ space instead of Trie node allocation.

---

## Similar Problems

1. [LeetCode #20: Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
2. [LeetCode #28: Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

---

## Revision Notes

- Problem: Longest common prefix across array of strings.
- Strategy: Vertical Scanning (Column by Column).
- Check `strs.empty()`.
- Loop column index `i` in `strs[0]`:
  - Loop string index `j` from 1 to $N-1$:
    - If `i >= strs[j].size() || strs[j][i] != strs[0][i]`: return `strs[0].substr(0, i)`.
- Optimal Complexity: Time $\mathcal{O}(S)$, Space $\mathcal{O}(1)$.
- Sorting Alternative: Compare `strs[0]` and `strs[N-1]` after sorting.
