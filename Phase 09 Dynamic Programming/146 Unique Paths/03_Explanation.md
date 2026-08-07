# Problem Summary

Find the number of unique paths for a robot moving from top-left `(0, 0)` to bottom-right `(m-1, n-1)` in an `m x n` grid, moving only **down** or **right**. The optimal approach uses **Combinatorics $\binom{m+n-2}{\min(m-1, n-1)}$**:
- Total moves $= m + n - 2$.
- Number of Down moves $= m - 1$.
- Unique Paths $= \binom{m + n - 2}{m - 1}$.
- Calculate using incremental loop: `res = res * (N - K + i) / i` for `i` from `1` to `K`.
This computes unique paths in $\mathcal{O}(\min(M, N))$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to count **paths in a grid moving only Down and Right**.
- Combinatorics $\binom{N}{K}$ / 2D Grid DP pattern.

---

## Important Clues

1. **"Robot can only move Down or Right"**: Fixed total move count $(m - 1) + (n - 1)$.
2. **"Number of unique paths"**: Combination formula $\binom{m+n-2}{m-1}$.

---

## Example

### Input
`m = 3, n = 2`

### Visual Step-by-Step Progression

```text
Grid (3x2):
S .
. .
. E

Paths:
1. R -> D -> D
2. D -> R -> D
3. D -> D -> R

Combinatorics: C(3+2-2, 3-1) = C(3, 2) = 3

Result: 3
```

---

## Alternative Solutions

### 1D Space-Optimized Grid DP ($\mathcal{O}(M \times N)$ Time, $\mathcal{O}(N)$ Space)
- Maintain `dp[n]` row initialized to 1. `dp[c] += dp[c-1]` for each cell.

---

## Edge Cases

1. **$1 \times 1$ grid**: `m = 1, n = 1` $\implies$ returns `1` (0 moves needed).
2. **Single row / single column**: `m = 1` or `n = 1` $\implies$ returns `1` (only 1 straight path).

---

## Interview Tips

- **Explain Combinatorics Formula Derivation**: State *"To reach the destination in an $M \times N$ grid, any valid path consists of exactly $M-1$ Down moves and $N-1$ Right moves. The total number of unique paths is equivalent to selecting $M-1$ Down moves out of $(M-1) + (N-1) = M+N-2$ total moves, given by $\binom{M+N-2}{M-1}$."*

---

## Similar Problems

1. [LeetCode #63: Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)
2. [LeetCode #64: Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)
3. [LeetCode #174: Dungeon Game](https://leetcode.com/problems/dungeon-game/)

---

## Revision Notes

- Problem: Unique paths in $M \times N$ grid moving Down or Right.
- Pattern: Combinatorics $\binom{m+n-2}{\min(m-1, n-1)}$.
- Formula: `N = m + n - 2; K = min(m-1, n-1); for (i = 1..K) res = res * (N - K + i) / i;`
- Crucial detail: Divide incrementally inside loop to prevent integer overflow.
- Optimal Complexity: Time $\mathcal{O}(\min(M, N))$, Space $\mathcal{O}(1)$.
