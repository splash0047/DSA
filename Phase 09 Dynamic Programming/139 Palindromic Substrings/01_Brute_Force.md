# Palindromic Substrings

- **Problem Number**: 647
- **Platform**: LeetCode #647
- **Difficulty**: Medium
- **Pattern**: All Substrings Generation & Validation

---

## Brute Force Intuition

Generate every possible contiguous substring `s[i...j]` using nested loops ($0 \le i \le j < N$). For each substring, check if it is a palindrome using a two-pointer helper function. Increment total count for every valid palindrome found.

---

## Algorithm

1. `count = 0`.
2. Loop `i` from `0` to `n - 1`:
   - Loop `j` from `i` to `n - 1`:
     - If `isPalindrome(s, i, j)`: `count++`.
3. Return `count`.

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
    int countSubstrings(std::string s) {
        int n = s.size();
        int count = 0;
        
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) {
                if (isPalindrome(s, i, j)) {
                    count++;
                }
            }
        }
        
        return count;
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
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

Validating all substrings takes cubic $\mathcal{O}(N^3)$ time. Using **Expand Around Center**, we can count all palindromic substrings in quadratic $\mathcal{O}(N^2)$ time and $\mathcal{O}(1)$ space!
