# Problem Summary

Given a binary array `nums`, find the maximum length of a contiguous subarray with an equal number of `0`s and `1`s. The optimal approach transforms `0`s into `-1`s and uses **Prefix Sum + Earliest Index Hash Map**. Equal numbers of `0`s and `1`s corresponds to a subarray sum of `0`. By recording the earliest index of each prefix sum, we maximize $i - \text{first\_seen}[\text{sum}]$ in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the longest subarray containing **equal counts of two competing items** (e.g. 0s & 1s, odd & even, positive & negative).
- $+1 / -1$ transformation reduces equal count matching to finding a subarray with sum $0$.

---

## Important Clues

1. **"Equal number of 0s and 1s"**: Replace 0 with -1, search for sum = 0.
2. **"Maximum length"**: Store **earliest index** in Hash Map.

---

## Example

### Input
`nums = [0, 1, 0]`

### Visual Step-by-Step Progression

```text
Transform: [ -1 , +1 , -1 ]
Map init: {0: -1}

i = 0: val = -1 -> sum = -1 -> Map: {0: -1, -1: 0}
i = 1: val = +1 -> sum =  0 -> MATCH at prev_idx -1! len = 1 - (-1) = 2 -> MAX!
i = 2: val = -1 -> sum = -1 -> MATCH at prev_idx  0! len = 2 - 0 = 2

Max Length: 2
```

---

## Alternative Solutions

### Flat Array Hash Map Optimization
- Since `prefix_sum` ranges between $-N$ and $+N$, an integer array `int first_seen[2 * N + 1]` initialized to $-2$ can replace `unordered_map` for $\mathcal{O}(1)$ strict array lookups without hash collisions.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **Entire Array Valid**: `nums = [0, 1, 0, 1]` -> Returns `4`.
2. **No Valid Subarray**: `nums = [1, 1, 1]` -> Returns `0`.
3. **Single Pair at end**: `nums = [1, 1, 0, 1]` -> Returns `2`.

---

## Interview Tips

- **Explain $+1/-1$ Value Mapping**: Start your explanation with *"By mapping every 0 to -1 and every 1 to +1, an equal count of 0s and 1s becomes equivalent to a subarray with sum 0. This allows us to apply the Prefix Sum Hash Map technique."*

---

## Similar Problems

1. [LeetCode #560: Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
2. [LeetCode #523: Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)

---

## Revision Notes

- Problem: Longest contiguous subarray with equal 0s and 1s.
- Strategy: Map `0 -> -1`, `1 -> +1`, Prefix Sum + `first_seen` Hash Map.
- Seed `first_seen[0] = -1`.
- For `i` from `0` to `N - 1`:
  - `prefix_sum += (nums[i] == 1 ? 1 : -1)`.
  - If `first_seen.count(prefix_sum)`:
    - `max_len = max(max_len, i - first_seen[prefix_sum])`.
  - Else:
    - `first_seen[prefix_sum] = i` (store only first appearance!).
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(N)$.
