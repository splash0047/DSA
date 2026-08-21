import os

BASE_DIR_P9 = r"c:\Users\Pinak chimurkar\DSA\Phase 09 Dynamic Programming"
BASE_DIR_P10 = r"c:\Users\Pinak chimurkar\DSA\Phase 10 Bit Manipulation & Advanced"

data_p9 = {
    "135 Climbing Stairs": """# 04 Interview Follow-ups & System Variations: Climbing Stairs

The problem finds the number of distinct ways to climb $N$ stairs (taking 1 or 2 steps). Standard approaches include 1D DP / 2-variable Fibonacci iteration in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In top-tier technical interviews, this problem is the gateway to **Matrix Exponentiation for $N = 10^9$**, variable step generalizations ($K$ steps), and closed-form Binet equations.

---

## 1. What if $N = 10^{18}$ (Scaling to Billions with Matrix Exponentiation)?

### 🛑 Why Linear $\mathcal{O}(N)$ Fails
If $N = 10^{18}$, looping $N$ times takes hundreds of years of CPU time.

### 💡 $\mathcal{O}(\log N)$ Matrix Fast Power
- Formulate the recurrence as a matrix transition:
  $$\begin{pmatrix} F(n+1) \\ F(n) \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} F(n) \\ F(n-1) \end{pmatrix} \implies \begin{pmatrix} F(n+1) \\ F(n) \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^N \begin{pmatrix} F(1) \\ F(0) \end{pmatrix}$$
- Compute the $N$-th power of the $2 \times 2$ matrix using **Binary Exponentiation** (Repeated Squaring) in $\mathcal{O}(\log N)$ multiplications.
- Supports answers modulo $10^9 + 7$.

---

## 2. Generalization: Climbing Stairs with $K$ Steps (1 to $K$ Steps per Leap)

### 💡 Sliding Window DP ($\mathcal{O}(N)$ Time)
- Recurrence: $DP[i] = \sum_{j=1}^K DP[i - j]$.
- Instead of summing $K$ elements every step ($\mathcal{O}(N \cdot K)$):
  - Maintain a running `window_sum`.
  - $DP[i] = \text{window\_sum}$.
  - Slide window: `window_sum += DP[i] - DP[i - K]`.
- **Time Complexity**: strictly $\mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(K)$.

---

## Summary Matrix: Trade-offs at a Glance

| Constraint / Scale | Optimal Approach | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Standard $N \le 10^5$** | 2-Variable Fibonacci State | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Massive $N = 10^{18}$** | Matrix Exponentiation | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| **$K$ Variable Steps** | Sliding Window DP Accumulator | $\mathcal{O}(N)$ | $\mathcal{O}(K)$ |
""",

    "136 House Robber": """# 04 Interview Follow-ups & System Variations: House Robber

The problem finds the maximum money you can rob without robbing two adjacent houses. The standard optimal approach uses two variables (`rob1`, `rob2`) in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is extended to trees (House Robber III / Tree DP), circular streets (House Robber II), and bounded capacity constraints.

---

## 1. Generalization: House Robber on a Binary Tree (LeetCode #337 / House Robber III)

### 💡 Tree DP Tuple State: `(rob_this_node, skip_this_node)`
- For each tree node, return a pair:
  1. `rob_node = node.val + left.skip + right.skip`
  2. `skip_node = max(left.rob, left.skip) + max(right.rob, right.skip)`
- Post-order DFS traversal in $\mathcal{O}(N)$ time and $\mathcal{O}(H)$ stack space.

---

## Summary Matrix: Trade-offs at a Glance

| Topology | State Model | Time | Space |
| :--- | :--- | :--- | :--- |
| **1D Line (I)** | 2 scalars (`rob1`, `rob2`) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Circular Neighborhood (II)**| Split into 2 Linear passes | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Binary Tree (III)** | Post-order `(rob, skip)` pair | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
""",

    "137 House Robber II": """# 04 Interview Follow-ups & System Variations: House Robber II

The problem extends House Robber to a circular street (first and last house are neighbors). The optimal approach breaks the circular dependency into two linear sub-problems in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem demonstrates the standard paradigm for **Linearizing Circular Dynamic Programming**.

---

## 1. The 2-Pass Linearization Architecture

### 💡 Mutual Exclusion of First and Last Houses
- You can either rob House $0$ OR House $N-1$, but never both.
- **Subproblem 1**: Rob from House $0$ to $N - 2$ (excludes last house).
- **Subproblem 2**: Rob from House $1$ to $N - 1$ (excludes first house).
- **Result**: $\max(\text{Solve}(0 \dots N-2),\; \text{Solve}(1 \dots N-1))$.

---

## Summary Matrix: Trade-offs at a Glance

| Topology | Strategy | Time Complexity | Extra Space |
| :--- | :--- | :--- | :--- |
| **Circular Street** | $\max(\text{Line}(0 \dots N-2), \text{Line}(1 \dots N-1))$ | $\mathcal{O}(N)$ (2 passes) | $\mathcal{O}(1)$ |
""",

    "138 Longest Palindromic Substring": """# 04 Interview Follow-ups & System Variations: Longest Palindromic Substring

The problem finds the longest palindromic substring in $S$. While Expand Around Center runs in $\mathcal{O}(N^2)$ time and $\mathcal{O}(1)$ space, the optimal **Manacher's Algorithm** achieves strictly $\mathcal{O}(N)$ linear time and $\mathcal{O}(N)$ space.

In technical interviews, this problem is the gold standard for linear string algorithms and palindromic radius symmetry.

---

## 1. Manacher's Algorithm ($\mathcal{O}(N)$ Linear Time)

### 💡 Virtual Character Insertion & Symmetry Radius
1. Preprocess string with `#` delimiters (e.g., `"aba"` $\to$ `"#a#b#a#"` of length $2N + 1$) so all even and odd palindromes have odd lengths.
2. Maintain `center` $C$ and right boundary $R$.
3. For each index $i$:
   - Let mirror index be $i' = 2C - i$.
   - If $i < R$, initialize radius $P[i] = \min(R - i, P[i'])$.
   - Expand palindrome radius around $i$ while characters match.
   - If $i + P[i] > R$, update new center $C = i$ and boundary $R = i + P[i]$.
- **Time Complexity**: $\mathcal{O}(N)$ strictly (each right expansion advances $R$ forward).

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Time Complexity | Space Complexity | Best Used When |
| :--- | :--- | :--- | :--- |
| **Expand Around Center** | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | Short strings / Simple code |
| **2D Dynamic Programming**| $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | Substring range queries |
| **Manacher's Algorithm** | **$\mathcal{O}(N)$ (Optimal)** | $\mathcal{O}(N)$ | Production string matching |
""",

    "139 Palindromic Substrings": """# 04 Interview Follow-ups & System Variations: Palindromic Substrings

The problem counts the total number of palindromic substrings in $S$. Expand Around Center runs in $\mathcal{O}(N^2)$ time and $\mathcal{O}(1)$ space, and Manacher's Algorithm runs in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

In technical interviews, this problem is used to show how Manacher's radius array yields the total count in a single mathematical sum.

---

## 1. Counting Palindromes via Manacher's Radius Array in $\mathcal{O}(N)$

### 💡 Radius Sum Formula
- After running Manacher's Algorithm to compute radius array $P$:
  $$\text{Total Palindromic Substrings} = \sum_{i=0}^{2N} \lfloor \frac{P[i] + 1}{2} \rfloor$$
- **Time Complexity**: $\mathcal{O}(N)$ single pass, **Space Complexity**: $\mathcal{O}(N)$.

---

## Summary Matrix: Trade-offs at a Glance

| Method | Time | Space | Complexity |
| :--- | :--- | :--- | :--- |
| **Expand Around Center** | $\mathcal{O}(N^2)$ | $\mathcal{O}(1)$ | $2N - 1$ centers |
| **Manacher's Radius Sum**| $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | 1 linear pass |
""",

    "140 Decode Ways": """# 04 Interview Follow-ups & System Variations: Decode Ways

The problem counts the number of ways to decode a numeric string mapping $1 \to 'A', \dots, 26 \to 'Z'$. Optimal 1D DP uses two scalar variables in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem tests leading zero invalidations (`'0'`) and wildcard extensions (Decode Ways II with `'*'`).

---

## 1. The Leading Zero (`'0'`) Invalidation Rule

### 🛑 Edge Cases with Zeroes
- `'0'` alone cannot be mapped to any letter.
- Valid 2-digit numbers ending in zero are strictly `"10"` and `"20"`.
- Patterns like `"30"`, `"06"`, or `"00"` are completely invalid and evaluate to 0 ways.

---

## 2. Low-Memory $\mathcal{O}(1)$ Space Template

```cpp
int numDecodings(string s) {
    if (s.empty() || s[0] == '0') return 0;
    int prev2 = 1, prev1 = 1;
    
    for (int i = 1; i < s.size(); i++) {
        int curr = 0;
        if (s[i] != '0') curr += prev1;
        
        int two_digit = stoi(s.substr(i - 1, 2));
        if (two_digit >= 10 && two_digit <= 26) curr += prev2;
        
        prev2 = prev1;
        prev1 = curr;
    }
    return prev1;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Character Set | Strategy | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Standard (#91)** | Digits `0-9` | 2-Variable DP | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **With Wildcards (#639)**| Digits + `*` | 18-case State Machine | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
""",

    "141 Coin Change": """# 04 Interview Follow-ups & System Variations: Coin Change

The problem finds the fewest coins needed to make up a given amount (Unbounded Knapsack). The optimal bottom-up DP runs in $\mathcal{O}(\text{amount} \times C)$ time and $\mathcal{O}(\text{amount})$ space, or BFS for shortest unweighted path.

In technical interviews, interviewers test why greedy fails on non-canonical currency systems and integer linear programming at scale.

---

## 1. Why Greedy Fails on Arbitrary Coin Systems (Canonical Coin Systems)

### 🛑 The Greedy Counter-Example
Suppose coins are `[1, 3, 4]` and target amount is `6`:
- **Greedy Choice**: Picks largest coin $4$, leaving remainder $2 \implies 4 + 1 + 1 = 3\text{ coins}$.
- **Optimal Choice**: $3 + 3 = 2\text{ coins}$.
- **Insight**: Greedy is only optimal for **Canonical Coin Systems** (like US/Euro currency: 1, 5, 10, 25, 100). For arbitrary integer denominations, Dynamic Programming is mandatory.

---

## 2. Dynamic Programming vs. Breadth-First Search (BFS)

| Method | Best Scenario | Time | Space |
| :--- | :--- | :--- | :--- |
| **Bottom-Up DP** | Computing all amounts $\le A$ | $\mathcal{O}(A \times C)$ | $\mathcal{O}(A)$ array |
| **BFS Shortest Path** | Small answer (e.g., amount reached in 3 coins) | $\mathcal{O}(C^{\text{depth}})$ | $\mathcal{O}(A)$ visited |

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Space Model | Time | Space |
| :--- | :--- | :--- | :--- |
| **Bottom-Up 1D DP** | Tabulation | $\mathcal{O}(\text{Amount} \times C)$ | $\mathcal{O}(\text{Amount})$ |
| **BFS Shortest Path** | Queue of states | $\mathcal{O}(\text{Amount} \times C)$ | $\mathcal{O}(\text{Amount})$ |
""",

    "142 Maximum Product Subarray": """# 04 Interview Follow-ups & System Variations: Maximum Product Subarray

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
  $$\text{current\_max} = \max(\text{nums}[i],\; \text{current\_max} \times \text{nums}[i])$$
  $$\text{current\_min} = \min(\text{nums}[i],\; \text{current\_min} \times \text{nums}[i])$$

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
""",

    "143 Word Break": """# 04 Interview Follow-ups & System Variations: Word Break

The problem determines if string $S$ can be segmented into dictionary words. Optimal approaches include **1D DP with Trie** in $\mathcal{O}(N^2 + \sum L)$ time and $\mathcal{O}(N + \text{Trie})$ space.

In technical interviews, this problem is extended to Word Break II (reconstructing all valid sentences via memoized DFS).

---

## 1. 1D DP with Trie Optimization

```cpp
bool wordBreak(string s, vector<string>& wordDict) {
    unordered_set<string> dict(wordDict.begin(), wordDict.end());
    int n = s.size();
    vector<bool> dp(n + 1, false);
    dp[0] = true;
    
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            if (dp[j] && dict.count(s.substr(j, i - j))) {
                dp[i] = true;
                break;
            }
        }
    }
    return dp[n];
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Problem | Goal | Optimal Approach | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Word Break I (#139)** | Boolean check | 1D Dynamic Programming | $\mathcal{O}(N^2)$ | $\mathcal{O}(N)$ |
| **Word Break II (#140)** | All sentences | Memoized DFS Backtracking | $\mathcal{O}(N^2 + \text{Sentences})$ | $\mathcal{O}(N^2)$ |
""",

    "144 Longest Increasing Subsequence": """# 04 Interview Follow-ups & System Variations: Longest Increasing Subsequence

The problem finds the length of the longest strictly increasing subsequence. While standard DP runs in $\mathcal{O}(N^2)$, the optimal **Patience Sorting (Greedy + Binary Search)** achieves $\mathcal{O}(N \log N)$ time and $\mathcal{O}(N)$ space.

In top-tier technical interviews, this is the premier example of replacing $\mathcal{O}(N^2)$ DP with binary search patience piles.

---

## 1. Patience Sorting with Binary Search ($\mathcal{O}(N \log N)$ Optimal)

### 💡 The `tails` Array Invariant
- Maintain an array `tails` where `tails[i]` stores the **smallest tail of all increasing subsequences of length $i + 1$** found so far.
- For each $x \in \text{nums}$:
  - Find first element in `tails` $\ge x$ using `std::lower_bound` in $\mathcal{O}(\log L)$.
  - If $x$ is greater than all elements: append $x$ to `tails`.
  - Else: overwrite `tails[idx] = x` (greedily lowers the bar for future extensions).
- **Result**: Length of LIS is `tails.size()`.

---

## 2. Generalization: 2D Russian Doll Envelopes (LeetCode #354 / Hard)

### 💡 2D Sort + 1D LIS Reduction
1. Sort envelopes by: **Width ASCENDING, and Height DESCENDING for ties**.
2. Run standard 1D LIS on the heights!
- *Why Height Descending?* Sorting heights in descending order ensures two envelopes with the exact same width can never be nested inside one another.
- **Time Complexity**: $\mathcal{O}(N \log N)$, **Space Complexity**: $\mathcal{O}(N)$.

---

## Summary Matrix: Trade-offs at a Glance

| Problem | Algorithm | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **1D LIS (#300)** | Patience Sorting + Binary Search | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ |
| **Russian Dolls (#354)**| 2D Sort + 1D Patience Sort | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ |
| **Dynamic LIS** | Fenwick Tree / Segment Tree | $\mathcal{O}(\log N)$ / insert | $\mathcal{O}(N)$ |
""",

    "145 Partition Equal Subset Sum": """# 04 Interview Follow-ups & System Variations: Partition Equal Subset Sum

The problem determines if array can be partitioned into two subsets with equal sum. This reduces to **0-1 Knapsack Subset Sum** with $\text{Target} = \text{TotalSum} / 2$. Optimal solutions use 1D DP in $\mathcal{O}(N \times \text{Target})$ time and $\mathcal{O}(\text{Target})$ space, or **Bitset Optimization**.

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
| **1D Array DP** | Reverse loop `j = Target -> num` | $\mathcal{O}(N \cdot \text{Target})$ | $\mathcal{O}(\text{Target})$ |
| **Bitset Register (Optimal)**| Bitwise Shift `dp |= (dp << x)` | $\mathcal{O}(N \cdot \frac{\text{Target}}{64})$ | $\mathcal{O}(\frac{\text{Target}}{64})$ |
""",

    "146 Unique Paths": """# 04 Interview Follow-ups & System Variations: Unique Paths

The problem finds the number of unique paths from top-left to bottom-right of an $M \times N$ grid. Optimal solutions include **Combinatorics** in $\mathcal{O}(\min(M, N))$ time and $\mathcal{O}(1)$ space, or **1D DP**.

In technical interviews, this problem tests combinatorics vs. DP trade-offs and obstacle handling (Unique Paths II).

---

## 1. Closed-Form Combinatorics Formula ($\mathcal{O}(1)$ Space)

### 💡 Mathematical Derivation
- To reach bottom-right from $(0, 0)$, you must take exactly:
  - $M - 1$ downward moves ($D$).
  - $N - 1$ rightward moves ($R$).
- Total moves: $(M - 1) + (N - 1) = M + N - 2$.
- Number of unique combinations to choose the downward moves:
  $$\text{Total Paths} = \binom{M + N - 2}{M - 1} = \frac{(M + N - 2)!}{(M - 1)! (N - 1)!}$$
- Calculate multiplicatively in $\mathcal{O}(\min(M, N))$ time with zero overflow:
  ```cpp
  int uniquePaths(int m, int n) {
      long long ans = 1;
      int total_steps = m + n - 2;
      int k = min(m - 1, n - 1);
      for (int i = 1; i <= k; i++) {
          ans = ans * (total_steps - k + i) / i;
      }
      return (int)ans;
  }
  ```

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Grid Model | Optimal Strategy | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **No Obstacles (I)** | Empty Grid | Combinatorics $\binom{m+n-2}{m-1}$ | $\mathcal{O}(\min(M, N))$ | $\mathcal{O}(1)$ |
| **With Obstacles (II)**| Grid with Obstacles | 1D Dynamic Programming | $\mathcal{O}(MN)$ | $\mathcal{O}(N)$ |
""",

    "147 Longest Common Subsequence": """# 04 Interview Follow-ups & System Variations: Longest Common Subsequence

The problem finds the length of the longest common subsequence of two strings. Optimal solutions use **2-Row Rolling 1D DP** in $\mathcal{O}(M \times N)$ time and $\mathcal{O}(\min(M, N))$ space.

In technical interviews, this is the prime template for sequence alignment (Bioinformatics BLAST, Git Diff), and Hirschberg's linear-space string reconstruction algorithm.

---

## 1. Reconstructing the Exact LCS in $\mathcal{O}(\min(M, N))$ Space (Hirschberg's Algorithm)

### 🛑 The Memory Bottleneck of Standard Backtracking
Standard LCS reconstruction stores the full $M \times N$ matrix for pointer backtracking. For two DNA sequences of length $100,000$, this requires 40GB RAM.

### 💡 Hirschberg's Divide & Conquer Algorithm
- Split string $A$ in half at $mid = M / 2$.
- Compute forward LCS of $A[0 \dots mid]$ and $B$, and backward LCS of $A[mid+1 \dots M]$ and $reverse(B)$ using 2-row rolling DP in $\mathcal{O}(N)$ space.
- Find the split point in $B$ that maximizes the sum of forward and backward LCS.
- Recursively solve on the two smaller halves!
- **Time Complexity**: $\mathcal{O}(M \times N)$ (geometric series $1 + 1/2 + 1/4 \dots \le 2$), **Space Complexity**: strictly $\mathcal{O}(N)$!

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Purpose | Time | Space |
| :--- | :--- | :--- | :--- |
| **2-Row Rolling DP** | Length only | $\mathcal{O}(MN)$ | $\mathcal{O}(\min(M, N))$ |
| **Full 2D Matrix DP** | Length + String Reconstruction | $\mathcal{O}(MN)$ | $\mathcal{O}(MN)$ |
| **Hirschberg's Algorithm**| Length + String Reconstruction | $\mathcal{O}(MN)$ | $\mathcal{O}(\min(M, N))$ |
""",

    "148 Best Time to Buy and Sell Stock with Cooldown": """# 04 Interview Follow-ups & System Variations: Stock with Cooldown

The problem finds maximum profit with unlimited transactions but a 1-day cooldown after selling. The optimal solution uses a **3-State Finite State Machine** in $\mathcal{O}(N)$ time and strictly $\mathcal{O}(1)$ space.

In technical interviews, this problem tests state machine formulation and arbitrary $K$-day cooldown generalizations.

---

## 1. The 3-State Finite State Machine ($\mathcal{O}(1)$ Space)

### 💡 State Transitions
1. **`held`**: Currently holding stock.
   $$\text{held} = \max(\text{held},\; \text{rest} - \text{price})$$
2. **`sold`**: Just sold stock today (enters cooldown tomorrow).
   $$\text{sold} = \text{held} + \text{price}$$
3. **`rest`**: In cooldown or free to buy.
   $$\text{rest} = \max(\text{rest},\; \text{prev\_sold})$$

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
""",

    "149 Coin Change II": """# 04 Interview Follow-ups & System Variations: Coin Change II

The problem finds the number of combinations that make up a given amount using unbounded coins. The optimal 1D DP loop runs in $\mathcal{O}(\text{amount} \times C)$ time and $\mathcal{O}(\text{amount})$ space.

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
""",

    "150 Target Sum": """# 04 Interview Follow-ups & System Variations: Target Sum

The problem assigns `+` and `-` signs to array elements to equal `target`. By algebraic reformulation, this transforms into **0-1 Knapsack Subset Sum** for $P = (\text{target} + \text{sum}) / 2$ in $\mathcal{O}(N \times P)$ time and $\mathcal{O}(P)$ space.

In technical interviews, this problem tests problem inversion into standard DP models.

---

## 1. Algebraic Reduction to Subset Sum

### 💡 Mathematical Derivation
- Let $P$ be the subset of numbers with `+` sign, and $N$ be the subset with `-` sign:
  $$\text{Sum}(P) - \text{Sum}(N) = \text{target}$$
  $$\text{Sum}(P) + \text{Sum}(N) = \text{total\_sum}$$
- Adding the two equations:
  $$2 \times \text{Sum}(P) = \text{target} + \text{total\_sum} \implies \text{Sum}(P) = \frac{\text{target} + \text{total\_sum}}{2}$$
- **Impossibility Checks**:
  1. `(target + total_sum)` must be non-negative and even.
  2. `abs(target) <= total_sum`.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Problem Form | Time | Space |
| :--- | :--- | :--- | :--- |
| **Subset Sum DP (Optimal)**| Find subsets summing to $P$ | $\mathcal{O}(N \cdot P)$ | $\mathcal{O}(P)$ |
| **Recursion with Memo** | 2D `(index, current_sum)` | $\mathcal{O}(N \cdot \text{Sum})$ | $\mathcal{O}(N \cdot \text{Sum})$ |
""",

    "151 Edit Distance": """# 04 Interview Follow-ups & System Variations: Edit Distance

The problem finds the minimum operations (insert, delete, replace) to convert `word1` to `word2`. Optimal solutions use 2-Row Rolling 1D DP in $\mathcal{O}(M \times N)$ time and $\mathcal{O}(\min(M, N))$ space.

In technical interviews, this is the benchmark Levenshtein Distance problem. Interviewers probe Ukkonen's Banded Algorithm ($K$-bounded distance) and asymmetric operation costs.

---

## 1. Ukkonen's Banded Algorithm for Small Edit Distance $K$

### 🛑 The Inefficiency
If two strings have length $100,000$ and we only want to check if their edit distance is $\le 3$, computing full $10^{10}$ cells is wasteful.

### 💡 Banded Diagonal DP
- Only compute cells within distance $K$ of the main diagonal: $|i - j| \le K$.
- **Time Complexity**: $\mathcal{O}(K \times \min(M, N))$ instead of $\mathcal{O}(M \times N)$!

---

## Summary Matrix: Trade-offs at a Glance

| Variant | Strategy | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Standard Levenshtein** | 2-Row Rolling DP | $\mathcal{O}(MN)$ | $\mathcal{O}(\min(M, N))$ |
| **Bounded Edit Distance ($K$)**| Ukkonen's Diagonal Band | $\mathcal{O}(K \cdot \min(M, N))$ | $\mathcal{O}(K)$ |
"""
}

