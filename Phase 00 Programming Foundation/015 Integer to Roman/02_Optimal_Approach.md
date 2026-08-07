# Integer to Roman

## Pattern Used

- **Pattern**: **Greedy Value Matching / Table Lookup**
- **Concept**: Maintain an ordered table of the 13 base Roman numeral values (including subtractive forms like `900: CM`, `400: CD`, `90: XC`, `40: XL`, `9: IX`, `4: IV`) sorted in descending order. Greedily match and subtract the largest possible Roman value at each step.

---

## Observation

1. Roman numerals are written largest to smallest.
2. Including the 6 subtractive pairs (`CM`, `CD`, `XC`, `XL`, `IX`, `IV`) alongside standard symbols (`M`, `D`, `C`, `L`, `X`, `V`, `I`) produces 13 distinct value steps:
   `[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]`
3. For any input `num`, we greedily subtract the largest value $\le \text{num}$ from `num` and append its corresponding symbol string to our result.

---

## Intuition

Think of making change with coins of values 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1.
- You want to give the change using the fewest possible coins/symbols.
- At each step, take the largest coin value that fits into `num`, append its symbol, and subtract its value from `num`.

---

## Algorithm

1. Define arrays `values` and `symbols` of size 13 in descending order.
2. Initialize string `result = ""`.
3. Loop `i` from `0` to `12`:
   - While `num >= values[i]`:
     - `result += symbols[i]`
     - `num -= values[i]`
4. Return `result`.

---

## Clean C++17 Solution

```cpp
#include <string>

class Solution {
public:
    std::string intToRoman(int num) {
        const int values[] = {
            1000, 900, 500, 400, 
            100, 90, 50, 40, 
            10, 9, 5, 4, 1
        };
        const char* symbols[] = {
            "M", "CM", "D", "CD", 
            "C", "XC", "L", "XL", 
            "X", "IX", "V", "IV", "I"
        };
        
        std::string result = "";
        
        for (int i = 0; i < 13; ++i) {
            while (num >= values[i]) {
                result += symbols[i];
                num -= values[i];
            }
        }
        
        return result;
    }
};
```

---

## Dry Run

### Input
- `num = 3749`

### Execution Trace

| Step | `values[i]` | `symbols[i]` | `num` (Before -> After) | `result` State |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `1000` | `"M"` | `3749 -> 2749 -> 1749 -> 749` | `"MMM"` |
| 2 | `900` | `"CM"` | `749 < 900` (skip) | `"MMM"` |
| 3 | `500` | `"D"` | `749 -> 249` | `"MMMD"` |
| 4 | `100` | `"C"` | `249 -> 149 -> 49` | `"MMMDCC"` |
| 5 | `40` | `"XL"` | `49 -> 9` | `"MMMDCCXL"` |
| 6 | `9` | `"IX"` | `9 -> 0` | `"MMMDCCXLIX"` |

### Result
- Output: `"MMDCCXLIX"`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(1)$
  - Since $num \le 3999$, the outer loop runs 13 times and the inner while loop executes at most 15 times total. Execution time is strictly bounded.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses fixed 13-element arrays.

---

## Why This is Optimal

- Bounded input $num \le 3999$ completes in constant time $\mathcal{O}(1)$.
- Uses $\mathcal{O}(1)$ auxiliary memory.

---

## Common Mistakes

1. **Omitting Subtractive Form Entries**: Forgetting to include entries like `900: CM`, `400: CD`, `90: XC`, `40: XL`, `9: IX`, `4: IV` in the lookup table.
2. **Incorrect Symbol Ordering**: Putting smaller values before larger values in the lookup array breaks the greedy strategy.
