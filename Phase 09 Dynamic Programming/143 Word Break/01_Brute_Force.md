# Word Break

- **Problem Number**: 139
- **Platform**: LeetCode #139
- **Difficulty**: Medium
- **Pattern**: Unmemoized Substring Branching Recursion

---

## Brute Force Intuition

Store `wordDict` in a hash set for $\mathcal{O}(1)$ string lookup. At each starting index `start`, test every possible prefix `s[start...end]`. If `s[start...end]` is in `wordDict`, recursively check if the remaining suffix `s[end+1...N]` can also be segmented into valid dictionary words.

---

## Algorithm

1. `wordSet = unordered_set<string>(wordDict.begin(), wordDict.end())`.
2. `canSegment(s, start, wordSet)`:
   - If `start == s.length()`, return `true`.
   - For `end` from `start + 1` to `s.length()`:
     - `prefix = s.substr(start, end - start)`.
     - If `wordSet.count(prefix)` and `canSegment(s, end, wordSet)`:
       - Return `true`.
   - Return `false`.

---

## Code

```cpp
#include <string>
#include <vector>
#include <unordered_set>

class Solution {
private:
    bool canSegment(const std::string& s, int start, const std::unordered_set<std::string>& wordSet) {
        if (start == s.size()) {
            return true;
        }
        
        for (int end = start + 1; end <= s.size(); ++end) {
            std::string prefix = s.substr(start, end - start);
            if (wordSet.find(prefix) != wordSet.end() && canSegment(s, end, wordSet)) {
                return true;
            }
        }
        
        return false;
    }

public:
    bool wordBreak(std::string s, std::vector<std::string>& wordDict) {
        std::unordered_set<std::string> wordSet(wordDict.begin(), wordDict.end());
        return canSegment(s, 0, wordSet);
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(2^N)$
  - Branching factor of 2 at each index leads to exponential time for strings with overlapping valid prefix choices (e.g. `s = "aaaaaaa"`, `wordDict = ["a", "aa", "aaa"]`).

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Recursion call stack depth equals string length $N$.

---

## Why This Approach Is Not Optimal

Evaluating identical suffix subproblems takes exponential $\mathcal{O}(2^N)$ time. Using **1D Substring Partitioning DP**, we can compute segmentation validity in polynomial $\mathcal{O}(N^2 \cdot L)$ time!
