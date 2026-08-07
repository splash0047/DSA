# Find All Anagrams in a String

- **Problem Number**: 438
- **Platform**: LeetCode #438
- **Difficulty**: Medium
- **Pattern**: Sort Substrings

---

## Brute Force Intuition

For every starting index `i` in `s` (from `0` to `s.length() - p.length()`), extract the substring of length `p.length()`, sort it, and compare it with the sorted version of `p`.

---

## Algorithm

1. If `s.length() < p.length()`, return `{}`.
2. Create sorted string `sorted_p = p`, `std::sort(sorted_p.begin(), sorted_p.end())`.
3. Loop `i` from `0` to `s.length() - p.length()`:
   a. Extract `sub = s.substr(i, p.length())`.
   b. `std::sort(sub.begin(), sub.end())`.
   c. If `sub == sorted_p`: add `i` to `result`.
4. Return `result`.

---

## Code

```cpp
#include <vector>
#include <string>
#include <algorithm>

class Solution {
public:
    std::vector<int> findAnagrams(std::string s, std::string p) {
        std::vector<int> result;
        int s_len = s.length(), p_len = p.length();
        if (s_len < p_len) return result;
        
        std::string sorted_p = p;
        std::sort(sorted_p.begin(), sorted_p.end());
        
        for (int i = 0; i <= s_len - p_len; ++i) {
            std::string sub = s.substr(i, p_len);
            std::sort(sub.begin(), sub.end());
            if (sub == sorted_p) {
                result.push_back(i);
            }
        }
        
        return result;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}((S - P + 1) \times P \log P)$
  - Extracting and sorting $S - P + 1$ substrings of length $P$ takes $\mathcal{O}(S \cdot P \log P)$ time, causing TLE.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(P)$
  - Storage for extracted substrings.

---

## Why This Approach Is Not Optimal

Sorting substrings repeatedly takes $\mathcal{O}(S \cdot P \log P)$ time. A **Fixed-Size Sliding Window (Frequency Vector)** updates character frequency counts in $\mathcal{O}(1)$ time per step, solving the problem in linear $\mathcal{O}(S)$ time.
