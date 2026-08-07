# Trapping Rain Water

## Pattern Used

- **Pattern**: **Monotonic Decreasing Stack (Bounded Basin Fill)** OR **Two Pointers**
- **Stack Concept**: Maintain a stack `std::stack<int> st` storing indices in **monotonically decreasing height order**.
  - Iterate `i` from `0` to `n - 1`.
  - While `!st.empty()` and `height[i] > height[st.top()]`:
    - The bar `st.top()` acts as the **bottom of a basin**!
    - Pop `mid = st.top()`.
    - If `st.empty()`, break (no left boundary wall exists to trap water).
    - `left_boundary = st.top()`, `right_boundary = i`.
    - `bounded_height = min(height[left_boundary], height[right_boundary]) - height[mid]`.
    - `distance = right_boundary - left_boundary - 1`.
    - `water += bounded_height * distance`.
  - Push index `i` onto `st`.

---

## Observation

1. Water is trapped horizontally in **basins** bounded between a left wall (`st.top()`), bottom floor (`mid`), and right wall (`i`).
2. When a taller bar `i` arrives, it closes off any lower basin floors stored in the stack.
3. Calculating water horizontal layer by layer using a Monotonic Stack takes linear $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space!

*(Alternatively, Two Pointers `left` and `right` with `left_max` and `right_max` achieves $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space).*

---

## Intuition

Push bars onto stack while heights are decreasing. When a height increases, pop the basin floor, find the left boundary wall on the stack top, and compute trapped water volume for that basin layer.

---

## Algorithm (Monotonic Stack Approach)

1. `n = height.size()`, `total_water = 0`, `std::stack<int> st`.
2. Loop `i` from `0` to `n - 1`:
   a. While `!st.empty()` and `height[i] > height[st.top()]`:
      - `mid = st.top()`.
      - `st.pop()`.
      - If `st.empty()`, break;
      - `left = st.top()`.
      - `bounded_height = min(height[left], height[i]) - height[mid]`.
      - `width = i - left - 1`.
      - `total_water += bounded_height * width`.
   b. `st.push(i)`.
3. Return `total_water`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <stack>
#include <algorithm>

class Solution {
public:
    int trap(const std::vector<int>& height) {
        int n = height.size();
        int total_water = 0;
        std::stack<int> st; // Monotonic Decreasing Stack of indices
        
        for (int i = 0; i < n; ++i) {
            while (!st.empty() && height[i] > height[st.top()]) {
                int mid = st.top();
                st.pop();
                
                if (st.empty()) {
                    break; // No left wall to hold water
                }
                
                int left = st.top();
                int bounded_h = std::min(height[left], height[i]) - height[mid];
                int width = i - left - 1;
                
                total_water += bounded_h * width;
            }
            
            st.push(i);
        }
        
        return total_water;
    }
};
```

---

## Dry Run

### Input
- `height = [0, 1, 0, 2, 1, 0, 1, 3]`

### Execution Trace

- `i = 0` (h=0): Push `0`. Stack: `[0]`
- `i = 1` (h=1): `1 > 0` $\implies$ Pop `0` (`mid=0`). Stack empty $\rightarrow$ Break. Push `1`. Stack: `[1]`
- `i = 2` (h=0): Push `2`. Stack: `[1, 2]`
- `i = 3` (h=2): `2 > 0` $\implies$ Pop `2` (`mid=2`). Left=1 (h=1).
  - `bounded_h = min(1, 2) - 0 = 1`. `width = 3 - 1 - 1 = 1`.
  - `water += 1 * 1 = 1`.
  - Pop `1` (h=1). Stack empty $\rightarrow$ Break. Push `3`. Stack: `[3]`
- Continues filling horizontal layers...

### Result
- Output Total Water: `6`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Each index is pushed onto `st` once and popped at most once.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Stack stores at most $N$ indices.

---

## Why This is Optimal

- Computes trapped rain water in a single linear pass in $\mathcal{O}(N)$ time.
- Standard stack implementation demonstrates mastery of Monotonic Stack basin filling.

---

## Common Mistakes

1. **Forgetting `st.empty()` Check After Pop**: Attempting to read `st.top()` after popping `mid` without verifying `!st.empty()`. If no left boundary exists, water spills out!
2. **Confusing Width Formula**: Writing `i - left` instead of `i - left - 1`. Width is the number of empty spaces *between* `left` and `i`.
