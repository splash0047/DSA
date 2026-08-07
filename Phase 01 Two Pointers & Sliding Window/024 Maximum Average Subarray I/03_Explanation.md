# Problem Summary

Given an integer array `nums` and an integer `k`, find the maximum average among all contiguous subarrays of fixed length `k`. Using a **Fixed-Size Sliding Window**, we compute the initial sum of the first $k$ elements, then slide the window across the array by adding `nums[i]` and subtracting `nums[i-k]` in $\mathcal{O}(N)$ linear time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to compute a property (sum, average, max, min) for **all contiguous subarrays of fixed size K**.
- Fixed-Size Sliding Window pattern applies directly.

---

## Important Clues

1. **"Contiguous subarray of length equal to k"**: Fixed window size $K$.
2. **"Maximum average value"**: Maximize sum over fixed $K$.

---

## Example

### Input
`nums = [1, 12, -5, -6, 50, 3]`, `k = 4`

### Visual Step-by-Step Progression

```text
Window 1: [ 1 , 12 , -5 , -6 ]  50 ,  3   -> sum = 2

Window 2:   1 [ 12 , -5 , -6 , 50 ]   3   -> sum = 2 + 50 - 1 = 51 (MAX!)

Window 3:   1 , 12 [ -5 , -6 , 50 ,   3 ] -> sum = 51 + 3 - 12 = 42

Max Avg: 51 / 4 = 12.75
```

---

## Alternative Solutions

### Prefix Sum Array (O(N) Time, O(N) Space)
- Construct prefix sum array `P` where `P[i] = sum(nums[0...i-1])`.
- Any subarray sum `nums[i...i+k-1] = P[i+k] - P[i]`.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **$k = N$**: Entire array is the only window.
2. **$k = 1$**: Maximum element in `nums`.
3. **All Negative Numbers**: `nums = [-1, -12, -5, -6]`, `k = 2` -> Correctly returns max negative average.

---

## Interview Tips

- **Mention Float Truncation**: Point out the importance of using `double` for `current_sum` and `max_sum` to prevent integer division truncation.
- **Compare Sliding Window vs Prefix Sum**: Highlight that Sliding Window accomplishes $\mathcal{O}(N)$ time with $\mathcal{O}(1)$ space, whereas Prefix Sum requires $\mathcal{O}(N)$ extra space.

---

## Similar Problems

1. [LeetCode #209: Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
2. [LeetCode #1343: Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)

---

## Revision Notes

- Problem: Max average subarray of fixed size $K$.
- Strategy: Fixed-Size Sliding Window.
- Compute sum of first $k$ elements into `double current_sum`.
- Set `max_sum = current_sum`.
- Loop `i` from `k` to `N - 1`:
  - `current_sum += nums[i] - nums[i - k]`.
  - `max_sum = max(max_sum, current_sum)`.
- Return `max_sum / k`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
