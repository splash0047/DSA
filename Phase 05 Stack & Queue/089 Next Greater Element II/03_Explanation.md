# Problem Summary

Given a circular integer array `nums`, find the Next Greater Element for every element in `nums` searching circularly. The optimal approach uses a **Monotonic Decreasing Stack over a Virtual $2N$ Iteration**:
1. Loop `i` backward from `2N - 1` down to `0`. Access `curr = nums[i % N]`.
2. While `!st.empty() && st.top() <= curr`: `st.pop()`.
3. When $i < N$: `ans[i] = st.empty() ? -1 : st.top()`.
4. `st.push(curr)`.
This evaluates circular Next Greater Elements in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find **Next Greater / Smaller Elements in a circular array**.
- Monotonic Stack + Virtual $2N$ Modulo Traversal pattern.

---

## Important Clues

1. **"Circular integer array"**: Index modulo $i \pmod N$ wrap-around.
2. **"Search circularly for next greater number"**: $2N$ virtual iteration.

---

## Example

### Input
`nums = [1, 2, 1]`

### Visual Step-by-Step Progression

```text
Virtual Concatenated Array: [1, 2, 1,   1, 2, 1]

Backward Pass (i = 5 down to 0):
i = 2 (val 1) -> Next Greater is 2 (wrapped from second half)
i = 1 (val 2) -> No greater element -> -1
i = 0 (val 1) -> Next Greater is 2

Result: [2, -1, 2]
```

---

## Alternative Solutions

### Double Loop Circular Search (Brute Force)
- For each `i`, scan `(i + j) % N` for $j \in [1, N-1]$.
- **Time Complexity**: $\mathcal{O}(N^2)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **All Identical Elements**: `[5, 5, 5]` -> Returns `[-1, -1, -1]`.
2. **Strictly Decreasing Circular Array**: `[3, 2, 1]` -> Wraps around: `3 -> -1`, `2 -> 3`, `1 -> 3` $\implies$ `[-1, 3, 3]`.
3. **Single Element Array**: `[7]` -> Returns `[-1]`.

---

## Interview Tips

- **Explain Virtual Modulo vs Vector Doubling**: State *"Instead of allocating a physical $2N$ array which uses double memory, we simulate traversing $2N$ elements by looping `i` from `2N - 1` down to `0` and accessing `nums[i % N]`, saving memory while maintaining $\mathcal{O}(N)$ time."*

---

## Similar Problems

1. [LeetCode #496: Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)
2. [LeetCode #739: Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
3. [LeetCode #901: Online Stock Span](https://leetcode.com/problems/online-stock-span/)

---

## Revision Notes

- Problem: Next Greater Element in circular array `nums`.
- Pattern: Monotonic Decreasing Stack (`stack<int> st`) over $2N$ virtual iterations.
- Loop `i` from `2 * N - 1` down to `0`:
  - `curr = nums[i % N]`.
  - `while (!st.empty() && st.top() <= curr) st.pop()`.
  - `if (i < N) ans[i] = st.empty() ? -1 : st.top()`.
  - `st.push(curr)`.
- Return `ans`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(N)$.
