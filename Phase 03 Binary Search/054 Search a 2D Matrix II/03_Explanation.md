# Problem Summary

Given an $M \times N$ matrix where rows and columns are independently sorted in ascending order, search for `target`. The optimal approach starts at the **Top-Right Corner** `(0, N-1)`. Moving left decreases values (`c--`) while moving down increases values (`r++`), operating like a Binary Search Tree to find `target` in $\mathcal{O}(M + N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- An $M \times N$ matrix has **independently sorted rows and columns**.
- Top-Right (or Bottom-Left) corner BST traversal pattern.

---

## Important Clues

1. **"Rows sorted left-to-right AND columns sorted top-to-bottom"**: 2D Search Space reduction from corner.
2. **"Difference between Matrix I and Matrix II"**: Matrix I is flat sorted $\implies \mathcal{O}(\log(M \times N))$; Matrix II is independently row/col sorted $\implies \mathcal{O}(M + N)$.

---

## Example

### Input
`matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22]]`, `target = 5`

### Visual Step-by-Step Progression

```text
Start at Top-Right Corner (0, 4):
[ 1 ,  4 ,  7 , 11 , 15 ] <- val 15 > 5 -> Move Left (c=3)
                     11   <- val 11 > 5 -> Move Left (c=2)
                      7   <- val  7 > 5 -> Move Left (c=1)
                      4   <- val  4 < 5 -> Move Down (r=1)

[ 2 ,  5 ,  8 , 12 , 19 ]
       ^ (val 5 == 5 -> MATCH!)

Result: true
```

---

## Alternative Solutions

### Divide and Conquer (Matrix Quad-Split)
- Divide matrix into 4 sub-quadrants around midpoint cell `(mid_r, mid_c)`. Recursively eliminate 1 quadrant.
- **Time Complexity**: $\mathcal{O}(N^{\log_2 3}) \approx \mathcal{O}(N^{1.58})$.
- **Space Complexity**: $\mathcal{O}(\log N)$ recursion stack.

---

## Edge Cases

1. **Target Smaller Than Top-Left `(0, 0)`**: Immediately terminates at `c < 0` $\rightarrow$ `false`.
2. **Target Larger Than Bottom-Right `(M-1, N-1)`**: Terminates at `r >= M` $\rightarrow$ `false`.
3. **Single Cell Matrix**: `matrix = [[5]]`, `target = 5` -> Returns `true`.

---

## Interview Tips

- **Explain Why Corner Choice Matters**: State *"Starting at Top-Right `(0, N-1)` or Bottom-Left `(M-1, 0)` provides deterministic orthogonal choices (one direction increases value, the other decreases value). Starting at Top-Left `(0, 0)` or Bottom-Right `(M-1, N-1)` creates ambiguity because both available directions move in the same relative magnitude."*

---

## Similar Problems

1. [LeetCode #74: Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
2. [LeetCode #378: Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

---

## Revision Notes

- Problem: Search target in row & col sorted $M \times N$ matrix.
- Pattern: Top-Right Corner Traversal (`r = 0, c = N - 1`).
- `while (r < M && c >= 0)`:
  - `if (matrix[r][c] == target) return true`.
  - `else if (matrix[r][c] > target) c--`.
  - `else r++`.
- Return `false`.
- Optimal Complexity: Time $\mathcal{O}(M + N)$, Space $\mathcal{O}(1)$.
