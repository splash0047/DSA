# Valid Anagram

- **Problem Number**: 242
- **Platform**: LeetCode #242
- **Difficulty**: Easy
- **Pattern**: String Sorting

---

## Brute Force Intuition

Two strings are anagrams if and only if they contain the exact same characters with the exact same frequencies. 

If we sort the characters of string `s` and string `t` alphabetically, two anagram strings will produce identical sorted strings.

---

## Algorithm

1. If `s.length() != t.length()`, return `false` immediately.
2. Sort string `s` using `std::sort(s.begin(), s.end())`.
3. Sort string `t` using `std::sort(t.begin(), t.end())`.
4. Return `s == t`.

---

## Code

```cpp
#include <string>
#include <algorithm>

class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        std::sort(s.begin(), s.end());
        std::sort(t.begin(), t.end());
        
        return s == t;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log N)$
  - Sorting two strings of length $N$ takes $\mathcal{O}(N \log N)$ time.
  - Comparing strings takes $\mathcal{O}(N)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$ or $\mathcal{O}(N)$
  - Depending on whether string sorting is done in-place or creates copies.

---

## Why This Approach Is Not Optimal

Sorting takes $\mathcal{O}(N \log N)$ time. Because the problem limits characters to lowercase English letters (or a fixed character set), we can count character frequencies in linear $\mathcal{O}(N)$ time using a **Fixed-Size Frequency Array**.
