# Problem Summary

Find the length of the longest strictly increasing subsequence in an integer array `nums`. The optimal approach uses **Patience Sorting / Binary Search (`std::lower_bound`)**:
- Maintain dynamic `tails` vector storing smallest tail element of increasing subsequences of each length.
- For each `num` in `nums`:
  - `auto it = lower_bound(tails.begin(), tails.end(), num);`
  - If `it == tails.end()`: `tails.push_back(num);` (extend LIS).
  - Else: `*it = num;` (greedily lower tail value).
- Return `tails.size()`.
This calculates LIS length in $\mathcal{O}(N \log N)$ time and $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need the **length of the longest strictly increasing subsequence / chain**.
- Patience Sorting / Binary Search LIS pattern.

---

## Important Clues

1. **"Longest strictly increasing subsequence"**: LIS pattern.
2. **"O(N log N) time complexity follow-up"**: Patience sorting binary search.

---

## Example

### Input
`nums = [10, 9, 2, 5, 3, 7, 101, 18]`

### Visual Step-by-Step Progression

```text
Elements processed: 10, 9, 2, 5, 3, 7, 101, 18

Tails progression:
[10] -> [9] -> [2] -> [2, 5] -> [2, 3] -> [2, 3, 7] -> [2, 3, 7, 101] -> [2, 3, 7, 18]

Length of tails = 4
```

---

## Alternative Solutions

### 1. 1D Dynamic Programming ($\mathcal{O}(N^2)$ Time, $\mathcal{O}(N)$ Space)
- Maintain `dp[i]` array where `dp[i] = max(1, 1 + dp[j])` for all `j < i` with `nums[j] < nums[i]`.

### 2. Segment Tree / Fenwick Tree ($\mathcal{O}(N \log N)$ Time, $\mathcal{O}(N)$ Space)
- Coordinate compress numbers and query max LIS length in range $[0, \text{num}-1]$.

---

## Edge Cases

1. **Strictly decreasing array**: `nums = [5, 4, 3, 2, 1]` $\implies$ returns `1`.
2. **All identical elements**: `nums = [7, 7, 7, 7]` $\implies$ `lower_bound` replaces index 0, returns `1`.
3. **Single element array**: `nums = [10]` $\implies$ returns `1`.

---

## Interview Tips

- **Explain Why `tails` Doesn't Store the Actual LIS**: State *"The `tails` array stores the smallest tail element for each length $k$ to maximize future expansion probability. While its length is strictly equal to the LIS length, the elements inside `tails` at the end do NOT necessarily form a valid LIS sequence."*

---

## Similar Problems

1. [LeetCode #354: Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/)
2. [LeetCode #673: Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/)
3. [LeetCode #1048: Longest String Chain](https://leetcode.com/problems/longest-string-chain/)

---

## Revision Notes

- Problem: Length of longest strictly increasing subsequence.
- Pattern: Patience Sorting with `std::lower_bound`.
- Loop: `it = lower_bound(tails.begin(), tails.end(), num); if (it == tails.end()) tails.push_back(num); else *it = num;`
- Result: `return tails.size();`
- Optimal Complexity: Time $\mathcal{O}(N \log N)$, Space $\mathcal{O}(N)$.
