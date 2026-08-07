# Min Stack

## Pattern Used

- **Pattern**: **Dual Stack / Pair Stack Tracking**
- **Concept**: Maintain a primary stack `st` storing `std::pair<int, int>` where each entry contains `{value, current_min_at_this_level}`.
  - When pushing `val`, compute `new_min = st.empty() ? val : min(val, st.top().second)`.
  - Push `{val, new_min}` onto `st`.
  - `getMin()` simply returns `st.top().second` in $\mathcal{O}(1)$ time!

---

## Observation

1. Stack LIFO order preserves history: when an element is popped, the minimum element of the remaining stack automatically reverts to what it was before that element was pushed!
2. By storing the minimum value *at the moment of insertion* alongside each element, every stack level carries its own historical minimum.
3. This eliminates the need for any linear scanning or re-evaluation.

---

## Intuition

Each node on the stack remembers the minimum element in the stack up to that height.

---

## Algorithm

1. Primary Stack: `std::stack<std::pair<int, int>> st`.
2. `push(val)`:
   - If `st.empty()`, `curr_min = val`.
   - Else `curr_min = min(val, st.top().second)`.
   - `st.push({val, curr_min})`.
3. `pop()`:
   - `st.pop()`.
4. `top()`:
   - `return st.top().first`.
5. `getMin()`:
   - `return st.top().second`.

---

## Clean C++17 Solution

```cpp
#include <stack>
#include <utility>
#include <algorithm>

class MinStack {
private:
    std::stack<std::pair<int, int>> st; // {val, min_so_far}
public:
    MinStack() {}
    
    void push(int val) {
        if (st.empty()) {
            st.push({val, val});
        } else {
            int current_min = std::min(val, st.top().second);
            st.push({val, current_min});
        }
    }
    
    void pop() {
        st.pop();
    }
    
    int top() {
        return st.top().first;
    }
    
    int getMin() {
        return st.top().second;
    }
};
```

---

## Dry Run

### Input Operations
`push(-2)`, `push(0)`, `push(-3)`, `getMin()`, `pop()`, `top()`, `getMin()`

### Execution Trace

| Operation | Value | Stack Entry `{val, min_so_far}` | `st.top().first` | `getMin()` (`st.top().second`) |
| :--- | :--- | :--- | :--- | :--- |
| `push(-2)` | `-2` | `{-2, -2}` | `-2` | `-2` |
| `push(0)` | `0` | `{0, -2}` | `0` | `-2` |
| `push(-3)` | `-3` | `{-3, -3}` | `-3` | **`-3`** |
| `pop()` | - | Pops `{-3, -3}` | `0` | `-2` |
| `top()` | - | Inspect `st.top()` | **`0`** | `-2` |
| `getMin()` | - | Inspect `st.top()` | `0` | **`-2`** |

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(1)$ for all operations (`push`, `pop`, `top`, `getMin`).
  - Stack operations take strict constant time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Stores $N$ pair entries in stack memory.

---

## Why This is Optimal

- Meets the mandatory $\mathcal{O}(1)$ time complexity for all methods.
- Simple, robust implementation without integer overflow risks.

---

## Common Mistakes

1. **Integer Overflow in Single Variable Math Trick**: Attempting 1-stack math tricks like pushing `2 * val - min` can overflow 32-bit signed integer limits (`INT_MIN`, `INT_MAX`). Storing `{val, min_so_far}` pairs avoids overflow completely.
2. **Missing `st.empty()` Check on First Push**: Dereferencing `st.top()` on an empty stack during initial push.
