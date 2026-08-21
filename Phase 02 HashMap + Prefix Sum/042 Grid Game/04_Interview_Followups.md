# 04 Interview Follow-ups & System Variations: Grid Game

The problem involves two robots moving across a $2 \times N$ matrix. Robot 1 wants to minimize the score Robot 2 can collect, while Robot 2 plays greedily to maximize its score. Using Prefix Sums on the 2 rows, Robot 1 checks each possible downward column transition in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is used to test Game Theory (Minimax principle), prefix/suffix state tracking, and $K$-row generalizations.

---

## 1. Minimax Game Theory: Why Robot 2 Only Has 2 Available Choices

### 💡 The Structural Invariant of $2 \times N$ Grid
- When Robot 1 transitions from Row 0 to Row 1 at column $i$, it sets all visited cells to `0`.
- This leaves only two disjoint paths for Robot 2:
  1. **Top Suffix Path**: Stay on Row 0 until the end: $\text{Sum}(\text{grid}[0][i+1 \dots N-1])$.
  2. **Bottom Prefix Path**: Drop immediately to Row 1: $\text{Sum}(\text{grid}[1][0 \dots i-1])$.
- Robot 2 will always choose the maximum of these two values:
  $$\text{Robot2\_Score}(i) = \max\Big(\text{top\_suffix}[i + 1],\; \text{bottom\_prefix}[i - 1]\Big)$$
- Robot 1 picks the transition column $i$ that minimizes this value:
  $$\text{Minimax Score} = \min_{0 \le i < N} \Big( \max(\text{top\_suffix}[i + 1],\; \text{bottom\_prefix}[i - 1]) \Big)$$

---

## 2. Low-Memory $\mathcal{O}(1)$ Space Implementation

### 💡 Running Suffix and Prefix Variables
```cpp
long long gridGame(vector<vector<int>>& grid) {
    int n = grid[0].size();
    long long top_sum = 0, bottom_sum = 0;
    for (int x : grid[0]) top_sum += x;
    
    long long min_robot2 = LLONG_MAX;
    for (int i = 0; i < n; i++) {
        top_sum -= grid[0][i]; // top_sum now represents grid[0][i+1...n-1]
        
        long long robot2 = max(top_sum, bottom_sum);
        min_robot2 = min(min_robot2, robot2);
        
        bottom_sum += grid[1][i]; // bottom_sum becomes grid[1][0...i]
    }
    return min_robot2;
}
```
- **Space Complexity**: strictly $\mathcal{O}(1)$.

---

## 3. Generalization: $K \times N$ Matrix ($K > 2$ Rows)

### 🛑 Why Simple Top/Bottom Prefix Fails
When $K > 2$, Robot 1's path divides the grid into complex unvisited regions, giving Robot 2 many non-trivial paths.
- **Solution**: Dynamic Programming with Minimax evaluation or Backward Induction Game Tree search.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Space Model | Time Complexity | Extra Memory |
| :--- | :--- | :--- | :--- |
| **Prefix/Suffix Arrays** | 2 Arrays of size $N$ | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **Running Scalars (Optimal)**| `top_sum` & `bottom_sum` | $\mathcal{O}(N)$ | strictly $\mathcal{O}(1)$ |
| **$K \times N$ Grid Game** | Minimax DP | $\mathcal{O}(N^K)$ / DP Tree | $\mathcal{O}(K \cdot N)$ |
