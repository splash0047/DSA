# 04 Interview Follow-ups & System Variations: Fruit Into Baskets

The problem finds the maximum number of fruits you can pick from trees with only 2 baskets (each basket holding only 1 type of fruit). This is an exact alias for **Longest Subarray with At Most 2 Distinct Elements**. The optimal sliding window achieves $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is used to test problem pattern abstraction, non-shrinking window optimization, and generalized $K$-type capacity.

---

## 1. Pattern Abstraction: Equivalence to Longest Subarray with $\le 2$ Distinct Elements

### 💡 Recognizing Disguised Sliding Window Problems
- Fruit types = Distinct integers.
- 2 Baskets = Maximum 2 distinct keys allowed in sliding window.
- Contiguous trees = Contiguous subarray.
- Always translate real-world story problems into formal mathematical DSA invariants for the interviewer.

---

## 2. Low-Memory Optimization: Eliminating the Hash Map ($\mathcal{O}(1)$ Working Memory)

### 🛑 Hash Map Overhead
Using `unordered_map<int, int>` introduces heap allocations for node buckets.

### 💡 4-Variable State Tracker
Track only the two active fruit types and the continuous consecutive streak of the most recent type:
```cpp
int totalFruit(vector<int>& fruits) {
    int last_fruit = -1, second_last_fruit = -1;
    int last_fruit_count = 0;
    int current_max = 0, max_fruits = 0;
    
    for (int fruit : fruits) {
        if (fruit == last_fruit || fruit == second_last_fruit) {
            current_max++;
        } else {
            // New fruit type: length resets to the consecutive run of the last fruit + 1
            current_max = last_fruit_count + 1;
        }
        
        if (fruit == last_fruit) {
            last_fruit_count++;
        } else {
            second_last_fruit = last_fruit;
            last_fruit = fruit;
            last_fruit_count = 1;
        }
        max_fruits = max(max_fruits, current_max);
    }
    return max_fruits;
}
```
- **Advantages**: 0 heap allocations, 0 map lookups, purely in CPU registers.

---

## 3. Generalization: $K$ Baskets (At Most $K$ Fruit Types)

### 💡 Dynamic Map with Non-Shrinking Window
- Maintain `unordered_map<int, int> count`.
- As `right` advances, if `count.size() > K`, decrement `count[fruits[left]]` and increment `left++`.
- Time Complexity: $\mathcal{O}(N)$, Space Complexity: $\mathcal{O}(K)$.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Baskets ($K$) | Data Structure | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **State Machine Tracking** | $K = 2$ | 4 primitive variables | $\mathcal{O}(N)$ | strictly $\mathcal{O}(1)$ |
| **Standard Sliding Window**| $K = 2$ | `unordered_map<int, int>` | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ heap |
| **Generalized $K$ Baskets**| Arbitrary $K$ | Hash Map / Non-Shrinking | $\mathcal{O}(N)$ | $\mathcal{O}(K)$ |
