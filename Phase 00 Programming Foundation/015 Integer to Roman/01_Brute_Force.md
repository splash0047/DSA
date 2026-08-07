# Integer to Roman

- **Problem Number**: 12
- **Platform**: LeetCode #12
- **Difficulty**: Medium
- **Pattern**: Hardcoded Decimal Place Mapping

---

## Brute Force Intuition

Since the input `num` is strictly constrained to the range $1 \le \text{num} \le 3999$, we can decompose `num` into its thousands, hundreds, tens, and units places, and use pre-defined lookup tables for each decimal digit position.

---

## Algorithm

1. Define 4 lookup arrays for Thousands, Hundreds, Tens, and Units places.
2. Extract digit for thousands: `num / 1000`.
3. Extract digit for hundreds: `(num % 1000) / 100`.
4. Extract digit for tens: `(num % 100) / 10`.
5. Extract digit for units: `num % 10`.
6. Concatenate mapped strings and return.

---

## Code

```cpp
#include <string>
#include <vector>

class Solution {
public:
    std::string intToRoman(int num) {
        std::vector<std::string> thousands = {"", "M", "MM", "MMM"};
        std::vector<std::string> hundreds  = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        std::vector<std::string> tens      = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        std::vector<std::string> ones      = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
        
        return thousands[num / 1000] + 
               hundreds[(num % 1000) / 100] + 
               tens[(num % 100) / 10] + 
               ones[num % 10];
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(1)$
  - Performs constant math operations and string lookups.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Fixed lookup tables.

---

## Why This Approach Is Not Optimal

While running in constant time, hardcoding 40 table entries relies heavily on input constraint limits ($num \le 3999$). A **Greedy Value Table Lookup** algorithm provides a far cleaner, general structure using 13 fundamental value-symbol pairs.
