# Next Greater Element II

## Pattern Used

- **Pattern**: **Monotonic Decreasing Stack + Virtual Concatenated Array ($2N$)**
- **Concept**:
  1. A circular array of length $N$ is equivalent to concatenating `nums` with itself, forming a virtual array of length $2N$.
  2. Iterate `i` from `2N - 1` down to `0` (or `0` to `2N - 1`). Use index modulo `i % N` to simulate accessing the circular array.
  3. Maintain a **Monotonic Decreasing Stack** `st` storing element values/indices.
  4. At each step `i`:
     - While `!st.empty() && st.top() <= nums[i % N]`: `st.pop()`.
     - If `i < N` (during the second half of iteration): `ans[i] = st.empty() ? -1 : st.top()`.
     - `st.push(nums[i % N])`.

---

## Observation

1. Why traverse $2N$ iterations?
   - Traversing from right to left over $2N$ elements allows elements near the end of `nums` to see elements at the beginning of `nums` (wrapping around the circular array).
2. Processing backwards from `2N - 1` down to `0` maintains the Next Greater Element at `st.top()` ready for immediate query!

---

## Intuition

Simulate scanning a duplicated array `[nums, nums]` from right to left using a Monotonic Stack to resolve circular Next Greater Element queries.

---

## Algorithm

1. `n = nums.size()`.
2. Initialize `ans(n, -1)` and `std::stack<int> st`.
3. Loop `i` from `2 * n - 1` down to `0`:
   a. `curr_val = nums[i % n]`.
   b. While `!st.empty()` and `st.top() <= curr_val`:
      - `st.pop()`.
   c. If `i < n`:
      - `ans[i] = st.empty() ? -1 : st.top()`.
   d. `st.push(curr_val)`.
4. Return `ans`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <stack>

class Solution {
public:
    std::vector<int> nextGreaterElements(const std::vector<int>& nums) {
        int n = nums.size();
        std::vector<int> ans(n, -1);
        std::stack<int> st;
        
        // Traverse virtual 2N array backward
        for (int i = 2 * n - 1; i >= 0; --i) {
            int curr = nums[i % n];
            
            while (!st.empty() && st.top() <= curr) {
                st.pop();
            }
            
            if (i < n) {
                ans[i] = st.empty() ? -1 : st.top();
            }
            
            st.push(curr);
        }
        
        return ans;
    }
};
```

---

## Dry Run

### Input
- `nums = [1, 2, 1]` ($N = 3$)
- Virtual array range: $i \in [5 \dots 0]$

### Execution Trace

- Virtual sequence: `[1, 2, 1,  1, 2, 1]` (indices 0..2 repeated as 3..5)

| Step `i` | `i % N` | `curr` | Stack Action | `ans[i]` (when $i < 3$) |
| :--- | :--- | :--- | :--- | :--- |
| `5` | `2` | `1` | Push `1` | - |
| `4` | `1` | `2` | Pop `1`, Push `2` | - |
| `3` | `0` | `1` | Push `1`. Stack: `[2, 1]` | - |
| `2` | `2` | `1` | `1 < top (2)` $\implies$ Push `1`. Stack: `[2, 1]` | **`ans[2] = 2`** |
| `1` | `1` | `2` | Pop `1`. `st.top() == 2` $\implies$ Pop `2`. Stack empty. Push `2`. | **`ans[1] = -1`** |
| `0` | `0` | `1` | `1 < top (2)` $\implies$ Push `1`. | **`ans[0] = 2`** |

### Result
- Output: `[2, -1, 2]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - $2N$ iterations. Each element is pushed and popped from `st` at most twice.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Stack stores at most $N$ elements.

---

## Why This is Optimal

- Solves circular Next Greater Element in linear $\mathcal{O}(N)$ time.
- Uses minimal stack memory without allocating an actual doubled array.

---

## Common Mistakes

1. **Actually Allocating a $2N$ Vector**: Creating `vector<int> doubled_nums` doubles memory usage unnecessarily. Use index modulo `i % n` on the original vector instead!
2. **Using Strict `<` instead of `<=`**: Using `<` keeps duplicate values on top of stack, causing equal values to be reported as "greater". Use `<=` so equal values are popped off.
