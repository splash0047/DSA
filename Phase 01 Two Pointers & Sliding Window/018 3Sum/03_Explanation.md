# Problem Summary

Given an integer array `nums`, find all unique triplets `[nums[i], nums[j], nums[k]]` that add up to `0`. The optimal approach sorts the array, fixes `nums[i]` in an outer loop, and uses **Two Pointers** (`left = i + 1`, `right = N - 1`) to find target pair sums of `-nums[i]`. In-place duplicate skipping avoids duplicate triplets without extra set memory in $\mathcal{O}(N^2)$ time and $\mathcal{O}(1)$ extra space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find $K$ elements summing to a target (K-Sum family: 2Sum, 3Sum, 4Sum).
- Sorting simplifies duplicate removal and allows Two Pointer pair searches.

---

## Important Clues

1. **"Return all triplets summing to 0"**: Multi-element sum problem.
2. **"Must not contain duplicate triplets"**: Sorting + adjacent duplicate skipping eliminates duplicate sets natively.

---

## Example

### Input
`nums = [-1, 0, 1, 2, -1, -4]`

### Visual Step-by-Step Progression

```text
1. Sort array: [-4, -1, -1, 0, 1, 2]

2. Fix i = 1 (val = -1):
   -1 + (-1) + 2 = 0  ->  Add triplet [-1, -1, 2]
   -1 + ( 0) + 1 = 0  ->  Add triplet [-1,  0, 1]

3. Fix i = 2 (val = -1):
   Duplicate of index 1 -> SKIP!

Result: [[-1, -1, 2], [-1, 0, 1]]
```

---

## Alternative Solutions

### Hash Set for Target Complement
- Fix `nums[i]`, then use a Hash Set for `-(nums[i] + nums[j])`. Requires sorting result or using `std::set` to prevent duplicates.
- **Time Complexity**: $\mathcal{O}(N^2)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **All Zeroes**: `nums = [0, 0, 0, 0]` -> Returns `[[0, 0, 0]]`.
2. **No Triplets Match**: `nums = [1, 2, 3]` -> Returns `[]`.
3. **Fewer than 3 elements**: `nums = [0, 1]` -> Returns `[]`.

---

## Interview Tips

- **Explain Duplicate Prevention Strategy**: Clearly state: *"We sort first so duplicate elements are adjacent. We skip duplicate `nums[i]` at the outer loop, and skip duplicate `nums[left]` and `nums[right]` after recording a valid triplet."*
- **Highlight Early Exit**: Mention `if (nums[i] > 0) break;` as a performance optimization.

---

## Similar Problems

1. [LeetCode #1: Two Sum](https://leetcode.com/problems/two-sum/)
2. [LeetCode #16: 3Sum Closest](https://leetcode.com/problems/3sum-closest/)
3. [LeetCode #18: 4Sum](https://leetcode.com/problems/4sum/)
4. [LeetCode #611: Valid Triangle Number](https://leetcode.com/problems/valid-triangle-number/)

---

## Revision Notes

- Problem: Find all unique triplets summing to 0.
- Strategy: Sort + Fixed Outer Loop + Two Pointers.
- Sort `nums`. Loop `i` from `0` to `N - 3`:
  - `if (nums[i] > 0) break`.
  - `if (i > 0 && nums[i] == nums[i-1]) continue`.
  - `left = i + 1`, `right = N - 1`.
  - While `left < right`:
    - `sum == 0`: add triplet, skip duplicate `left` & `right` values, `left++`, `right--`.
    - `sum < 0`: `left++`.
    - `sum > 0`: `right--`.
- Optimal Complexity: Time $\mathcal{O}(N^2)$, Space $\mathcal{O}(1)$.
