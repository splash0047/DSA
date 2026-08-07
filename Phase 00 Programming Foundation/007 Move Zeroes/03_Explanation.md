# Problem Summary

Given an integer array `nums`, relocate all `0`s to the end of the array while maintaining the relative order of non-zero elements in-place. The optimal approach uses a **Two Pointers (Read / Write)** strategy where `read_index` scans for non-zero elements and swaps them into `write_index` in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to partition an array based on element criteria (zero vs non-zero, odd vs even).
- The operation must be performed **in-place** with $\mathcal{O}(1)$ space.
- Relative order of non-zero elements must be preserved.

---

## Important Clues

1. **"In-place without making a copy"**: Requires $\mathcal{O}(1)$ extra memory.
2. **"Maintain relative order"**: Excludes quicksort partition (which doesn't preserve relative ordering).

---

## Example

### Input
`nums = [0, 1, 0, 3, 12]`

### Visual Step-by-Step Progression

```text
Initial:  [ 0 ,  1 ,  0 ,  3 ,  12 ]
           w     r (r finds 1 -> swap with w)

Step 1:   [ 1 ,  0 ,  0 ,  3 ,  12 ]
                 w         r (r finds 3 -> swap with w)

Step 2:   [ 1 ,  3 ,  0 ,  0 ,  12 ]
                      w         r (r finds 12 -> swap with w)

Final:    [ 1 ,  3 , 12 ,  0 ,   0 ]
```

---

## Alternative Solutions

### Two-Pass Overwriting
1. First pass: Move all non-zero elements to `nums[write_index++]`.
2. Second pass: Fill all positions from `write_index` to $N-1$ with `0`.
3. **Time Complexity**: $\mathcal{O}(N)$.
4. **Space Complexity**: $\mathcal{O}(1)$.
5. *Difference*: Uses explicit assignment instead of `swap`.

---

## Edge Cases

1. **No Zeroes**: `nums = [1, 2, 3]` -> Array remains unchanged.
2. **All Zeroes**: `nums = [0, 0, 0]` -> Array remains unchanged.
3. **Single Element**: `nums = [0]` -> Array remains unchanged.
4. **Zeroes Already at End**: `nums = [1, 2, 0, 0]` -> Handled cleanly without redundant operations.

---

## Interview Tips

- **Mention Write Minimization**: Highlight that the two-pointer swap strategy minimizes write operations when the array contains few zeroes.
- **Compare Swap vs Two-Pass Fill**: Explain why swap accomplishes the task in a single loop traversal without needing a secondary zero-filling loop.

---

## Similar Problems

1. [LeetCode #27: Remove Element](https://leetcode.com/problems/remove-element/)
2. [LeetCode #26: Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

---

## Revision Notes

- Problem: Move zeroes to end of array in-place.
- Strategy: Two Pointers (`write_index`, `read_index`).
- Loop `read_index` from 0 to $N-1$:
  - If `nums[read_index] != 0`: `swap(nums[write_index++], nums[read_index])`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
