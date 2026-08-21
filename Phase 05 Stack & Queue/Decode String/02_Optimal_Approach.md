# Decode String - Optimal Approach (Dual Stack)

- **Problem Number**: 394
- **Platform**: LeetCode #394
- **Difficulty**: Medium
- **Pattern**: Two Stacks (`countStack` and `stringStack`)

---

## Optimal Intuition

Use two stacks:
1. `countStack`: stores the multiplier $K$ before `'['`.
2. `strStack`: stores the previous string accumulated before `'['`.

When encountering `']'`, pop multiplier $K$ and previous string, duplicate the current substring $K$ times, and append to the previous string.

---

## Code

```cpp
#include <string>
#include <stack>

class Solution {
public:
    std::string decodeString(std::string s) {
        std::stack<int> countStack;
        std::stack<std::string> strStack;
        std::string currStr = "";
        int currNum = 0;

        for (char c : s) {
            if (isdigit(c)) {
                currNum = currNum * 10 + (c - '0');
            } else if (c == '[') {
                countStack.push(currNum);
                strStack.push(currStr);
                currNum = 0;
                currStr = "";
            } else if (c == ']') {
                int k = countStack.top(); countStack.pop();
                std::string prevStr = strStack.top(); strStack.pop();

                std::string repeated = "";
                while (k-- > 0) repeated += currStr;

                currStr = prevStr + repeated;
            } else {
                currStr += c;
            }
        }
        return currStr;
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(\text{Output Length})$
- **Space Complexity**: $\mathcal{O}(\text{Output Length} + \text{Nesting Depth})$
