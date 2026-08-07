# Palindromic Substrings

## Pattern Used

- **Pattern**: **Expand Around Center (Two-Pointer Mirror Traversal)**
- **Concept**:
  - A string of length $N$ has $2N - 1$ possible centers:
    - $N$ single character centers `(i, i)`.
    - $N - 1$ adjacent character pair centers `(i, i + 1)`.
  - For each center `(left, right)`:
    - Expand outward as long as `left >= 0 && right < n && s[left] == s[right]`.
    - Every successful step where `s[left] == s[right]` represents 1 valid palindromic substring! Increment `total_count++`.

---

## Observation

1. Whenever `s[left] == s[right]` matches during an outward expansion, `s[left...right]` is guaranteed to be a valid palindromic substring.
2. Expanding from $2N - 1$ centers counts every single palindromic substring in $\mathcal{O}(N^2)$ total time.

---

## Intuition

Treat every character and every boundary between characters as a potential mirror center. Expand two pointers left and right. Each time the two pointers see matching characters, you've found another valid palindromic substring!

---

## Algorithm

1. `count = 0`.
2. `expand(s, left, right)` helper:
   - `c = 0`.
   - While `left >= 0 && right < n && s[left] == s[right]`:
     - `c++`.
     - `left--`, `right++`.
   - Return `c`.
3. Loop `i` from `0` to `n - 1`:
   - `count += expand(s, i, i)` (Odd length palindromes).
   - `count += expand(s, i, i + 1)` (Even length palindromes).
4. Return `count`.

---

## Clean C++17 Solution

```cpp
#include <string>

class Solution {
private:
    int expandAroundCenter(const std::string& s, int left, int right) {
        int count = 0;
        int n = s.size();
        
        while (left >= 0 && right < n && s[left] == s[right]) {
            count++;   // Valid palindrome substring found
            left--;
            right++;
        }
        
        return count;
    }

public:
    int countSubstrings(std::string s) {
        int n = s.size();
        int totalPalindromes = 0;
        
        for (int i = 0; i < n; ++i) {
            totalPalindromes += expandAroundCenter(s, i, i);     // Odd-length centers
            totalPalindromes += expandAroundCenter(s, i, i + 1); // Even-length centers
        }
        
        return totalPalindromes;
    }
};
```

---

## Dry Run

### Input
- `s = "aaa"`

### Execution Trace

- `i = 0`:
  - `expand(0, 0)`: `"a"` $\implies$ `count = 1`.
  - `expand(0, 1)`: `"aa"` $\implies$ `count = 1`.
- `i = 1`:
  - `expand(1, 1)`: `"a"`, `"aaa"` $\implies$ `count = 2`.
  - `expand(1, 2)`: `"aa"` $\implies$ `count = 1`.
- `i = 2`:
  - `expand(2, 2)`: `"a"` $\implies$ `count = 1`.
  - `expand(2, 3)`: mismatch $\implies$ `count = 0`.

- Total = `1 + 1 + 2 + 1 + 1 = 6`.

### Result
- Output: `6`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - There are $2N - 1$ centers, each expanding at most $N/2$ steps. Total time $= \mathcal{O}(N^2)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses constant extra space.

---

## Why This is Optimal

- Counts all palindromic substrings in quadratic $\mathcal{O}(N^2)$ time.
- Operates in $\mathcal{O}(1)$ space without creating auxiliary 2D DP tables.

---

## Common Mistakes

1. **Forgetting Even-Length Centers**: Omitting `expand(i, i + 1)` misses even-length palindromes like `"aa"`.
2. **Counting Length Instead of Number of Matches**: Returning length instead of number of valid matching expansions.
