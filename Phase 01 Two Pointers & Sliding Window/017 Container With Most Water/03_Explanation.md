# Problem Summary

Given an array `height` representing vertical line heights, find two lines that form a container holding the maximum area of water. The optimal approach uses **Two Pointers (Boundary Shrinking)** starting at `left = 0` and `right = N - 1`. At each step, calculate `area = min(height[left], height[right]) * (right - left)`, update `max_water`, and advance the pointer pointing to the **shorter line** in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to maximize a 2-variable product function $f(i, j) = \min(A[i], A[j]) \times (j - i)$.
- Shrinking boundary logic allows greedy pruning of unpromising pairs.

---

## Important Clues

1. **"Container containing most water"**: Area formula $\min(h_i, h_j) \times (j - i)$.
2. **"May not slant container"**: Height is strictly limited by the shorter line.

---

## Example

### Input
`height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`

### Visual Step-by-Step Progression

```text
L -> [ 1 , 8 , 6 , 2 , 5 , 4 , 8 , 3 , 7 ] <- R   (area = 1 * 8 = 8, move L)

     [ 1 , 8 , 6 , 2 , 5 , 4 , 8 , 3 , 7 ] <- R   (area = 7 * 7 = 49 -> MAX!)
           L

Final Max Area: 49
```

---

## Alternative Solutions

### Brute Force Pairwise Evaluation
- Test all pairs $(i, j)$ in $\mathcal{O}(N^2)$ time and $\mathcal{O}(1)$ space. (Causes TLE).

---

## Edge Cases

1. **Minimum Size Array**: `height = [1, 1]` -> Returns `1`.
2. **Strictly Increasing Heights**: `height = [1, 2, 3, 4, 5]` -> Evaluated correctly.
3. **Strictly Decreasing Heights**: `height = [5, 4, 3, 2, 1]` -> Evaluated correctly.

---

## Interview Tips

- **Prove the Greedy Choice**: Be ready to explain: *"Why do we move the shorter line? Because if we keep the shorter line and decrease the width, the area can NEVER exceed the current area. So we can safely discard the shorter line."*

---

## Similar Problems

1. [LeetCode #42: Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
2. [LeetCode #407: Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/)

---

## Revision Notes

- Problem: Find max water area $\min(h_i, h_j) \times (j - i)$.
- Strategy: Two Pointers (`left = 0`, `right = N - 1`).
- `while (left < right)`:
  - `area = min(height[left], height[right]) * (right - left)`.
  - `max_water = max(max_water, area)`.
  - If `height[left] < height[right]`: `left++`.
  - Else: `right--`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
