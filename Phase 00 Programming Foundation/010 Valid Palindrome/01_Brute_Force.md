# Valid Palindrome

- **Problem Number**: 125
- **Platform**: LeetCode #125
- **Difficulty**: Easy
- **Pattern**: Filtered Copy and String Reverse

---

## Brute Force Intuition

The most straightforward way to check if a phrase is a valid palindrome is to filter out all non-alphanumeric characters, convert all remaining characters to lowercase into a new string `filtered`, create a reversed copy `rev`, and check if `filtered == rev`.

---

## Algorithm

1. Iterate through characters `c` in `s`:
   - If `std::isalnum(c)`, append `std::tolower(c)` to `filtered`.
2. Create `rev = filtered`.
3. Reverse `rev` using `std::reverse(rev.begin(), rev.end())`.
4. Return `filtered == rev`.

---

## Code

```cpp
#include <string>
#include <algorithm>
#include <cctype>

class Solution {
public:
    bool isPalindrome(const std::string& s) {
        std::string filtered = "";
        for (char c : s) {
            if (std::isalnum(static_cast<unsigned char>(c))) {
                filtered += std::tolower(static_cast<unsigned char>(c));
            }
        }
        
        std::string rev = filtered;
        std::reverse(rev.begin(), rev.end());
        
        return filtered == rev;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass to filter string, $\mathcal{O}(N)$ to reverse, $\mathcal{O}(N)$ to compare.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Allocates two auxiliary strings (`filtered` and `rev`) of size up to $N$.

---

## Why This Approach Is Not Optimal

While running in linear time, allocating two new strings uses $\mathcal{O}(N)$ auxiliary memory. Using **Two Pointers (Left / Right)** allows us to perform the check in-place with $\mathcal{O}(1)$ space.
