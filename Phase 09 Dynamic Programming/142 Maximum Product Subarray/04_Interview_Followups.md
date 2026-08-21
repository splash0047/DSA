# 04 Interview Follow-ups & System Variations: Maximum Product Subarray

The problem finds the contiguous subarray with the largest product. The optimal solution tracks both `current_max` and `current_min` (to handle negative-times-negative reversals) in $\mathcal{O}(N)$ time and strictly $\mathcal{O}(1)$ space.

In technical interviews, this problem is compared with Prefix/Suffix bidirectional scanning.

---

## 1. Two Running Variables Invariant Proof

### 💡 Negative Multiplier Inversion
- When multiplying by a negative number `nums[i] < 0`:
  - The largest product becomes the smallest negative number.
  - The smallest negative number becomes the largest positive number.
- Swap before multiplying: `swap(current_max, current_min)`.
- Update:
  $$	ext{current\_max} = \max(	ext{nums}[i],\; 	ext{current\_max} 	imes 	ext{nums}[i])$$
  $$	ext{current\_min} = \min(	ext{nums}[i],\; 	ext{current\_min} 	imes 	ext{nums}[i])$$

---

## 2. Alternative: 2-Pass Left-to-Right & Right-to-Left Scan

```cpp
int maxProduct(vector<int>& nums) {
    int n = nums.size(), ans = nums[0];
    int pref = 0, suff = 0;
    
    for (int i = 0; i < n; i++) {
        pref = (pref == 0 ? 1 : pref) * nums[i];
        suff = (suff == 0 ? 1 : suff) * nums[n - 1 - i];
        ans = max(ans, max(pref, suff));
    }
    return ans;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Method | Variables | Time | Space |
| :--- | :--- | :--- | :--- |
| **Min/Max State Tracking** | `current_max`, `current_min` | $\mathcal{O}(N)$ (1 pass) | $\mathcal{O}(1)$ |
| **Bidirectional Prefix/Suffix**| `pref`, `suff` accumulators | $\mathcal{O}(N)$ (1 loop) | $\mathcal{O}(1)$ |
