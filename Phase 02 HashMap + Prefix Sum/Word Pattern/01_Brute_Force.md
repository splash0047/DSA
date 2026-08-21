# Word Pattern - Brute Force

- **Problem Number**: 290
- **Platform**: LeetCode #290
- **Difficulty**: Easy
- **Pattern**: String Tokenization + Pairwise Consistency Check

---

## Algorithm

1. Split `s` into a list of word tokens.
2. If `pattern.length != words.length`, return `false`.
3. For each pair $(i, j)$:
   - Check if `(pattern[i] == pattern[j]) != (words[i] == words[j])`. If so, return `false`.
4. Return `true`.

---

## Code

```cpp
#include <string>
#include <vector>
#include <sstream>

class Solution {
public:
    bool wordPattern(std::string pattern, std::string s) {
        std::stringstream ss(s);
        std::string word;
        std::vector<std::string> words;
        while (ss >> word) words.push_back(word);

        if (pattern.size() != words.size()) return false;

        for (int i = 0; i < pattern.size(); i++) {
            for (int j = i + 1; j < pattern.size(); j++) {
                if ((pattern[i] == pattern[j]) != (words[i] == words[j])) {
                    return false;
                }
            }
        }
        return true;
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(N^2 \cdot L)$ where $L$ is word length.
- **Space Complexity**: $\mathcal{O}(N \cdot L)$ for words list.
