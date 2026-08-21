# 04 Interview Follow-ups & System Variations: Stock with Cooldown

The problem finds maximum profit with unlimited transactions but a 1-day cooldown after selling. The optimal solution uses a **3-State Finite State Machine** in $\mathcal{O}(N)$ time and strictly $\mathcal{O}(1)$ space.

In technical interviews, this problem tests state machine formulation and arbitrary $K$-day cooldown generalizations.

---

## 1. The 3-State Finite State Machine ($\mathcal{O}(1)$ Space)

### 💡 State Transitions
1. **`held`**: Currently holding stock.
   $$	ext{held} = \max(	ext{held},\; 	ext{rest} - 	ext{price})$$
2. **`sold`**: Just sold stock today (enters cooldown tomorrow).
   $$	ext{sold} = 	ext{held} + 	ext{price}$$
3. **`rest`**: In cooldown or free to buy.
   $$	ext{rest} = \max(	ext{rest},\; 	ext{prev\_sold})$$

```cpp
int maxProfit(vector<int>& prices) {
    int held = -prices[0], sold = 0, rest = 0;
    for (int i = 1; i < prices.size(); i++) {
        int prev_sold = sold;
        sold = held + prices[i];
        held = max(held, rest - prices[i]);
        rest = max(rest, prev_sold);
    }
    return max(sold, rest);
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Parameter | Value |
| :--- | :--- |
| **State Machine** | 3 States (`held`, `sold`, `rest`) |
| **Time Complexity** | $\mathcal{O}(N)$ strictly |
| **Space Complexity** | Strictly $\mathcal{O}(1)$ |
