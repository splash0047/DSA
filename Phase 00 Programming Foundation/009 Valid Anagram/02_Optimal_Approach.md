# Valid Anagram

## Pattern Used

- **Pattern**: **Frequency Array / Hash Map Table**
- **Concept**: Maintain a character frequency counter of fixed size 26 for lowercase English letters.

---

## Observation

1. If two strings are anagrams, every character that appears in `s` must appear with the exact same frequency in `t`.
2. As we iterate through string `s`, we increment the count for character `s[i]`. As we iterate through string `t`, we decrement the count for character `t[i]`.
3. If both strings are valid anagrams, every single count in our frequency array will return to `0`.

---

## Intuition

Imagine a tally ledger of 26 letters:
- For every letter in `s`, add +1 to its tally.
- For every letter in `t`, subtract -1 from its tally.
- If all tallies end at 0, the two strings are anagrams.

---

## Algorithm

1. If `s.length() != t.length()`, return `false`.
2. Initialize an integer array `counts[26] = {0}`.
3. Loop `i` from `0` to `n - 1`:
   a. Increment `counts[s[i] - 'a']++`.
   b. Decrement `counts[t[i] - 'a']--`.
4. Loop through `counts`:
   a. If any value is not equal to `0`, return `false`.
5. Return `true`.

---

## Clean C++17 Solution

```cpp
#include <string>
#include <vector>

class Solution {
public:
    bool isAnagram(const std::string& s, const std::string& t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        int counts[26] = {0};
        int n = s.length();
        
        for (int i = 0; i < n; ++i) {
            counts[s[i] - 'a']++;
            counts[t[i] - 'a']--;
        }
        
        for (int count : counts) {
            if (count != 0) {
                return false;
            }
        }
        
        return true;
    }
};
```

---

## Dry Run

### Input
- `s = "anagram"`, `t = "nagaram"`

### Execution Trace

| Char Index | `s[i]` | `t[i]` | Frequency Array Modifications |
| :--- | :--- | :--- | :--- |
| 0 | `'a'` | `'n'` | `counts['a']++` (+1), `counts['n']--` (-1) |
| 1 | `'n'` | `'a'` | `counts['n']++` (0), `counts['a']--` (0) |
| 2 | `'a'` | `'g'` | `counts['a']++` (+1), `counts['g']--` (-1) |
| 3 | `'g'` | `'a'` | `counts['g']++` (0), `counts['a']--` (0) |
| 4 | `'r'` | `'r'` | `counts['r']++` (+1), `counts['r']--` (0) |
| 5 | `'a'` | `'a'` | `counts['a']++` (+1), `counts['a']--` (0) |
| 6 | `'m'` | `'m'` | `counts['m']++` (+1), `counts['m']--` (0) |

- Final Check: All 26 elements in `counts` are `0`.
- Output: `true`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass through strings of length $N$.
  - Final check loops through 26 fixed elements ($\mathcal{O}(1)$).

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses a fixed array of 26 integers regardless of input string length.

---

## Why This is Optimal

- We must inspect every character in `s` and `t` at least once ($\Omega(N)$ time).
- We use constant $\mathcal{O}(1)$ space (26 integers).

---

## Common Mistakes

1. **Forgetting Length Check**: If `s` and `t` have different lengths, checking frequency maps after single loop can cause out-of-bounds access. Always return `false` early if `s.length() != t.length()`.
2. **Hardcoding Alphabet Size for Unicode**: If follow-up asks for Unicode characters, fixed size 26 array fails. Use `std::unordered_map<char, int>` for Unicode support.
