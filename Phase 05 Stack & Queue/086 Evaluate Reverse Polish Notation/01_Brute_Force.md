# Evaluate Reverse Polish Notation

- **Problem Number**: 150
- **Platform**: LeetCode #150
- **Difficulty**: Medium
- **Pattern**: Vector In-Place Reduction

---

## Brute Force Intuition

Iterate through `tokens`. Whenever an operator (`+`, `-`, `*`, `/`) is encountered at index `i`, evaluate `tokens[i-2] (operator) tokens[i-1]`, replace `tokens[i-2]` with the result, and erase `tokens[i-1]` and `tokens[i]`. Repeat until only 1 token remains.

---

## Algorithm

1. Loop while `tokens.size() > 1`:
   a. Find the first index `i` where `tokens[i]` is an operator (`"+"`, `"-"`, `"*"`, `"/"`).
   b. `b = stoi(tokens[i - 1])`, `a = stoi(tokens[i - 2])`.
   c. Evaluate `res = a (op) b`.
   d. `tokens[i - 2] = to_string(res)`.
   e. Erase `tokens[i - 1]` and `tokens[i]`.
2. Return `stoi(tokens[0])`.

---

## Code

```cpp
#include <vector>
#include <string>
#include <stdexcept>

class Solution {
public:
    int evalRPN(std::vector<std::string>& tokens) {
        while (tokens.size() > 1) {
            int i = 0;
            while (i < tokens.size() && tokens[i] != "+" && tokens[i] != "-" && tokens[i] != "*" && tokens[i] != "/") {
                i++;
            }
            
            long long a = std::stoll(tokens[i - 2]);
            long long b = std::stoll(tokens[i - 1]);
            long long res = 0;
            
            if (tokens[i] == "+") res = a + b;
            else if (tokens[i] == "-") res = a - b;
            else if (tokens[i] == "*") res = a * b;
            else if (tokens[i] == "/") res = a / b;
            
            tokens[i - 2] = std::to_string(res);
            tokens.erase(tokens.begin() + i - 1, tokens.begin() + i + 1);
        }
        
        return std::stoi(tokens[0]);
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - Vector element deletion via `erase` shifts remaining elements in $\mathcal{O}(N)$ time, repeated up to $N/2$ times.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$ or $\mathcal{O}(N)$ depending on string conversions.

---

## Why This Approach Is Not Optimal

Repeated vector element deletion takes quadratic $\mathcal{O}(N^2)$ time. Using an **Operand Stack**, we can evaluate Postfix / RPN expressions in a single pass in linear $\mathcal{O}(N)$ time.
