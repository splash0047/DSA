# Problem Summary

Given a sorted array `nums` where every element appears twice except one single element, find the single element. The optimal approach uses **Binary Search on Even/Odd Index Parity**. Before the single element, pairs start at even indices `(0,1), (2,3)`. By forcing `mid` to be an even index, if `nums[mid] == nums[mid+1]`, the single element lies to the right (`low = mid + 2`); otherwise `high = mid`. This completes in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- Pair alignment / index parity pattern changes after a single unique element.
- Index Parity Binary Search pattern.

---

## Important Clues

1. **"Every element appears twice except one"**: Index parity property.
2. **"O(log n) time and O(1) space"**: Mandatory binary search requirement.

---

## Example

### Input
`nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]`

### Visual Step-by-Step Progression

```text
Indices:  0  1  2  3  4  5  6  7  8
Values:  [1, 1, 2, 3, 3, 4, 4, 8, 8]
          |--|  ^  |--|  |--|  |--|
          Pairs Single  Pairs shift!

Before single element: nums[even] == nums[even + 1]
After single element:  nums[even] != nums[even + 1]

Binary Search locates single element '2' at index 2 in O(log N)!
```

---

## Alternative Solutions

### Bitwise XOR (O(N) Time, O(1) Space)
- XOR all elements. Duplicate pairs cancel out, leaving the single element.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **Single Element at Beginning**: `nums = [1, 2, 2, 3, 3]` -> Returns `1`.
2. **Single Element at End**: `nums = [1, 1, 2, 2, 3]` -> Returns `3`.
3. **Array of Length 1**: `nums = [7]` -> Returns `7`.

---

## Interview Tips

- **Explain Index Parity Pattern**: Clearly state *"Before the single element, paired duplicates occupy indices `(even, odd)`. After the single element, paired duplicates shift to `(odd, even)`. This structural shift allows binary search to eliminate half the array at each step."*

---

## Similar Problems

1. [LeetCode #136: Single Number](https://leetcode.com/problems/single-number/)
2. [LeetCode #260: Single Number III](https://leetcode.com/problems/single-number-iii/)

---

## Revision Notes

- Problem: Single element in sorted duplicate-pair array in $\mathcal{O}(\log N)$.
- Strategy: Binary Search on Even Index Parity.
- `low = 0`, `high = N - 1`.
- `while (low < high)`:
  - `mid = low + (high - low) / 2`.
  - `if (mid % 2 == 1) mid--`.
  - `if (nums[mid] == nums[mid + 1]) low = mid + 2`.
  - `else high = mid`.
- Return `nums[low]`.
- Optimal Complexity: Time $\mathcal{O}(\log N)$, Space $\mathcal{O}(1)$.
