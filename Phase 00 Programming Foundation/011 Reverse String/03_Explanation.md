# Problem Summary

Given a vector of characters `s`, reverse it in-place using $\mathcal{O}(1)$ auxiliary space. We accomplish this in $\mathcal{O}(N)$ time using two pointers (`left = 0`, `right = s.size() - 1`) swapping symmetric pairs of elements until they meet at the center.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to reverse an array, string, or range in-place.
- Two pointers move symmetrically inward from outer boundaries towards center.

---

## Important Clues

1. **"In-place with O(1) extra memory"**: Rejects extra buffer array allocation.
2. **"Modify input array directly"**: Return type is `void`.

---

## Example

### Input
`s = ["h", "e", "l", "l", "o"]`

### Visual Step-by-Step Progression

```text
L -> [ 'h' ,  'e' ,  'l' ,  'l' ,  'o' ] <- R   (swap 'h' and 'o')
       'o'    'e'    'l'    'l'    'h'

       [ 'o' ,  'e' ,  'l' ,  'l' ,  'h' ]
                 L             R                (swap 'e' and 'l')
                 'l'           'e'

Final: [ 'o' ,  'l' ,  'l' ,  'e' ,  'h' ]
```

---

## Alternative Solutions

### Recursive Approach
- Swap `s[left]` and `s[right]`, then recurse on `reverse(s, left + 1, right - 1)`.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$ due to recursion call stack.

---

## Edge Cases

1. **Empty Vector**: `s = []` -> No-op.
2. **Single Character**: `s = ["a"]` -> No-op.
3. **Even Length Vector**: `s = ["a", "b"]` -> Swaps once.
4. **Odd Length Vector**: `s = ["a", "b", "c"]` -> Center element remains untouched.

---

## Interview Tips

- **Mention STL Equivalent**: State *"While `std::reverse(s.begin(), s.end())` achieves this in one line, I will implement the two-pointer swap logic explicitly."*

---

## Similar Problems

1. [LeetCode #345: Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/)
2. [LeetCode #541: Reverse String II](https://leetcode.com/problems/reverse-string-ii/)
3. [LeetCode #151: Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)

---

## Revision Notes

- Problem: Reverse character vector in-place.
- Strategy: Two Pointers (`left = 0`, `right = s.size() - 1`).
- Loop `while (left < right)`: `std::swap(s[left++], s[right--])`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
- C++ STL equivalent: `std::reverse(s.begin(), s.end())`.
