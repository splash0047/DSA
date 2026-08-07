# Problem Summary

Find the number of distinct ways to climb $n$ stairs taking either 1 or 2 steps at a time. The optimal approach uses **Space-Optimized 1D Dynamic Programming**:
- Base cases: `if (n <= 2) return n;`
- Maintain `prev2 = 1` and `prev1 = 2`.
- Loop `i` from `3` to `n`:
  - `curr = prev1 + prev2; prev2 = prev1; prev1 = curr;`
- Return `prev1`.
This calculates total ways in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to count **total ways to reach a target using small step choices (1 or 2)**.
- Fibonacci / 1D DP Pattern.

---

## Important Clues

1. **"Climb 1 or 2 steps at a time"**: Subproblem dependence $f(n) = f(n-1) + f(n-2)$.
2. **"Distinct ways to reach n"**: Combinatorial counting DP.

---

## Example

### Input
`n = 5`

### Visual Step-by-Step Progression

```text
Stairs:
Step 1: 1 way
Step 2: 2 ways (1+1, 2)
Step 3: 3 ways (2+1 = 3)
Step 4: 5 ways (3+2 = 5)
Step 5: 8 ways (5+3 = 8)

Result: 8
```

---

## Alternative Solutions

### 1. Matrix Exponentiation ($\mathcal{O}(\log N)$ Time, $\mathcal{O}(1)$ Space)
- Use $2 \times 2$ matrix multiplication to compute $N^{th}$ Fibonacci number in logarithmic time.

### 2. Memoized Top-Down Recursion ($\mathcal{O}(N)$ Time, $\mathcal{O}(N)$ Space)
- Store subproblem results in `vector<int> memo(n+1, -1)`.

---

## Edge Cases

1. **$n = 1$**: Return `1`.
2. **$n = 2$**: Return `2`.
3. **$n = 45$ (Max constraint)**: Fits safely within 32-bit signed integer.

---

## Interview Tips

- **Mention Space Optimization Progression**: State *"Starting from top-down recursion $\mathcal{O}(2^N)$, we memoize to $\mathcal{O}(N)$ space, convert to bottom-up 1D DP array $\mathcal{O}(N)$, and finally reduce space to $\mathcal{O}(1)$ by storing only the last two variables."*

---

## Similar Problems

1. [LeetCode #746: Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)
2. [LeetCode #198: House Robber](https://leetcode.com/problems/house-robber/)
3. [LeetCode #509: Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

---

## Revision Notes

- Problem: Ways to climb $n$ stairs taking 1 or 2 steps.
- Pattern: Fibonacci Sequence DP.
- Code: `prev2 = 1; prev1 = 2; for (3..n) { curr = prev1 + prev2; prev2 = prev1; prev1 = curr; }`
- Result: `return prev1;`
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
