# Problem Summary

Given a sorted integer array `nums` (which may contain negative values), return a new array containing the squares of each number sorted in non-decreasing order. The optimal approach uses **Two Pointers (Outside-In)** at `left = 0` and `right = N - 1` to compare absolute values and fill a `result` vector backwards from index $N - 1$ down to `0` in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You have a pre-sorted array with non-monotonic transformations (like squaring negative and positive numbers).
- Largest values are concentrated at the array boundaries, pointing to an Outside-In Two Pointer approach.

---

## Important Clues

1. **"Sorted in non-decreasing order"**: Hints that sorting logic can be avoided.
2. **"Squares of each number"**: $x^2 = (-x)^2$, so largest values are at outer edges.

---

## Example

### Input
`nums = [-4, -1, 0, 3, 10]`

### Visual Step-by-Step Progression

```text
L -> [ -4 , -1 ,  0 ,  3 ,  10 ] <- R
     |-4| = 4, |10| = 10 -> write 100 at back

L -> [ -4 , -1 ,  0 ,  3 ,  10 ] <- R
     |-4| = 4, |3| = 3   -> write 16

Result (filling backwards): [0, 1, 9, 16, 100]
```

---

## Alternative Solutions

### Square and Sort (Brute Force)
- Multiply each element by itself and call `std::sort`.
- **Time Complexity**: $\mathcal{O}(N \log N)$.
- **Space Complexity**: $\mathcal{O}(1)$ extra space.

---

## Edge Cases

1. **All Non-Negative Numbers**: `nums = [0, 1, 2, 3]` -> Elements placed in original order.
2. **All Negative Numbers**: `nums = [-5, -3, -1]` -> Elements placed in reverse original order.
3. **Single Element**: `nums = [-3]` -> Returns `[9]`.

---

## Interview Tips

- **Explain Why Filling Backwards Works**: Emphasize *"Since the largest absolute values are at the boundaries, comparing boundary elements yields the largest squares first, requiring us to populate the output array from right to left."*

---

## Similar Problems

1. [LeetCode #88: Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
2. [LeetCode #360: Sort Transformed Array](https://leetcode.com/problems/sort-transformed-array/)

---

## Revision Notes

- Problem: Return sorted array of squares from sorted input `nums`.
- Pattern: Two Pointers Outside-In (`left = 0`, `right = N - 1`, `pos = N - 1`).
- `while (left <= right)`:
  - If `abs(nums[left]) > abs(nums[right])`: `res[pos--] = nums[left]*nums[left]`, `left++`.
  - Else: `res[pos--] = nums[right]*nums[right]`, `right--`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(N)$.
