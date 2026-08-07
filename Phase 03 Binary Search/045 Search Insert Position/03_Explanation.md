# Problem Summary

Given a sorted array `nums` of distinct integers and a `target`, return the index if found, or the insertion index if not present. The optimal approach uses **Binary Search (Lower Bound)** to find the smallest index `i` such that `nums[i] >= target`. If `nums[mid] >= target`, we record `ans = mid` and contract `high = mid - 1`, returning `ans` in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the **first index** satisfying a condition ($\ge \text{target}$) in a sorted array.
- Lower Bound Binary Search pattern.

---

## Important Clues

1. **"Index where it would be inserted in order"**: Exact definition of Lower Bound.
2. **"O(log n) runtime constraint"**: Signals Binary Search logic.

---

## Example

### Input
`nums = [1, 3, 5, 6]`, `target = 2`

### Visual Step-by-Step Progression

```text
Target = 2
Search range: [1, 3, 5, 6] (L=0, H=3, ans=4)
              L  M     H   mid=1 -> nums[1]=3 >= 2 -> ans=1, H=0

Search range: [1]          (L=0, H=0)
              M
              mid=0 -> nums[0]=1 < 2 -> L=1

Loop terminates (L > H).
Insertion Index: ans = 1
```

---

## Alternative Solutions

### C++ Standard Library `std::lower_bound`
- `return std::lower_bound(nums.begin(), nums.end(), target) - nums.begin();`
- **Time Complexity**: $\mathcal{O}(\log N)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **Target Smaller Than First Element**: `nums = [2, 4, 6]`, `target = 1` -> Returns `0`.
2. **Target Larger Than Last Element**: `nums = [2, 4, 6]`, `target = 7` -> Returns `3` (`N`).
3. **Exact Match at End**: `nums = [2, 4, 6]`, `target = 6` -> Returns `2`.

---

## Interview Tips

- **Connect Search Insert Position to Lower Bound**: State *"Finding the insertion position of `target` in a sorted array is mathematically identical to finding the Lower Bound (first index `i` where `nums[i] >= target`)."*

---

## Similar Problems

1. [LeetCode #704: Binary Search](https://leetcode.com/problems/binary-search/)
2. [LeetCode #34: Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

---

## Revision Notes

- Problem: Search target or return insertion index in sorted array.
- Pattern: Lower Bound Binary Search.
- `low = 0`, `high = N - 1`, `ans = N`.
- `while (low <= high)`:
  - `mid = low + (high - low) / 2`.
  - `if (nums[mid] >= target) ans = mid, high = mid - 1`.
  - `else low = mid + 1`.
- Return `ans`.
- Optimal Complexity: Time $\mathcal{O}(\log N)$, Space $\mathcal{O}(1)$.
