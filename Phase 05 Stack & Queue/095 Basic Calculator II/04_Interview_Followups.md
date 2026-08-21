# 04 Interview Follow-ups & System Variations: Basic Calculator II

The problem evaluates an arithmetic expression containing non-negative integers, `+`, `-`, `*`, `/` and spaces without parentheses. While a Stack achieves $\mathcal{O}(N)$ space, the optimal approach uses **Two Running Scalars** (`last_num` and `running_sum`) in $\mathcal{O}(N)$ time and strictly $\mathcal{O}(1)$ space.

In technical interviews, this problem is extended to nested parentheses and full Recursive Descent Parsers (Basic Calculator III).

---

## 1. Low-Memory Optimization: Eliminating the Stack ($\mathcal{O}(1)$ Space)

### 💡 Running Precedence Accumulator
```cpp
int calculate(string s) {
    long long running_sum = 0, last_num = 0, current_num = 0;
    char op = '+';
    
    for (int i = 0; i < s.size(); i++) {
        if (isdigit(s[i])) {
            current_num = current_num * 10 + (s[i] - '0');
        }
        if ((!isdigit(s[i]) && s[i] != ' ') || i == s.size() - 1) {
            if (op == '+') {
                running_sum += last_num;
                last_num = current_num;
            } else if (op == '-') {
                running_sum += last_num;
                last_num = -current_num;
            } else if (op == '*') {
                last_num = last_num * current_num;
            } else if (op == '/') {
                last_num = last_num / current_num;
            }
            op = s[i];
            current_num = 0;
        }
    }
    return running_sum + last_num;
}
```

---

## 2. Generalization: Basic Calculator III (With Parentheses `()`)

### 💡 Recursive Descent Parser
- Whenever encountering `'('`, recursively call `calculate(s)` starting from the inner expression.
- Return the sub-result when encountering `')'`.
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(D)$ recursion depth.

---

## Summary Matrix: Trade-offs at a Glance

| Calculator Level | Features | Optimal Approach | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Basic Calculator II (#227)** | `+`, `-`, `*`, `/` | 2 Running Scalars (`last_num`) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Basic Calculator I (#224)** | `+`, `-`, `()` | Sign Stack | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **Basic Calculator III (#772)**| `+`, `-`, `*`, `/`, `()`| Recursive Descent Parser | $\mathcal{O}(N)$ | $\mathcal{O}(D)$ |
