# Find All Anagrams in a String

## Pattern Used

- **Pattern**: **Fixed-Size Sliding Window (Frequency Vector Matching)**
- **Concept**: Maintain two character frequency vectors of size 26 (`p_freq` and `window_freq`). Slide a window of fixed size `p.length()` across `s`.

---

## Observation

1. Two strings are anagrams if and only if their 26-element character frequency vectors match identically.
2. Instead of building frequency vectors from scratch for every window, we can slide the window across `s` by adding 1 character on the right and removing 1 character from the left in $\mathcal{O}(1)$ time.
3. In C++, comparing two `std::vector<int>` objects of size 26 using `==` takes $\mathcal{O}(26) = \mathcal{O}(1)$ constant time!

---

## Intuition

1. Build target frequency vector `p_freq` for `p` and initial window frequency vector `window_freq` for `s[0 ... p_len - 1]`.
2. If `p_freq == window_freq`, index `0` is a valid start index.
3. Slide window from index `p_len` to `s_len - 1`:
   - Increment `window_freq[s[i] - 'a']++` (incoming character).
   - Decrement `window_freq[s[i - p_len] - 'a']--` (outgoing character).
   - If `p_freq == window_freq`, append `i - p_len + 1` to `result`.

---

## Algorithm

1. `s_len = s.length()`, `p_len = p.length()`.
2. If `s_len < p_len`, return `{}`.
3. `std::vector<int> p_freq(26, 0), window_freq(26, 0)`.
4. Loop `i` from `0` to `p_len - 1`:
   - `p_freq[p[i] - 'a']++`
   - `window_freq[s[i] - 'a']++`
5. If `p_freq == window_freq`, `result.push_back(0)`.
6. Loop `i` from `p_len` to `s_len - 1`:
   a. `window_freq[s[i] - 'a']++`
   b. `window_freq[s[i - p_len] - 'a']--`
   c. If `p_freq == window_freq`: `result.push_back(i - p_len + 1)`.
7. Return `result`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <string>

class Solution {
public:
    std::vector<int> findAnagrams(const std::string& s, const std::string& p) {
        std::vector<int> result;
        int s_len = s.length();
        int p_len = p.length();
        
        if (s_len < p_len) return result;
        
        std::vector<int> p_freq(26, 0);
        std::vector<int> window_freq(26, 0);
        
        // Initialize frequency for target string p and initial window of s
        for (int i = 0; i < p_len; ++i) {
            p_freq[p[i] - 'a']++;
            window_freq[s[i] - 'a']++;
        }
        
        if (p_freq == window_freq) {
            result.push_back(0);
        }
        
        // Slide fixed window across s
        for (int i = p_len; i < s_len; ++i) {
            window_freq[s[i] - 'a']++;           // Add incoming character
            window_freq[s[i - p_len] - 'a']--;   // Remove outgoing character
            
            if (p_freq == window_freq) {
                result.push_back(i - p_len + 1);
            }
        }
        
        return result;
    }
};
```

---

## Dry Run

### Input
- `s = "cbaebabacd"`, `p = "abc"`
- `s_len = 10`, `p_len = 3`

### Execution Trace

| Window Index `i` | Incoming | Outgoing | Window Substring | `p_freq == window_freq`? | Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Initial (`0..2`) | - | - | `"cba"` | **Yes** (Matches `"abc"`) | Add index `0` |
| `3` | `'e'` | `'c'` | `"bae"` | No | - |
| `4` | `'b'` | `'b'` | `"aeb"` | No | - |
| `5` | `'a'` | `'a'` | `"eba"` | No | - |
| `6` | `'b'` | `'e'` | `"bab"` | No | - |
| `7` | `'a'` | `'b'` | `"aba"` | No | - |
| `8` | `'c'` | `'a'` | `"bac"` | **Yes** (Matches `"abc"`) | Add index `6` |
| `9` | `'d'` | `'b'` | `"acd"` | No | - |

### Result
- Output: `[0, 6]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(S)$
  - Single pass through `s` of length $S$. Comparing 26-element vectors takes $\mathcal{O}(26) = \mathcal{O}(1)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses two 26-element vectors (constant memory).

---

## Why This is Optimal

- Solves all anagram start positions in a single pass ($\Omega(S)$ lower bound).
- Uses $\mathcal{O}(1)$ auxiliary space.

---

## Common Mistakes

1. **Missing `s.length() < p.length()` Boundary Guard**: Accessing `s[i]` during initial setup when `s` is shorter than `p` causes out-of-bounds access.
2. **Incorrect Start Index Math**: Writing `i - p_len` instead of `i - p_len + 1` when pushing matching start indices.
