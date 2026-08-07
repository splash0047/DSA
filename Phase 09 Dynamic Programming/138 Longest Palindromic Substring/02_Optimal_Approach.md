# Longest Palindromic Substring

## Pattern Used

- **Pattern**: **Expand Around Center** (or **Interval DP / Manacher's Algorithm**)
- **Concept**:
  - A palindrome mirrors symmetrically around its center.
  - There are $2N - 1$ possible centers in a string of length $N$:
    - $N$ odd-length centers (centered on a single character `s[i]`).
    - $N - 1$ even-length centers (centered between `s[i]` and `s[i+1]`).
  - For each center, expand outward (`left--`, `right++`) as long as `s[left] == s[right]`.
  - Update `start` and `maxLen` whenever a longer palindrome is found.

---

## Observation

1. Instead of picking a start and end boundary and checking inward ($\mathcal{O}(N^3)$), pick a center point and expand outward ($\mathcal{O}(N^2)$)!
2. As soon as `s[left] != s[right]`, expansion stops immediately, avoiding unnecessary character comparisons.

---

## Intuition

Think of every character (and every space between two characters) as a potential mirror center. Expand two pointers left and right from that center as far as the characters on both sides match. Record the longest valid mirror expansion found.

---

## Algorithm

1. If `s.length() <= 1`, return `s`.
2. `start = 0`, `maxLen = 0`.
3. `expand(left, right)` helper:
   - While `left >= 0 && right < n && s[left] == s[right]`:
     - `left--`, `right++`.
   - Length of expanded palindrome $= \text{right} - \text{left} - 1$.
   - If length $> \text{maxLen}$:
     - `maxLen = length`.
     - `start = left + 1`.
4. Loop `i` from `0` to `n - 1`:
   - `expand(i, i)` (Odd length expansion).
   - `expand(i, i + 1)` (Even length expansion).
5. Return `s.substr(start, maxLen)`.

---

## Clean C++17 Solution

```cpp
#include <string>
#include <algorithm>

class Solution {
private:
    int start = 0;
    int maxLen = 0;
    
    void expandAroundCenter(const std::string& s, int left, int right) {
        int n = s.size();
        while (left >= 0 && right < n && s[left] == s[right]) {
            left--;
            right++;
        }
        
        // After loop breaks, valid palindrome range is [left + 1, right - 1]
        int currentLen = right - left - 1;
        if (currentLen > maxLen) {
            maxLen = currentLen;
            start = left + 1;
        }
    }

public:
    std::string longestPalindrome(std::string s) {
        int n = s.size();
        if (n <= 1) return s;
        
        start = 0;
        maxLen = 0;
        
        for (int i = 0; i < n; ++i) {
            expandAroundCenter(s, i, i);     // Odd-length palindromes (single character center)
            expandAroundCenter(s, i, i + 1); // Even-length palindromes (two character center)
        }
        
        return s.substr(start, maxLen);
    }
};
```

---

## Dry Run

### Input
- `s = "babad"`

### Execution Trace

- `i = 0 ('b')`:
  - `expand(0, 0)`: `"b"`, len 1. `start = 0, maxLen = 1`.
  - `expand(0, 1)`: `"ba"` mismatch.
- `i = 1 ('a')`:
  - `expand(1, 1)`: `"aba"`, len 3. `start = 0, maxLen = 3`.
  - `expand(1, 2)`: `"ab"` mismatch.
- `i = 2 ('b')`:
  - `expand(2, 2)`: `"bab"`, len 3 (not > 3).
  - `expand(2, 3)`: `"ba"` mismatch.
- `i = 3 ('a')`:
  - `expand(3, 3)`: `"ada"` mismatch.

### Result
- Output: `s.substr(0, 3)` = `"bab"` (or `"aba"`)

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - There are $2N - 1$ centers. Expanding from each center takes $\mathcal{O}(N)$ in the worst case. Overall time $= \mathcal{O}(N^2)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space.

---

## Why This is Optimal

- Reduces time complexity from cubic $\mathcal{O}(N^3)$ to quadratic $\mathcal{O}(N^2)$ while using $\mathcal{O}(1)$ auxiliary space (beating 2D DP table's $\mathcal{O}(N^2)$ space).

---

## Common Mistakes

1. **Forgetting Even Length Palindromes**: Only checking `expand(i, i)` and missing `expand(i, i + 1)` (fails on `"cbbd"`).
2. **Incorrect Substring Start Index**: Forgetting that after the while loop breaks, `left` has decremented by 1, so valid start index is `left + 1`.
