# Decode String - Brute Force (Recursive Parser)

- **Problem Number**: 394
- **Platform**: LeetCode #394
- **Difficulty**: Medium
- **Pattern**: Recursive Descent Parsing

---

## Algorithm

Parse tokens recursively. When `'['` is encountered, recurse to decode the inner substring; when `']'` is encountered, return the decoded substring.

---

## Code

```cpp
#include <string>

class Solution {
    std::string decode(const std::string& s, int& i) {
        std::string res = "";
        int num = 0;

        while (i < s.size()) {
            char c = s[i];
            if (isdigit(c)) {
                num = num * 10 + (c - '0');
                i++;
            } else if (c == '[') {
                i++; // skip '['
                std::string inner = decode(s, i);
                while (num > 0) {
                    res += inner;
                    num--;
                }
            } else if (c == ']') {
                i++; // skip ']'
                return res;
            } else {
                res += c;
                i++;
            }
        }
        return res;
    }
public:
    std::string decodeString(std::string s) {
        int i = 0;
        return decode(s, i);
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(\text{Output Length})$
- **Space Complexity**: $\mathcal{O}(\text{Max Nesting Depth})$
