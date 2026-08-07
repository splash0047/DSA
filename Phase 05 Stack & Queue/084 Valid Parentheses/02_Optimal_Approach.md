# Valid Parentheses

## Pattern Used

- **Pattern**: **Stack (LIFO Matching)**
- **Concept**: Maintain a stack of opening brackets (`std::stack<char>`).
  - When encountering an opening bracket `(`, `{`, `[`, push it onto the stack.
  - When encountering a closing bracket `)`, `}`, `]`:
    - Check if stack is empty (unmatched closing bracket) $\implies$ return `false`.
    - Compare current closing bracket with `stack.top()`. If they do not match, return `false`.
    - Pop the matching opening bracket from the stack.
  - At the end, if stack is empty, return `true`.

---

## Observation

1. LIFO Property: The **most recently opened** bracket MUST be the **first to be closed**!
2. This Last-In-First-Out behavior matches a Stack perfectly.
3. Odd Length Fast-Path: If `s.length() % 2 != 0`, brackets can never be fully paired $\implies$ return `false` immediately.

---

## Intuition

Push opening brackets onto a stack. When a closing bracket arrives, inspect the top of the stack. If it matches, pop it off.

---

## Algorithm

1. If `s.length() % 2 != 0`, return `false`.
2. Initialize `std::stack<char> st`.
3. For each char `ch` in `s`:
   a. If `ch == '(' || ch == '{' || ch == '['`:
      - `st.push(ch)`.
   b. Else:
      - If `st.empty()` return `false`.
      - `top = st.top()`.
      - If `ch == ')' && top != '('`: return `false`.
      - If `ch == '}' && top != '{'`: return `false`.
      - If `ch == ']' && top != '['`: return `false`.
      - `st.pop()`.
4. Return `st.empty()`.

---

## Clean C++17 Solution

```cpp
#include <string>
#include <stack>

class Solution {
public:
    bool isValid(const std::string& s) {
        if (s.length() % 2 != 0) return false;
        
        std::stack<char> st;
        
        for (char ch : s) {
            if (ch == '(' || ch == '{' || ch == '[') {
                st.push(ch);
            } else {
                if (st.empty()) return false;
                
                char top = st.top();
                if ((ch == ')' && top == '(') ||
                    (ch == '}' && top == '{') ||
                    (ch == ']' && top == '[')) {
                    st.pop();
                } else {
                    return false;
                }
            }
        }
        
        return st.empty();
    }
};
```

---

## Dry Run

### Input
- `s = "([])"`

### Execution Trace

| Step | Char `ch` | Action | Stack State (Bottom -> Top) |
| :--- | :--- | :--- | :--- |
| 1 | `(` | Push `(` | `(` |
| 2 | `[` | Push `[` | `(`, `[` |
| 3 | `]` | Matches `top = [` $\rightarrow$ Pop | `(` |
| 4 | `)` | Matches `top = (` $\rightarrow$ Pop | Empty |
| End | - | `st.empty()` is `true` | **Return `true`** |

### Result
- Output: `true`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass over $N$ characters with $\mathcal{O}(1)$ stack operations.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Stack stores up to $N$ opening brackets in worst case (e.g. `s = "((((("`).

---

## Why This is Optimal

- Verifies validity in a single linear pass $\mathcal{O}(N)$ time.
- Uses optimal stack space.

---

## Common Mistakes

1. **Stack Underflow Crash**: Calling `st.top()` when `st.empty() == true` (e.g., input `s = ")"`). Always check `if (st.empty()) return false` before inspecting `st.top()`.
2. **Unmatched Remaining Openers**: Returning `true` without checking `st.empty()` at the end (e.g. input `s = "(("` leaves stack non-empty).
