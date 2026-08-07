# Problem Summary

Given a binary array `nums` and an integer `k`, find the maximum consecutive 1s achievable by flipping at most `k` zeroes. This is equivalent to finding the **longest subarray containing at most `k` zeroes**. Using a **Variable-Size Sliding Window**, we expand `right` and track `zero_count`. When `zero_count > k`, we shrink `left` in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You are allowed at most $K$ element flips/modifications to create a contiguous uniform binary array.
- Variable Sliding Window (`zero_count <= k`) pattern applies.

---

## Important Clues

1. **"Flip at most k zeroes"**: $K$ allowed 0-to-1 flips.
2. **"Maximum consecutive 1s"**: Maximize valid window length.

---

## Example

### Input
`nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]`, `k = 2`

### Visual Step-by-Step Progression

```text
Window: [ 1 , 1 , 1 , 0 , 0 ] 0 , 1 , 1 , 1 , 1 , 0   -> 2 zeroes (Valid, len 5)

Window:   1 , 1 , 1 [ 0 , 0 , 1 , 1 , 1 , 1 ] 0       -> 2 zeroes (Valid, len 6 -> MAX!)

Max Consecutive 1s: 6
```

---

## Alternative Solutions

### Non-Shrinking Sliding Window (O(N) Time, O(1) Space)
- Expand `right`. If `zero_count > k`, advance `left` by 1 step (without `while` loop), keeping the window size fixed at the maximum valid length found so far.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **$k = 0$**: Equivalent to finding longest consecutive 1s without flips.
2. **Array All Zeroes**: Returns `min(k, N)`.
3. **Array All Ones**: Returns $N$.

---

## Interview Tips

- **Reframe Problem Statement**: Start by saying *"Flipping at most k zeroes is mathematically identical to finding the longest subarray containing at most k zeroes."*

---

## Similar Problems

1. [LeetCode #485: Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/)
2. [LeetCode #487: Max Consecutive Ones II](https://leetcode.com/problems/max-consecutive-ones-ii/)
3. [LeetCode #424: Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

---

## Revision Notes

- Problem: Longest subarray of consecutive 1s with $\le k$ zeroes flipped.
- Strategy: Variable Sliding Window (`zero_count`).
- `left = 0`, `zero_count = 0`, `max_len = 0`.
- Loop `right` from `0` to `N - 1`:
  - `if (nums[right] == 0) zero_count++`.
  - `while (zero_count > k)`:
    - `if (nums[left] == 0) zero_count--`.
    - `left++`.
  - `max_len = max(max_len, right - left + 1)`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
