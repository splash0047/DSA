# Problem Summary

Given two strings `s1` and `s2`, return `true` if `s2` contains any permutation of `s1` as a contiguous substring. The optimal solution uses a **Fixed-Size Sliding Window** of size `s1.length()` with a 26-element character frequency difference array `count`. As the window slides through `s2`, character counts are updated in $\mathcal{O}(1)$ time, returning `true` whenever all 26 entries reach 0 in $\mathcal{O}(L_2)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to search for an **anagram / permutation** of a string inside a larger text.
- Fixed-Size Sliding Window with frequency matching applies directly.

---

## Important Clues

1. **"Permutation of s1 is substring of s2"**: Substring must have length `s1.length()` and matching character frequencies.
2. **"Lowercase English letters"**: Signals 26-element array usage.

---

## Example

### Input
`s1 = "ab"`, `s2 = "eidbaooo"`

### Visual Step-by-Step Progression

```text
s1: "ab" (length 2)

s2:  e  i  d [ b  a ] o  o  o
             |______|
          Window "ba" has 1 'a' and 1 'b' -> Matches s1!

Result: true
```

---

## Alternative Solutions

### Match Counter Optimization
- Instead of checking `isZero()` across 26 elements at every step, maintain a `matches` count (number of characters whose frequency diff is currently 0).
- Update `matches` during window sliding in $\mathcal{O}(1)$ time.
- **Time Complexity**: $\mathcal{O}(L_2)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **`s1` Longer Than `s2`**: `s1 = "abc"`, `s2 = "ab"` -> Returns `false` immediately.
2. **`s1 == s2`**: `s1 = "a"`, `s2 = "a"` -> Returns `true`.
3. **No Matching Permutation**: `s1 = "ab"`, `s2 = "eidboaoo"` -> Returns `false`.

---

## Interview Tips

- **Explain Why Substring Length is Fixed**: State *"A permutation of `s1` must contain all characters of `s1`, so its length MUST equal `s1.length()`. This allows us to fix our sliding window size to `s1.length()`."*

---

## Similar Problems

1. [LeetCode #438: Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
2. [LeetCode #76: Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

---

## Revision Notes

- Problem: Check if `s2` contains a permutation of `s1`.
- Strategy: Fixed-Size Sliding Window of size `len1`.
- `if (len1 > len2) return false`.
- Maintain `count[26] = {0}` tracking character differences.
- Init window `0..len1-1`: `count[s1[i]]++`, `count[s2[i]]--`.
- Slide `i` from `len1` to `len2-1`:
  - `count[s2[i]]--` (add incoming).
  - `count[s2[i - len1]]++` (remove outgoing).
  - If `isZero(count)` return `true`.
- Optimal Complexity: Time $\mathcal{O}(L_2)$, Space $\mathcal{O}(1)$.
