# Problem Summary

Given an integer array `nums` and an integer `k`, return the **maximum length** of a contiguous subarray that sums to `k`. The optimal approach uses **Prefix Sum + Earliest Index Hash Map**. We track running `prefix_sum` and record only the first appearance of each prefix sum. For each element at index `i`, if `prefix_sum - k` is in `first_seen`, we compute length `i - first_seen[prefix_sum - k]` in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the **LONGEST contiguous subarray** with a specific target sum $K$ (especially when array contains negative numbers).
- Storing **earliest index** of each prefix sum in a Hash Map to maximize window length.

---

## Important Clues

1. **"Maximum size / length of subarray"**: Store earliest index of prefix sum.
2. **"Sum equals k with negative numbers"**: Disqualifies sliding window; requires Prefix Sum + Hash Map.

---

## Example

### Input
`nums = [1, -1, 5, -2, 3]`, `k = 3`

### Visual Step-by-Step Progression

```text
Map init: {0: -1}

i = 0: num =  1 -> sum = 1 -> target = -2 (not found) -> Map: {0:-1, 1:0}
i = 1: num = -1 -> sum = 0 -> target = -3 (not found) -> Map: {0:-1, 1:0} (0 already exists at -1!)
i = 2: num =  5 -> sum = 5 -> target =  2 (not found) -> Map: {0:-1, 1:0, 5:2}
i = 3: num = -2 -> sum = 3 -> target =  0 (FOUND at -1!) -> len = 3 - (-1) = 4 -> MAX!

Max Length: 4 ([1, -1, 5, -2])
```

---

## Alternative Solutions

### Two Pointer / Sliding Window (Only if array contains ALL POSITIVE numbers)
- If `nums[i] >= 0` for all elements, sliding window can solve this in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.
- *However, when negative numbers are present, Hash Map is required.*

---

## Edge Cases

1. **Entire Array Sums to K**: `nums = [1, 2, 3]`, `k = 6` -> Returns `3`.
2. **No Subarray Sums to K**: `nums = [1, 2, 3]`, `k = 10` -> Returns `0`.
3. **Array with zeroes**: `nums = [0, 0, 3]`, `k = 3` -> `first_seen[0] = -1` yields length `3`.

---

## Interview Tips

- **Compare Problem 325 vs Problem 560**:
  - LeetCode #560 (Subarray Sum Equals K): Count total valid subarrays $\rightarrow$ Store **frequency** of prefix sums in Hash Map.
  - LeetCode #325 (Max Size Subarray Sum Equals K): Maximize subarray length $\rightarrow$ Store **earliest index** of prefix sums in Hash Map.

---

## Similar Problems

1. [LeetCode #560: Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
2. [LeetCode #525: Contiguous Array](https://leetcode.com/problems/contiguous-array/)

---

## Revision Notes

- Problem: Longest subarray summing to $k$.
- Pattern: Prefix Sum + `first_seen` Hash Map.
- Seed `first_seen[0] = -1`.
- For `i` from `0` to `N - 1`:
  - `prefix_sum += nums[i]`.
  - `if (first_seen.count(prefix_sum - k)) max_len = max(max_len, i - first_seen[prefix_sum - k])`.
  - `if (!first_seen.count(prefix_sum)) first_seen[prefix_sum] = i`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(N)$.
