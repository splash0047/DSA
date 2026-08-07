# Problem Summary

Given an integer array `nums` and an integer `k`, return `true` if there exists a contiguous subarray of **length at least 2** whose sum is a multiple of `k`. The optimal solution uses **Prefix Sum + Hash Map (Earliest Index Tracking)**. We store the first occurrence index of each prefix sum remainder modulo `k`. If a remainder recurs at index `i` with `i - prev_index >= 2`, we return `true` in $\mathcal{O}(N)$ time and $\mathcal{O}(\min(N, K))$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to check for a contiguous subarray whose sum is a multiple of $K$ with a **minimum length constraint** (e.g. length $\ge 2$).
- Storing **earliest index** in a Hash Map to measure window length.

---

## Important Clues

1. **"Length at least two"**: Index gap $i - \text{prev\_index} \ge 2$.
2. **"Sum is a multiple of k"**: Congruence relation $P[i] \pmod k = P[j] \pmod k$.

---

## Example

### Input
`nums = [23, 2, 4, 6, 7]`, `k = 6`

### Visual Step-by-Step Progression

```text
Map init: {0: -1}

i = 0: num = 23 -> sum = 23 -> rem = 5 -> map {0: -1, 5: 0}
i = 1: num = 2  -> sum = 25 -> rem = 1 -> map {0: -1, 5: 0, 1: 1}
i = 2: num = 4  -> sum = 29 -> rem = 5 -> MATCH at prev_idx 0!
       Length = 2 - 0 = 2 >= 2 -> Return true!

Subarray: [2, 4] (sum = 6)
```

---

## Alternative Solutions

### Cumulative Sum Array (O(N^2) Time, O(N) Space)
- Compute prefix sum array `P`.
- Check all pairs `(i, j)` where `j - i >= 2` and `(P[j] - P[i]) % k == 0`.
- **Time Complexity**: $\mathcal{O}(N^2)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **Zeroes in Input**: `nums = [0, 0]`, `k = 1` -> Returns `true` (sum 0 is multiple of 1, length 2).
2. **Subarray starting at index 0**: `nums = [5, 0, 0]`, `k = 5` -> `remainder_map[0] = -1` validates length $2 - (-1) = 3 \ge 2$.
3. **Length 1 Multiple**: `nums = [6]`, `k = 6` -> Returns `false` (length is only 1).

---

## Interview Tips

- **Explain Why We Only Store EARLIEST Index**: State *"To maximize the length of a candidate subarray $i - \text{prev\_index}$, we must store only the EARLIEST index at which each remainder occurs. Updating the map with later indices would shrink the window length."*

---

## Similar Problems

1. [LeetCode #974: Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/)
2. [LeetCode #525: Contiguous Array](https://leetcode.com/problems/contiguous-array/)

---

## Revision Notes

- Problem: Check if continuous subarray of length $\ge 2$ has sum divisible by $k$.
- Strategy: Prefix Sum Modulo + Earliest Index Hash Map.
- Seed `remainder_map[0] = -1`.
- For `i` from `0` to `N - 1`:
  - `prefix_sum += nums[i]`.
  - `rem = prefix_sum % k`.
  - If `map.count(rem)`:
    - If `i - map[rem] >= 2` return `true`.
  - Else:
    - `map[rem] = i` (store only first appearance!).
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(\min(N, K))$.
