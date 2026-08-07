# Problem Summary

Given two strings `s` and `t`, return the **minimum window substring** of `s` containing all characters of `t`. Using a **Variable-Size Sliding Window** with a 128-element character frequency array `target_count` and a `required` counter, we expand `right` until all target characters are satisfied (`required == 0`), then shrink `left` to minimize window length in $\mathcal{O}(M + N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the **shortest substring** containing a required collection of target elements.
- Expand / Shrink Sliding Window pattern applies.

---

## Important Clues

1. **"Minimum window substring"**: Shortest valid window.
2. **"Every character in t (including duplicates)"**: Exact character frequency matching.

---

## Example

### Input
`s = "ADOBECODEBANC"`, `t = "ABC"`

### Visual Step-by-Step Progression

```text
1. Expand right until valid:
   [ A  D  O  B  E  C ] O  D  E  B  A  N  C  -> "ADOBEC" (len 6)

2. Expand right & shrink left:
   A  D  O  B  E  C  O  D  E [ B  A  N  C ]  -> "BANC" (len 4 -> MIN!)

Result: "BANC"
```

---

## Alternative Solutions

### Filtered Sliding Window
- Pre-filter indices of characters in `s` that appear in `t`, creating a list of `{index, char}` pairs.
- Run sliding window on the filtered list.
- **Time Complexity**: $\mathcal{O}(M + N)$.
- **Space Complexity**: $\mathcal{O}(M)$ for filtered list.
- *Useful when $M \gg N$ and $s$ has very few characters matching $t$.*

---

## Edge Cases

1. **`t` Longer Than `s`**: `s = "a"`, `t = "aa"` -> Returns `""`.
2. **`s == t`**: `s = "a"`, `t = "a"` -> Returns `"a"`.
3. **No Valid Substring**: `s = "ADOBE"`, `t = "XYZ"` -> Returns `""`.

---

## Interview Tips

- **Explain Negative Counts**: Clarify *"When `target_count[c]` goes negative, it represents extra occurrences of character `c` in the current window beyond what `t` requires."*

---

## Similar Problems

1. [LeetCode #30: Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)
2. [LeetCode #567: Permutation in String](https://leetcode.com/problems/permutation-in-string/)

---

## Revision Notes

- Problem: Minimum substring in `s` covering all characters in `t`.
- Strategy: Sliding Window + `target_count[128]` + `required` counter.
- Populate `target_count[c]++` for $c \in t$, `required = t.length()`.
- Expand `right`:
  - `if (target_count[s[right]] > 0) required--`.
  - `target_count[s[right]]--`.
  - `while (required == 0)`:
    - Update `min_len = min(min_len, right - left + 1)`.
    - `target_count[s[left]]++`.
    - `if (target_count[s[left]] > 0) required++`.
    - `left++`.
- Optimal Complexity: Time $\mathcal{O}(M + N)$, Space $\mathcal{O}(1)$.
