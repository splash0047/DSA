# Backspace String Compare

- **Problem Number**: 844
- **Platform**: LeetCode #844
- **Difficulty**: Easy
- **Pattern**: Stack Simulation

---

## Brute Force Intuition

Simulate typing both strings into a text editor using a Stack / String buffer:
- For each character `c`:
  - If `c != '#'`, push `c` onto the stack.
  - If `c == '#'` and stack is not empty, pop the top character off the stack.
- After processing `s` and `t`, compare their processed stack outputs for equality.

---

## Algorithm

1. Define helper function `process(string str)`:
   a. Create string `res = ""`.
   b. Loop `c` in `str`:
      - If `c != '#'`, `res.push_back(c)`.
      - Else if `!res.empty()`, `res.pop_back()`.
   c. Return `res`.
2. Return `process(s) == process(t)`.

---

## Code

```cpp
#include <string>

class Solution {
public:
    bool backspaceCompare(std::string s, std::string t) {

        std::string a = "";
        std::string b = "";

        for (char c : s) {
            if (c != '#') {
                a.push_back(c);
            } 
            else if (!a.empty()) {
                a.pop_back();
            }
        }

        for (char c : t) {
            if (c != '#') {
                b.push_back(c);
            } 
            else if (!b.empty()) {
                b.pop_back();
            }
        }

        return a == b;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N + M)$
  - Where $N = \text{s.length}$ and $M = \text{t.length}$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N + M)$
  - Allocates two auxiliary strings of size up to $N$ and $M$.

---

## Why This Approach Is Not Optimal

This approach allocates $\mathcal{O}(N + M)$ auxiliary memory. The follow-up challenge asks to solve the problem using **$\mathcal{O}(1)$ space**. By using **Two Pointers scanning backwards**, we can process backspaces on the fly in constant memory.
