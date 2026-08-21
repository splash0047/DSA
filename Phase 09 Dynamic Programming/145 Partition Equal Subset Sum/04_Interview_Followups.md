# 04 Interview Follow-ups & System Variations: Partition Equal Subset Sum

The problem determines if array can be partitioned into two subsets with equal sum. This reduces to **0-1 Knapsack Subset Sum** with $	ext{Target} = 	ext{TotalSum} / 2$. Optimal solutions use 1D DP in $\mathcal{O}(N 	imes 	ext{Target})$ time and $\mathcal{O}(	ext{Target})$ space, or **Bitset Optimization**.

In technical interviews, this problem is used to test Bitwise Parallelism (`std::bitset`).

---

## 1. Bitset Optimization: 64x Speedup in Hardware Registers

### 💡 CPU Register Parallelism
- Represent reachable subset sums as a bitmask:
  ```cpp
  bool canPartition(vector<int>& nums) {
      int sum = 0;
      for (int x : nums) sum += x;
      if (sum % 2 != 0) return false;
      
      bitset<10001> dp;
      dp[0] = 1;
      for (int x : nums) {
          dp |= (dp << x); // Bitwise shifts update all subset sums simultaneously!
      }
      return dp[sum / 2];
  }
  ```
- **Performance**: Performs 64 state transitions per single CPU instruction cycle.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Strategy | Time Complexity | Extra Space |
| :--- | :--- | :--- | :--- |
| **1D Array DP** | Reverse loop `j = Target -> num` | $\mathcal{O}(N \cdot 	ext{Target})$ | $\mathcal{O}(	ext{Target})$ |
| **Bitset Register (Optimal)**| Bitwise Shift `dp |= (dp << x)` | $\mathcal{O}(N \cdot rac{	ext{Target}}{64})$ | $\mathcal{O}(rac{	ext{Target}}{64})$ |
