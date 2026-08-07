# Edit Distance

- **Problem Number**: 72
- **Platform**: LeetCode #72
- **Difficulty**: Medium / Hard
- **Pattern**: Unmemoized Levenshtein Distance Recursion

---

## Brute Force Intuition

Compare `word1[i]` and `word2[j]` from indices $i = 0, j = 0$:
1. If `word1[i] == word2[j]`: Characters match $\implies$ no edit needed $\implies$ `minDistance(i + 1, j + 1)`.
2. If `word1[i] != word2[j]`: Mismatch $\implies$ try all 3 edit operations:
   - **Insert**: `1 + minDistance(i, j + 1)`
   - **Delete**: `1 + minDistance(i + 1, j)`
   - **Replace**: `1 + minDistance(i + 1, j + 1)`
   - Return `min({insert, delete, replace})`.

---

## Algorithm

1. `minDistance(i, j)`:
   - Base Case 1: If `i == word1.length()`, return `word2.length() - j` (must insert remaining characters).
   - Base Case 2: If `j == word2.length()`, return `word1.length() - i` (must delete remaining characters).
   - If `word1[i] == word2[j]`:
     - Return `minDistance(i + 1, j + 1)`.
   - Else:
     - `ins = 1 + minDistance(i, j + 1)`.
     - `del = 1 + minDistance(i + 1, j)`.
     - `rep = 1 + minDistance(i + 1, j + 1)`.
     - Return `min({ins, del, rep})`.

---

## Code

```cpp
#include <string>
#include <algorithm>

class Solution {
private:
    int minDistanceHelper(const std::string& w1, const std::string& w2, int i, int j) {
        if (i == w1.size()) return w2.size() - j;
        if (j == w2.size()) return w1.size() - i;
        
        if (w1[i] == w2[j]) {
            return minDistanceHelper(w1, w2, i + 1, j + 1);
        } else {
            int ins = 1 + minDistanceHelper(w1, w2, i, j + 1);
            int del = 1 + minDistanceHelper(w1, w2, i + 1, j);
            int rep = 1 + minDistanceHelper(w1, w2, i + 1, j + 1);
            return std::min({ins, del, rep});
        }
    }

public:
    int minDistance(std::string word1, std::string word2) {
        return minDistanceHelper(word1, word2, 0, 0);
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(3^{M + N})$
  - Branching factor of 3 at each character mismatch yields exponential decision tree.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(M + N)$
  - Recursion call stack depth.

---

## Why This Approach Is Not Optimal

Evaluating overlapping $(i, j)$ states repeatedly takes exponential $\mathcal{O}(3^{M + N})$ time. Using **Space-Optimized Levenshtein Distance 1D DP (Double Buffering)**, we compute Edit Distance in quadratic $\mathcal{O}(M \times N)$ time and $\mathcal{O}(N)$ space!
