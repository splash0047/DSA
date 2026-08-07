# Problem Summary

Implement a class `NumMatrix` supporting multiple 2D region sum queries on a static matrix. The optimal approach uses a **2D Prefix Sum Array** `pref` of size $(M + 1) \times (N + 1)$ pre-computed in $\mathcal{O}(M \times N)$ time. By applying the 2D Inclusion-Exclusion Principle (`pref[r2+1][c2+1] - pref[r1][c2+1] - pref[r2+1][c1] + pref[r1][c1]`), every region query is answered in $\mathcal{O}(1)$ time and $\mathcal{O}(M \times N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to query sub-rectangle sums on a static 2D grid multiple times.
- 2D Inclusion-Exclusion Prefix Sum pattern.

---

## Important Clues

1. **"2D matrix range query"**: 2D Prefix Sum formulation.
2. **"Multiple sumRegion queries"**: Must optimize query to $\mathcal{O}(1)$.

---

## Example

### Input
`matrix = [[3, 0, 1], [5, 6, 3], [1, 2, 0]]`

### Visual Inclusion-Exclusion Diagram

```text
Full Area (0,0 -> r2,c2)    :   +------------------+
                                |  A  |     B      |
                                |-----+------------|
                                |  C  | Target (X) |
                                +------------------+

Target Area X = Full(0,0 -> r2,c2) - Top(A+B) - Left(A+C) + TopLeft(A)

Formula: pref[r2+1][c2+1] - pref[r1][c2+1] - pref[r2+1][c1] + pref[r1][c1]
Query Time: O(1)
```

---

## Alternative Solutions

### 1D Prefix Sum per Row (O(M) Query Time, O(M * N) Space)
- Pre-compute 1D prefix sums for each row independently.
- `sumRegion` iterates across rows from `r1` to `r2` and adds row sums in $\mathcal{O}(M)$ time per query.
- **Time Complexity**: Constructor $\mathcal{O}(M \times N)$, Query $\mathcal{O}(M)$.
- **Space Complexity**: $\mathcal{O}(M \times N)$.

---

## Edge Cases

1. **Entire 2D Matrix Query**: `sumRegion(0, 0, m-1, n-1)` $\rightarrow$ Returns `pref[m][n]`.
2. **Single Cell Query**: `sumRegion(r, c, r, c)` $\rightarrow$ Returns `matrix[r][c]`.
3. **Single Row Matrix ($M=1$)**: 2D formula reduces cleanly to 1D behavior.

---

## Interview Tips

- **Draw Inclusion-Exclusion Diagram**: On a whiteboard, sketch the 4 overlapping regions to visually prove why adding back `pref[r1][c1]` is mathematically necessary.

---

## Similar Problems

1. [LeetCode #303: Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)
2. [LeetCode #1292: Maximum Side Length of a Square with a Sum Less than or Equal to Threshold](https://leetcode.com/problems/maximum-side-length-of-a-square-with-a-sum-less-than-or-equal-to-threshold/)

---

## Revision Notes

- Problem: 2D matrix region sum query `(r1, c1)` to `(r2, c2)`.
- Pattern: 2D Prefix Sum Array of size $(M + 1) \times (N + 1)$.
- Build: `pref[r][c] = matrix[r-1][c-1] + pref[r-1][c] + pref[r][c-1] - pref[r-1][c-1]`.
- Query: `pref[r2+1][c2+1] - pref[r1][c2+1] - pref[r2+1][c1] + pref[r1][c1]`.
- Optimal Complexity: Constructor $\mathcal{O}(M \times N)$, Query $\mathcal{O}(1)$, Space $\mathcal{O}(M \times N)$.
