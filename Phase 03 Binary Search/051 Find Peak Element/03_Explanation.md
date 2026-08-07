# Problem Summary

Given an un-sorted array `nums` where `nums[-1] = nums[N] = -\infty`, find any peak element (an element strictly greater than its neighbors). The optimal solution uses **Binary Search on Slope Direction**. By comparing `nums[mid]` with `nums[mid + 1]`, if `nums[mid] < nums[mid + 1]` (uphill slope), we move right (`low = mid + 1`); otherwise we move left (`high = mid`). When `low == high`, `nums[low]` is guaranteed to be a peak in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find a **local maximum / peak** in an array (even if unsorted!).
- Binary Search on local gradient / slope direction.

---

## Important Clues

1. **"Strictly greater than its neighbors"**: Peak element definition.
2. **"nums[-1] = nums[n] = -\infty"**: Guarantees at least one peak always exists!
3. **"O(log n) runtime constraint"**: Binary search requirement.

---

## Example

### Input
`nums = [1, 2, 1, 3, 5, 6, 4]`

### Visual Step-by-Step Progression

```text
Slope Walk:
1 -> 2 -> 1 -> 3 -> 5 -> 6 -> 4
               ^ (mid=3, val 3 < 5 -> Uphill right -> low=4)

               5 -> 6 -> 4
                    ^ (mid=5, val 6 > 4 -> Downhill -> high=5)

Peak Found at Index: 5 (Value = 6)
```

---

## Alternative Solutions

### Sequential First Drop Scan (O(N) Time, O(1) Space)
- Scan array from index 0 to $N-2$. The first element `nums[i]` such that `nums[i] > nums[i+1]` is a peak.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **Strictly Increasing Array**: `nums = [1, 2, 3, 4, 5]` -> Returns `4` (last index).
2. **Strictly Decreasing Array**: `nums = [5, 4, 3, 2, 1]` -> Returns `0` (first index).
3. **Single Element**: `nums = [1]` -> Returns `0`.

---

## Interview Tips

- **Explain Why Binary Search Works on Unsorted Array**: State *"Even though the array is unsorted, `nums[-1] = nums[N] = -\infty` guarantees that following the ascending slope upwards MUST eventually hit a local maximum peak."*

---

## Similar Problems

1. [LeetCode #852: Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/)
2. [LeetCode #1901: Find a Peak Element II](https://leetcode.com/problems/find-a-peak-element-ii/)

---

## Revision Notes

- Problem: Find any peak element in array in $\mathcal{O}(\log N)$.
- Pattern: Binary Search on Gradient (`nums[mid]` vs `nums[mid+1]`).
- `low = 0`, `high = N - 1`.
- `while (low < high)`:
  - `mid = low + (high - low) / 2`.
  - `if (nums[mid] < nums[mid + 1]) low = mid + 1`.
  - `else high = mid`.
- Return `low`.
- Optimal Complexity: Time $\mathcal{O}(\log N)$, Space $\mathcal{O}(1)$.
