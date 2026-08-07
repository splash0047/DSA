# Problem Summary

Given an array of strings `tokens` representing an arithmetic expression in **Reverse Polish Notation** (Postfix), evaluate the expression and return the result. The optimal approach uses an **Operand Stack** `std::stack<long long> st`. We push integer tokens onto `st`. When an operator is encountered, we pop $b$ (right operand) and $a$ (left operand), calculate $a \text{ (op) } b$, and push the result back onto `st` in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to evaluate **postfix / prefix / infix arithmetic expressions**.
- Operand Stack Expression Evaluation pattern.

---

## Important Clues

1. **"Reverse Polish Notation (Postfix)"**: Operands precede operators $\implies$ Operand Stack pattern.
2. **"Division truncates toward zero"**: Standard integer division `/` behavior in C++.

---

## Example

### Input
`tokens = ["4", "13", "5", "/", "+"]`

### Visual Step-by-Step Progression

```text
Processing tokens ["4", "13", "5", "/", "+"]:

t = "4"  -> Push 4      | 4 |
t = "13" -> Push 13     | 13 | 4 |
t = "5"  -> Push 5      | 5 | 13 | 4 |
t = "/"  -> b=5, a=13  -> 13/5 = 2  -> Push 2  | 2 | 4 |
t = "+"  -> b=2, a=4   -> 4+2 = 6   -> Push 6  | 6 |

Final Result: 6
```

---

## Alternative Solutions

### In-Place Vector Replacement (Brute Force)
- Search for operators sequentially in `vector<string>` and collapse 3 tokens `[a, b, op]` into 1 result token using `erase()`.
- **Time Complexity**: $\mathcal{O}(N^2)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **Single Token Input**: `tokens = ["3"]` -> Returns `3`.
2. **Negative Numbers**: `tokens = ["-4", "3", "+"]` -> Correctly parses `-4` via `stoll()`.
3. **Truncation Toward Zero**: `-7 / 3 = -2` in C++ integer division.

---

## Interview Tips

- **Highlight Operand Order Caution**: State *"In postfix evaluation, when popping operands for operator `op`, `b = st.top()` is the RIGHT operand and `a = st.top()` is the LEFT operand. The calculation MUST be $a \text{ (op) } b$, which is non-commutative for subtraction and division."*

---

## Similar Problems

1. [LeetCode #224: Basic Calculator](https://leetcode.com/problems/basic-calculator/)
2. [LeetCode #227: Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)
3. [LeetCode #282: Expression Add Operators](https://leetcode.com/problems/expression-add-operators/)

---

## Revision Notes

- Problem: Evaluate Reverse Polish Notation (Postfix) expression.
- Pattern: Operand Stack (`std::stack<long long> st`).
- Loop `string t` in `tokens`:
  - `if (t is operator)`:
    - `b = st.top(); st.pop(); a = st.top(); st.pop();`
    - `st.push(a (op) b);`
  - `else st.push(stoll(t));`
- Return `st.top()`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(N)$.
