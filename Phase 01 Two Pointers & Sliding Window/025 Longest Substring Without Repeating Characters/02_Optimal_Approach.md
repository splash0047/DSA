# Longest Substring Without Repeating Characters

## Pattern Used

- **Pattern**: **Variable-Size Sliding Window (Last Seen Index Table)**
- **Concept**: Maintain a window `[left ... right]`. Store the **last seen index** of every character in a direct access array `last_seen[256]` initialized to `-1`.

---

## Observation

1. When expanding `right`, if `s[right]` was previously seen at `last_idx` and `last_idx >= left` (i.e. inside the current window), a duplicate has occurred!
2. To restore window validity, we do NOT need to increment `left` step by step. We can directly jump `left = last_idx + 1`!
3. Window length at step `right` is `right - left + 1`.

---

## Intuition

Imagine a sliding window stretching rightward:
- As `right` moves forward, record `last_seen[s[right]] = right`.
- If you encounter a character `s[right]` that was already seen inside your active window (`last_seen[s[right]] >= left`), instantly jump your `left` border to index `last_seen[s[right]] + 1`.
- Update `max_len = max(max_len, right - left + 1)` at each step.

---

## Algorithm

1. Initialize `last_seen[256]` array filled with `-1`.
2. `left = 0`, `max_len = 0`.
3. Loop `right` from `0` to `n - 1`:
   a. `c = s[right]`.
   b. If `last_seen[c] >= left`:
      - `left = last_seen[c] + 1`.
   c. `last_seen[c] = right`.
   d. `max_len = max(max_len, right - left + 1)`.
4. Return `max_len`.

---

## Clean C++17 Solution

```cpp
#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(const std::string& s) {
        std::vector<int> last_seen(256, -1);
        int max_len = 0;
        int left = 0;
        int n = s.length();
        
        for (int right = 0; right < n; ++right) {
            unsigned char c = static_cast<unsigned char>(s[right]);
            
            if (last_seen[c] >= left) {
                left = last_seen[c] + 1;
            }
            
            last_seen[c] = right;
            max_len = std::max(max_len, right - left + 1);
        }
        
        return max_len;
    }
};
```

---

## Dry Run

### Input
- `s = "abcabcbb"`

### Execution Trace

| `right` | `s[right]` | `last_seen[c]` | `left` (Before -> After) | Current Window | `right - left + 1` | `max_len` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | `'a'` | `-1` | `0 -> 0` | `"a"` | `1` | `1` |
| 1 | `'b'` | `-1` | `0 -> 0` | `"ab"` | `2` | `2` |
| 2 | `'c'` | `-1` | `0 -> 0` | `"abc"` | `3` | `3` |
| 3 | `'a'` | `0` | `0 -> 1` (`'a'` duplicate at 0) | `"bca"` | `3` | `3` |
| 4 | `'b'` | `1` | `1 -> 2` (`'b'` duplicate at 1) | `"cab"` | `3` | `3` |
| 5 | `'c'` | `2` | `2 -> 3` (`'c'` duplicate at 2) | `"abc"` | `3` | `3` |
| 6 | `'b'` | `4` | `3 -> 5` (`'b'` duplicate at 4) | `"cb"` | `2` | `3` |
| 7 | `'b'` | `6` | `5 -> 7` (`'b'` duplicate at 6) | `"b"` | `1` | `3` |

### Result
- Output: `3`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass through string of length $N$. Array lookups and updates take $\mathcal{O}(1)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses a fixed array of 256 integers.

---

## Why This is Optimal

- Inspects each character in `s` once ($\Omega(N)$ lower bound).
- `left` pointer jumps in $\mathcal{O}(1)$ instead of shrinking element-by-element.

---

## Common Mistakes

1. **Forgetting `last_seen[c] >= left` Check**: If `last_seen[c]` is smaller than `left`, the duplicate occurred outside the active window! Jumping `left` to `last_seen[c] + 1` would erroneously move `left` backward!
2. **Using `std::unordered_map` Overhead**: While correct, `std::unordered_map` adds unnecessary dynamic allocation. `std::vector<int>(256, -1)` or `int last_seen[256]` executes significantly faster.
