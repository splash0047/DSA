# Longest Palindromic Substring

- **Problem Number**: 5
- **Platform**: LeetCode #5
- **Difficulty**: Medium
- **Pattern**: All Substrings Generation & Palindrome Validation

---

## Brute Force Intuition

Generate all possible substrings of `s` using nested loops `i` and `j` ($0 \le i \le j < N$). For each substring `s[i...j]`, check whether it is a palindrome by verifying if it reads the same forward and backward. Track the substring with maximum length.

---

## Algorithm

1. `maxLen = 0`, `start = 0`.
2. Loop `i` from `0` to `n - 1`:
   - Loop `j` from `i` to `n - 1`:
     - If `isPalindrome(s, i, j)` and `j - i + 1 > maxLen`:
       - `maxLen = j - i + 1`.
       - `start = i`.
3. Return `s.substr(start, maxLen)`.
4. `isPalindrome(s, left, right)`:
   - While `left < right`:
     - If `s[left] != s[right]`, return `false`.
     - `left++`, `right--`.
   - Return `true`.

---

## Code

```cpp
#include <string>

class Solution {
private:
    bool isPalindrome(const std::string& s, int left, int right) {
        while (left < right) {
            if (s[left] != s[right]) return false;
            left++;
            right--;
        }
        return true;
    }

public:
    std::string longestPalindrome(std::string s) {
        int n = s.size();
        if (n <= 1) return s;
        
        int start = 0;
        int maxLen = 0;
        
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) {
                if (isPalindrome(s, i, j) && (j - i + 1) > maxLen) {
                    maxLen = j - i + 1;
                    start = i;
                }
            }
        }
        
        return s.substr(start, maxLen);
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^3)$
  - Generating $\mathcal{O}(N^2)$ substrings and running an $\mathcal{O}(N)$ palindrome check per substring takes cubic $\mathcal{O}(N^3)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses constant auxiliary space.

---

## Why This Approach Is Not Optimal

Testing all substrings takes cubic $\mathcal{O}(N^3)$ time, causing TLE for $N = 1000$. Using **Expand Around Center** (or **2D DP Table**), we can find the longest palindromic substring in quadratic $\mathcal{O}(N^2)$ time and $\mathcal{O}(1)$ space!
