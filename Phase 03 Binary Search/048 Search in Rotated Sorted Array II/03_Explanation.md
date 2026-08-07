# Problem Summary

Given a rotated sorted array `nums` containing **duplicates** and a `target`, return `true` if `target` exists in `nums`, or `false` otherwise. The optimal approach uses **Modified Binary Search with Duplicate Shrinking**. When `nums[low] == nums[mid] == nums[high]`, we cannot determine which half is sorted, so we shrink `low++` and `high--`. This achieves $\mathcal{O}(\log N)$ average time ($\mathcal{O}(N)$ worst case) and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- A rotated sorted array contains **duplicate values**.
- Handling edge-case ambiguity when boundary elements equal the midpoint.

---

## Important Clues

1. **"Not necessarily with distinct values"**: Presence of duplicates.
2. **"Decrease operation steps as much as possible"**: Average $\mathcal{O}(\log N)$ binary search.

---

## Example

### Input
`nums = [2, 5, 6, 0, 0, 1, 2]`, `target = 0`

### Visual Step-by-Step Progression

```text
L=0 (2), H=6 (2), M=3 (val 0)
nums[3] = 0 == target 0 -> MATCH!

Result: true
```

---

## Follow-up Answer: Impact of Duplicates on Complexity

**Question**: Does allowing duplicates affect the runtime complexity? How and why?

**Answer**: 
- **Yes!** The worst-case time complexity degrades from $\mathcal{O}(\log N)$ to $\mathcal{O}(N)$.
- **Why**: When `nums[low] == nums[mid] == nums[high]` (e.g., `nums = [1, 1, 1, 1, 1, 2, 1]`), we cannot determine whether the left half or right half is sorted. We are forced to shrink boundaries linearly (`low++`, `high--`), inspecting elements one by one.

---

## Edge Cases

1. **All Elements Identical**: `nums = [1, 1, 1, 1]`, `target = 2` -> Linear fallback returns `false`.
2. **Pivot Surrounded by Duplicates**: `nums = [3, 1, 2, 3, 3, 3, 3]`, `target = 2` -> Handled correctly.
3. **No Duplicates Present**: Degrades gracefully to $\mathcal{O}(\log N)$ binary search.

---

## Interview Tips

- **Proactively Address the Follow-up**: Explain *"When duplicates are present, `nums[low] == nums[mid] == nums[high]` prevents us from eliminating half of the elements deterministically. In the worst case (all elements identical), complexity becomes $\mathcal{O}(N)$."*

---

## Similar Problems

1. [LeetCode #33: Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
2. [LeetCode #154: Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

---

## Revision Notes

- Problem: Search target in rotated sorted array WITH duplicates.
- Pattern: Binary Search + Duplicate Trimming.
- `while (low <= high)`:
  - `if (nums[mid] == target) return true`.
  - `if (nums[low] == nums[mid] && nums[mid] == nums[high]) low++, high--, continue`.
  - Normal rotated binary search logic.
- Optimal Complexity: Average $\mathcal{O}(\log N)$, Worst-case $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
