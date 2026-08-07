# Minimum Window Substring

- **Problem Number**: 76
- **Platform**: LeetCode #76
- **Difficulty**: Hard
- **Pattern**: All Substrings Evaluation / Hash Map Check

---

## Brute Force Intuition

Generate every possible contiguous substring `s[i ... j]` of string `s`. For each substring, check if it contains all characters of string `t` with their required frequencies using a frequency map. Track the shortest valid substring found.

---

## Algorithm

1. Build frequency map `t_map` for string `t`.
2. `min_len = INF`, `start_idx = -1`.
3. Outer loop `i` from `0` to `m - 1`.
4. Inner loop `j` from `i` to `m - 1`:
   a. Maintain frequency map `s_map` for substring `s[i ... j]`.
   b. If `s_map` contains all characters of `t_map` with required frequencies:
      - If `j - i + 1 < min_len`:
        - `min_len = j - i + 1`, `start_idx = i`.
      - Break inner loop.
5. Return `start_idx == -1 ? "" : s.substr(start_idx, min_len)`.

---

## Code

```cpp
#include <string>
#include <unordered_map>

class Solution {
private:
    bool isValid(const std::unordered_map<char, int>& s_map, 
                 const std::unordered_map<char, int>& t_map) {
        for (const auto& [ch, count] : t_map) {
            if (s_map.find(ch) == s_map.end() || s_map.at(ch) < count) {
                return false;
            }
        }
        return true;
    }
public:
    std::string minWindow(const std::string& s, const std::string& t) {
        int m = s.length(), n = t.length();
        if (m < n) return "";
        
        std::unordered_map<char, int> t_map;
        for (char c : t) t_map[c]++;
        
        int min_len = 1e9;
        int start_idx = -1;
        
        for (int i = 0; i < m; ++i) {
            std::unordered_map<char, int> s_map;
            for (int j = i; j < m; ++j) {
                s_map[s[j]]++;
                if (isValid(s_map, t_map)) {
                    if (j - i + 1 < min_len) {
                        min_len = j - i + 1;
                        start_idx = i;
                    }
                    break;
                }
            }
        }
        
        return start_idx == -1 ? "" : s.substr(start_idx, min_len);
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(M^2 \times |T|)$
  - Generating all substrings takes $\mathcal{O}(M^2)$ time; checking validity takes $\mathcal{O}(|T|)$ time per substring.
  - For $M = 10^5$, this causes severe TLE.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(M + N)$
  - Memory for frequency maps.

---

## Why This Approach Is Not Optimal

Re-evaluating substring frequencies from scratch takes polynomial time. Using a **Variable-Size Sliding Window (Expand / Shrink with Required Counter)**, we can expand `right` to cover target characters and shrink `left` to minimize window length in linear $\mathcal{O}(M + N)$ time.
