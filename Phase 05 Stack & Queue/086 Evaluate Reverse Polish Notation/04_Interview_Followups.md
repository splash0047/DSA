# 04 Interview Follow-ups & System Variations: Evaluate Reverse Polish Notation

The problem evaluates an arithmetic expression in Reverse Polish Notation (Postfix). The optimal stack-based approach runs in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

In technical interviews, this problem is compared with Infix-to-Postfix conversion (Dijkstra's Shunting-Yard Algorithm), integer truncation quirks across languages, and AST Expression Tree parsing.

---

## 1. The Integer Truncation Towards Zero Bug (C++ vs. Python)

### 🛑 The Hazard of `//` in Python
In Python, `//` performs **floor division** (rounds towards $-\infty$):
- `-3 // 2 = -2` in Python.
- But RPN specifications require **truncating towards zero**: $-3 / 2 = -1$.
- **Python Fix**: Use `int(a / b)` or `math.trunc(a / b)`.
- In C++ and Java, `/` natively truncates towards zero.

---

## 2. Infix to Postfix Conversion: Dijkstra's Shunting-Yard Algorithm

### 💡 Operator Precedence Stack
- Operands go directly to output queue.
- Operators $\in \{+, -, 	imes, /\}$:
  - While top of operator stack has $\ge$ precedence, pop to output.
  - Push current operator.
- `'('`: Push to stack; `')'`: Pop operators to output until `'('` is reached.

---

## Summary Matrix: Trade-offs at a Glance

| Expression Form | Evaluation Method | Time | Space |
| :--- | :--- | :--- | :--- |
| **Postfix (RPN)** | Single Operand Stack | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **Infix (Standard)** | Shunting-Yard Algorithm | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **Prefix (Polish)** | Right-to-Left Stack Scan | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
