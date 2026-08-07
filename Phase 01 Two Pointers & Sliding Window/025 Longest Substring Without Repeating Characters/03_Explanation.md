# Problem Summary

Given a string `s`, find the length of the longest contiguous substring containing only distinct characters. The optimal approach uses a **Variable-Size Sliding Window** with a 256-element direct access table (`last_seen`). As the `right` pointer expands the window, if `s[right]` was previously seen inside the active window (`last_seen[c] >= left`), the `left` pointer instantly jumps to `last_seen[c] + 1`, achieving $\mathcal{O}(N)$ single-pass time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the **longest contiguous substring** satisfying a uniqueness condition.
- Using a Hash Table / Lookup Array to store last seen indices allows $\mathcal{O}(1)$ window boundary jumps.

---

## Important Clues

1. **"Longest substring"**: Must be contiguous.
2. **"Without repeating characters"**: Uniqueness constraint inside sliding window.

---

## Example

### Input
`s = "abcabcbb"`

### Visual Step-by-Step Progression

```text
Window: [ a  b  c ] a  b  c  b  b   -> max_len = 3
          L        R

Window:   a [ b  c  a ] b  c  b  b   -> next 'a' saw duplicate at 0! Jump L to 1. max_len = 3
             L        R

Window:   a  b [ c  a  b ] c  b  b   -> next 'b' saw duplicate at 1! Jump L to 2. max_len = 3
                L        R

Max Length: 3 ("abc")
```

---

## Alternative Solutions

### Sliding Window with Set & Shrink Loop
- Expand `right`. If `s[right]` is in `set`, increment `left` and erase `s[left]` until `s[right]` is unique.
- **Time Complexity**: $\mathcal{O}(N)$ (Each element visited at most twice).
- **Space Complexity**: $\mathcal{O}(\min(N, M))$.

---

## Edge Cases

1. **Empty String**: `s = ""` -> Returns `0`.
2. **All Identical Characters**: `s = "bbbbb"` -> Returns `1`.
3. **All Unique Characters**: `s = "abcdef"` -> Returns `6`.
4. **Spaces & Symbols**: `s = "a b c a"` -> ASCII array size 256 handles spaces and symbols seamlessly.

---

## Interview Tips

- **Explain `last_seen[c] >= left` Guard**: Crucial detail! Explain *"We only jump `left` if the previously recorded index of `c` lies WITHIN our current active window."*
- **Highlight ASCII Table Optimization**: Mention using a fixed size 256 array instead of `std::unordered_map` for zero heap overhead.

---

## Similar Problems

1. [LeetCode #159: Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)
2. [LeetCode #340: Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)
3. [LeetCode #992: Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)

---

## Revision Notes

- Problem: Longest substring with no repeating characters.
- Strategy: Sliding Window + `last_seen[256]` initialized to `-1`.
- `left = 0`, `max_len = 0`.
- Loop `right` from `0` to `N - 1`:
  - `if (last_seen[c] >= left) left = last_seen[c] + 1`.
  - `last_seen[c] = right`.
  - `max_len = max(max_len, right - left + 1)`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
