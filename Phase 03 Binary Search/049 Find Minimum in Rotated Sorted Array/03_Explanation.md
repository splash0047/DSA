# Problem Summary

Given a rotated sorted array `nums` of unique elements, find the minimum element in $\mathcal{O}(\log N)$ time. The optimal approach uses **Binary Search comparing `nums[mid]` with `nums[high]`**. If `nums[mid] > nums[high]`, the minimum lies strictly to the right (`low = mid + 1`); otherwise `high = mid`. When `low == high`, `nums[low]` is the minimum element in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the **rotation pivot / minimum element** in a rotated sorted array.
- Binary Search comparing midpoint with right boundary `high`.

---

## Important Clues

1. **"Rotated sorted array"**: Rotated search pattern.
2. **"O(log n) time constraint"**: Binary Search requirement.

---

## Example

### Input
`nums = [4, 5, 6, 7, 0, 1, 2]`

### Visual Step-by-Step Progression

```text
[ 4 , 5 , 6 , 7 , 0 , 1 , 2 ]   L=0, H=6, M=3 (val 7 > 2 -> L=4)
              ^
[ 4 , 5 , 6 , 7 , 0 , 1 , 2 ]   L=4, H=6, M=5 (val 1 < 2 -> H=5)
                      ^
[ 4 , 5 , 6 , 7 , 0 , 1 , 2 ]   L=4, H=5, M=4 (val 0 < 1 -> H=4)
                  ^
L == H = 4.
Minimum Element: nums[4] = 0
```

---

## Alternative Solutions

### Compare `nums[mid]` with adjacent elements `nums[mid-1]` and `nums[mid+1]`
- Check if `nums[mid] < nums[mid-1]` (found minimum!) or `nums[mid] > nums[mid+1]` (next element is minimum).
- **Time Complexity**: $\mathcal{O}(\log N)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **Array Not Rotated**: `nums = [11, 13, 15, 17]` -> `nums[mid] < nums[high]` always moves `high` left, returning `nums[0] = 11`.
2. **Single Element Array**: `nums = [1]` -> Returns `1`.
3. **Two Elements Array**: `nums = [2, 1]` -> `low=0, high=1, mid=0`, `nums[0] > nums[1] -> low=1`, returns `1`.

---

## Interview Tips

- **Explain Why Comparing `mid` with `high` is Superior to `low`**: State *"If the array is NOT rotated (e.g. `[1, 2, 3]`), comparing `nums[mid]` with `nums[low]` gives `nums[mid] >= nums[low]`, which would incorrectly suggest the minimum is to the right! Comparing `nums[mid]` with `nums[high]` handles both rotated and unrotated arrays seamlessly."*

---

## Similar Problems

1. [LeetCode #154: Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)
2. [LeetCode #33: Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

---

## Revision Notes

- Problem: Find minimum element in rotated sorted array.
- Pattern: Binary Search (`while (low < high)`).
- Compare `nums[mid]` with `nums[high]`:
  - `if (nums[mid] > nums[high]) low = mid + 1`.
  - `else high = mid`.
- Return `nums[low]`.
- Optimal Complexity: Time $\mathcal{O}(\log N)$, Space $\mathcal{O}(1)$.
