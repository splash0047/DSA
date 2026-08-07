# Problem Summary

Given a 2D binary matrix of `'0'`s and `'1'`s, find the area of the largest rectangle containing only `'1'`s. The optimal approach converts each row of the matrix into a **1D Histogram**:
1. Maintain `heights[cols]`. If `matrix[r][c] == '1'`, `heights[c]++`; else `heights[c] = 0`.
2. Run **Largest Rectangle in Histogram (LeetCode #84)** using a Monotonic Stack on `heights` at each row base $R$.
3. Update global `max_area`.
This evaluates the maximal rectangle in $\mathcal{O}(R \times C)$ time and $\mathcal{O}(C)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the **largest subgrid / rectangle of identical values** in a 2D matrix.
- 2D Matrix Reduction to 1D Monotonic Stack Histogram pattern.

---

## Important Clues

1. **"Largest rectangle containing only 1s"**: 2D Histogram extension.
2. **"Linear O(R * C) time constraint"**: Row-by-row Monotonic Stack processing.

---

## Example

### Input
```text
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
```

### Visual Step-by-Step Progression

```text
Row 2 Histogram:
heights = [3, 1, 3, 2, 2]

Histogram visualization:
3   3
3 1 3 2 2
Row base: 2
Cols 2..4 form rectangle of height 2 and width 3 -> Area = 6!

Maximal Rectangle Area: 6
```

---

## Alternative Solutions

### Dynamic Programming (O(R * C) Time, O(R * C) Space)
- Maintain `left[c]`, `right[c]`, `height[c]` arrays for each cell to track leftmost and rightmost boundaries of height $H$.
- **Time Complexity**: $\mathcal{O}(R \times C)$.
- **Space Complexity**: $\mathcal{O}(C)$.

---

## Edge Cases

1. **Empty Matrix**: `matrix = []` or `matrix = [[]]` -> Returns `0`.
2. **Matrix of All '0's**: `heights` stay 0 $\implies$ Returns `0`.
3. **Single Cell Matrix**: `[["1"]]` -> Returns `1`.

---

## Interview Tips

- **Highlight Modular Reduction**: State *"Maximal Rectangle (LeetCode #85) is an elegant 2D generalization of Largest Rectangle in Histogram (LeetCode #84). By maintaining a 1D column height array and updating it at each row $R$, we reduce a 2D matrix problem into $R$ 1D histogram sub-problems solved in $\mathcal{O}(C)$ time each."*

---

## Similar Problems

1. [LeetCode #84: Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)
2. [LeetCode #221: Maximal Square](https://leetcode.com/problems/maximal-square/)
3. [LeetCode #1277: Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)

---

## Revision Notes

- Problem: Largest rectangle of `'1'`s in binary matrix.
- Pattern: Dynamic Histogram + Monotonic Stack (`heights` array of size $C$).
- Loop row `r` from `0` to `R - 1`:
  - `if (matrix[r][c] == '1') heights[c]++` else `heights[c] = 0`.
  - `max_area = max(max_area, largestRectangleArea(heights))`.
- Sub-routine: Monotonic Increasing Stack (LeetCode #84).
- Optimal Complexity: Time $\mathcal{O}(R \times C)$, Space $\mathcal{O}(C)$.
