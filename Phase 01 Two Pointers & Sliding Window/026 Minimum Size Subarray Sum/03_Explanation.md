# Problem Summary

Given an array of positive integers `nums` and a `target`, find the **minimal length** of a contiguous subarray whose sum is $\ge \text{target}$. Using a **Variable-Size Sliding Window**, we expand `right` until `sum >= target`, then shrink `left` while updating `min_len`. This completes in $\mathcal{O}(N)$ linear time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the **shortest contiguous subarray** satisfying a sum or condition on an array of **positive numbers**.
- Variable-Size Sliding Window (Expand / Shrink) pattern applies directly.

---

## Important Clues

1. **"Minimal length of subarray"**: Finding shortest valid window.
2. **"Array of positive integers"**: Guarantees sum increases when expanding `right` and decreases when shrinking `left`.

---

## Example

### Input
`target = 7`, `nums = [2, 3, 1, 2, 4, 3]`

### Visual Step-by-Step Progression

```text
Window 1: [ 2 , 3 , 1 , 2 ]  4 , 3   -> sum = 8 >= 7 (len = 4)
            L           R

Window 2:   2 [ 3 , 1 , 2 , 4 ]  3   -> sum = 10 >= 7 -> shrink L to [1, 2, 4] sum = 7 >= 7 (len = 3)
                L           R

Window 3:   2 , 3 , 1 , 2 [ 4 , 3 ] -> sum = 9 >= 7 -> shrink L to [4, 3] sum = 7 >= 7 (len = 2 -> MIN!)
                            L   R

Min Subarray Length: 2 ([4, 3])
```

---

## Alternative Solutions

### Binary Search on Prefix Sums (O(N log N) Time, O(N) Space)
- Construct prefix sum array `P`.
- For each `P[i]`, binary search for index `j` where `P[j] - P[i] >= target`.
- **Time Complexity**: $\mathcal{O}(N \log N)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **Total Array Sum < Target**: `target = 11`, `nums = [1, 1, 1]` -> Returns `0`.
2. **Single Element >= Target**: `target = 4`, `nums = [1, 4, 4]` -> Returns `1`.
3. **Entire Array Equals Target**: `target = 10`, `nums = [1, 2, 3, 4]` -> Returns `4`.

---

## Interview Tips

- **Mention Positive Numbers Condition**: Emphasize *"Because all elements are positive, adding elements strictly increases the sum and shrinking the left border strictly decreases the sum, enabling monotonic sliding window optimization."*
- **Explain Follow-Up O(N log N)**: Mention that prefix sums + binary search provides the $\mathcal{O}(N \log N)$ alternative.

---

## Similar Problems

1. [LeetCode #713: Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)
2. [LeetCode #862: Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)
3. [LeetCode #904: Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)

---

## Revision Notes

- Problem: Minimal length subarray with sum $\ge \text{target}$.
- Strategy: Variable-Size Sliding Window.
- `left = 0`, `sum = 0`, `min_len = INF`.
- Loop `right` from `0` to `N - 1`:
  - `sum += nums[right]`.
  - `while (sum >= target)`:
    - `min_len = min(min_len, right - left + 1)`.
    - `sum -= nums[left++]`.
- Return `min_len == INF ? 0 : min_len`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
