# Longest Repeating Character Replacement

- **Problem Number**: 424
- **Platform**: LeetCode #424
- **Difficulty**: Medium
- **Pattern**: All Substrings Check

---

## Brute Force Intuition

Generate all possible substrings `s[i ... j]`. For each substring, count character frequencies to find the maximum frequency of any single character `max_freq`. 

The number of character replacements needed to make all characters in `s[i ... j]` identical is:
$$\text{replacements\_needed} = \text{length} - \text{max\_freq} = (j - i + 1) - \text{max\_freq}$$

If $\text{replacements\_needed} \le k$, the substring can be made valid by performing at most $k$ replacements. Track the maximum length among all valid substrings.

---

## Algorithm

1. `max_len = 0`.
2. Outer loop `i` from `0` to `n - 1`.
3. Inner loop `j` from `i` to `n - 1`:
   a. Maintain frequency map `count[26]` for substring `s[i ... j]`.
   b. `max_freq = max(count[0...25])`.
   c. If `(j - i + 1) - max_freq <= k`:
      - `max_len = max(max_len, j - i + 1)`.
4. Return `max_len`.

---

## Code

```cpp
#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    int characterReplacement(const std::string& s, int k) {
        int max_len = 0;
        int n = s.length();
        
        for (int i = 0; i < n; ++i) {
            std::vector<int> count(26, 0);
            int max_freq = 0;
            
            for (int j = i; j < n; ++j) {
                count[s[j] - 'A']++;
                max_freq = std::max(max_freq, count[s[j] - 'A']);
                
                if ((j - i + 1) - max_freq <= k) {
                    max_len = std::max(max_len, j - i + 1);
                }
            }
        }
        
        return max_len;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - Outer loop $N$, inner loop up to $N$. For $N = 10^5$, causes TLE.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - 26-element array.

---

## Why This Approach Is Not Optimal

Re-evaluating substring frequencies takes quadratic time. A **Variable-Size Sliding Window (Max Frequency Tracking)** allows updating character frequencies in $\mathcal{O}(1)$ time, reducing execution time to linear $\mathcal{O}(N)$.
