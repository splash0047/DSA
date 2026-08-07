# Decode Ways

## Pattern Used

- **Pattern**: **1D Dynamic Programming (Space-Optimized Fibonacci-Style DP)**
- **Concept**:
  - `dp[i]` represents number of ways to decode substring `s[0...i-1]`.
  - At index `i` (corresponding to character `s[i-1]`):
    1. **Single Digit Check**: If `s[i-1] != '0'`, `dp[i] += dp[i-1]`.
    2. **Two Digit Check**: If two-digit number formed by `s[i-2...i-1]` is between `10` and `26`, `dp[i] += dp[i-2]`.
  - Notice `dp[i]` depends only on `dp[i-1]` (`prev1`) and `dp[i-2]` (`prev2`).
  - Use 2 state variables `prev1` and `prev2` to optimize auxiliary space to $\mathcal{O}(1)$.

---

## Observation

1. A single digit `'0'` cannot be decoded on its own.
2. Two-digit numbers starting with `'0'` (e.g. `"06"`) are invalid. Only numbers in range $[10, 26]$ are valid two-digit decodings.

---

## Intuition

As you process each character in the string:
- If the current character is valid on its own (`'1'` to `'9'`), it can extend all valid decodings from the previous step.
- If the current character combined with the preceding character forms a valid number between `10` and `26`, it can extend all valid decodings from two steps ago.
- Sum these possibilities up.

---

## Algorithm

1. If `s.empty()` or `s[0] == '0'`, return `0`.
2. `prev2 = 1` (ways for empty string `dp[0]`).
3. `prev1 = 1` (ways for `s[0]`).
4. Loop `i` from `2` to `n`:
   - `curr = 0`.
   - `oneDigit = s[i - 1] - '0'`.
   - `twoDigit = (s[i - 2] - '0') * 10 + (s[i - 1] - '0')`.
   - If `oneDigit != 0`: `curr += prev1`.
   - If `twoDigit >= 10 && twoDigit <= 26`: `curr += prev2`.
   - `prev2 = prev1`.
   - `prev1 = curr`.
5. Return `prev1`.

---

## Clean C++17 Solution

```cpp
#include <string>

class Solution {
public:
    int numDecodings(std::string s) {
        if (s.empty() || s[0] == '0') {
            return 0;
        }
        
        int n = s.size();
        int prev2 = 1; // dp[0]
        int prev1 = 1; // dp[1]
        
        for (int i = 2; i <= n; ++i) {
            int curr = 0;
            int oneDigit = s[i - 1] - '0';
            int twoDigit = (s[i - 2] - '0') * 10 + (s[i - 1] - '0');
            
            // Single-digit decode option ('1'-'9')
            if (oneDigit != 0) {
                curr += prev1;
            }
            
            // Two-digit decode option (10-26)
            if (twoDigit >= 10 && twoDigit <= 26) {
                curr += prev2;
            }
            
            prev2 = prev1;
            prev1 = curr;
        }
        
        return prev1;
    }
};
```

---

## Dry Run

### Input
- `s = "226"`

### Execution Trace

- `s[0] = '2' != '0'`. `prev2 = 1, prev1 = 1`.
- `i = 2` (`s[1] = '2'`):
  - `oneDigit = 2` $\implies$ `curr += prev1 (1)` $\implies$ `curr = 1`.
  - `twoDigit = 22` (valid 10-26) $\implies$ `curr += prev2 (1)` $\implies$ `curr = 2`.
  - `prev2 = 1, prev1 = 2`.
- `i = 3` (`s[2] = '6'`):
  - `oneDigit = 6` $\implies$ `curr += prev1 (2)` $\implies$ `curr = 2`.
  - `twoDigit = 26` (valid 10-26) $\implies$ `curr += prev2 (1)` $\implies$ `curr = 3`.
  - `prev2 = 2, prev1 = 3`.

### Result
- Output: `3` (Decodings: `"BZ"`, `"VF"`, `"BBF"`)

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single loop from `2` to `N`.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses constant extra space (`prev1`, `prev2`, `curr`).

---

## Why This is Optimal

- Solves string decoding count in linear $\mathcal{O}(N)$ time.
- Uses $\mathcal{O}(1)$ space by maintaining only the last 2 DP state variables.

---

## Common Mistakes

1. **Leading Zero Handled Improperly**: Allowing `'0'` to be decoded as single digit or allowing `"06"` as valid two digit.
2. **Missing `s[0] == '0'` Early Guard**: Failing to return `0` immediately when input string starts with `'0'`.
