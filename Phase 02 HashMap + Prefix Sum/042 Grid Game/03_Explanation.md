# Problem Summary

Two robots play a game on a $2 \times N$ grid moving right and down. Robot 1 wants to **minimize** Robot 2's maximum score, while Robot 2 wants to **maximize** its score. When Robot 1 transitions to Row 1 at column `i`, Robot 2 can only collect either the remaining elements on Row 0 (`top_sum`) or remaining elements on Row 1 (`bottom_sum`). The optimal approach uses **Prefix / Suffix Sums** to update `top_sum` and `bottom_sum` in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- Two non-overlapping paths on a 2-row grid compete in a Minimax game.
- Prefix / Suffix Sum split strategy applies cleanly to 2-row grids.

---

## Important Clues

1. **"2 x N grid, move right & down only"**: Robot 1 can only change row ONCE at some column $i \in [0, N-1]$.
2. **"Robot 1 minimizes Robot 2's max score"**: Minimax calculation: $\min_i \max(\text{top\_rem}_i, \text{bottom\_rem}_i)$.

---

## Example

### Input
`grid = [[2, 5, 4], [1, 5, 1]]`

### Visual Step-by-Step Progression

```text
Robot 1 drops at col 1:
[ 0 , 0 , 4 ]  <- Top remaining for Robot 2: 4
[ 1 , 0 , 0 ]  <- Bottom remaining for Robot 2: 1

Robot 2 score = max(4, 1) = 4 (MINIMIZED!)

Result: 4
```

---

## Alternative Solutions

### 1D Prefix Sum Arrays
- Compute `prefix_top` and `prefix_bot` arrays of size $N$.
- Loop $i$ from $0$ to $N-1$:
  - `r2 = max(prefix_top[N-1] - prefix_top[i], prefix_bot[i-1])`.
  - `result = min(result, r2)`.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **$N = 1$**: `grid = [[3], [2]]` -> Robot 1 takes both cells, Robot 2 gets `0`.
2. **Large Grid Values**: Sum exceeds $2^{31} - 1$; use `long long`.
3. **All identical values**: Robot 1 drops in middle to split remaining regions evenly.

---

## Interview Tips

- **Explain Why Robot 2 Only Has 2 Choices**: State *"Because Robot 1 zeroes out `(0, 0...i)` and `(1, i...N-1)`, Robot 2 can either stay on Row 0 until the end (getting `top_sum`), or immediately drop to Row 1 at column 0 (getting `bottom_sum`). Any other path collects strictly less."*

---

## Similar Problems

1. [LeetCode #1074: Number of Submatrices That Sum to Target](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/)
2. [LeetCode #1524: Number of Sub-arrays With Odd Sum](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/)

---

## Revision Notes

- Problem: Minimax score for Robot 2 on $2 \times N$ grid.
- Strategy: Prefix/Suffix Sum split.
- `top_sum = sum(grid[0])`, `bottom_sum = 0`, `result = INF`.
- Loop `i` from `0` to `N - 1`:
  - `top_sum -= grid[0][i]`.
  - `result = min(result, max(top_sum, bottom_sum))`.
  - `bottom_sum += grid[1][i]`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
