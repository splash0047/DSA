# Valid Palindrome

## Pattern Used

- **Pattern**: **Two Pointers (Left / Right)**
- **Concept**: Compare characters from both ends using `left` and `right` pointers, skipping non-alphanumeric characters on the fly.

---

## Observation

1. A palindrome reads the same forward and backward.
2. We do not need to create a new string. Instead, we can place a pointer `left = 0` at the beginning and `right = s.length() - 1` at the end.
3. Advance `left` forward until it hits an alphanumeric character; decrement `right` backward until it hits an alphanumeric character.
4. Compare `tolower(s[left])` and `tolower(s[right])`. If they differ, return `false`.

---

## Intuition

Simulate scanning the string simultaneously from both ends towards the center. Ignore spaces, punctuation, and case differences during the scan. If the two pointers meet without finding any mismatch, the string is a valid palindrome.

---

## Algorithm

1. `left = 0`, `right = s.length() - 1`.
2. While `left < right`:
   a. While `left < right` and `!isalnum(s[left])`: `left++`.
   b. While `left < right` and `!isalnum(s[right])`: `right--`.
   c. If `tolower(s[left]) != tolower(s[right])`: return `false`.
   d. `left++`, `right--`.
3. Return `true`.

---

## Clean C++17 Solution

```cpp
#include <string>
#include <cctype>

class Solution {
public:
    bool isPalindrome(const std::string& s) {
        int left = 0;
        int right = s.length() - 1;
        
        while (left < right) {
            while (left < right && !std::isalnum(static_cast<unsigned char>(s[left]))) {
                left++;
            }
            while (left < right && !std::isalnum(static_cast<unsigned char>(s[right]))) {
                right--;
            }
            
            if (std::tolower(static_cast<unsigned char>(s[left])) != 
                std::tolower(static_cast<unsigned char>(s[right]))) {
                return false;
            }
            
            left++;
            right--;
        }
        
        return true;
    }
};
```

---

## Dry Run

### Input
- `s = "A man, a plan, a canal: Panama"`

### Execution Trace

| Step | `left` Pointer (`s[left]`) | `right` Pointer (`s[right]`) | Characters Compared | Match? | Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `0` (`'A'`) | `29` (`'a'`) | `'a'` vs `'a'` | **Yes** | `left++`, `right--` |
| 2 | `1` (`' '` -> skip) $\rightarrow$ `2` (`'m'`) | `28` (`'m'`) | `'m'` vs `'m'` | **Yes** | `left++`, `right--` |
| 3 | `3` (`'a'`) | `27` (`'a'`) | `'a'` vs `'a'` | **Yes** | `left++`, `right--` |
| 4 | `4` (`'n'`) | `26` (`'n'`) | `'n'` vs `'n'` | **Yes** | `left++`, `right--` |
| ... | ... | ... | ... | ... | ... |
| End | `left >= right` | - | - | - | Return `true` |

### Result
- Output: `true`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Each character in `s` is visited at most once by `left` or `right`.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - No auxiliary string memory allocated; operates directly on input `s`.

---

## Why This is Optimal

- Every character must be examined at least once ($\Omega(N)$ time lower bound).
- Uses zero extra memory ($\mathcal{O}(1)$ space).

---

## Common Mistakes

1. **Forgetting `left < right` in Inner Loops**: If string has no alphanumeric characters (e.g. `" , , "`), omitting `left < right` in inner while loops causes out-of-bounds array access.
2. **Missing `static_cast<unsigned char>`**: In C++, passing a negative `char` value to `std::isalnum` or `std::tolower` causes undefined behavior.
