# Daily Temperatures

## Pattern Used

- **Pattern**: **Monotonic Decreasing Stack (Next Greater Element)**
- **Concept**: Maintain a stack of array indices `std::stack<int> st` such that temperatures corresponding to these indices are stored in **monotonically decreasing order**.
  - Iterate through `temperatures` at index `i`.
  - While `st` is non-empty and `temperatures[i] > temperatures[st.top()]`:
    - The current day `i` is the NEXT WARMER DAY for index `st.top()`!
    - Pop index `prev_idx = st.top()`.
    - Record `ans[prev_idx] = i - prev_idx`.
  - Push current index `i` onto `st`.

---

## Observation

1. Finding the next warmer day is mathematically identical to finding the **Next Greater Element** to the right for each element in an array!
2. The stack stores indices of days whose next warmer day has not yet been found.
3. Every index is pushed onto `st` once and popped from `st` once $\implies$ Total operations $= 2N = \mathcal{O}(N)$.

---

## Intuition

Keep track of unresolved cooler days on a stack. When a warmer day arrives, resolve all previous cooler days on the stack that are strictly cooler than the current day.

---

## Algorithm

1. `n = temperatures.size()`.
2. Initialize `ans(n, 0)` and `std::stack<int> st`.
3. Loop `i` from `0` to `n - 1`:
   a. While `!st.empty()` and `temperatures[i] > temperatures[st.top()]`:
      - `prev_idx = st.top()`.
      - `st.pop()`.
      - `ans[prev_idx] = i - prev_idx`.
   b. `st.push(i)`.
4. Return `ans`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <stack>

class Solution {
public:
    std::vector<int> dailyTemperatures(const std::vector<int>& temperatures) {
        int n = temperatures.size();
        std::vector<int> ans(n, 0);
        std::stack<int> st; // Stores indices of unresolved days
        
        for (int i = 0; i < n; ++i) {
            while (!st.empty() && temperatures[i] > temperatures[st.top()]) {
                int prev_idx = st.top();
                st.pop();
                ans[prev_idx] = i - prev_idx;
            }
            st.push(i);
        }
        
        return ans;
    }
};
```

---

## Dry Run

### Input
- `temperatures = [73, 74, 75, 71, 69, 72, 76, 73]`

### Execution Trace

| Day `i` | Temp `temperatures[i]` | Stack Action / Evictions | `ans` Array State |
| :--- | :--- | :--- | :--- |
| `0` | `73` | Push `0` | `[0,0,0,0,0,0,0,0]` |
| `1` | `74` | `74 > 73` $\implies$ Pop `0`, `ans[0] = 1-0 = 1`. Push `1`. | `[1,0,0,0,0,0,0,0]` |
| `2` | `75` | `75 > 74` $\implies$ Pop `1`, `ans[1] = 2-1 = 1`. Push `2`. | `[1,1,0,0,0,0,0,0]` |
| `3` | `71` | Push `3` | `[1,1,0,0,0,0,0,0]` |
| `4` | `69` | Push `4` | `[1,1,0,0,0,0,0,0]` |
| `5` | `72` | `72 > 69` $\implies$ Pop `4`, `ans[4] = 5-4 = 1`. <br>`72 > 71` $\implies$ Pop `3`, `ans[3] = 5-3 = 2`. Push `5`. | `[1,1,0,2,1,0,0,0]` |
| `6` | `76` | Pops `5` (`ans[5]=1`), Pops `2` (`ans[2]=4`). Push `6`. | `[1,1,4,2,1,1,0,0]` |
| `7` | `73` | Push `7` | `[1,1,4,2,1,1,0,0]` |

### Result
- Output: `[1, 1, 4, 2, 1, 1, 0, 0]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Each index is pushed and popped from `st` at most once.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Stack stores at most $N$ indices in worst case.

---

## Why This is Optimal

- Solves Next Warmer Day search in linear $\mathcal{O}(N)$ time.
- Uses optimal monotonic stack space.

---

## Common Mistakes

1. **Pushing Temperatures Instead of Indices**: Pushing `temperatures[i]` onto stack instead of index `i`. Storing indices allows calculating day differences `i - prev_idx`.
2. **Strictly Warmer Condition**: Using `>=` instead of `>`. The problem requires a **warmer** temperature, so equal temperatures do NOT resolve the waiting period.
