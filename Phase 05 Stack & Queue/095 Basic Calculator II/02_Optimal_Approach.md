# Basic Calculator II

## Pattern Used

- **Pattern**: **Single-Pass Precedence Parsing with Stack / Constant Space Accumulator**
- **Concept**: Track the current number `num` and the previous operator `op` (initialized to `'+'`).
  - Scan `s` character by character.
  - If digit, `num = num * 10 + (ch - '0')`.
  - When an operator or end of string is reached:
    - If `op == '+'`: Push `num` onto stack (or add to running total).
    - If `op == '-'`: Push `-num` onto stack.
    - If `op == '*'`: Pop top, multiply by `num`, push `top * num`.
    - If `op == '/'`: Pop top, divide by `num`, push `top / num`.
    - Update `op = ch`, reset `num = 0`.
  - Sum all values remaining in the stack!

---

## Observation

1. High Precedence (`*`, `/`): Must be evaluated **immediately** with the preceding number on top of the stack.
2. Low Precedence (`+`, `-`): Deferred by pushing `+num` or `-num` onto the stack.
3. At the end of the string, all remaining values in the stack represent signed terms ready to be summed together!

---

## Intuition

Convert subtraction into adding negative numbers. Perform multiplication and division on-the-fly against the top element of the stack. Sum the stack at the end.

---

## Algorithm

1. `n = s.length()`, `num = 0`, `op = '+'`, `stack<long long> st`.
2. Loop `i` from `0` to `n - 1`:
   a. `ch = s[i]`.
   b. If `isdigit(ch)`: `num = num * 10 + (ch - '0')`.
   c. If `(!isdigit(ch) && ch != ' ')` OR `i == n - 1`:
      - If `op == '+'`: `st.push(num)`.
      - If `op == '-'`: `st.push(-num)`.
      - If `op == '*'`: `last = st.top(); st.pop(); st.push(last * num)`.
      - If `op == '/'`: `last = st.top(); st.pop(); st.push(last / num)`.
      - `op = ch`, `num = 0`.
3. `res = 0`. While `!st.empty()`: `res += st.top(); st.pop()`.
4. Return `res`.

---

## Clean C++17 Solution

```cpp
#include <string>
#include <stack>
#include <cctype>
#include <numeric>

class Solution {
public:
    int calculate(const std::string& s) {
        int n = s.length();
        long long current_num = 0;
        char op = '+';
        std::stack<long long> st;
        
        for (int i = 0; i < n; ++i) {
            char ch = s[i];
            
            if (std::isdigit(ch)) {
                current_num = current_num * 10 + (ch - '0');
            }
            
            if ((!std::isdigit(ch) && ch != ' ') || i == n - 1) {
                if (op == '+') {
                    st.push(current_num);
                } else if (op == '-') {
                    st.push(-current_num);
                } else if (op == '*') {
                    long long last = st.top();
                    st.pop();
                    st.push(last * current_num);
                } else if (op == '/') {
                    long long last = st.top();
                    st.pop();
                    st.push(last / current_num);
                }
                
                op = ch;
                current_num = 0;
            }
        }
        
        long long result = 0;
        while (!st.empty()) {
            result += st.top();
            st.pop();
        }
        
        return static_cast<int>(result);
    }
};
```

---

## Dry Run

### Input
- `s = "3+2*2"`

### Execution Trace

- `i = 0` (`ch = '3'`): `current_num = 3`
  - `i == 0` check triggers operator evaluation for `op = '+'`:
  - `st.push(3)`. Stack: `[3]`. `op = '+'`, `current_num = 0`.
- `i = 1` (`ch = '+'`): `op = '+'`, `current_num = 0`.
- `i = 2` (`ch = '2'`): `current_num = 2`.
- `i = 3` (`ch = '*'`):
  - Operator evaluation for `op = '+'`: `st.push(2)`. Stack: `[3, 2]`.
  - `op = '*'`, `current_num = 0`.
- `i = 4` (`ch = '2'`, end of string `i == 4`): `current_num = 2`.
  - Trigger for `op = '*'`: Pop `2`, `last * current_num = 2 * 2 = 4`, `st.push(4)`. Stack: `[3, 4]`.

- Sum Stack: `3 + 4 = 7`.

### Result
- Output: `7`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass over string `s` of length $N$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Stack stores at most $N$ numbers. *(Can be optimized to $\mathcal{O}(1)$ space using `last_num` and `sum` variables).*

---

## Why This is Optimal

- Evaluates infix expressions with operator precedence in linear $\mathcal{O}(N)$ time.
- Handles whitespace seamlessly.

---

## Common Mistakes

1. **Missing End-of-String Condition**: Forgetting `i == n - 1` in the operator trigger check, causing the last number in the string to be ignored!
2. **Integer Truncation in Division**: Integer division in C++ automatically truncates toward zero (e.g. `3 / 2 = 1`), matching requirement.
