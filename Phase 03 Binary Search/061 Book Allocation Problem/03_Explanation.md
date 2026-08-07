# Problem Summary

Given `n` books with page counts `arr` and `m` students, allocate contiguous books to all $m$ students such that the maximum pages assigned to any student is **minimized**. The optimal approach uses **Binary Search on Answer Space** over range $[\max(\text{arr}), \sum \text{arr}]$. At midpoint limit `mid`, we simulate greedy allocation. If required students $\le m$, we record `ans = mid` and contract `high = mid - 1` in $\mathcal{O}(N \log(\sum \text{arr}))$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **minimize the maximum allocation** of contiguous items among $M$ recipients.
- Minimax Binary Search on Answer Space pattern.

---

## Important Clues

1. **"Books allocated in contiguous order"**: Sequential subarray partitioning.
2. **"Maximum number of pages is minimized"**: Minimax objective function.

---

## Example

### Input
`arr = [12, 34, 67, 90]`, `m = 2`

### Visual Step-by-Step Progression

```text
Page Limit = 113:
Student 1: 12 + 34 + 67 = 113
Student 2: 90

Both students <= 113 pages! Minimum maximum pages = 113.
```

---

## Alternative Solutions

### Dynamic Programming (O(N^2 * M) Time, O(N * M) Space)
- `dp[i][j] = min_k(max(sum(arr[k...i]), dp[k-1][j-1]))`.
- **Time Complexity**: $\mathcal{O}(N^2 \times M)$.
- **Space Complexity**: $\mathcal{O}(N \times M)$.

---

## Edge Cases

1. **`m > n`**: Impossible to allocate $\rightarrow$ Returns `-1`.
2. **`m == n`**: Every student gets 1 book $\rightarrow$ Returns $\max(\text{arr})$.
3. **`m == 1`**: Single student reads all books $\rightarrow$ Returns $\sum \text{arr}$.

---

## Interview Tips

- **Highlight Template Universality**: State *"Book Allocation Problem, Painter's Partition Problem, and Split Array Largest Sum are identical variants of Binary Search on Answer Space with range $[\max, \sum]$."*

---

## Similar Problems

1. [LeetCode #410: Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)
2. [GFG: Painter's Partition Problem](https://practice.geeksforgeeks.org/problems/the-painters-partition-problem1535/1)
3. [LeetCode #1011: Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)

---

## Revision Notes

- Problem: Minimize maximum pages allocated to $m$ students.
- Guard: `if (m > n) return -1`.
- Pattern: Binary Search on Answer Space (`low = max`, `high = sum`).
- `while (low <= high)`:
  - `mid = low + (high - low) / 2`.
  - Simulate greedy allocation for `mid`.
  - `if (students <= m) ans = mid, high = mid - 1`.
  - `else low = mid + 1`.
- Return `ans`.
- Optimal Complexity: Time $\mathcal{O}(N \log(\sum \text{arr}))$, Space $\mathcal{O}(1)$.
