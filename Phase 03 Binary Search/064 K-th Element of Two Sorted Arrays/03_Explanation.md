# Problem Summary

Given two sorted arrays `a` and `b` of size `n` and `m`, find the $k^{\text{th}}$ element of the combined sorted array in $\mathcal{O}(\log(n + m))$ time. The optimal approach uses **Binary Search on Array Partitions** over the smaller array. We search for partition cut `px` in range $[\max(0, k-m), \min(n, k)]$ and `py = k - px` such that `maxLeftA <= minRightB` and `maxLeftB <= minRightA`. The $k^{\text{th}}$ element is $\max(\text{maxLeftA}, \text{maxLeftB})$ in $\mathcal{O}(\log(\min(n, m)))$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the **$k^{\text{th}}$ element / median** across two pre-sorted arrays without merging.
- Binary Search on Array Partitions pattern.

---

## Important Clues

1. **"Two sorted arrays"**: Exploiting sorted properties.
2. **"k-th position of combined sorted array"**: Generalization of Median problem.

---

## Example

### Input
`a = [2, 3, 6, 7, 9]`, `b = [1, 4, 8, 10]`, `k = 5`

### Visual Step-by-Step Progression

```text
Combined elements cut at k=5:
Array B (size 4): [1, 4 | 8, 10]   (px = 2)
Array A (size 5): [2, 3, 6 | 7, 9] (py = 3)

Valid cut! Left elements = {1, 4, 2, 3, 6} (5 elements)
5th Element = max(4, 6) = 6
```

---

## Alternative Solutions

### Two-Pointer Linear Counter (O(K) Time, O(1) Space)
- Advance pointers `i` and `j` $K$ times without allocating extra array.
- **Time Complexity**: $\mathcal{O}(K)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **$k = 1$**: Handled by setting `high = min(n, 1)`. Returns $\min(a[0], b[0])$.
2. **$k == n + m$**: Returns $\max(a[n-1], b[m-1])$.
3. **$k > m$**: Forces `low = k - m` to avoid taking $> m$ elements from `b`.

---

## Interview Tips

- **Explain Range Bounds Math**: State *"We set `low = max(0, k - m)` and `high = min(n, k)` because array `a` must contribute AT LEAST $k - m$ elements if $k > m$, and CANNOT contribute more than $n$ elements or $k$ total elements."*

---

## Similar Problems

1. [LeetCode #4: Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
2. [LeetCode #658: Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)

---

## Revision Notes

- Problem: Find $k^{\text{th}}$ element of two sorted arrays in $\mathcal{O}(\log(\min(n, m)))$.
- Guard: Ensure `a.size() <= b.size()`.
- Search range: `low = max(0, k - m)`, `high = min(n, k)`.
- `px = (low + high) / 2`, `py = k - px`.
- Boundary variables: `maxLeftA, minRightA, maxLeftB, minRightB` with `INT_MIN/INT_MAX`.
- `if (maxLeftA <= minRightB && maxLeftB <= minRightA) return max(maxLeftA, maxLeftB)`.
- Else adjust `high = px - 1` or `low = px + 1`.
- Optimal Complexity: Time $\mathcal{O}(\log(\min(n, m)))$, Space $\mathcal{O}(1)$.
