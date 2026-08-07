# Problem Summary

Given an integer array `bloomDay`, `m` bouquets, and `k` adjacent flowers per bouquet, find the minimum number of days needed to make `m` bouquets. If impossible (`1LL * m * k > n`), return `-1`. The optimal approach uses **Binary Search on Answer Space** over range $[\min(\text{bloomDay}), \max(\text{bloomDay})]$. On midpoint `day`, we count $k$-adjacent bloomed flowers. If `bouquets >= m`, we record `ans = mid` and contract `high = mid - 1` in $\mathcal{O}(N \log(\max D))$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the **minimum day / time** required to gather $M$ groups of $K$ adjacent bloomed items.
- Binary Search on Answer Space (Monotonic Predicate Function).

---

## Important Clues

1. **"Minimum number of days"**: Answer space search for time/day.
2. **"k adjacent flowers"**: Consecutive bloomed element requirement.

---

## Example

### Input
`bloomDay = [1, 10, 3, 10, 2]`, `m = 3`, `k = 1`

### Visual Step-by-Step Progression

```text
Day 1: [x, _, _, _, _] -> 1 bouquet
Day 2: [x, _, _, _, x] -> 2 bouquets
Day 3: [x, _, x, _, x] -> 3 bouquets (Requirement met!)

Minimum Days: 3
```

---

## Alternative Solutions

### Sequential Days Scan (Brute Force)
- Test days $d = \min(\text{bloomDay}), \dots, \max(\text{bloomDay})$.
- **Time Complexity**: $\mathcal{O}(N \times \max D)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **Impossible Requirement**: `m = 3`, `k = 2`, `n = 5` ($3 \times 2 = 6 > 5$) $\rightarrow$ Returns `-1`.
2. **$k = 1$**: Adjacent condition becomes trivial (any bloomed flower counts).
3. **$m \times k == n$**: Must wait for the last flower to bloom $\rightarrow$ Returns $\max(\text{bloomDay})$.

---

## Interview Tips

- **Explain Long Long Guard**: Mention *"We check `if (1LL * m * k > n)` to prevent integer overflow when multiplying `m` ($10^6$) and `k` ($10^5$)."*

---

## Similar Problems

1. [LeetCode #875: Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)
2. [LeetCode #1011: Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)

---

## Revision Notes

- Problem: Minimum days to make $m$ bouquets of $k$ adjacent flowers.
- Guard: `if (1LL * m * k > n) return -1`.
- Pattern: Binary Search on Answer Space (`low = min`, `high = max`).
- `while (low <= high)`:
  - `mid = low + (high - low) / 2`.
  - Count $k$-adjacent bloomed flowers (`bd <= mid`).
  - `if (bouquets >= m) ans = mid, high = mid - 1`.
  - `else low = mid + 1`.
- Return `ans`.
- Optimal Complexity: Time $\mathcal{O}(N \log(\max D))$, Space $\mathcal{O}(1)$.
