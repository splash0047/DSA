# Problem Summary

Determine the maximum money you can rob from an array of houses `nums` without robbing two adjacent houses. The optimal approach uses **Space-Optimized Include/Exclude DP**:
- Maintain `prev2 = 0` (max loot 2 houses ago) and `prev1 = 0` (max loot 1 house ago).
- Iterate `num` in `nums`:
  - `curr = max(num + prev2, prev1);`
  - `prev2 = prev1; prev1 = curr;`
- Return `prev1`.
This calculates max loot in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **maximize/minimize total value by picking elements with non-adjacent constraints**.
- Include / Exclude DP pattern.

---

## Important Clues

1. **"Cannot rob two adjacent houses"**: Non-adjacent selection constraint.
2. **"Maximum amount of money"**: Optimization subproblem.

---

## Example

### Input
`nums = [2, 7, 9, 3, 1]`

### Visual Step-by-Step Progression

```text
Houses: [2, 7, 9, 3, 1]

- House 1 (2): max(2+0, 0)  = 2
- House 2 (7): max(7+0, 2)  = 7
- House 3 (9): max(9+2, 7)  = 11 (Rob 2 + 9)
- House 4 (3): max(3+7, 11) = 11
- House 5 (1): max(1+11, 11)= 12 (Rob 2 + 9 + 1)

Result: 12
```

---

## Alternative Solutions

### 1. 1D DP Array ($\mathcal{O}(N)$ Time, $\mathcal{O}(N)$ Space)
- Maintain `dp[N]` array where `dp[i] = max(nums[i] + dp[i-2], dp[i-1])`.

### 2. Top-Down Memoization ($\mathcal{O}(N)$ Time, $\mathcal{O}(N)$ Space)
- Recurse with `memo[i]` array storing visited state max values.

---

## Edge Cases

1. **Single house**: `nums = [5]` $\implies$ returns `5`.
2. **Two houses**: `nums = [2, 7]` $\implies$ returns `max(2, 7) = 7`.
3. **All zeros**: `nums = [0, 0, 0]` $\implies$ returns `0`.

---

## Interview Tips

- **State Transition Rationale**: State *"At house `i`, our choices are binary: either rob house `i` (gaining `nums[i] + prev2`) or skip house `i` (carrying forward `prev1`). Max of these options yields the optimal decision at each step."*

---

## Similar Problems

1. [LeetCode #213: House Robber II](https://leetcode.com/problems/house-robber-ii/)
2. [LeetCode #337: House Robber III](https://leetcode.com/problems/house-robber-iii/)
3. [LeetCode #740: Delete and Earn](https://leetcode.com/problems/delete-and-earn/)

---

## Revision Notes

- Problem: Max money without robbing adjacent houses.
- Pattern: Include / Exclude DP.
- Recurrence: `curr = max(num + prev2, prev1)`.
- Variables: `prev2 = 0; prev1 = 0;`
- Update: `prev2 = prev1; prev1 = curr;`
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
