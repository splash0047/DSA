# Problem Summary

Given a string `s` representing an arithmetic expression with operators `+`, `-`, `*`, `/` (without parentheses), evaluate the expression. The optimal approach uses **Single-Pass Precedence Parsing with an Operand Stack**:
- Track `current_num` and `op` (initialized to `'+'`).
- When encountering an operator or end of string `i == N - 1`:
  - `+`: Push `current_num`
  - `-`: Push `-current_num`
  - `*`: Pop `last`, push `last * current_num`
  - `/`: Pop `last`, push `last / current_num`
  - Reset `op = ch`, `current_num = 0`.
- Sum all stack values at the end in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to evaluate **infix arithmetic expressions with operator precedence** (`*`, `/` over `+`, `-`).
- Single-Pass Precedence Parsing pattern.

---

## Important Clues

1. **"Evaluate string arithmetic expression with +, -, *, /"**: Expression Parsing pattern.
2. **"Truncates toward zero"**: C++ integer division behavior.

---

## Example

### Input
`s = "3+2*2"`

### Visual Step-by-Step Progression

```text
Parsing "3+2*2":

1. Number 3 with initial op '+' -> Push +3      | 3 |
2. Number 2 with op '+'         -> Push +2      | 2 | 3 |
3. Number 2 with op '*'         -> Pop 2, push 2*2=4  | 4 | 3 |

Sum stack: 3 + 4 = 7
Result: 7
```

---

## Alternative Solutions

### O(1) Space Accumulator Approach
- Track `sum`, `last_num`, and `current_num`. Perform inline addition/multiplication without an explicit stack.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **Leading/Trailing Whitespace**: `s = " 3/2 "` -> Ignored during iteration.
2. **Multi-Digit Numbers**: `s = "14-3/2"` -> Built using `current_num = current_num * 10 + (ch - '0')`.
3. **Only One Number**: `s = "42"` -> Evaluated on `i == n - 1`.

---

## Interview Tips

- **Explain Why Negative Push Handles Subtraction**: State *"By pushing `-current_num` onto the stack when `op == '-'`, we convert subtraction into addition ($A - B = A + (-B)$). This allows us to simply sum all remaining stack elements at the end in a unified final step."*

---

## Similar Problems

1. [LeetCode #224: Basic Calculator](https://leetcode.com/problems/basic-calculator/)
2. [LeetCode #772: Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/)
3. [LeetCode #150: Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

---

## Revision Notes

- Problem: Evaluate infix expression `s` with `+`, `-`, `*`, `/`.
- Pattern: Single-Pass Stack Precedence (`op` tracking).
- Loop `i` from `0` to `N - 1`:
  - `if (isdigit(ch)) current_num = current_num * 10 + (ch - '0')`.
  - `if (!isdigit(ch) && ch != ' ' || i == N - 1)`:
    - `+` $\implies$ `st.push(num)`
    - `-` $\implies$ `st.push(-num)`
    - `*` $\implies$ `st.top() *= num`
    - `/` $\implies$ `st.top() /= num`
    - `op = ch; num = 0;`
- Return sum of `st` elements.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(N)$ (or $\mathcal{O}(1)$).
