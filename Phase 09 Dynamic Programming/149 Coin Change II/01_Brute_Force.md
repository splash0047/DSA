# Coin Change II

- **Problem Number**: 518
- **Platform**: LeetCode #518
- **Difficulty**: Medium
- **Pattern**: Unmemoized Combination Branching Recursion

---

## Brute Force Intuition

At each coin index `idx`, we have two options:
1. **Include current coin `coins[idx]`**: Subtract `coins[idx]` from `amount`, remain at index `idx` (unbounded supply allows reusing same coin).
2. **Skip current coin `coins[idx]`**: Move to next coin index `idx + 1`.

Sum the combination counts from both branches.

---

## Algorithm

1. `countCombinations(coins, idx, amount)`:
   - Base Case 1: `if (amount == 0) return 1;` (valid combination found).
   - Base Case 2: `if (amount < 0 || idx == coins.size()) return 0;`
   - `include = countCombinations(coins, idx, amount - coins[idx])`.
   - `exclude = countCombinations(coins, idx + 1, amount)`.
   - Return `include + exclude`.

---

## Code

```cpp
#include <vector>

class Solution {
private:
    int countCombinations(const std::vector<int>& coins, int idx, int amount) {
        if (amount == 0) return 1;
        if (amount < 0 || idx == coins.size()) return 0;
        
        // Include current coin (stay at idx) + Exclude current coin (move to idx + 1)
        int include = countCombinations(coins, idx, amount - coins[idx]);
        int exclude = countCombinations(coins, idx + 1, amount);
        
        return include + exclude;
    }

public:
    int change(int amount, std::vector<int>& coins) {
        return countCombinations(coins, 0, amount);
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(2^{\text{amount} + N})$
  - Branching factor of 2 at each step yields exponential decision tree.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(\text{amount} + N)$
  - Recursion call stack depth.

---

## Why This Approach Is Not Optimal

Evaluating duplicate $(idx, \text{amount})$ subproblem states takes exponential time. Using **Space-Optimized Unbounded Knapsack 1D DP**, we compute total combination count in pseudo-polynomial $\mathcal{O}(\text{amount} \times \text{coins.length})$ time and $\mathcal{O}(\text{amount})$ space!
