# Valid Parentheses

- **Problem Number**: 20
- **Platform**: LeetCode #20
- **Difficulty**: Easy
- **Pattern**: String Replacement / Elimination

---

## Brute Force Intuition

Repeatedly search for adjacent matching bracket pairs `"()"`, `"{}"`, and `"[]"` inside string `s` and remove them using string replace/erase. Repeat until no matching pairs remain. If `s` becomes empty, it is valid; otherwise it is invalid.

---

## Algorithm

1. Loop while `s` contains `"()"`, `"{}"`, or `"[]"`:
   a. Find position of `"()"`, `"{}"`, or `"[]"`.
   b. Erase matching pair from `s`.
2. Return `s.empty()`.

---

## Code

```cpp
#include <string>

class Solution {
public:
    bool isValid(std::string s) {
        if (s.length() % 2 != 0) return false;
        
        while (true) {
            size_t pos1 = s.find("()");
            size_t pos2 = s.find("{}");
            size_t pos3 = s.find("[]");
            
            if (pos1 != std::string::npos) {
                s.erase(pos1, 2);
            } else if (pos2 != std::string::npos) {
                s.erase(pos2, 2);
            } else if (pos3 != std::string::npos) {
                s.erase(pos3, 2);
            } else {
                break;
            }
        }
        
        return s.empty();
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - In each iteration, `find` and `erase` scan and shift string of length $N$, repeated up to $N/2$ times.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$ or $\mathcal{O}(1)$ depending on string copy creation.

---

## Why This Approach Is Not Optimal

Repeated string replacement takes quadratic $\mathcal{O}(N^2)$ time. Using a **LIFO Stack**, we can process and match brackets in a single pass in linear $\mathcal{O}(N)$ time.
