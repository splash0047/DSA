# Decode Ways

- **Problem Number**: 91
- **Platform**: LeetCode #91
- **Difficulty**: Medium
- **Pattern**: Unmemoized Backtracking Branching

---

## Brute Force Intuition

At each index `i` of string `s`, we can decode either:
1. **Single Digit**: Take `s[i]`. If `s[i] != '0'`, valid digit $\implies$ recurse to `i + 1`.
2. **Two Digits**: Take `s[i...i+1]`. If `10 <= stoi(s[i...i+1]) <= 26`, valid letter $\implies$ recurse to `i + 2`.

Sum the number of valid decoding paths from both branches.

---

## Algorithm

1. `decode(s, i)`:
   - Base Case: If `i == s.length()`, return `1` (valid complete decoding).
   - If `s[i] == '0'`, return `0` (leading zeros invalid).
   - `ways = decode(s, i + 1)`.
   - If `i + 1 < s.length()` and `stoi(s[i...i+1]) <= 26`:
     - `ways += decode(s, i + 2)`.
   - Return `ways`.

---

## Code

```cpp
#include <string>

class Solution {
private:
    int decodeHelper(const std::string& s, int i) {
        int n = s.size();
        if (i == n) return 1;
        if (s[i] == '0') return 0; // Leading zero invalid
        
        // Single digit decode
        int ways = decodeHelper(s, i + 1);
        
        // Two digit decode check
        if (i + 1 < n) {
            int twoDigit = (s[i] - '0') * 10 + (s[i + 1] - '0');
            if (twoDigit >= 10 && twoDigit <= 26) {
                ways += decodeHelper(s, i + 2);
            }
        }
        
        return ways;
    }

public:
    int numDecodings(std::string s) {
        if (s.empty()) return 0;
        return decodeHelper(s, 0);
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(2^N)$
  - Branching factor of 2 at each index creates an exponential recursion tree.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Recursion call stack depth equals $N$.

---

## Why This Approach Is Not Optimal

Evaluating identical suffix subproblems repeatedly takes exponential $\mathcal{O}(2^N)$ time. Using **Space-Optimized 1D Dynamic Programming**, we compute total decode ways in linear $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space!
