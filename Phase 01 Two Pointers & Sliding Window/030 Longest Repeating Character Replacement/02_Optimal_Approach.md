# Longest Repeating Character Replacement

## Pattern Used

- **Pattern**: **Variable-Size Sliding Window (Max Frequency Tracking)**
- **Concept**: Maintain a window `[left ... right]` and track the maximum frequency `max_freq` of any single character inside the current window.

---

## Observation

1. Window validity condition:
$$\text{window\_length} - \text{max\_freq} \le k$$
$$\text{where } \text{window\_length} = \text{right} - \text{left} + 1$$
2. If `(right - left + 1) - max_freq > k`, the current window requires strictly more than $k$ replacements to make all characters identical.
3. To restore validity, we shrink the window by advancing `left++` and decrementing `count[s[left] - 'A']--`.
4. *Key Insight*: We do NOT need to decrease `max_freq` when shrinking `left`! A smaller `max_freq` would only decrease max window length, which cannot produce a new maximum result. We only care when `max_freq` increases!

---

## Intuition

Expand `right` pointer step by step:
1. Increment frequency of `s[right]`.
2. Update `max_freq = max(max_freq, count[s[right] - 'A'])`.
3. If window becomes invalid (`window_len - max_freq > k`), shrink `left` by 1 step.
4. Record `max_len = max(max_len, right - left + 1)`.

---

## Algorithm

1. `count[26] = {0}`, `left = 0`, `max_freq = 0`, `max_len = 0`.
2. Loop `right` from `0` to `n - 1`:
   a. `count[s[right] - 'A']++`.
   b. `max_freq = max(max_freq, count[s[right] - 'A'])`.
   c. If `(right - left + 1) - max_freq > k`:
      - `count[s[left] - 'A']--`
      - `left++`
   d. `max_len = max(max_len, right - left + 1)`.
3. Return `max_len`.

---

## Clean C++17 Solution

```cpp
#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    int characterReplacement(const std::string& s, int k) {
        std::vector<int> count(26, 0);
        int left = 0;
        int max_freq = 0;
        int max_len = 0;
        int n = s.length();
        
        for (int right = 0; right < n; ++right) {
            count[s[right] - 'A']++;
            max_freq = std::max(max_freq, count[s[right] - 'A']);
            
            // Shrink window if replacements needed exceed k
            while ((right - left + 1) - max_freq > k) {
                count[s[left] - 'A']--;
                left++;
            }
            
            max_len = std::max(max_len, right - left + 1);
        }
        
        return max_len;
    }
};
```

---

## Dry Run

### Input
- `s = "AABABBA"`, `k = 1`

### Execution Trace

| `right` | `s[right]` | `max_freq` | Window Range | Window Length | Replacements (`len - max_freq`) | Valid? | `max_len` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | `'A'` | 1 ('A') | `"A"` | 1 | 0 | Yes | 1 |
| 1 | `'A'` | 2 ('A') | `"AA"` | 2 | 0 | Yes | 2 |
| 2 | `'B'` | 2 ('A') | `"AAB"` | 3 | 1 | Yes | 3 |
| 3 | `'A'` | 3 ('A') | `"AABA"` | 4 | 1 ($\le 1$) | **Yes** | **4** |
| 4 | `'B'` | 3 ('A') | `"AABAB"` | 5 | 2 ($> 1$) | No $\rightarrow$ Shrink `l=1` | 4 |
| 5 | `'B'` | 3 ('A') | `"ABAB"` | 4 | 2 ($> 1$) | No $\rightarrow$ Shrink `l=2` | 4 |
| 6 | `'A'` | 3 ('A') | `"BABBA"` | 5 | 2 ($> 1$) | No $\rightarrow$ Shrink `l=3` | 4 |

### Result
- Output: `4`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass through $N$ characters. Array updates and comparisons take $\mathcal{O}(1)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses 26-element integer vector.

---

## Why This is Optimal

- Inspects each character in `s` once ($\Omega(N)$ lower bound).
- Operates in $\mathcal{O}(1)$ space.

---

## Common Mistakes

1. **Re-calculating `max_freq` on Shrink**: Thinking `max_freq` must be re-calculated over all 26 elements when `left` advances. (Not necessary, because `max_len` only grows when `max_freq` increases!).
2. **Incorrect Replacement Formula**: Writing `(right - left + 1) - max_freq < k` instead of `> k`.
