# Problem Summary

Given an array `nums` containing integers `0`, `1`, and `2`, sort them in-place in a single pass. The **Dutch National Flag Algorithm** uses three pointers (`low`, `mid`, `high`) to partition elements into 0s, 1s, and 2s regions in $\mathcal{O}(N)$ single-pass time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to partition an array into **three distinct categories** in a single pass.
- In-place 3-way partitioning (e.g. Dutch National Flag Problem).

---

## Important Clues

1. **"Values 0, 1, 2 only"**: Three discrete categories.
2. **"Single-pass algorithm in O(1) space"**: Signals 3-Pointer Dutch National Flag strategy.

---

## Example

### Input
`nums = [2, 0, 2, 1, 1, 0]`

### Visual Step-by-Step Progression

```text
[ 0..low-1: 0s ] | [ low..mid-1: 1s ] | [ mid..high: Unknown ] | [ high+1..n-1: 2s ]

Initial: low=0, mid=0, high=5
nums[mid] == 2 -> swap with high, high--

Result after single pass: [0, 0, 1, 1, 2, 2]
```

---

## Alternative Solutions

### Counting Sort (Two-Pass)
- Pass 1: Count frequency of 0, 1, 2.
- Pass 2: Overwrite array in order.
- **Time Complexity**: $\mathcal{O}(N)$ (2 passes).
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **All Elements Identical**: `nums = [0, 0, 0]` -> No swaps needed.
2. **Already Sorted**: `nums = [0, 1, 2]` -> `mid` increments cleanly.
3. **Reversed Order**: `nums = [2, 1, 0]` -> Handled in minimum swaps.

---

## Interview Tips

- **Explain Pointer Responsibilities**:
  - `low`: Next position for `0`.
  - `mid`: Current element under inspection.
  - `high`: Next position for `2`.
- **Highlight Why `mid` Doesn't Increment on `high` Swap**: Emphasize *"When swapping with `high`, the element moved to `mid` is unknown and must be re-evaluated on the next iteration."*

---

## Similar Problems

1. [LeetCode #280: Wiggle Sort](https://leetcode.com/problems/wiggle-sort/)
2. [LeetCode #324: Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/)

---

## Revision Notes

- Problem: Sort 0s, 1s, and 2s in-place in 1 pass.
- Strategy: Dutch National Flag (3 Pointers).
- `low = 0`, `mid = 0`, `high = N - 1`.
- `while (mid <= high)`:
  - `nums[mid] == 0`: `swap(nums[low++], nums[mid++])`.
  - `nums[mid] == 1`: `mid++`.
  - `nums[mid] == 2`: `swap(nums[mid], nums[high--])`. (Do NOT `mid++`).
- Optimal Complexity: Time $\mathcal{O}(N)$ (1 pass), Space $\mathcal{O}(1)$.
