# Problem Summary

Given two sorted arrays `nums1` and `nums2` of size `m` and `n`, find the median of the merged arrays in $\mathcal{O}(\log(m + n))$ time. The optimal approach uses **Binary Search on Array Partitions** over the smaller array (size $\min(m, n)$). We place cuts `px` and `py` such that left elements are $\le$ right elements (`maxLeft1 <= minRight2` and `maxLeft2 <= minRight1`). This calculates the median in $\mathcal{O}(\log(\min(m, n)))$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the **median or K-th element** across two pre-sorted arrays without merging.
- Binary Search on Array Partitions pattern.

---

## Important Clues

1. **"Two sorted arrays"**: Leveraging pre-sorted order.
2. **"O(log(m + n)) time"**: Requires binary search cut partition across arrays.

---

## Example

### Input
`nums1 = [1, 2]`, `nums2 = [3, 4]`

### Visual Step-by-Step Progression

```text
Partitioning:
nums1: [1, 2 | ]   (px = 2, maxLeft1 = 2, minRight1 = INF)
nums2: [   | 3, 4] (py = 0, maxLeft2 = -INF, minRight2 = 3)

Cut validation: 2 <= 3 AND -INF <= INF (VALID PARTITION!)
Total elements = 4 (even).
Median = (max(2, -INF) + min(INF, 3)) / 2.0 = (2 + 3) / 2.0 = 2.5
```

---

## Alternative Solutions

### Two-Pointer Linear Counter (O(M + N) Time, O(1) Space)
- Advance two pointers `i` and `j` up to index $(m+n)/2$ without allocating extra memory.
- **Time Complexity**: $\mathcal{O}(M + N)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **One Array Empty**: `nums1 = []`, `nums2 = [1]` -> Handled via `INT_MIN` / `INT_MAX` boundary fallbacks.
2. **No Overlap Between Arrays**: `nums1 = [1, 2]`, `nums2 = [3, 4]` -> Cut falls at boundaries.
3. **Single Element Each**: `nums1 = [1]`, `nums2 = [2]` -> Returns `1.5`.

---

## Interview Tips

- **Explain Why Swapping Arrays is Mandatory**: State *"We enforce `if (nums1.size() > nums2.size()) swap()` so that binary search runs on the smaller array. This guarantees that `py = (m + n + 1) / 2 - px` never results in out-of-bound indices, while also optimizing runtime to $\mathcal{O}(\log(\min(M, N)))$."*

---

## Similar Problems

1. [GFG: K-th Element of Two Sorted Arrays](https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-arrays1370/1)
2. [LeetCode #658: Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)

---

## Revision Notes

- Problem: Median of 2 sorted arrays in $\mathcal{O}(\log(\min(M, N)))$.
- Guard: Ensure `nums1.size() <= nums2.size()`.
- Range: `low = 0`, `high = m`.
- `px = (low + high) / 2`, `py = (m + n + 1) / 2 - px`.
- Boundary variables: `maxLeft1, minRight1, maxLeft2, minRight2` with `INT_MIN/INT_MAX`.
- If `maxLeft1 <= minRight2 && maxLeft2 <= minRight1`:
  - Odd total: return `max(maxLeft1, maxLeft2)`.
  - Even total: return `(max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0`.
- Else adjust `high = px - 1` or `low = px + 1`.
- Optimal Complexity: Time $\mathcal{O}(\log(\min(M, N)))$, Space $\mathcal{O}(1)$.
