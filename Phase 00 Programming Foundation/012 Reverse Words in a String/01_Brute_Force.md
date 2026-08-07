# Reverse Words in a String

- **Problem Number**: 151
- **Platform**: LeetCode #151
- **Difficulty**: Medium
- **Pattern**: String Tokenization & Reversal

---

## Brute Force Intuition

The most straightforward way to reverse the words in a string is to use C++ string streams (`std::stringstream`) to automatically extract individual words (ignoring spaces), collect them into a `std::vector<std::string>`, reverse the vector of words, and construct the final output string with single space separators.

---

## Algorithm

1. Feed `s` into `std::stringstream ss`.
2. Extract words one by one into a `std::vector<std::string> words`.
3. Reverse `words` using `std::reverse(words.begin(), words.end())`.
4. Join all words in `words` with a single space `" "` between adjacent words.
5. Return the resulting string.

---

## Code

```cpp
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

class Solution {
public:
    std::string reverseWords(std::string s) {
        std::stringstream ss(s);
        std::string word;
        std::vector<std::string> words;
        
        while (ss >> word) {
            words.push_back(word);
        }
        
        std::reverse(words.begin(), words.end());
        
        std::string result = "";
        for (size_t i = 0; i < words.size(); ++i) {
            result += words[i];
            if (i + 1 < words.size()) {
                result += " ";
            }
        }
        
        return result;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Tokenization, vector reversal, and string concatenation each take linear $\mathcal{O}(N)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Stores words in a vector and creates a new result string.

---

## Why This Approach Is Not Optimal

While running in linear time, this approach allocates extra heap memory for a vector of strings. In C++, strings are mutable, allowing us to solve the problem **in-place** in $\mathcal{O}(1)$ auxiliary space using **Two-Pass In-Place Reversal**.
