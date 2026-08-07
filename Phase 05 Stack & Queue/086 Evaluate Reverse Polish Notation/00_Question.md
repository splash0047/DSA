# 086. Evaluate Reverse Polish Notation

- **Platform**: LeetCode
- **Problem Number**: #150
- **Difficulty**: Medium
- **URL**: [LeetCode #150 - Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

---

## Problem Statement

You are given an array of strings `tokens` that represents an arithmetic expression in a **Reverse Polish Notation** (Postfix Notation).

Evaluate the expression. Return *an integer that represents the value of the expression*.

**Note that**:

- The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
- Each operand may be an integer or another expression.
- The division between two integers always **truncates toward zero**.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in reverse polish notation.
- The answer and all intermediate calculations can be represented in a **32-bit** integer.

---

## Examples

### Example 1
```text
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

### Example 2
```text
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

### Example 3
```text
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

---

## Constraints

- $1 \le \text{tokens.length} \le 10^4$
- `tokens[i]` is either an operator: `"+"`, `"-"`, `"*"`, or `"/"`, or an integer in the range $[-200, 200]$.
