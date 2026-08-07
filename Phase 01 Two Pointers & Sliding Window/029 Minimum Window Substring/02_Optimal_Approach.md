# Minimum Window Substring

## Pattern Used

- **Pattern**: **Variable-Size Sliding Window (Expand / Shrink with Required Counter)**
- **Concept**: Maintain a frequency array `target_count` of size 128 for characters of `t`, and a variable `required` tracking how many characters from `t` still need to be satisfied in the active window `[left ... right]`.

---

## Observation

1. Populate `target_count` with character frequencies of `t`. Set `required = t.length()`.
2. As `right` expands:
   - If `target_count[s[right]] > 0`, `s[right]` is a character we needed from `t`; decrement `required--`.
   - Decrement `target_count[s[right]]--`. (Note: counts can become negative, indicating extra redundant characters in our window).
3. Whenever `required == 0`, the current window `[left ... right]` contains ALL characters of `t`!
   - Update `min_len` and record `start_idx = left`.
   - Try to shrink `left` border: increment `target_count[s[left]]++`. If `target_count[s[left]] > 0`, it means we just released a character that was strictly required by `t`, so increment `required++`. Advance `left++`.

---

## Intuition

1. **Expand `right`**: Search forward until all required characters of `t` are present in the window (`required == 0`).
2. **Shrink `left`**: Once valid, squeeze the window from the left as much as possible to eliminate extraneous characters and find the minimum valid window length.
3. Repeat until `right` reaches the end of `s`.

---

## Algorithm

1. `m = s.length()`, `n = t.length()`. If `m < n`, return `""`.
2. Array `target_count[128] = {0}`.
3. For each `c` in `t`: `target_count[c]++`.
4. `left = 0`, `required = n`, `min_len = INF`, `start_idx = 0`.
5. Loop `right` from `0` to `m - 1`:
   a. If `target_count[s[right]] > 0`: `required--`.
   b. `target_count[s[right]]--`.
   c. While `required == 0`:
      - If `right - left + 1 < min_len`:
        - `min_len = right - left + 1`, `start_idx = left`.
      - `target_count[s[left]]++`.
      - If `target_count[s[left]] > 0`: `required++`.
      - `left++`.
6. Return `min_len == INF ? "" : s.substr(start_idx, min_len)`.

---

## Clean C++17 Solution

```cpp
#include <string>
#include <vector>

class Solution {
public:
    std::string minWindow(const std::string& s, const std::string& t) {
        int m = s.length();
        int n = t.length();
        
        if (m < n) return "";
        
        std::vector<int> target_count(128, 0);
        for (char c : t) {
            target_count[c]++;
        }
        
        int left = 0;
        int required = n;
        int min_len = 1e9;
        int start_idx = 0;
        
        for (int right = 0; right < m; ++right) {
            unsigned char right_char = static_cast<unsigned char>(s[right]);
            
            if (target_count[right_char] > 0) {
                required--;
            }
            target_count[right_char]--;
            
            while (required == 0) {
                if (right - left + 1 < min_len) {
                    min_len = right - left + 1;
                    start_idx = left;
                }
                
                unsigned char left_char = static_cast<unsigned char>(s[left]);
                target_count[left_char]++;
                
                if (target_count[left_char] > 0) {
                    required++;
                }
                left++;
            }
        }
        
        return min_len == 1e9 ? "" : s.substr(start_idx, min_len);
    }
};
```

---

## Dry Run

### Input
- `s = "ADOBECODEBANC"`, `t = "ABC"`
- `required = 3` (`A:1, B:1, C:1`)

### Execution Trace

| `right` | `s[right]` | `required` | Window `s[left..right]` | `required == 0`? | Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `0..5` | `'A','D','O','B','E','C'` | `3 -> 0` | `"ADOBEC"` | **Yes** | Valid window! `min_len = 6` (`start=0`). Shrink `l=1` (`"DOBEC"`), `required=1`. |
| `6..9` | `'O','D','E','B'` | `1 -> 0` | `"DOBECODEB"` | **Yes** | Valid! Shrink `left` past `'D','O','B'`. Window: `"CODEB"`, `min_len=5`. |
| `10..12`| `'A','N','C'` | `0` | `"CODEBANC"` | **Yes** | Valid! Shrink `left` past `'C','O','D','E'`. Window: `"BANC"`, `min_len=4`. |

### Result
- Output: `"BANC"`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(M + N)$
  - `target_count` initialization takes $\mathcal{O}(N)$.
  - `right` and `left` pointers advance at most $M$ times in single pass.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Direct access array of size 128 (ASCII characters).

---

## Why This is Optimal

- Solves Hard string matching in linear $\mathcal{O}(M + N)$ time.
- Uses constant $\mathcal{O}(1)$ space.

---

## Common Mistakes

1. **Not Handling Negative Counts Properly**: Failing to realize `target_count[c]` can become negative for characters not in `t` or for extra duplicate characters.
2. **Missing `target_count[c] > 0` Check**: Checking `target_count[c] == 0` instead of `> 0` when incrementing `required`.
