# Problem Summary

Given an integer array `nums`, find the **leftmost pivot index** where the sum of elements strictly to the left equals the sum of elements strictly to the right. The optimal approach computes `total_sum` first, then scans `nums` maintaining a running `left_sum`. At each index `i`, we check if `left_sum == total_sum - left_sum - nums[i]` in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find a balance / equilibrium point in an array where left side property equals right side property.
- Total Sum minus Left Sum derivation: $\text{right\_sum} = \text{total\_sum} - \text{left\_sum} - \text{curr\_val}$.

---

## Important Clues

1. **"Strictly to the left equals strictly to the right"**: Pivot index `i` is excluded from both sums.
2. **"Leftmost pivot index"**: Return the first index `i` that satisfies the condition.

---

## Example

### Input
`nums = [1, 7, 3, 6, 5, 6]`

### Visual Step-by-Step Progression

```text
total_sum = 28

i = 0 (1): left =  0, right = 28 -  0 - 1 = 27 (0 != 27)
i = 1 (7): left =  1, right = 28 -  1 - 7 = 20 (1 != 20)
i = 2 (3): left =  8, right = 28 -  8 - 3 = 17 (8 != 17)
i = 3 (6): left = 11, right = 28 - 11 - 6 = 11 (11 == 11 -> MATCH!)

Pivot Index: 3
```

---

## Alternative Solutions

### Prefix Sum & Suffix Sum Arrays (O(N) Time, O(N) Space)
- Construct `prefix` array and `suffix` array.
- Find first `i` where `prefix[i-1] == suffix[i+1]`.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **Pivot at Index 0**: `nums = [2, 1, -1]` -> `total_sum = 2`, `i = 0`: `left = 0`, `right = 2 - 0 - 2 = 0` -> Returns `0`.
2. **Pivot at Last Index**: `nums = [-1, 1, 2]` -> `left = 0`, `right = 0` at index 2 -> Returns `2`.
3. **No Pivot Exists**: `nums = [1, 2, 3]` -> Returns `-1`.

---

## Interview Tips

- **Explain Exclusion of `nums[i]`**: Clearly state *"The problem statement specifies elements STRICTLY to the left and right. Thus, `nums[i]` itself is not part of `left_sum` or `right_sum`."*

---

## Similar Problems

1. [LeetCode #1991: Find the Middle Index in Array](https://leetcode.com/problems/find-the-middle-index-in-array/)
2. [LeetCode #560: Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

---

## Revision Notes

- Problem: Find first index where left sum equals right sum.
- Strategy: Total Sum & Running `left_sum`.
- `total_sum = accumulate(nums)`.
- `left_sum = 0`.
- Loop `i` from `0` to `N - 1`:
  - `if (left_sum == total_sum - left_sum - nums[i]) return i`.
  - `left_sum += nums[i]`.
- Return `-1`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
