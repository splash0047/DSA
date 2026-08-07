# Problem Summary

Given two strings `s` and `p`, return an array of all start indices of `p`'s anagrams in `s`. The optimal approach uses a **Fixed-Size Sliding Window** of size `p.length()` with two 26-element character frequency vectors (`p_freq` and `window_freq`). Updating frequency vectors in $\mathcal{O}(1)$ as the window slides through `s` finds all anagram start indices in $\mathcal{O}(S)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find **all starting indices of anagram matches** inside a larger text string.
- Fixed-Size Sliding Window with frequency vector comparison applies directly.

---

## Important Clues

1. **"Return all start indices of p's anagrams"**: Multi-match anagram search.
2. **"Anagram"**: Substring length equals `p.length()` with identical frequency distribution.

---

## Example

### Input
`s = "cbaebabacd"`, `p = "abc"`

### Visual Step-by-Step Progression

```text
s = [ c  b  a ] e  b  a  b  a  c  d  -> window "cba" matches! Start index = 0
      |_______|

s =  c  b  a  e  b  a [ b  a  c ] d  -> window "bac" matches! Start index = 6
                      |_______|

Result: [0, 6]
```

---

## Alternative Solutions

### Single Match Counter Optimization
- Instead of comparing 26-element vectors, maintain a `count` variable tracking how many character frequencies match `p`.
- **Time Complexity**: $\mathcal{O}(S)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **`s` Shorter Than `p`**: `s = "a"`, `p = "ab"` -> Returns `[]`.
2. **`s` and `p` Equal Length**: `s = "ab"`, `p = "ba"` -> Returns `[0]`.
3. **Overlapping Anagram Matches**: `s = "abab"`, `p = "ab"` -> Returns `[0, 1, 2]`.

---

## Interview Tips

- **Mention Vector Equality in C++**: Point out *"In C++, `std::vector<int> == std::vector<int>` compares elements directly. Since vectors are size 26, equality check takes constant $\mathcal{O}(26) = \mathcal{O}(1)$ time."*

---

## Similar Problems

1. [LeetCode #567: Permutation in String](https://leetcode.com/problems/permutation-in-string/)
2. [LeetCode #3: Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

## Revision Notes

- Problem: Find all starting indices of `p`'s anagrams in `s`.
- Strategy: Fixed-Size Sliding Window of size `p.length()`.
- `if (s_len < p_len) return {}`.
- Maintain `p_freq(26)` and `window_freq(26)`.
- Fill initial window `0..p_len-1`.
- Slide `i` from `p_len` to `s_len-1`:
  - `window_freq[s[i]]++` (incoming).
  - `window_freq[s[i - p_len]]--` (outgoing).
  - `if (p_freq == window_freq) result.push_back(i - p_len + 1)`.
- Optimal Complexity: Time $\mathcal{O}(S)$, Space $\mathcal{O}(1)$.
