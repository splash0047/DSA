# Problem Summary

Given an $M \times N$ matrix where each row is sorted and `matrix[i][0] > matrix[i-1][N-1]`, determine if `target` exists in the matrix. The optimal approach treats the entire matrix as a **Virtual 1D Array** of length $M \times N$. Using binary search on range `[0 ... (M * N) - 1]`, 1D index `mid` maps to 2D cell `matrix[mid / N][mid % N]` in $\mathcal{O}(1)$ time, finding `target` in $\mathcal{O}(\log(M \times N))$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- A 2D matrix is sorted sequentially across rows such that `matrix[i][0] > matrix[i-1][n-1]`.
- Virtual 1D Binary Search pattern.

---

## Important Clues

1. **"First integer of each row is greater than last integer of previous row"**: Signals matrix can be flattened into a single sorted 1D array.
2. **"O(log(m * n)) time"**: Single binary search requirement.

---

## Example

### Input
`matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]`, `target = 3`

### Visual Step-by-Step Progression

```text
2D Matrix:
[ 1 ,  3 ,  5 ,  7 ]
[10 , 11 , 16 , 20 ]
[23 , 30 , 34 , 60 ]

Virtual 1D Array (Length 12):
[1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]

Binary Search mid=1 -> matrix[1/4][1%4] = matrix[0][1] = 3 == 3 -> MATCH!
```

---

## Alternative Solutions

### Two-Step Binary Search (Row then Column)
1. Binary search on first column `matrix[i][0]` to identify candidate row `R` in $\mathcal{O}(\log M)$.
2. Binary search inside row `R` for `target` in $\mathcal{O}(\log N)$.
- **Time Complexity**: $\mathcal{O}(\log M + \log N) = \mathcal{O}(\log(M \times N))$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **Single Cell Matrix**: `matrix = [[5]]`, `target = 5` -> Returns `true`.
2. **Target Smaller Than Minimum**: `matrix = [[1, 3]]`, `target = 0` -> Returns `false`.
3. **Target Larger Than Maximum**: `matrix = [[1, 3]]`, `target = 5` -> Returns `false`.

---

## Interview Tips

- **Explain Index Conversion Math**: Clearly state *"For any 1D index `idx` in an $M \times N$ matrix, the row index is `idx / N` (integer division by column count) and the column index is `idx % N` (modulo by column count)."*

---

## Similar Problems

1. [LeetCode #240: Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)
2. [LeetCode #704: Binary Search](https://leetcode.com/problems/binary-search/)

---

## Revision Notes

- Problem: Search target in $M \times N$ sorted matrix in $\mathcal{O}(\log(M \times N))$.
- Pattern: Virtual 1D Binary Search.
- `low = 0`, `high = M * N - 1`.
- `while (low <= high)`:
  - `mid = low + (high - low) / 2`.
  - `val = matrix[mid / N][mid % N]`.
  - `if (val == target) return true`.
  - `else if (val < target) low = mid + 1`.
  - `else high = mid - 1`.
- Return `false`.
- Optimal Complexity: Time $\mathcal{O}(\log(M \times N))$, Space $\mathcal{O}(1)$.
