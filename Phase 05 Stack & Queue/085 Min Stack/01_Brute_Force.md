# Min Stack

- **Problem Number**: 155
- **Platform**: LeetCode #155
- **Difficulty**: Medium
- **Pattern**: Vector Linear Scan

---

## Brute Force Intuition

Use a `std::vector<int> st` to store stack elements.
- `push(val)`: Append `val` to `st`.
- `pop()`: Remove last element `st.pop_back()`.
- `top()`: Return last element `st.back()`.
- `getMin()`: Perform a linear scan over all elements in `st` to find and return the minimum value.

---

## Algorithm

1. `push(val)`: `st.push_back(val)`.
2. `pop()`: `st.pop_back()`.
3. `top()`: `return st.back()`.
4. `getMin()`:
   - `min_val = st[0]`.
   - Loop `x` in `st`: `min_val = min(min_val, x)`.
   - Return `min_val`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class MinStack {
private:
    std::vector<int> st;
public:
    MinStack() {}
    
    void push(int val) {
        st.push_back(val);
    }
    
    void pop() {
        st.pop_back();
    }
    
    int top() {
        return st.back();
    }
    
    int getMin() {
        return *std::min_element(st.begin(), st.end());
    }
};
```

---

## Time Complexity

- **`push` / `pop` / `top`**: $\mathcal{O}(1)$
- **`getMin`**: $\mathcal{O}(N)$
  - Scans all $N$ stack elements to find minimum.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Vector stores $N$ elements.

---

## Why This Approach Is Not Optimal

`getMin()` takes $\mathcal{O}(N)$ time. The problem statement mandates that **all methods** (including `getMin`) must run in $\mathcal{O}(1)$ time. Using **Auxiliary Min Stack** or **Value-Min Pair Stack**, we achieve $\mathcal{O}(1)$ time for all operations.
