# Problem Summary

Given an integer array `nums` and a `target`, find all unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` summing to `target`. The optimal approach sorts the array, fixes `nums[i]` and `nums[j]` in two outer loops, and uses **Two Pointers** (`left = j + 1`, `right = N - 1`) with `long long` sum casting and adjacent duplicate skipping to complete in $\mathcal{O}(N^3)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find $K$ elements summing to a target ($K = 4$).
- Generalizing Two Pointers by adding nested outer loops for $K > 2$.

---

## Important Clues

1. **"Unique quadruplets"**: Requires duplicate prevention.
2. **"Sum equals target"**: K-Sum formulation.
3. **Large target/elements range ($-10^9 \le \text{nums}[i] \le 10^9$)**: Signals potential integer overflow; use `long long`.

---

## Example

### Input
`nums = [1, 0, -1, 0, -2, 2]`, `target = 0`

### Visual Step-by-Step Progression

```text
Sort: [-2, -1, 0, 0, 1, 2]

Fix i=0 (-2), j=1 (-1):
  L=4 (1), R=5 (2) -> sum = -2 + -1 + 1 + 2 = 0 -> Found [-2, -1, 1, 2]

Fix i=0 (-2), j=2 (0):
  L=3 (0), R=5 (2) -> sum = -2 + 0 + 0 + 2 = 0 -> Found [-2, 0, 0, 2]

Fix i=1 (-1), j=2 (0):
  L=3 (0), R=4 (1) -> sum = -1 + 0 + 0 + 1 = 0 -> Found [-1, 0, 0, 1]

Result: [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]
```

---

## Alternative Solutions

### Recursive K-Sum Solver
Generalize K-Sum using recursion:
- Base case $K = 2$: Two Pointers.
- Recursive case $K > 2$: Outer loop for current index, recurse on $K - 1$ sum.
- **Time Complexity**: $\mathcal{O}(N^{K-1})$.
- **Space Complexity**: $\mathcal{O}(K)$ recursion stack.

---

## Edge Cases

1. **Fewer than 4 elements**: `nums = [1, 2, 3]` -> Returns `[]`.
2. **Integer Overflow**: `nums = [1000000000, 1000000000, 1000000000, 1000000000]`, `target = 0` -> Handled safely via `long long`.
3. **All Identical Elements**: `nums = [2, 2, 2, 2, 2]`, `target = 8` -> Returns `[[2, 2, 2, 2]]`.

---

## Interview Tips

- **Mention General K-Sum Recursion**: Show breadth of knowledge by mentioning that 4Sum can be cleanly generalized to any $K$-Sum using a recursive solver with base case $K=2$.
- **Highlight Integer Overflow Guard**: Mention casting `(long long)nums[i] + nums[j] + nums[left] + nums[right]` to prevent integer overflow bugs.

---

## Similar Problems

1. [LeetCode #15: 3Sum](https://leetcode.com/problems/3sum/)
2. [LeetCode #454: 4Sum II](https://leetcode.com/problems/4sum-ii/)

---

## Revision Notes

- Problem: Find all unique quadruplets summing to target.
- Strategy: Sort + 2 Outer Loops + Two Pointers.
- `if (n < 4) return {}`.
- Loop `i` from `0` to `N-4`: skip duplicate `nums[i]`.
- Loop `j` from `i+1` to `N-3`: skip duplicate `nums[j]`.
- `left = j + 1`, `right = N - 1`.
- `sum = (long long)nums[i] + nums[j] + nums[left] + nums[right]`.
- `sum == target`: add quad, skip duplicate `left`/`right`, `left++`, `right--`.
- Optimal Complexity: Time $\mathcal{O}(N^3)$, Space $\mathcal{O}(1)$.
