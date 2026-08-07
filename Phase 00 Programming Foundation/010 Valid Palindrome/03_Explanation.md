# Problem Summary

Given a string `s`, determine if it is a valid palindrome after ignoring case and skipping non-alphanumeric characters. Using a **Two Pointers (Left / Right)** strategy, we scan inward from both ends, skipping invalid characters and checking character equality in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You are checking symmetry or equality of sequences from both ends.
- Filtering or skipping invalid elements dynamically during traversal.
- Performing in-place string or array checks without extra memory.

---

## Important Clues

1. **"Converting all uppercase into lowercase"**: Case-insensitive comparison (`std::tolower`).
2. **"Removing all non-alphanumeric characters"**: Skip non-alphanumeric chars (`!std::isalnum`).
3. **"Reads the same forward and backward"**: Classic Two-Pointer convergence pattern.

---

## Example

### Input
`s = "A man, a plan, a canal: Panama"`

### Visual Step-by-Step Progression

```text
s = "A man, a plan, a canal: Panama"
     L                            R  -> 'a' == 'a'

s = "A man, a plan, a canal: Panama"
       L                        R    -> 'm' == 'm'

s = "A man, a plan, a canal: Panama"
        L                      R     -> 'a' == 'a'
...
Pointers meet in middle -> return true
```

---

## Alternative Solutions

### Regex Cleaning + Reverse
1. Filter string using regular expressions or `std::copy_if`.
2. Reverse string and compare.
3. **Time Complexity**: $\mathcal{O}(N)$.
4. **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **Empty String / Only Spaces**: `s = "   "` -> Returns `true`.
2. **No Alphanumeric Chars**: `s = ".,,"` -> Returns `true`.
3. **Single Character**: `s = "a"` -> Returns `true`.
4. **Even Length Palindrome**: `s = "abba"` -> Returns `true`.
5. **Odd Length Palindrome**: `s = "aba"` -> Returns `true`.

---

## Interview Tips

- **Highlight Safety against Out-of-Bounds**: Point out `while (left < right && !std::isalnum(...))` bounds protection for strings containing only punctuation.
- **Mention C++ `<cctype>` Caveat**: Mention `static_cast<unsigned char>` when invoking `std::isalnum` / `std::tolower` to demonstrate clean C++ standards knowledge.

---

## Similar Problems

1. [LeetCode #680: Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)
2. [LeetCode #234: Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
3. [LeetCode #9: Palindrome Number](https://leetcode.com/problems/palindrome-number/)

---

## Revision Notes

- Problem: Check valid palindrome ignoring case and non-alphanumeric chars.
- Strategy: Two Pointers (`left = 0`, `right = s.length() - 1`).
- `while (left < right)`:
  - Skip non-alphanumeric: `while (left < right && !isalnum(s[left])) left++`.
  - Skip non-alphanumeric: `while (left < right && !isalnum(s[right])) right--`.
  - Compare `tolower(s[left]) != tolower(s[right])` -> return `false`.
  - `left++`, `right--`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
