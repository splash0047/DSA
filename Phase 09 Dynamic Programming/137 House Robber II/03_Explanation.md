# Problem Summary

Determine the maximum money you can rob from houses arranged in a **circle** (house `0` is adjacent to house `n-1`) without robbing adjacent houses. The optimal approach uses **Circular Array Splitting**:
- Edge case: `if (n == 1) return nums[0];`
- Run linear House Robber DP on range `[0, n-2]` (excludes last house).
- Run linear House Robber DP on range `[1, n-1]` (excludes first house).
- Return `max(robRange(0, n-2), robRange(1, n-1))`.
This evaluates circular house robbing in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You have a **circular constraint where end elements are adjacent**.
- Circular Array Splitting into 2 Linear Subproblems pattern.

---

## Important Clues

1. **"Houses arranged in a circle"**: First and last houses are adjacent.
2. **"Cannot rob adjacent houses"**: Must exclude at least one end house (`0` or `n-1`).

---

## Example

### Input
`nums = [2, 3, 2]`

### Visual Step-by-Step Progression

```text
Circular Array: 2 - 3 - 2 (in a loop)

Case 1 (Exclude last 2):
Array [2, 3] -> Max loot = 3

Case 2 (Exclude first 2):
Array [3, 2] -> Max loot = 3

Max(3, 3) = 3
```

---

## Alternative Solutions

### Vector Slicing ($\mathcal{O}(N)$ Time, $\mathcal{O}(N)$ Space)
- Create explicit sub-vectors `nums[0...n-2]` and `nums[1...n-1]`.

---

## Edge Cases

1. **Single house**: `nums = [1]` $\implies$ returns `1` (crucial `n == 1` check).
2. **Two houses**: `nums = [2, 3]` $\implies$ returns `max(2, 3) = 3`.
3. **Three identical houses**: `nums = [3, 3, 3]` $\implies$ returns `3`.

---

## Interview Tips

- **Explain Circular Splitting Logic**: State *"Because the first and last houses are neighbors, robbing both is impossible. Therefore, the global optimum MUST lie in either excluding the last house `[0, n-2]` or excluding the first house `[1, n-1]`. Evaluating linear DP on both ranges guarantees finding the global maximum."*

---

## Similar Problems

1. [LeetCode #198: House Robber](https://leetcode.com/problems/house-robber/)
2. [LeetCode #337: House Robber III](https://leetcode.com/problems/house-robber-iii/)
3. [LeetCode #1388: Pizza With 3n Slices](https://leetcode.com/problems/pizza-with-3n-slices/)

---

## Revision Notes

- Problem: House robbing with circular adjacency constraint.
- Pattern: Range DP `max(range(0, n-2), range(1, n-1))`.
- Base case: `if (n == 1) return nums[0];`
- `robRange(start, end)`: Standard linear DP with `prev1`, `prev2`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
