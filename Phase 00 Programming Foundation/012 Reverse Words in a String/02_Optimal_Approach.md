# Reverse Words in a String

## Pattern Used

- **Pattern**: **Two-Pass In-Place Reversal**
- **Concept**: 
  1. Reverse the entire string.
  2. Reverse each individual word within the string.
  3. Clean up leading, trailing, and multiple consecutive spaces.

---

## Observation

Consider what happens when we reverse the entire string `"the sky is blue"`:
- Entire Reverse: `"eulb si yks eht"`
- Notice that the words are now in the correct **reverse order** (`"blue"`, `"is"`, `"sky"`, `"the"`), but the characters *inside* each individual word are inverted (`"eulb"` instead of `"blue"`).
- By reversing the characters of each individual word back, we restore their original character order: `"blue is sky the"`.

---

## Intuition

1. **Reverse Entire String**: Moves words to their target positions (reversed order).
2. **Reverse Each Word**: Restores correct spelling for each word.
3. **In-Place Space Cleaning**: Use a read/write two-pointer strategy to remove extra spaces without allocating a new string.

---

## Algorithm

1. Reverse the entire string `s`.
2. Use a write pointer `write_idx = 0` to clean extra spaces and write words in-place:
   a. Iterate through `s` using `i`:
   b. When `s[i] != ' '`:
      - If `write_idx != 0`, write a single space `s[write_idx++] = ' '`.
      - Store `start = write_idx`.
      - Copy word characters: `while (i < n && s[i] != ' ') s[write_idx++] = s[i++]`.
      - Reverse the word in-place: `std::reverse(s.begin() + start, s.begin() + write_idx)`.
3. Resize string `s.resize(write_idx)`.

---

## Clean C++17 Solution

```cpp
#include <string>
#include <algorithm>

class Solution {
public:
    std::string reverseWords(std::string s) {
        // Step 1: Reverse the entire string
        std::reverse(s.begin(), s.end());
        
        int n = s.length();
        int write_idx = 0;
        
        for (int i = 0; i < n; ++i) {
            if (s[i] != ' ') {
                // Insert a single space between words
                if (write_idx != 0) {
                    s[write_idx++] = ' ';
                }
                
                int start = write_idx;
                
                // Copy word characters
                while (i < n && s[i] != ' ') {
                    s[write_idx++] = s[i++];
                }
                
                // Step 2: Reverse each word back to original character order
                std::reverse(s.begin() + start, s.begin() + write_idx);
            }
        }
        
        // Step 3: Truncate trailing garbage/spaces
        s.resize(write_idx);
        return s;
    }
};
```

---

## Dry Run

### Input
- `s = "  hello world  "`

### Execution Trace

| Step | Operation | String State |
| :--- | :--- | :--- |
| Start | Initial String | `"  hello world  "` |
| 1 | Reverse All | `"  dlrow olleh  "` |
| 2 | Process Word 1 (`"dlrow"`) | Add space? No (`write_idx == 0`). Copy `"dlrow"`, reverse $\rightarrow$ `"world"`. `write_idx = 5`. |
| 3 | Process Word 2 (`"olleh"`) | Add space? Yes (`s[5] = ' '`). Copy `"olleh"`, reverse $\rightarrow$ `"hello"`. `write_idx = 11`. |
| 4 | `s.resize(11)` | `"world hello"` |

### Result
- Output: `"world hello"`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Reversing entire string takes $\mathcal{O}(N)$.
  - Word copying and individual reversals visit each character a constant number of times.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Operates strictly in-place on the input string `s` using constant auxiliary space.

---

## Why This is Optimal

- Every character must be inspected to strip extra spaces and reverse word order ($\Omega(N)$ time).
- Achieves $\mathcal{O}(1)$ extra memory.

---

## Common Mistakes

1. **Failing to Remove Multiple Consecutive Spaces**: Not advancing `i` past extra spaces properly.
2. **Leaving Leading or Trailing Spaces**: Incorrect boundary checks when inserting space separators.
