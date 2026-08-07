# Problem Summary

Given an integer array `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals `k`. The optimal approach uses **Prefix Sum + Hash Map Frequency Counting**. We track running `prefix_sum` and maintain a hash map of prefix sum frequencies. For each element, we add `prefix_counts[prefix_sum - k]` to our answer in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to count or locate continuous subarrays whose sum equals $K$ (especially when array contains negative numbers).
- Target sum algebraic relationship $P[j] - P[i] = K \implies P[i] = P[j] - K$.

---

## Important Clues

1. **"Subarray sum equals k"**: Subarray sum formula $P[j] - P[i - 1] = k$.
2. **"Negative numbers allowed"**: Sliding window fails; requires Hash Map + Prefix Sum.

---

## Example

### Input
`nums = [1, 1, 1]`, `k = 2`

### Visual Step-by-Step Progression

```text
Map init: {0: 1}

i = 0: num = 1 -> sum = 1 -> look for (1 - 2) = -1 (not found) -> Map: {0:1, 1:1}
i = 1: num = 1 -> sum = 2 -> look for (2 - 2) = 0  (FOUND! +1) -> Map: {0:1, 1:1, 2:1}
i = 2: num = 1 -> sum = 3 -> look for (3 - 2) = 1  (FOUND! +1) -> Map: {0:1, 1:1, 2:1, 3:1}

Total Count: 2
```

---

## Alternative Solutions

### Cumulative Sum Array (O(N^2) Time, O(N) Space)
- Pre-compute prefix sum array `P`.
- Check all pairs `(i, j)` where `P[j] - P[i] == k`.
- **Time Complexity**: $\mathcal{O}(N^2)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **$k = 0$ with zeroes in array**: `nums = [0, 0]`, `k = 0` -> Returns `3`.
2. **Negative elements**: `nums = [1, -1, 1, -1]`, `k = 0` -> Correctly tracks recurring prefix sums.
3. **Single element array**: `nums = [3]`, `k = 3` -> Returns `1`.

---

## Interview Tips

- **Always Explain `prefix_counts[0] = 1`**: State *"We seed the hash map with `{0: 1}` to handle cases where a prefix sum itself equals `k`, representing a valid subarray starting from index 0."*
- **Explain Order of Operations**: Mention querying the map *before* adding the current `prefix_sum` to prevent self-matching when $k = 0$.

---

## Similar Problems

1. [LeetCode #974: Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/)
2. [LeetCode #525: Contiguous Array](https://leetcode.com/problems/contiguous-array/)
3. [LeetCode #523: Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)

---

## Revision Notes

- Problem: Total subarrays summing to $k$.
- Pattern: Prefix Sum + Hash Map.
- Map stores `{prefix_sum : frequency}`, initialized with `{0 : 1}`.
- For each `num` in `nums`:
  - `prefix_sum += num`.
  - `if (map.count(prefix_sum - k)) count += map[prefix_sum - k]`.
  - `map[prefix_sum]++`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(N)$.
