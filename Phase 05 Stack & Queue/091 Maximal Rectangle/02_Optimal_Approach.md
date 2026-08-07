# Maximal Rectangle

## Pattern Used

- **Pattern**: **Dynamic Histogram Heights + Monotonic Stack (LeetCode #84 Sub-routine)**
- **Concept**: Maintain a 1D array `heights` of size `cols`. Process the binary matrix row-by-row:
  - For each cell `(r, c)`:
    - If `matrix[r][c] == '1'`, increment `heights[c] += 1`.
    - If `matrix[r][c] == '0'`, reset `heights[c] = 0`.
  - Pass `heights` into `largestRectangleInHistogram(heights)` to get the maximum rectangle using row `r` as the base.
  - Update global `max_area`.

---

## Observation

1. Each row in the binary matrix can be viewed as the ground level of a **Histogram**!
2. The height of bar `c` at row `r` is the count of consecutive `'1'`s directly above `(r, c)`.
3. Running LeetCode #84 (Largest Rectangle in Histogram) on the updated `heights` array at each row $R$ finds the largest rectangle ending at or above row $R$ in $\mathcal{O}(C)$ time.
4. Total runtime for $R$ rows $= \mathcal{O}(R \times C)$.

---

## Intuition

Accumulate consecutive `'1'`s column-wise to convert each row into a histogram. Solve the 1D histogram problem for each row using a Monotonic Stack.

---

## Algorithm

1. If `matrix` is empty, return `0`.
2. `rows = matrix.size()`, `cols = matrix[0].size()`, `max_area = 0`.
3. `heights` vector of size `cols` initialized to `0`.
4. Loop `r` from `0` to `rows - 1`:
   a. For `c` from `0` to `cols - 1`:
      - If `matrix[r][c] == '1'`: `heights[c] += 1`.
      - Else: `heights[c] = 0`.
   b. `area = largestRectangleArea(heights)`.
   c. `max_area = max(max_area, area)`.
5. Return `max_area`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <stack>
#include <algorithm>

class Solution {
private:
    int largestRectangleArea(const std::vector<int>& heights) {
        int n = heights.size();
        int max_area = 0;
        std::stack<int> st;
        
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

public:
    int maximalRectangle(const std::vector<std::vector<char>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return 0;
        
        int rows = matrix.size();
        int cols = matrix[0].size();
        int max_area = 0;
        
        std::vector<int> heights(cols, 0);
        
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (matrix[r][c] == '1') {
                    heights[c] += 1;
                } else {
                    heights[c] = 0; // Reset height on '0'
                }
            }
            
            // Calculate max area for histogram at current row base
            max_area = std::max(max_area, largestRectangleArea(heights));
        }
        
        return max_area;
    }
};
```

---

## Dry Run

### Input
```text
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
```

### Execution Trace

- **Row 0**: `heights = [1, 0, 1, 0, 0]` $\implies$ Histogram Max Area = `1`
- **Row 1**: `heights = [2, 0, 2, 1, 1]` $\implies$ Histogram Max Area = `3`
- **Row 2**: `heights = [3, 1, 3, 2, 2]` $\implies$ Histogram Max Area = **`6`** (Heights `[3, 2, 2]` at cols 2..4 form $2 \times 3 = 6$)
- **Row 3**: `heights = [4, 0, 0, 3, 0]` $\implies$ Histogram Max Area = `4`

### Result
- Output: `6`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(R \times C)$
  - Updating `heights` takes $\mathcal{O}(C)$; histogram evaluation takes $\mathcal{O}(C)$ per row. Repeated for $R$ rows $\implies \mathcal{O}(R \times C)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(C)$
  - Stores 1D `heights` vector and Monotonic Stack of size $C$.

---

## Why This is Optimal

- Solves 2D Maximal Rectangle in optimal $\mathcal{O}(R \times C)$ time.
- Uses minimal $\mathcal{O}(C)$ auxiliary space.

---

## Common Mistakes

1. **Not Resetting `heights[c] = 0` on `'0'`**: Accumulating heights across `'0'` cells. When `matrix[r][c] == '0'`, the bar height MUST reset to 0 because rectangles cannot span over `'0'`s.
2. **Re-calculating Heights from Scratch**: Computing heights from top to current cell in $\mathcal{O}(R)$ per cell instead of incrementally updating `heights[c] += 1`.
