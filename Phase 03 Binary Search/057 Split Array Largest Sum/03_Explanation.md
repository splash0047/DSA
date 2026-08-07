# Problem Summary

Given an integer array `nums` and `k`, split `nums` into `k` contiguous non-empty subarrays such that the largest sum among these `k` subarrays is minimized. The optimal approach uses **Binary Search on Answer Space** over range $[\max(\text{nums}), \sum \text{nums}]$. At midpoint limit `mid`, we simulate greedy subarray creation. If required subarrays $\le k$, we record `ans = mid` and contract `high = mid - 1` in $\mathcal{O}(N \log(\sum \text{nums}))$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You are asked to **minimize the maximum sum / workload / distance** when partitioning contiguous elements into $K$ groups.
- Minimax Binary Search on Answer Space pattern.

---

## Important Clues

1. **"Split into k non-empty subarrays"**: Contiguous partitioning.
2. **"Largest sum among these k subarrays is minimized"**: Minimax objective function.

---

## Example

### Input
`nums = [7, 2, 5, 10, 8]`, `k = 2`

### Visual Step-by-Step Progression

```text
Target range: [10 ... 32]

Limit = 18:
Subarray 1: [7, 2, 5] (sum = 14 <= 18)
Subarray 2: [10, 8]   (sum = 18 <= 18)

Total subarrays: 2 <= 2 (Valid! Minimized max sum = 18)
```

---

## Alternative Solutions

### Dynamic Programming (O(N^2 * K) Time, O(N * K) Space)
- `dp[i][m] = min_j(max(sum(nums[i...j]), dp[j+1][m-1]))`.
- **Time Complexity**: $\mathcal{O}(N^2 \times K)$.
- **Space Complexity**: $\mathcal{O}(N \times K)$.

---

## Edge Cases

1. **$k = N$**: Minimum largest sum is $\max(\text{nums})$ (each element in its own subarray).
2. **$k = 1$**: Minimum largest sum is $\sum \text{nums}$ (single subarray containing all elements).
3. **All identical elements**: Handled cleanly by greedy partition.

---

## Interview Tips

- **Highlight Equivalence Across Problems**: Point out *"Split Array Largest Sum (LeetCode #410), Book Allocation Problem (GFG), and Painter's Partition Problem (GFG) are identical problem formulations solved by the exact same Binary Search on Answer Space template."*

---

## Similar Problems

1. [LeetCode #1011: Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
2. [GFG: Book Allocation Problem](https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1)
3. [GFG: Painter's Partition Problem](https://practice.geeksforgeeks.org/problems/the-painters-partition-problem1535/1)

---

## Revision Notes

- Problem: Minimize largest sum when splitting array into $k$ contiguous subarrays.
- Pattern: Binary Search on Answer Space (`low = max(nums)`, `high = sum(nums)`).
- `while (low <= high)`:
  - `mid = low + (high - low) / 2`.
  - Simulate greedy partitioning for `mid`.
  - `if (subarrays_count <= k) ans = mid, high = mid - 1`.
  - `else low = mid + 1`.
- Return `ans`.
- Optimal Complexity: Time $\mathcal{O}(N \log(\sum \text{nums}))$, Space $\mathcal{O}(1)$.
