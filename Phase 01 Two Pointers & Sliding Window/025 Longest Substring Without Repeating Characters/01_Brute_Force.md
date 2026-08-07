# Longest Substring Without Repeating Characters

- **Problem Number**: 3
- **Platform**: LeetCode #3
- **Difficulty**: Medium
- **Pattern**: All Substrings Check

---

## Brute Force Intuition

Generate every possible contiguous substring `s[i ... j]`. For each substring, check if all characters are unique using a Hash Set. Track the maximum length among all valid unique substrings.

---

## Algorithm

1. Initialize `max_len = 0`.
2. Outer loop `i` from `0` to `n - 1`.
3. Inner loop `j` from `i` to `n - 1`:
   a. Check if character `s[j]` is already in `seen` set.
   b. If in `seen`: break inner loop.
   c. Insert `s[j]` into `seen`.
   d. `max_len = max(max_len, j - i + 1)`.
4. Return `max_len`.

---

## Code

```cpp
#include <string>
#include <unordered_set>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(const std::string& s) {
        int max_len = 0;
        int n = s.length();
        
        for (int i = 0; i < n; ++i) {
            std::unordered_set<char> seen;
            for (int j = i; j < n; ++j) {
                if (seen.find(s[j]) != seen.end()) {
                    break;
                }
                seen.insert(s[j]);
                max_len = std::max(max_len, j - i + 1);
            }
        }
        
        return max_len;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - Outer loop $N$, inner loop up to $N$. Checking set takes average $\mathcal{O}(1)$.
  - For $N = 5 \times 10^4$, $N^2 = 2.5 \times 10^9$ operations, causing TLE.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(\min(N, M))$
  - Where $M$ is the size of the character set (e.g. 256).

---

## Why This Approach Is Not Optimal

The brute force approach re-evaluates character uniqueness for overlapping substrings. A **Variable-Size Sliding Window (Hash Map Index Tracking)** allows computing the longest valid substring in linear $\mathcal{O}(N)$ time by jumping the left pointer past duplicate characters.
