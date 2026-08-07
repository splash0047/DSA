# Problem Summary

Given a unimodal mountain array `arr`, return the index of the peak element. The optimal approach uses **Binary Search on Mountain Slope**. By comparing `arr[mid]` with `arr[mid + 1]`, if `arr[mid] < arr[mid + 1]` (uphill slope), the peak lies to the right (`low = mid + 1`); otherwise `high = mid`. When `low == high`, `low` is the peak index in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- An array is **unimodal** (strictly increases to a single peak, then strictly decreases).
- Binary Search on slope / gradient comparison.

---

## Important Clues

1. **"Mountain array"**: Unimodal sequence property.
2. **"O(log(arr.length)) time"**: Binary search requirement.

---

## Example

### Input
`arr = [0, 10, 5, 2]`

### Visual Step-by-Step Progression

```text
Slope:  0  ->  10  ->  5  ->  2
               ^^ (PEAK!)

Binary Search:
mid=1 (10 > 5) -> downhill -> high=1
mid=0 (0 < 10) -> uphill   -> low=1

Peak Index: 1 (Value 10)
```

---

## Alternative Solutions

### Golden Section Search / Ternary Search
- Perform ternary search by dividing space into 3 parts using `m1` and `m2`.
- **Time Complexity**: $\mathcal{O}(\log_3 N) = \mathcal{O}(\log N)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **Minimum Mountain Array Size ($N = 3$)**: `arr = [0, 1, 0]` -> Returns `1`.
2. **Peak Near Beginning**: `arr = [0, 100, 5, 4, 3, 2, 1]` -> Returns `1`.
3. **Peak Near End**: `arr = [1, 2, 3, 4, 5, 100, 0]` -> Returns `5`.

---

## Interview Tips

- **Compare Problem 162 vs Problem 852**:
  - LeetCode #162 (Find Peak Element): Unsorted array, may contain **multiple peaks**.
  - LeetCode #852 (Peak Index in a Mountain Array): Strictly unimodal array, contains **exactly one peak**.
  - *Both are solved using identical binary search slope comparisons!*

---

## Similar Problems

1. [LeetCode #162: Find Peak Element](https://leetcode.com/problems/find-peak-element/)
2. [LeetCode #1095: Find in Mountain Array](https://leetcode.com/problems/find-in-mountain-array/)

---

## Revision Notes

- Problem: Peak index in unimodal mountain array.
- Pattern: Binary Search on Slope (`arr[mid]` vs `arr[mid+1]`).
- `low = 0`, `high = N - 1`.
- `while (low < high)`:
  - `mid = low + (high - low) / 2`.
  - `if (arr[mid] < arr[mid + 1]) low = mid + 1`.
  - `else high = mid`.
- Return `low`.
- Optimal Complexity: Time $\mathcal{O}(\log N)$, Space $\mathcal{O}(1)$.
