# Isomorphic Strings - Brute Force

- **Problem Number**: 205
- **Platform**: LeetCode #205
- **Difficulty**: Easy
- **Pattern**: String Reconstruction / Linear Search

---

## Algorithm

1. For each character `s[i]`, find its first occurrence index in `s`.
2. Find the first occurrence index of `t[i]` in `t`.
3. If their first occurrence indices differ at any position $i$, the character mapping pattern is inconsistent $\implies$ return `false`.
4. Return `true`.

---

## Code

```cpp
#include <string>

class Solution {
public:
    bool isIsomorphic(std::string s, std::string t) {
        if (s.size() != t.size()) return false;
        for (int i = 0; i < s.size(); i++) {
            if (s.find(s[i]) != t.find(t[i])) {
                return false;
            }
        }
        return true;
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$ due to `std::string::find` linear scanning.
- **Space Complexity**: $\mathcal{O}(1)$.
