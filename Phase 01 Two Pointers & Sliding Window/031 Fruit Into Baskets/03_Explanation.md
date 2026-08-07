# Problem Summary

Given an array `fruits` representing a row of fruit trees, find the maximum number of fruits you can collect using 2 baskets (where each basket holds only 1 type of fruit). This is equivalent to finding the **longest subarray containing at most 2 distinct integers**. Using a **Variable-Size Sliding Window** with a frequency map `basket`, we expand `right` and shrink `left` when `basket.size() > 2` in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the longest contiguous subarray containing **at most K distinct elements** ($K = 2$).
- Variable Sliding Window with map key tracking applies directly.

---

## Important Clues

1. **"Two baskets, each holding single type of fruit"**: Max 2 distinct fruit types ($K = 2$).
2. **"Pick from every tree while moving right"**: Must be a contiguous subarray.

---

## Example

### Input
`fruits = [1, 2, 3, 2, 2]`

### Visual Step-by-Step Progression

```text
Window 1: [ 1 , 2 ] 3 , 2 , 2   -> basket {1:1, 2:1} size=2 (len=2)

Window 2:   1 [ 2 , 3 ] 2 , 2   -> 3 added! size=3 > 2 -> erase 1!

Window 3:   1 , 1 [ 2 , 3 , 2 , 2 ] -> basket {2:3, 3:1} size=2 (len=4 -> MAX!)

Max Fruits Collected: 4
```

---

## Alternative Solutions

### Non-Shrinking Sliding Window (O(N) Time, O(1) Space)
- Expand `right` pointer. If `basket.size() > 2`, shrink `left` by 1 step (without `while` loop), keeping window size fixed at current max length.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **Array Size $\le 2$**: `fruits = [1, 2]` -> Returns `2`.
2. **All Identical Fruits**: `fruits = [1, 1, 1]` -> Returns `3`.
3. **Alternating 2 Fruits**: `fruits = [1, 2, 1, 2]` -> Returns `4`.

---

## Interview Tips

- **Reframe the Problem**: Start by stating *"Fruit Into Baskets is identical to finding the Longest Subarray with at Most 2 Distinct Elements."*

---

## Similar Problems

1. [LeetCode #159: Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)
2. [LeetCode #340: Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)

---

## Revision Notes

- Problem: Longest subarray with $\le 2$ distinct fruit types.
- Strategy: Variable Sliding Window (`basket` hash map).
- Loop `right` from `0` to `N - 1`:
  - `basket[fruits[right]]++`.
  - `while (basket.size() > 2)`:
    - `basket[fruits[left]]--`.
    - `if (basket[fruits[left]] == 0) basket.erase(fruits[left])`.
    - `left++`.
  - `max_len = max(max_len, right - left + 1)`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
