# Reorganize String

- **Problem Number**: 767
- **Platform**: LeetCode #767
- **Difficulty**: Medium
- **Pattern**: Backtracking / Permutations Search

---

## Brute Force Intuition

Generate all possible permutations of string `s` using backtracking. For each permutation, check if any two adjacent characters are identical. Return the first permutation that satisfies the condition. If no valid permutation is found after checking all $N!$ possibilities, return `""`.

---

## Algorithm

1. Sort `s` to generate lexicographical permutations.
2. For each permutation of `s`:
   - Check if `s[i] != s[i+1]` for all $0 \le i < N - 1$.
   - If valid, return `s`.
3. If loop finishes without returning, return `""`.

---

## Code

```cpp
#include <string>
#include <algorithm>

class Solution {
private:
    bool isValid(const std::string& s) {
        for (int i = 0; i < (int)s.size() - 1; ++i) {
            if (s[i] == s[i + 1]) return false;
        }
        return true;
    }

public:
    std::string reorganizeString(std::string s) {
        std::sort(s.begin(), s.end());
        do {
            if (isValid(s)) {
                return s;
            }
        } while (std::next_permutation(s.begin(), s.end()));
        
        return "";
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N! \times N)$
  - Generating $N!$ permutations for a string of length $N$ takes factorial time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space.

---

## Why This Approach Is Not Optimal

Generating permutations takes factorial $\mathcal{O}(N!)$ time, which TLEs even for $N = 12$. Using **Max-Heap Greedy Character Placement**, we can reorganize the string in $\mathcal{O}(N \log \Sigma)$ time (where $\Sigma = 26$ is the alphabet size).
