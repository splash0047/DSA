# Problem Summary

Implement a class `NumArray` that supports answering multiple range sum queries on a static array `nums`. The optimal approach pre-computes a **1D Prefix Sum Array** `pref` of size $N + 1$ in $\mathcal{O}(N)$ constructor time. Each `sumRange(left, right)` query is answered in $\mathcal{O}(1)$ constant time using the formula `pref[right + 1] - pref[left]`, requiring $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to perform multiple **range sum queries** on an array that is **immutable** (never modified after initialization).
- 1D Prefix Sum pre-computation pattern.

---

## Important Clues

1. **"Immutable array"**: Values never change, making static prefix sum pre-computation ideal.
2. **"Multiple sumRange queries"**: Optimizing query time to $\mathcal{O}(1)$ is essential.

---

## Example

### Input
`nums = [-2, 0, 3, -5, 2, -1]`

### Visual Step-by-Step Progression

```text
nums: [ -2 ,  0 ,  3 , -5 ,  2 , -1 ]
pref: [ 0 , -2 , -2 ,  1 , -4 , -2 , -3 ]

Query (2, 5):
  Sum from index 2 to 5 = pref[6] - pref[2]
                        = -3 - (-2) = -1

Query Time: O(1)
```

---

## Alternative Solutions

### Segment Tree / Binary Indexed Tree (Fenwick Tree)
- Build Segment Tree in $\mathcal{O}(N)$ time.
- Query in $\mathcal{O}(\log N)$ time.
- *Overkill for static arrays! Segment trees are only needed when array updates (`update(idx, val)`) occur dynamically.*

---

## Edge Cases

1. **`left = 0`**: `sumRange(0, R)` $\rightarrow$ `pref[R + 1] - pref[0] = pref[R + 1]`.
2. **Single Element Query (`left == right`)**: `sumRange(i, i)` $\rightarrow$ `pref[i + 1] - pref[i] = nums[i]`.
3. **Entire Array Query (`left = 0, right = N - 1`)**: Returns `pref[N]`.

---

## Interview Tips

- **Explain 1-Based Offset Prefix Array Rationale**: State *"By sizing `pref` to $N + 1$ with `pref[0] = 0`, we eliminate special `if (left == 0)` conditional checks inside `sumRange()`."*

---

## Similar Problems

1. [LeetCode #304: Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)
2. [LeetCode #307: Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/)

---

## Revision Notes

- Problem: Immutable array range sum queries `sumRange(L, R)`.
- Strategy: 1D Prefix Sum Array of size $N + 1$.
- Constructor: `pref[0] = 0`, `pref[i+1] = pref[i] + nums[i]`.
- `sumRange(left, right)`: `return pref[right + 1] - pref[left]`.
- Optimal Complexity: Constructor $\mathcal{O}(N)$, Query $\mathcal{O}(1)$, Space $\mathcal{O}(N)$.
