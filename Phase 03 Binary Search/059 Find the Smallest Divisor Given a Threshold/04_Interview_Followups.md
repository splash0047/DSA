# 04 Interview Follow-ups & System Variations: Find the Smallest Divisor Given a Threshold

The problem finds the smallest positive divisor such that the sum of division results is $\le 	ext{threshold}$. The optimal Binary Search on the Answer runs in range $[1, \max(	ext{nums})]$ in $\mathcal{O}(N \log(\max(	ext{nums})))$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem reinforces integer ceiling division and monotonic step functions.

---

## 1. Monotonicity Analysis

- As divisor $D$ increases:
  $$	ext{Result}(D) = \sum \lceil 	ext{nums}[i] / D ceil$$
  monotonically **decreases**.
- Range: `left = 1` (maximum possible sum), `right = max(nums)` (minimum possible sum = $N$).

---

## Summary Matrix: Trade-offs at a Glance

| Range | Feasibility Formula | Time | Space |
| :--- | :--- | :--- | :--- |
| $[1, \max(	ext{nums})]$ | $\sum (x + d - 1) / d \le 	ext{threshold}$ | $\mathcal{O}(N \log(\max A))$ | $\mathcal{O}(1)$ |
