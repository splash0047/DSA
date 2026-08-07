# Roman to Integer

- **Problem Number**: 13
- **Platform**: LeetCode #13
- **Difficulty**: Easy
- **Pattern**: String Search / Hash Map Lookup

---

## Brute Force Intuition

Search for two-character subtractive pairs (`"IV"`, `"IX"`, `"XL"`, `"XC"`, `"CD"`, `"CM"`) first by scanning the string, adding their special values (4, 9, 40, 90, 400, 900) to the running total, and replacing them with empty spaces. Afterwards, sum up the values of remaining individual single Roman symbols.

---

## Algorithm

1. Check for two-character combinations:
   - If `"IV"` present, add `4`, remove `"IV"`.
   - If `"IX"` present, add `9`, remove `"IX"`.
   - If `"XL"` present, add `40`, remove `"XL"`.
   - If `"XC"` present, add `90`, remove `"XC"`.
   - If `"CD"` present, add `400`, remove `"CD"`.
   - If `"CM"` present, add `900`, remove `"CM"`.
2. Iterate through remaining characters and add single character values (`'I'=1`, `'V'=5`, etc.).
3. Return total sum.

---

## Code

```cpp
#include <string>
#include <unordered_map>

class Solution {
public:
    int romanToInt(std::string s) {
        int total = 0;
        
        std::unordered_map<std::string, int> double_map = {
            {"IV", 4}, {"IX", 9}, {"XL", 40}, {"XC", 90}, {"CD", 400}, {"CM", 900}
        };
        std::unordered_map<char, int> single_map = {
            {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}
        };
        
        for (const auto& [pair, val] : double_map) {
            size_t pos = s.find(pair);
            while (pos != std::string::npos) {
                total += val;
                s.replace(pos, 2, " ");
                pos = s.find(pair);
            }
        }
        
        for (char c : s) {
            if (single_map.count(c)) {
                total += single_map[c];
            }
        }
        
        return total;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Scanning and string replacements take $\mathcal{O}(N)$ time (since string length $N \le 15$).

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Fixed map lookups.

---

## Why This Approach Is Not Optimal

Repeated string searches and replacements are clumsy and unnecessarily modify string memory. A clean single-pass algorithm can process the string in linear time using **Lookahead Comparison**.
