# Problem Summary

Given package weights `weights` and a deadline of `days` days, find the minimum ship weight capacity to ship all packages in order. The optimal approach uses **Binary Search on Answer Space** over range $[\max(W), \sum W]$. At midpoint capacity `mid`, we simulate day-by-day loading. If `days_needed <= days`, we record `ans = mid` and contract `high = mid - 1`, finding minimum capacity in $\mathcal{O}(N \log(\sum W))$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the **least capacity / threshold** to process sequential tasks within $D$ time units.
- Binary Search on Answer Space (Monotonic Feasibility Function).

---

## Important Clues

1. **"Least weight capacity of the ship"**: Minimum answer space search.
2. **"In the order given"**: Sequential allocation constraint.

---

## Example

### Input
`weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, `days = 5`

### Visual Step-by-Step Progression

```text
Cap range: [10 ... 55]

Day 1 (Cap 15): 1 + 2 + 3 + 4 + 5 = 15
Day 2 (Cap 15): 6 + 7 = 13
Day 3 (Cap 15): 8
Day 4 (Cap 15): 9
Day 5 (Cap 15): 10

Total Days: 5 <= 5 (Valid minimum capacity = 15!)
```

---

## Alternative Solutions

### Sequential Capacity Testing (Brute Force)
- Test capacities $C = \max(W), \max(W)+1, \dots$ until `days_needed <= days`.
- **Time Complexity**: $\mathcal{O}(N \times \sum W)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **`days == weights.length`**: Minimum capacity equals $\max(W)$.
2. **`days == 1`**: Minimum capacity equals $\sum W$.
3. **Identical Package Weights**: Handled smoothly by simulation loop.

---

## Interview Tips

- **Explain Lower Bound Rationale**: State *"The minimum possible capacity MUST be at least $\max(\text{weights})$, because the ship must be capable of carrying the single heaviest package on the belt."*

---

## Similar Problems

1. [LeetCode #875: Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)
2. [LeetCode #410: Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)
3. [LeetCode #1482: Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)

---

## Revision Notes

- Problem: Least ship capacity to deliver packages within $D$ days.
- Pattern: Binary Search on Answer Space (`low = max(W)`, `high = sum(W)`).
- `while (low <= high)`:
  - `mid = low + (high - low) / 2`.
  - Simulate greedy day allocation for `mid`.
  - `if (days_needed <= days) ans = mid, high = mid - 1`.
  - `else low = mid + 1`.
- Return `ans`.
- Optimal Complexity: Time $\mathcal{O}(N \log(\sum W))$, Space $\mathcal{O}(1)$.
