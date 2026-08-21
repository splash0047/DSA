# Isomorphic Strings - Optimal Approach

- **Problem Number**: 205
- **Platform**: LeetCode #205
- **Difficulty**: Easy
- **Pattern**: Last Seen Index Array / Bijection Tracking

---

## Optimal Intuition

Maintain two arrays mapping each character to its most recent 1-indexed position seen so far. If at any index `s[i]` and `t[i]` recorded different last-seen timestamps, they cannot be isomorphic.

---

## Code

```cpp
#include <string>

class Solution {
public:
    bool isIsomorphic(std::string s, std::string t) {
        if (s.size() != t.size()) return false;
        int map_s[256] = {0};
        int map_t[256] = {0};

        for (int i = 0; i < s.size(); i++) {
            unsigned char c1 = s[i];
            unsigned char c2 = t[i];

            if (map_s[c1] != map_t[c2]) return false;

            map_s[c1] = i + 1;
            map_t[c2] = i + 1;
        }
        return true;
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(N)$ single pass.
- **Space Complexity**: $\mathcal{O}(1)$ (fixed 256-element arrays).
