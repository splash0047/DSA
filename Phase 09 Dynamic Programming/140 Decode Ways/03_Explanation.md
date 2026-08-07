# Problem Summary

Determine the number of ways to decode a digit string `s` into letters `A-Z` ('1' -> A, ..., '26' -> Z). The optimal approach uses **Space-Optimized 1D Dynamic Programming**:
- Check early zero: `if (s[0] == '0') return 0;`
- Maintain `prev2 = 1` and `prev1 = 1`.
- For `i` from `2` to `n`:
  - `oneDigit = s[i-1] - '0'`, `twoDigit = stoi(s[i-2...i-1])`.
  - If `oneDigit != 0`: `curr += prev1`.
  - If `10 <= twoDigit <= 26`: `curr += prev2`.
  - `prev2 = prev1; prev1 = curr;`
- Return `prev1`.
This counts total decode ways in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to count **ways to partition / decode a sequence under character validity rules**.
- 1D Substring Partitioning DP pattern.

---

## Important Clues

1. **"Number of ways to decode message"**: Partition counting DP.
2. **"Single digit ('1'-'9') or double digit ('10'-'26')"**: 1-step and 2-step transition options.

---

## Example

### Input
`s = "226"`

### Visual Step-by-Step Progression

```text
String: "2 2 6"

- '2' (index 0): 1 way ("B")
- '2' (index 1):
  - Single '2': "BB" (prev1=1)
  - Pair '22': "V"   (prev2=1)
  - Total ways = 2
- '6' (index 2):
  - Single '6': "BBF", "VF" (prev1=2)
  - Pair '26': "BZ"         (prev2=1)
  - Total ways = 3

Result: 3
```

---

## Alternative Solutions

### Top-Down Memoization ($\mathcal{O}(N)$ Time, $\mathcal{O}(N)$ Space)
- Recurse with `vector<int> memo(n+1, -1)` array storing valid ways per index.

---

## Edge Cases

1. **Leading zero**: `s = "06"` $\implies$ returns `0`.
2. **Contains invalid zero**: `s = "30"` $\implies$ returns `0` (30 > 26 and '0' invalid).
3. **Valid zero combinations**: `s = "10"` or `"20"` $\implies$ returns `1`.

---

## Interview Tips

- **Explain Single vs Two Digit Logic**: State *"At each position, we check two independent decoding branches: 1-digit decoding (if current digit is non-zero) and 2-digit decoding (if previous two digits form a number in range $[10, 26]$). Summing these branches updates our state."*

---

## Similar Problems

1. [LeetCode #91: Decode Ways II](https://leetcode.com/problems/decode-ways-ii/)
2. [LeetCode #70: Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
3. [LeetCode #139: Word Break](https://leetcode.com/problems/word-break/)

---

## Revision Notes

- Problem: Count ways to decode number string into 'A'-'Z'.
- Pattern: 1D DP (Fibonacci-style).
- Base check: `if (s[0] == '0') return 0;`
- Loop: `curr = 0; if (s[i-1] != '0') curr += prev1; if (10 <= twoDigit <= 26) curr += prev2; prev2 = prev1; prev1 = curr;`
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
