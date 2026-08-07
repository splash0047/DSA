# Evaluate Reverse Polish Notation

## Pattern Used

- **Pattern**: **Operand Stack Postfix Evaluation**
- **Concept**: Maintain an operand stack `std::stack<long long> st`.
  - Iterate through `tokens` from left to right.
  - If a token is an integer, convert and push it onto `st`.
  - If a token is an operator (`+`, `-`, `*`, `/`):
    - Pop second operand `b = st.top()`, `st.pop()`.
    - Pop first operand `a = st.top()`, `st.pop()`.
    - Evaluate `res = a (op) b` and push `res` back onto `st`.
  - At the end, `st.top()` contains the evaluated final result!

---

## Observation

1. Postfix notation (Reverse Polish Notation) eliminates the need for parentheses or operator precedence rules!
2. Operands always precede their operator.
3. Order of operands matters: When evaluating subtraction or division, the **first popped value is operand $B$** (right operand) and the **second popped value is operand $A$** (left operand) $\implies A - B$ or $A / B$.

---

## Intuition

Push numbers onto the stack. When an operator arrives, pop the top two numbers, apply the operation, and push the result back onto the stack.

---

## Algorithm

1. Initialize `std::stack<long long> st`.
2. For each token `t` in `tokens`:
   a. If `t == "+"`:
      - `b = st.top(); st.pop(); a = st.top(); st.pop(); st.push(a + b);`
   b. Else if `t == "-"`:
      - `b = st.top(); st.pop(); a = st.top(); st.pop(); st.push(a - b);`
   c. Else if `t == "*"`:
      - `b = st.top(); st.pop(); a = st.top(); st.pop(); st.push(a * b);`
   d. Else if `t == "/"`:
      - `b = st.top(); st.pop(); a = st.top(); st.pop(); st.push(a / b);`
   e. Else:
      - `st.push(std::stoll(t));`
3. Return `static_cast<int>(st.top())`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <string>
#include <stack>

class Solution {
public:
    int evalRPN(const std::vector<std::string>& tokens) {
        std::stack<long long> st;
        
        for (const std::string& t : tokens) {
            if (t == "+" || t == "-" || t == "*" || t == "/") {
                long long b = st.top(); st.pop();
                long long a = st.top(); st.pop();
                
                if (t == "+") st.push(a + b);
                else if (t == "-") st.push(a - b);
                else if (t == "*") st.push(a * b);
                else if (t == "/") st.push(a / b);
            } else {
                st.push(std::stoll(t));
            }
        }
        
        return static_cast<int>(st.top());
    }
};
```

---

## Dry Run

### Input
- `tokens = ["2", "1", "+", "3", "*"]`

### Execution Trace

| Step | Token `t` | Action | Stack State (Bottom -> Top) |
| :--- | :--- | :--- | :--- |
| 1 | `"2"` | Push `2` | `2` |
| 2 | `"1"` | Push `1` | `2`, `1` |
| 3 | `"+"` | `b=1, a=2` $\rightarrow$ `a+b = 3` $\rightarrow$ Push `3` | `3` |
| 4 | `"3"` | Push `3` | `3`, `3` |
| 5 | `"*"` | `b=3, a=3` $\rightarrow$ `a*b = 9` $\rightarrow$ Push `9` | `9` |
| End | - | Return `st.top()` | **Return `9`** |

### Result
- Output: `9`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass over $N$ tokens; each push and pop takes $\mathcal{O}(1)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Stack stores at most $(N + 1)/2$ operands.

---

## Why This is Optimal

- Evaluates RPN expression in a single linear pass $\mathcal{O}(N)$ time.
- Uses optimal stack space.

---

## Common Mistakes

1. **Reversing Operand Order**: Computing `b - a` or `b / a` instead of `a - b` or `a / b`. Remember: `b` is the second operand (top of stack) and `a` is the first operand (second from top).
2. **Integer Overflow on Multiplication**: Using 32-bit `int` for stack values when intermediate multiplication (e.g. `200 * 200 * ...`) or large input numbers are processed. Use `long long` for internal calculations.
