# Problem Summary

Given an integer array `nums` and an integer `k`, return the number of non-empty contiguous subarrays whose sum is divisible by `k`. The optimal approach uses **Prefix Sum + Modulo Frequency Table**. If two prefix sums have the same remainder modulo `k`, the subarray between them is divisible by `k`. Normalizing remainders via `((rem % k) + k) % k` yields $\mathcal{O}(N)$ time and $\mathcal{O}(K)$ space complexity.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to count continuous subarrays whose sum satisfies a **divisibility / modulo condition** ($S \pmod K = 0$).
- Remainder equality property: $P[j] \pmod K = P[i] \pmod K \implies (P[j] - P[i]) \pmod K = 0$.

---

## Important Clues

1. **"Sum divisible by k"**: Remainder modulo $k$ matching.
2. **"Negative numbers in input"**: Requires normalized remainder math `((rem % k) + k) % k`.

---

## Example

### Input
`nums = [4, 5, 0, -2, -3, 1]`, `k = 5`

### Visual Step-by-Step Progression

```text
Rem Table (mod 5):
Init: [0:1]

num=4 -> rem=4 -> count+=0 -> table [0:1, 4:1]
num=5 -> rem=4 -> count+=1 -> table [0:1, 4:2]
num=0 -> rem=4 -> count+=2 -> table [0:1, 4:3]
num=-2-> rem=2 -> count+=0 -> table [0:1, 2:1, 4:3]
num=-3-> rem=4 -> count+=3 -> table [0:1, 2:1, 4:4]
num=1 -> rem=0 -> count+=1 -> table [0:2, 2:1, 4:4]

Total Count: 7
```

---

## Alternative Solutions

### Hash Map instead of Vector
- Use `std::unordered_map<int, int>` for remainder tracking.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(\min(N, K))$.

---

## Edge Cases

1. **Negative numbers producing negative remainders**: Handled by `((rem % k) + k) % k`.
2. **$k > N$**: Handled properly; vector size $K$ handles any valid $K$.
3. **Entire array sum divisible by $k$**: Handled by `mod_counts[0] = 1`.

---

## Interview Tips

- **Explain Remainder Normalization**: Explicitly highlight *"In C++, negative integers produce negative modulo results (e.g. `-2 % 5 = -2`). To map remainders to a valid array index `[0, k - 1]`, we use `((rem % k) + k) % k`."*

---

## Similar Problems

1. [LeetCode #560: Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
2. [LeetCode #523: Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)

---

## Revision Notes

- Problem: Total subarrays whose sum is divisible by $k$.
- Pattern: Prefix Sum + Normalized Modulo Table `mod_counts[k]`.
- Seed `mod_counts[0] = 1`.
- For each `num` in `nums`:
  - `prefix_sum += num`.
  - `rem = ((prefix_sum % k) + k) % k`.
  - `count += mod_counts[rem]`.
  - `mod_counts[rem]++`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(K)$.
