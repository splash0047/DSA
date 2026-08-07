# Backspace String Compare

## Pattern Used

- **Pattern**: **Two Pointers (Backward Scan with Skip Counters)**
- **Concept**: Scan both strings **backwards** from right to left (`i = s.length() - 1`, `j = t.length() - 1`). Maintain `skip_s` and `skip_t` counters to track pending backspace characters.

---

## Observation

1. Backspace characters (`'#'`) delete characters that appear **before** (to the left of) them.
2. If we scan backwards from right to left:
   - When we see `'#'`, we increment our `skip` count.
   - When we see a regular letter and `skip > 0`, we decrement `skip` and ignore the letter (since it was backspaced).
   - When we see a regular letter and `skip == 0`, we have found the **next valid character** that survives backspacing!
3. Compare the next valid character from `s` with the next valid character from `t`.

---

## Intuition

Scanning backwards eliminates the need to record deleted characters in a stack, because we encounter the backspace symbol *before* the character it deletes. We can jump directly to the surviving characters and compare them in $\mathcal{O}(1)$ space.

---

## Algorithm

1. `i = s.length() - 1`, `j = t.length() - 1`, `skip_s = 0`, `skip_t = 0`.
2. While `i >= 0` or `j >= 0`:
   a. Find next valid character index `i` in `s`:
      - `while (i >= 0)`:
        - If `s[i] == '#'`: `skip_s++`, `i--`.
        - Else if `skip_s > 0`: `skip_s--`, `i--`.
        - Else: `break`.
   b. Find next valid character index `j` in `t`:
      - `while (j >= 0)`:
        - If `t[j] == '#'`: `skip_t++`, `j--`.
        - Else if `skip_t > 0`: `skip_t--`, `j--`.
        - Else: `break`.
   c. If one string has valid characters left while the other is exhausted (`(i >= 0) != (j >= 0)`), return `false`.
   d. If both have valid characters and `s[i] != t[j]`, return `false`.
   e. `i--`, `j--`.
3. Return `true`.

---

## Clean C++17 Solution

```cpp
#include <string>

class Solution {
public:
    bool backspaceCompare(const std::string& s, const std::string& t) {
        int i = s.length() - 1;
        int j = t.length() - 1;
        
        int skip_s = 0;
        int skip_t = 0;
        
        while (i >= 0 || j >= 0) {
            // Find next valid character in s
            while (i >= 0) {
                if (s[i] == '#') {
                    skip_s++;
                    i--;
                } else if (skip_s > 0) {
                    skip_s--;
                    i--;
                } else {
                    break;
                }
            }
            
            // Find next valid character in t
            while (j >= 0) {
                if (t[j] == '#') {
                    skip_t++;
                    j--;
                } else if (skip_t > 0) {
                    skip_t--;
                    j--;
                } else {
                    break;
                }
            }
            
            // If one string ended and other didn't
            if ((i >= 0) != (j >= 0)) {
                return false;
            }
            
            // If characters mismatch
            if (i >= 0 && j >= 0 && s[i] != t[j]) {
                return false;
            }
            
            i--;
            j--;
        }
        
        return true;
    }
};
```

---

## Dry Run

### Input
- `s = "ab#c"`, `t = "ad#c"`

### Execution Trace

| Step | `i` (`s[i]`) | `skip_s` | Valid `s[i]` | `j` (`t[j]`) | `skip_t` | Valid `t[j]` | Comparison | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `3` (`'c'`) | `0` | `'c'` | `3` (`'c'`) | `0` | `'c'` | `'c' == 'c'` (Match) | `i--`, `j--` |
| 2 | `2` (`'#'`) | `1` | - | `2` (`'#'`) | `1` | - | - | Backspace skip |
| 3 | `1` (`'b'`) | `0` (skips `'b'`) | - | `1` (`'d'`) | `0` (skips `'d'`) | - | - | Skip deleted chars |
| 4 | `0` (`'a'`) | `0` | `'a'` | `0` (`'a'`) | `0` | `'a'` | `'a' == 'a'` (Match) | `i--`, `j--` |
| End | `-1` | - | - | `-1` | - | - | `i < 0 && j < 0` | Return `true` |

### Result
- Output: `true`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N + M)$
  - Traverses `s` and `t` backwards once.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses constant extra space (`i`, `j`, `skip_s`, `skip_t`).

---

## Why This is Optimal

- Inspects each character at most once ($\mathcal{O}(N + M)$ time).
- Uses $\mathcal{O}(1)$ space.

---

## Common Mistakes

1. **Not Handling Multiple Backspaces**: Strings like `"a##c"` require `skip` counter to accumulate ($2$).
2. **Missing Out-of-Bounds Checks**: Not checking `i >= 0` inside inner while loops.
3. **Comparing Bounds Incorrectly**: Returning `true` when one string has remaining unskipped characters while the other is exhausted.
