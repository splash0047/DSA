# Permutation in String

- **Problem Number**: 567
- **Platform**: LeetCode #567
- **Difficulty**: Medium
- **Pattern**: Generate Permutations / Substring Search

---

## Brute Force Intuition

Generate all possible permutations of string `s1` (using `std::next_permutation`). For each generated permutation, search if it exists as a substring in `s2` using `s2.find()`.

---

## Algorithm

1. Sort string `s1`.
2. Do:
   - If `s2.find(s1) != std::string::npos`, return `true`.
3. While `std::next_permutation(s1.begin(), s1.end())`.
4. Return `false`.

---

## Code

```cpp
#include <string>
#include <algorithm>

class Solution {
public:
    bool checkInclusion(std::string s1, std::string s2) {
        if (s1.length() > s2.length()) return false;
        
        std::sort(s1.begin(), s1.end());
        
        do {
            if (s2.find(s1) != std::string::npos) {
                return true;
            }
        } while (std::next_permutation(s1.begin(), s1.end()));
        
        return false;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(L_1! \times L_2)$
  - Generating $L_1!$ permutations of `s1` and searching each in `s2` takes factorial time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space.

---

## Why This Approach Is Not Optimal

Generating permutations takes factorial $\mathcal{O}(L_1!)$ time. Since a permutation of `s1` has the exact same character frequency counts and fixed length $L_1$, a **Fixed-Size Sliding Window (Frequency Difference Counter)** solves the problem in linear $\mathcal{O}(L_2)$ time.
