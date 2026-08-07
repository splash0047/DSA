# Climbing Stairs

- **Problem Number**: 70
- **Platform**: LeetCode #70
- **Difficulty**: Easy
- **Pattern**: Naive Exponential Recursion

---

## Brute Force Intuition

To reach step $n$, you can either take 1 step from step $n-1$ or 2 steps from step $n-2$.
Therefore, the total number of ways to reach step $n$ is:
$$f(n) = f(n-1) + f(n-2)$$

A naive recursive implementation calculates $f(n)$ by recursively invoking $f(n-1)$ and $f(n-2)$ until reaching base cases $f(1) = 1$ and $f(2) = 2$.

---

## Algorithm

1. `climbStairs(n)`:
   - If `n <= 2`, return `n`.
   - Return `climbStairs(n - 1) + climbStairs(n - 2)`.

---

## Code

```cpp
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }
        return climbStairs(n - 1) + climbStairs(n - 2);
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(2^N)$
  - Each call branches into two recursive calls, creating a recursion tree of depth $N$ and $2^N$ nodes.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Call stack depth is $N$.

---

## Why This Approach Is Not Optimal

The recursion tree repeatedly recomputes identical subproblems (e.g., $f(3)$ is computed multiple times when evaluating $f(5)$). Using **Dynamic Programming (Space-Optimized Iterative DP)**, we eliminate redundant calls, achieving linear $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space!
