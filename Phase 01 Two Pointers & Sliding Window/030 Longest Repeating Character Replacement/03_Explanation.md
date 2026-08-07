# Problem Summary

Given a string `s` and an integer `k`, find the length of the longest substring containing identical characters after performing at most `k` character replacements. Using a **Variable-Size Sliding Window**, we track `max_freq` (the frequency of the most frequent character in the current window). If `(window_len - max_freq) > k`, we shrink `left`, completing in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You are allowed at most $K$ operations/replacements to form a contiguous uniform subarray.
- Sliding Window condition $f(\text{window}) \le K$ applies.

---

## Important Clues

1. **"At most k character replacements"**: $K$ allowed modifications.
2. **"Longest substring containing same letter"**: Maximize valid window length.

---

## Example

### Input
`s = "AABABBA"`, `k = 1`

### Visual Step-by-Step Progression

```text
Window 1: [ A  A  B  A ] B  B  A   -> len = 4, max_freq(A) = 3
                                      replacements = 4 - 3 = 1 <= 1 (Valid! len = 4)

Window 2:   A [ A  B  A  B ] B  A   -> len = 4, max_freq(A) = 2
                                      replacements = 4 - 2 = 2 > 1 (Shrink left)

Max Valid Length: 4 ("AAAA" after replacing 1 B)
```

---

## Alternative Solutions

### Binary Search on Window Length
- Binary search for window length $L \in [1, N]$.
- Check if any valid window of size $L$ exists using sliding window of size $L$.
- **Time Complexity**: $\mathcal{O}(N \log N)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **$k = 0$**: Equivalent to finding longest consecutive identical character substring.
2. **$k \ge N$**: Entire string can be made identical $\rightarrow$ Returns $N$.
3. **All Same Characters**: `s = "AAAA"`, `k = 2` -> Returns $N$.

---

## Interview Tips

- **Explain Why `max_freq` Doesn't Decrease on Shrinking**: Be ready to state *"We only care about finding a window LARGER than our previous best. A smaller `max_freq` cannot yield a new maximum length, so `max_freq` does not need to be updated downward when `left` advances."*

---

## Similar Problems

1. [LeetCode #1004: Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)
2. [LeetCode #2024: Maximize the Confusion of an Exam](https://leetcode.com/problemsize-the-confusion-of-an-exam/)

---

## Revision Notes

- Problem: Longest substring of same letter with $\le k$ replacements.
- Strategy: Variable Sliding Window (`count[26]`, `max_freq`).
- Loop `right` from `0` to `N - 1`:
  - `count[s[right]]++`.
  - `max_freq = max(max_freq, count[s[right]])`.
  - `while ((right - left + 1) - max_freq > k)`: `count[s[left]]--`, `left++`.
  - `max_len = max(max_len, right - left + 1)`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
