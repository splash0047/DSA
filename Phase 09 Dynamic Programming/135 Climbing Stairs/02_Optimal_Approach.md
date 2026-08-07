# Climbing Stairs

## Pattern Used

- **Pattern**: **1D Dynamic Programming (Fibonacci Sequence / Space Optimization)**
- **Concept**:
  - State: `dp[i]` represents number of ways to reach step `i`.
  - State Transition: `dp[i] = dp[i-1] + dp[i-2]`.
  - Notice that computing `dp[i]` only requires the previous two terms `dp[i-1]` and `dp[i-2]`.
  - Instead of maintaining an array of size $N$, use two integer variables `prev2` ($f(i-2)$) and `prev1` ($f(i-1)$) to update values iteratively in $\mathcal{O}(1)$ space.

---

## Observation

1. The number of ways to reach step $n$ forms the Fibonacci Sequence: $1, 2, 3, 5, 8, 13, \dots$
2. Storing only the last two computed steps reduces auxiliary space from $\mathcal{O}(N)$ (1D DP array) to $\mathcal{O}(1)$.

---

## Intuition

To figure out how many ways you can get to step 5, you only need to know how many ways you could get to step 4 and step 3. Keep two pointers for the previous two values and slide them forward step-by-step up to $n$.

---

## Algorithm

1. If `n <= 2`, return `n`.
2. `prev2 = 1` (ways to step 1).
3. `prev1 = 2` (ways to step 2).
4. Loop `i` from `3` to `n`:
   - `curr = prev1 + prev2`.
   - `prev2 = prev1`.
   - `prev1 = curr`.
5. Return `prev1`.

---

## Clean C++17 Solution

```cpp
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }
        
        int prev2 = 1; // Ways to reach step 1
        int prev1 = 2; // Ways to reach step 2
        
        for (int i = 3; i <= n; ++i) {
            int curr = prev1 + prev2;
            prev2 = prev1;
            prev1 = curr;
        }
        
        return prev1;
    }
};
```

---

## Dry Run

### Input
- `n = 5`

### Execution Trace

- `n = 5 > 2`. Init `prev2 = 1`, `prev1 = 2`.
- `i = 3`: `curr = 2 + 1 = 3`. `prev2 = 2`, `prev1 = 3`.
- `i = 4`: `curr = 3 + 2 = 5`. `prev2 = 3`, `prev1 = 5`.
- `i = 5`: `curr = 5 + 3 = 8`. `prev2 = 5`, `prev1 = 8`.
- Loop finishes. Return `prev1` = `8`.

### Result
- Output: `8`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single loop from `3` to `N` running in linear time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses only 3 scalar variables (`prev1`, `prev2`, `curr`).

---

## Why This is Optimal

- Computes $N^{th}$ Fibonacci step in linear $\mathcal{O}(N)$ time.
- Space optimization eliminates array allocation, achieving optimal $\mathcal{O}(1)$ space.

---

## Common Mistakes

1. **Off-by-One Base Cases**: Setting `prev1 = 1` instead of `2` for $n=2$.
2. **Allocating O(N) Array Unnecessarily**: Allocating a full `dp[N+1]` array when only 2 variables are needed.
