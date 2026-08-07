# Problem Summary

Given a rotated sorted array `nums` of distinct integers and a `target`, return its index or `-1` if not found. The optimal approach uses **Modified Binary Search**. At each step `mid`, at least one half (left or right) is guaranteed to be strictly sorted. By checking if `target` falls inside the bounds of the sorted half, we halve the search space in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- An array is **partially sorted / rotated** (shifted by pivot $K$).
- Modified Binary Search by identifying sorted half.

---

## Important Clues

1. **"Rotated at an unknown pivot index"**: Rotated sorted array pattern.
2. **"Distinct values"**: No duplicate ambiguity.

---

## Example

### Input
`nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 0`

### Visual Step-by-Step Progression

```text
[ 4 , 5 , 6 , 7 , 0 , 1 , 2 ]   L=0, H=6, M=3 (val 7)
  |___________|
   Left half is sorted [4..7]. Is 0 in [4..7]? NO! Move to Right half (L=4).

[ 4 , 5 , 6 , 7 , 0 , 1 , 2 ]   L=4, H=6, M=5 (val 1)
                  |___|
                   Left half is sorted [0..1]. Is 0 in [0..1]? YES! Move H=4.

[ 4 , 5 , 6 , 7 , 0 , 1 , 2 ]   L=4, H=4, M=4 (val 0 == 0 -> MATCH!)

Result Index: 4
```

---

## Alternative Solutions

### Find Pivot First, then Binary Search
1. Find pivot index `P` (minimum element) using binary search in $\mathcal{O}(\log N)$.
2. Determine which sorted subarray `[0 ... P-1]` or `[P ... N-1]` target belongs to.
3. Standard binary search on that subarray in $\mathcal{O}(\log N)$.
- **Time Complexity**: $\mathcal{O}(\log N)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **Array Not Rotated**: `nums = [1, 2, 3, 4, 5]`, `target = 3` -> Standard binary search behavior.
2. **Single Element Array**: `nums = [1]`, `target = 0` -> Returns `-1`.
3. **Target at Pivot Point**: `nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 0` -> Returns `4`.

---

## Interview Tips

- **Explain the Key Property**: State *"In any rotated sorted array split at index `mid`, AT LEAST ONE of the two halves `[low...mid]` or `[mid...high]` is guaranteed to be strictly sorted. We identify which half is sorted and check if `target` lies within its boundaries."*

---

## Similar Problems

1. [LeetCode #81: Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)
2. [LeetCode #153: Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

---

## Revision Notes

- Problem: Search target in rotated sorted array (distinct values).
- Pattern: Modified Binary Search (Identify Sorted Half).
- `while (low <= high)`:
  - `if (nums[mid] == target) return mid`.
  - `if (nums[low] <= nums[mid])`:
    - `if (nums[low] <= target && target < nums[mid]) high = mid - 1`.
    - `else low = mid + 1`.
  - `else`:
    - `if (nums[mid] < target && target <= nums[high]) low = mid + 1`.
    - `else high = mid - 1`.
- Optimal Complexity: Time $\mathcal{O}(\log N)$, Space $\mathcal{O}(1)$.
