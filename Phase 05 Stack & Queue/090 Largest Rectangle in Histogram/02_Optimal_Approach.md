# Largest Rectangle in Histogram

## Pattern Used

- **Pattern**: **Monotonic Increasing Stack (Single Pass Boundary Resolution)**
- **Concept**: Maintain a stack of bar indices `std::stack<int> st` such that bar heights corresponding to these indices are in **monotonically increasing order**.
  - Iterate `i` from `0` to `n` (using a dummy height `0` at index `n` to flush remaining elements).
  - While `!st.empty()` and `heights[i] < heights[st.top()]`:
    - The current bar `i` is the **Next Smaller Element (right boundary)** for the bar at `st.top()`!
    - Pop `h = heights[st.top()]`.
    - The new `st.top()` (after popping) is the **Previous Smaller Element (left boundary)**!
    - `width = st.empty() ? i : (i - st.top() - 1)`.
    - `max_area = max(max_area, h * width)`.
  - Push index `i` onto `st`.

---

## Observation

1. A bar `h` can form a rectangle spanning from its **Previous Smaller Element** on the left to its **Next Smaller Element** on the right.
2. A Monotonic Increasing Stack automatically identifies BOTH the Previous Smaller Element (`st.top()` after pop) AND Next Smaller Element (`i` before push) simultaneously!
3. Virtual Guard `heights[n] = 0` ensures all remaining non-popped bars in the stack are fully evaluated when the loop reaches `n`.

---

## Intuition

Keep bars ordered in increasing height on a stack. When a shorter bar arrives, pop the taller bars off the stack; for each popped bar, calculate the largest rectangle it could have formed using the current index as the right boundary and the new stack top as the left boundary.

---

## Algorithm

1. `n = heights.size()`, `max_area = 0`, `std::stack<int> st`.
2. Loop `i` from `0` to `n`:
   a. `curr_h = (i == n) ? 0 : heights[i]`.
   b. While `!st.empty()` and `curr_h < heights[st.top()]`:
      - `h = heights[st.top()]`.
      - `st.pop()`.
      - `w = st.empty() ? i : (i - st.top() - 1)`.
      - `max_area = max(max_area, h * w)`.
   c. `st.push(i)`.
3. Return `max_area`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <stack>
#include <algorithm>

class Solution {
public:
    int largestRectangleArea(const std::vector<int>& heights) {
        int n = heights.size();
        int max_area = 0;
        std::stack<int> st; // Monotonic Increasing Stack of indices
        
        for (int i = 0; i <= n; ++i) {
            int curr_h = (i == n) ? 0 : heights[i];
            
            while (!st.empty() && curr_h < heights[st.top()]) {
                int h = heights[st.top()];
                st.pop();
                
                int w = st.empty() ? i : (i - st.top() - 1);
                max_area = std::max(max_area, h * w);
            }
            
            st.push(i);
        }
        
        return max_area;
    }
};
```

---

## Dry Run

### Input
- `heights = [2, 1, 5, 6, 2, 3]`

### Execution Trace

- `i = 0` (h=2): Push `0`. Stack: `[0]`
- `i = 1` (h=1): `1 < 2` $\implies$ Pop `0` (h=2), `w = 1`, `area = 2*1 = 2`. Push `1`. Stack: `[1]`
- `i = 2` (h=5): Push `2`. Stack: `[1, 2]`
- `i = 3` (h=6): Push `3`. Stack: `[1, 2, 3]`
- `i = 4` (h=2):
  - `2 < 6` $\implies$ Pop `3` (h=6), `w = 4 - 2 - 1 = 1`, `area = 6*1 = 6`.
  - `2 < 5` $\implies$ Pop `2` (h=5), `w = 4 - 1 - 1 = 2`, `area = 5*2 = 10` (**Max Area = 10!**).
  - Push `4`. Stack: `[1, 4]`
- `i = 5` (h=3): Push `5`. Stack: `[1, 4, 5]`
- `i = 6` (h=0): Flushes remaining stack entries `5`, `4`, `1`.

### Result
- Output: `10` (Heights 5 and 6 form $5 \times 2 = 10$)

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Each index is pushed and popped from `st` exactly once.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Stack stores at most $N + 1$ indices.

---

## Why This is Optimal

- Computes largest histogram rectangle in optimal single-pass $\mathcal{O}(N)$ time.
- Uses minimal stack space.

---

## Common Mistakes

1. **Forgetting Dummy Height `0` at `i == n`**: Failing to flush the remaining non-popped bars in the stack after loop ends (e.g. input `heights = [1, 2, 3, 4]`).
2. **Incorrect Width Formula**: Writing `i - st.top()` instead of `i - st.top() - 1`. The width must exclude both the left smaller boundary (`st.top()`) and the right smaller boundary (`i`).
