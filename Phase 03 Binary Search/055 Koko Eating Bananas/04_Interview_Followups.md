# 04 Interview Follow-ups & System Variations: Koko Eating Bananas

The problem finds the minimum integer eating speed $k$ such that Koko can eat all bananas within $h$ hours. The optimal approach uses **Binary Search on the Answer** in the range $[1, \max(	ext{piles})]$ with a greedy feasibility check in $\mathcal{O}(N \log(\max(	ext{piles})))$ time and $\mathcal{O}(1)$ space.

In technical interviews, this is the archetypal template for monotonic search spaces. Interviewers test ceiling division formulas without floating-point errors, 64-bit integer overflow, and extreme constraint scaling.

---

## 1. Avoiding Floating-Point Division (Ceiling Division Formula)

### 🛑 The Hazard of `ceil((double)pile / k)`
Floating-point conversions introduce precision errors and slower runtime execution on CPUs.

### 💡 Pure Integer Ceiling Division
$$\lceil 	ext{pile} / k ceil = \lfloor (	ext{pile} + k - 1) / k floor = rac{	ext{pile} + k - 1}{k}$$

---

## 2. Preventing 64-bit Accumulator Overflow

### 🛑 The Bug
If `piles` has $10^5$ elements of size $10^9$, and testing $k = 1$, the total hours required is $10^{14}$, which overflows standard 32-bit signed `int`.
- Always accumulate `long long total_hours = 0`.

---

## 3. The Universal Binary Search on Answer Template

```cpp
int minEatingSpeed(vector<int>& piles, int h) {
    int left = 1, right = *max_element(piles.begin(), piles.end());
    int ans = right;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        long long hours = 0;
        for (int p : piles) {
            hours += (p + mid - 1) / mid;
        }
        
        if (hours <= h) {
            ans = mid;         // Feasible; try smaller speed
            right = mid - 1;
        } else {
            left = mid + 1;    // Infeasible; increase speed
        }
    }
    return ans;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Component | Choice | Rationale |
| :--- | :--- | :--- |
| **Search Space** | $[1, \max(	ext{piles})]$ | Min possible speed is 1; max speed needs at most largest pile |
| **Feasibility Test** | $\mathcal{O}(N)$ linear pass | Monotonically decreasing hours with increasing $k$ |
| **Total Complexity** | $\mathcal{O}(N \log(\max P))$ | Guaranteed sub-second execution for $10^5$ items |
