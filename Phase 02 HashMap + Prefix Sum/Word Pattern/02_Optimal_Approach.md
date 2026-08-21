# Word Pattern - Optimal Approach

- **Problem Number**: 290
- **Platform**: LeetCode #290
- **Difficulty**: Easy
- **Pattern**: Two-Way Hash Map / Last Seen Index Tracking

---

## Optimal Intuition

Map `char -> index` and `word -> index`. When examining the $i$-th element, check that `char_to_idx[pattern[i]] == word_to_idx[word]`. Update both to $i + 1$.

---

## Code

```cpp
#include <string>
#include <vector>
#include <sstream>
#include <unordered_map>

class Solution {
public:
    bool wordPattern(std::string pattern, std::string s) {
        std::stringstream ss(s);
        std::string word;
        std::vector<std::string> words;
        while (ss >> word) words.push_back(word);

        if (pattern.size() != words.size()) return false;

        std::unordered_map<char, int> char_map;
        std::unordered_map<std::string, int> word_map;

        for (int i = 0; i < pattern.size(); i++) {
            char c = pattern[i];
            const std::string& w = words[i];

            if (char_map[c] != word_map[w]) return false;

            char_map[c] = i + 1;
            word_map[w] = i + 1;
        }
        return true;
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(N \cdot L)$
- **Space Complexity**: $\mathcal{O}(N \cdot L)$
