# Longest Common Prefix

- **Problem Number**: 14
- **Platform**: LeetCode #14
- **Difficulty**: Easy
- **Pattern**: Horizontal Scanning

---

## Brute Force Intuition

Initialize the prefix as the first string `prefix = strs[0]`. Iterate through the remaining strings in the array, shrinking `prefix` character by character until `strs[i]` starts with `prefix`.

---

## Algorithm

1. If `strs` is empty, return `""`.
2. Set `prefix = strs[0]`.
3. Loop `i` from `1` to `strs.size() - 1`:
   - While `strs[i].find(prefix) != 0`:
     - Trim `prefix.pop_back()` (or `prefix = prefix.substr(0, prefix.length() - 1)`).
     - If `prefix` becomes empty, return `""`.
4. Return `prefix`.

---

## Code

```cpp
#include <vector>
#include <string>

class Solution {
public:
    std::string longestCommonPrefix(const std::vector<std::string>& strs) {
        if (strs.empty()) return "";
        
        std::string prefix = strs[0];
        
        for (size_t i = 1; i < strs.size(); ++i) {
            while (strs[i].find(prefix) != 0) {
                prefix = prefix.substr(0, prefix.length() - 1);
                if (prefix.empty()) return "";
            }
        }
        
        return prefix;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(S)$
  - Where $S$ is the total number of characters across all strings in `strs`.
  - In the worst case (e.g. `["a", "a", "a", "b"]`), comparing and trimming prefix takes $\mathcal{O}(S)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space.

---

## Why This Approach Is Not Optimal

Horizontal scanning compares entire strings sequentially. If a mismatch occurs at the very first character of the last string, horizontal scanning still processes all previous strings in full. **Vertical Scanning** avoids unnecessary character checks by scanning column-by-column.
