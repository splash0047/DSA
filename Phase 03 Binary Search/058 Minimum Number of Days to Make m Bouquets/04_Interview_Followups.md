# 04 Interview Follow-ups & System Variations: Minimum Number of Days to Make m Bouquets

The problem finds the minimum day $D$ to make $m$ bouquets of $k$ adjacent flowers from `bloomDay`. The optimal approach uses Binary Search on the Answer in range $[\min(	ext{bloomDay}), \max(	ext{bloomDay})]$ in $\mathcal{O}(N \log(\max - \min))$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem tests adjacency counting, impossibility edge cases, and integer overflow on $m 	imes k$.

---

## 1. 64-Bit Integer Overflow in Impossibility Check

### 🛑 The Hazard
If $m = 10^5$ and $k = 10^5$, total flowers required is $m 	imes k = 10^{10} > 2^{31} - 1$.
- `if (m * k > n)` will overflow 32-bit signed integers and fail to return `-1`.
- **Solution**: `if ((long long)m * k > nums.size()) return -1;`

---

## 2. Greedy Adjacent Flower Counting Feasibility

```cpp
bool canMake(vector<int>& bloomDay, int m, int k, int day) {
    int bouquets = 0, consecutive = 0;
    for (int b : bloomDay) {
        if (b <= day) {
            consecutive++;
            if (consecutive == k) {
                bouquets++;
                consecutive = 0;
            }
        } else {
            consecutive = 0; // Adjacency streak broken
        }
    }
    return bouquets >= m;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Search Range | Feasibility Check | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Standard** | $[\min(bloom), \max(bloom)]$ | Contiguous streak reset | $\mathcal{O}(N \log(	ext{Range}))$ | $\mathcal{O}(1)$ |