data_p10 = {
    "152 Single Number": """# 04 Interview Follow-ups & System Variations: Single Number

The problem finds the single number in an array where every other element appears twice. The optimal solution uses **Bitwise XOR Accumulation** ($x \oplus x = 0$) in $\mathcal{O}(N)$ time and strictly $\mathcal{O}(1)$ space.

In technical interviews, this problem is generalized to elements appearing 3 times (Single Number II) and finding two distinct unique elements (Single Number III).

---

## 1. The Single Number Trilogy Comparison

| Problem | Repetition Pattern | Optimal Bitwise Strategy | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Single Number I (#136)** | Twice except 1 | Total XOR sum: $x \oplus x = 0$ | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Single Number II (#137)**| Three times except 1 | Bitwise State Machine (`ones`, `twos`) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Single Number III (#260)**| Twice except TWO | XOR sum $\to$ Lowest set bit partition | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

---

## 2. Single Number III: Finding TWO Unique Elements

### 💡 Lowest Set Bit Partition
1. Compute total XOR: $X = a \oplus b$.
2. Because $a \neq b$, $X$ has at least one set bit (extract via `diff = X & (-X)`).
3. Split all numbers into two groups based on whether their `diff` bit is set.
4. XORing each group independently isolates $a$ and $b$!

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Space Model | Time Complexity | Extra Memory |
| :--- | :--- | :--- | :--- |
| **Bitwise XOR (Optimal)** | Register accumulator | $\mathcal{O}(N)$ | strictly $\mathcal{O}(1)$ |
| **Hash Set** | Dynamic set | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ memory |
""",

    "153 Number of 1 Bits": """# 04 Interview Follow-ups & System Variations: Number of 1 Bits

The problem counts the number of set bits (Hamming Weight) in a 32-bit unsigned integer. Optimal solutions include **Brian Kernighan's Algorithm** in $\mathcal{O}(\text{set bits})$ and hardware `POPCNT` instructions in $\mathcal{O}(1)$.

In technical interviews, this problem tests low-level bit tricks, hardware CPU instructions, and parallel bit counting.

---

## 1. Brian Kernighan's Algorithm (`n &= (n - 1)`)

### 💡 The Lowest Set Bit Clear Trick
- `n - 1` flips all bits from the rightmost set bit downwards.
- `n & (n - 1)` clears the lowest set bit to 0 in a single operation.
- Loop runs in strictly $\mathcal{O}(K)$ steps where $K$ is the number of set bits (not 32 steps!).

---

## 2. Hardware Instruction: `POPCNT`

### 💡 1-Cycle Native CPU Execution
- Modern x86 / ARM processors have dedicated silicon for counting bits:
  ```cpp
  int count = __builtin_popcount(n); // In GCC / Clang (maps directly to POPCNT instruction)
  ```

---

## Summary Matrix: Trade-offs at a Glance

| Method | Steps | Time Complexity | Hardware Direct |
| :--- | :--- | :--- | :--- |
| **Brian Kernighan** | Number of set bits | $\mathcal{O}(\text{Set Bits})$ | 0 extra space |
| **`__builtin_popcount`**| 1 CPU cycle | $\mathcal{O}(1)$ | **POPCNT instruction** |
| **Lookup Table (8-bit)**| 4 table lookups | $\mathcal{O}(1)$ | 256-byte static table |
""",

    "154 Counting Bits": """# 04 Interview Follow-ups & System Variations: Counting Bits

The problem returns an array of the number of 1 bits for every integer from $0$ to $N$. Optimal Bit Manipulation DP calculates the result in strictly $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ output space.

In technical interviews, this problem tests bitwise DP state transitions.

---

## 1. Two Bitwise Dynamic Programming Recurrences

### 💡 Recurrence A: Right-Shift (Even/Odd Transition)
$$\text{ans}[i] = \text{ans}[i \gg 1] + (i \ \& \ 1)$$
- Every right-shifted number $i \gg 1$ has already been computed. Add 1 if the last bit is set.

### 💡 Recurrence B: Brian Kernighan's Step
$$\text{ans}[i] = \text{ans}[i \ \& \ (i - 1)] + 1$$
- $i \ \& \ (i - 1)$ has strictly 1 fewer set bit than $i$.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Formula | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Right-Shift DP** | `ans[i >> 1] + (i & 1)` | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ auxiliary |
| **Lowest-Bit DP** | `ans[i & (i - 1)] + 1` | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ auxiliary |
| **Naive Popcount** | Call popcount on each $i$ | $\mathcal{O}(N \log N)$ | $\mathcal{O}(1)$ auxiliary |
"""
}

# Write Phase 09
for folder_name, content in data_p9.items():
    folder_path = os.path.join(BASE_DIR_P9, folder_name)
    if os.path.exists(folder_path):
        target_file = os.path.join(folder_path, "04_Interview_Followups.md")
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Written Phase 09: {target_file}")
    else:
        print(f"Folder NOT found: {folder_path}")

# Write Phase 10
for folder_name, content in data_p10.items():
    folder_path = os.path.join(BASE_DIR_P10, folder_name)
    if os.path.exists(folder_path):
        target_file = os.path.join(folder_path, "04_Interview_Followups.md")
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Written Phase 10: {target_file}")
    else:
        print(f"Folder NOT found: {folder_path}")
