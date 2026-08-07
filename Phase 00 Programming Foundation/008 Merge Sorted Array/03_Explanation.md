# Problem Summary

Given two sorted integer arrays `nums1` (of size $m+n$ with $m$ valid elements) and `nums2` (of size $n$), merge `nums2` into `nums1` as a single sorted array in-place. By merging **backwards from right to left** starting at index $m+n-1$, we place the largest remaining elements at the back of `nums1` without overwriting unread elements, achieving $\mathcal{O}(m + n)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You are merging two pre-sorted sequences.
- One sequence has a pre-allocated empty buffer at the end.
- In-place modification is required ($\mathcal{O}(1)$ auxiliary space constraint).

---

## Important Clues

1. **"Both arrays sorted in non-decreasing order"**: Points to Two Pointers / Merge step of Merge Sort.
2. **"`nums1` has length `m + n` with trailing zeroes"**: Strong hint to fill backwards from the end.

---

## Example

### Input
`nums1 = [1, 2, 3, 0, 0, 0]`, `m = 3`, `nums2 = [2, 5, 6]`, `n = 3`

### Visual Step-by-Step Progression

```text
nums1: [ 1 ,  2 ,  3 ,  _ ,  _ ,  _ ]
                   p1             p

nums2: [ 2 ,  5 ,  6 ]
                   p2

Step 1: 6 > 3 -> nums1[5] = 6, p2--, p--
nums1: [ 1 ,  2 ,  3 ,  _ ,  _ ,  6 ]

Step 2: 5 > 3 -> nums1[4] = 5, p2--, p--
nums1: [ 1 ,  2 ,  3 ,  _ ,  5 ,  6 ]

Step 3: 3 > 2 -> nums1[3] = 3, p1--, p--
nums1: [ 1 ,  2 ,  3 ,  3 ,  5 ,  6 ]

Step 4: 2 >= 2 -> nums1[2] = 2, p2--, p--
nums1: [ 1 ,  2 ,  2 ,  3 ,  5 ,  6 ]  <- Final Result
```

---

## Alternative Solutions

### Auxiliary Array Merge (Forward)
1. Allocate vector `temp` of size $m + n$.
2. Use standard two-pointer merge from front (`i = 0`, `j = 0`, `k = 0`).
3. Copy `temp` back into `nums1`.
4. **Time Complexity**: $\mathcal{O}(m + n)$.
5. **Space Complexity**: $\mathcal{O}(m + n)$.

---

## Edge Cases

1. **`m = 0`** (`nums1` empty): `nums1 = [0]`, `m = 0`, `nums2 = [1]`, `n = 1` $\rightarrow$ `nums2` elements copied entirely to `nums1`.
2. **`n = 0`** (`nums2` empty): `nums1` remains unchanged.
3. **All `nums2` elements smaller than `nums1`**: `nums1 = [4, 5, 6, 0, 0]`, `nums2 = [1, 2]` $\rightarrow$ `nums1` elements shifted right, `nums2` elements placed at front.

---

## Interview Tips

- **Explain Backward Merge Rationale**: Emphasize *"Merging from the back protects unread elements in `nums1` from being overwritten."*
- **Highlight Loop Guard**: Point out why `while (p2 >= 0)` is the exact correct loop condition (since if `nums1` runs out first, remaining `nums2` elements must still be copied).

---

## Similar Problems

1. [LeetCode #21: Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
2. [LeetCode #977: Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)
3. [LeetCode #986: Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)

---

## Revision Notes

- Problem: Merge two sorted arrays in-place into `nums1`.
- Pattern: Three Pointers filling backwards from index `m + n - 1`.
- `p1 = m - 1`, `p2 = n - 1`, `p = m + n - 1`.
- Loop `while (p2 >= 0)`:
  - If `p1 >= 0 && nums1[p1] > nums2[p2]`: `nums1[p--] = nums1[p1--]`.
  - Else: `nums1[p--] = nums2[p2--]`.
- Optimal Complexity: Time $\mathcal{O}(m + n)$, Space $\mathcal{O}(1)$.
