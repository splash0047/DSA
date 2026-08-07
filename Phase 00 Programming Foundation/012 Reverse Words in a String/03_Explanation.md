# Problem Summary

Given a string `s` containing words separated by spaces, reverse the order of the words while stripping leading, trailing, and multiple consecutive spaces. The optimal in-place solution reverses the entire string first, then reverses each individual word back, and cleans up spaces in-place in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to reverse token order (words) within a sequence without changing token character order.
- You are asked to handle string formatting (trimming whitespace) **in-place**.

---

## Important Clues

1. **"Reverse the order of words"**: Reversing whole string moves words to target positions.
2. **"Single space separating words, no extra spaces"**: In-place two-pointer space removal.

---

## Example

### Input
`s = "a good   example"`

### Visual Step-by-Step Progression

```text
Initial:        "a good   example"

1. Rev All:     "elpmaxe   doog a"

2. Process 1:   "example   doog a"
                 |_____| (word 1 reversed)

3. Process 2:   "example good   a"
                         |__| (word 2 reversed)

4. Process 3:   "example good a"
                              | (word 3 reversed)

Final Result:   "example good a"
```

---

## Alternative Solutions

### `std::stringstream` (Tokenization)
1. Read tokens into a vector of strings.
2. Reverse vector.
3. Join with spaces.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **Leading/Trailing Spaces**: `s = "  hello  "` -> Returns `"hello"`.
2. **Multiple Spaces Between Words**: `s = "a   b"` -> Returns `"b a"`.
3. **Single Word**: `s = "hello"` -> Returns `"hello"`.

---

## Interview Tips

- **Mention the 3-Step Strategy**: State clearly: *"1. Reverse whole string, 2. Reverse individual words, 3. Clean spaces in-place."*
- **Explain Space Cleaning**: Show how two pointers (`i` for reading, `write_idx` for writing) compact words and eliminate extra spaces.

---

## Similar Problems

1. [LeetCode #186: Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii/)
2. [LeetCode #557: Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/)

---

## Revision Notes

- Problem: Reverse word order in string, trim extra spaces.
- Strategy: In-place two-pass reversal.
- Step 1: `std::reverse(s.begin(), s.end())`.
- Step 2: Read with `i`, write with `write_idx`.
  - For each word, insert single space if `write_idx != 0`.
  - Copy word, then `std::reverse(s.begin() + start, s.begin() + write_idx)`.
- Step 3: `s.resize(write_idx)`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
