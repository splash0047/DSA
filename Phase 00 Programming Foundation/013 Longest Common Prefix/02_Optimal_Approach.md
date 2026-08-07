# Longest Common Prefix

## Pattern Used

- **Pattern**: **Vertical Scanning**
- **Concept**: Compare characters column-by-column across all strings simultaneously. Stop immediately at the first column where a character mismatch occurs or a string ends.

---

## Observation

1. The longest common prefix cannot be longer than the shortest string in the array.
2. By comparing character by character at column index `i` across all strings, we can terminate as soon as any string ends or any character does not match `strs[0][i]`.

---

## Intuition

Look at the input array as a 2D matrix of characters:
- Check Column 0 across all rows: if all match, append column 0 char.
- Check Column 1 across all rows: if all match, append column 1 char.
- The moment you find a row where the string is too short or column $i$ character differs from `strs[0][i]`, return `strs[0].substr(0, i)`.

---

## Algorithm

1. If `strs` is empty, return `""`.
2. Iterate `i` from `0` to `strs[0].length() - 1`:
   a. Get character `c = strs[0][i]`.
   b. Loop `j` from `1` to `strs.size() - 1`:
      - If `i >= strs[j].length()` or `strs[j][i] != c`:
        - Return `strs[0].substr(0, i)`.
3. Return `strs[0]`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <string>

class Solution {
public:
    std::string longestCommonPrefix(const std::vector<std::string>& strs) {
        if (strs.empty()) return "";
        
        for (size_t i = 0; i < strs[0].size(); ++i) {
            char c = strs[0][i];
            
            for (size_t j = 1; j < strs.size(); ++j) {
                if (i >= strs[j].size() || strs[j][i] != c) {
                    return strs[0].substr(0, i);
                }
            }
        }
        
        return strs[0];
    }
};
```

---

## Dry Run

### Input
- `strs = ["flower", "flow", "flight"]`

### Execution Trace

| Column Index `i` | Char `c` (`strs[0][i]`) | String 1 (`"flow"`) | String 2 (`"flight"`) | Match? | Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `0` | `'f'` | `'f'` | `'f'` | **Yes** | Continue |
| `1` | `'l'` | `'l'` | `'l'` | **Yes** | Continue |
| `2` | `'o'` | `'o'` | `'i'` | **No** (`'o' != 'i'`) | Return `strs[0].substr(0, 2)` $\rightarrow$ `"fl"` |

### Result
- Output: `"fl"`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(S)$
  - Where $S$ is the sum of characters across all strings.
  - In the worst case (where all strings are identical), inspects $S$ characters.
  - In the best case (early mismatch at index 0), inspects only $N$ characters.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses constant extra space.

---

## Why This is Optimal

- We stop at the earliest possible character mismatch without scanning redundant suffix characters.
- Operates in $\mathcal{O}(1)$ extra space.

---

## Common Mistakes

1. **Out-of-Bounds Error**: Forgetting the check `i >= strs[j].size()`, causing segmentation fault when `strs[j]` is shorter than `strs[0]`.
2. **Empty Input**: Accessing `strs[0]` without checking `if (strs.empty())`.
