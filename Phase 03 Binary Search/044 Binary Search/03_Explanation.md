# Problem Summary

Given a 1D sorted array `nums` and a `target`, return its index or `-1` if not present in $\mathcal{O}(\log N)$ time. Using **Iterative Binary Search**, we maintain bounds `low = 0` and `high = N - 1`, compute `mid = low + (high - low) / 2`, and halve the search space at each iteration in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- The input array is **sorted** in ascending/descending order.
- You must find an element or insertion point in $\mathcal{O}(\log N)$ time.

---

## Important Clues

1. **"Sorted in ascending order"**: Signals Binary Search pattern.
2. **"O(log n) runtime constraint"**: Mandatory binary search requirement.

---

## Example

### Input
`nums = [-1, 0, 3, 5, 9, 12]`, `target = 9`

### Visual Step-by-Step Progression

```text
low=0, high=5 -> mid=2 (nums[2] = 3 < 9) -> eliminate left half!
[-1 , 0 , 3 , 5 , 9 , 12]
              L   M   H

low=3, high=5 -> mid=4 (nums[4] = 9 == 9 -> MATCH!)

Result Index: 4
```

---

## Alternative Solutions

### Recursive Binary Search (O(log N) Time, O(log N) Space)
- Perform binary search recursively passing `(low, high)`.
- **Time Complexity**: $\mathcal{O}(\log N)$.
- **Space Complexity**: $\mathcal{O}(\log N)$ recursion call stack overhead.

---

## Edge Cases

1. **Single Element Array**: `nums = [5]`, `target = 5` -> Returns `0`.
2. **Target Smaller Than Minimum**: `nums = [1, 2, 3]`, `target = 0` -> Returns `-1`.
3. **Target Larger Than Maximum**: `nums = [1, 2, 3]`, `target = 5` -> Returns `-1`.

---

## Interview Tips

- **Explain Overflow Protection**: Emphasize *"We compute `mid` as `low + (high - low) / 2` to avoid integer overflow when `low + high` exceeds maximum 32-bit integer limits."*

---

## Similar Problems

1. [LeetCode #35: Search Insert Position](https://leetcode.com/problems/search-insert-position/)
2. [LeetCode #34: Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

---

## Revision Notes

- Problem: Search target in 1D sorted array in $\mathcal{O}(\log N)$.
- Pattern: Binary Search (`low = 0`, `high = N - 1`).
- `while (low <= high)`:
  - `mid = low + (high - low) / 2`.
  - `if (nums[mid] == target) return mid`.
  - `else if (nums[mid] < target) low = mid + 1`.
  - `else high = mid - 1`.
- Return `-1`.
- Optimal Complexity: Time $\mathcal{O}(\log N)$, Space $\mathcal{O}(1)$.
