# 04 Interview Follow-ups & System Variations: Coin Change II

The problem finds the number of combinations that make up a given amount using unbounded coins. The optimal 1D DP loop runs in $\mathcal{O}(	ext{amount} 	imes C)$ time and $\mathcal{O}(	ext{amount})$ space.

In technical interviews, this problem is famous for contrasting **Combinations (Coin Change II)** vs. **Permutations (Combination Sum IV)**.

---

## 1. Combinations vs. Permutations: The Loop Order Rule

### 🛑 The Critical Order Difference
```cpp
// 1. COMBINATIONS (Coin Change II): Outer Loop over COINS
for (int coin : coins) {
    for (int i = coin; i <= amount; i++) {
        dp[i] += dp[i - coin]; // Generates [1, 2] once; avoids duplicate [2, 1]
    }
}

// 2. PERMUTATIONS (Combination Sum IV): Outer Loop over AMOUNT
for (int i = 1; i <= amount; i++) {
    for (int coin : coins) {
        if (i >= coin) dp[i] += dp[i - coin]; // Counts [1, 2] and [2, 1] as distinct
    }
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Problem | Order Dependency | Outer Loop | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Coin Change II (#518)** | Combinations (Order irrelevant) | `for coin in coins` | $\mathcal{O}(A \cdot C)$ | $\mathcal{O}(A)$ |
| **Combination Sum IV (#377)**| Permutations (Order matters) | `for i = 1..amount` | $\mathcal{O}(A \cdot C)$ | $\mathcal{O}(A)$ |
