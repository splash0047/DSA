# Problem Summary

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s` (same characters with identical frequencies), and `false` otherwise. We verify this in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space by incrementing character counts for `s` and decrementing for `t` in a 26-element frequency array.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You are checking for **character permutations** or anagrams.
- The input consists of characters from a fixed alphabet (e.g., lowercase English letters).
- You need to compare frequency distributions of two sequences.

---

## Important Clues

1. **"Anagram"**: Reordered characters with identical frequency counts.
2. **"Lowercase English letters"**: Signals that a fixed size 26 array can be used instead of a hash table.

---

## Example

### Input
`s = "anagram"`, `t = "nagaram"`

### Visual Step-by-Step Progression

```text
s: "anagram"   ->  a:3, n:1, g:1, r:1, m:1
t: "nagaram"   ->  a:3, n:1, g:1, r:1, m:1

Balance array:
counts['a'-'a'] = +3 - 3 = 0
counts['n'-'a'] = +1 - 1 = 0
counts['g'-'a'] = +1 - 1 = 0
...
All counts 0 -> Valid Anagram!
```

---

## Alternative Solutions

### Unicode Support via Hash Map
If strings contain arbitrary Unicode characters:
```cpp
class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        if (s.length() != t.length()) return false;
        std::unordered_map<char, int> counts;
        for (int i = 0; i < s.length(); ++i) {
            counts[s[i]]++;
            counts[t[i]]--;
        }
        for (auto& [ch, count] : counts) {
            if (count != 0) return false;
        }
        return true;
    }
};
```
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(K)$ where $K$ is number of unique Unicode characters.

---

## Edge Cases

1. **Different Lengths**: `s = "a"`, `t = "ab"` -> Returns `false` immediately.
2. **Single Character Match**: `s = "a"`, `t = "a"` -> Returns `true`.
3. **Single Character Mismatch**: `s = "a"`, `t = "b"` -> Returns `false`.

---

## Interview Tips

- **Check Lengths First**: Mention early that checking `s.length() != t.length()` provides an instant $\mathcal{O}(1)$ exit.
- **Address Unicode Follow-Up**: Proactively explain how to adapt the solution using `std::unordered_map<char, int>` or `std::unordered_map<wchar_t, int>` for Unicode strings.

---

## Similar Problems

1. [LeetCode #49: Group Anagrams](https://leetcode.com/problems/group-anagrams/)
2. [LeetCode #438: Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
3. [LeetCode #567: Permutation in String](https://leetcode.com/problems/permutation-in-string/)

---

## Revision Notes

- Problem: Check if string `t` is an anagram of `s`.
- Check `s.length() != t.length()` early.
- Maintain `int counts[26] = {0}`.
- Single loop: `counts[s[i] - 'a']++`, `counts[t[i] - 'a']--`.
- Check all 26 entries equal `0`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
- Unicode variant: Use `std::unordered_map<char, int>`.
