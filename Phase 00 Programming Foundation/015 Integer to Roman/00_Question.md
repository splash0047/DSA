# 015. Integer to Roman

- **Platform**: LeetCode
- **Problem Number**: #12
- **Difficulty**: Medium
- **URL**: [LeetCode #12 - Integer to Roman](https://leetcode.com/problems/integer-to-roman/)

---

## Problem Statement

Seven different symbols represent Roman numerals with the following values:

| Symbol | Value |
| :--- | :--- |
| `I` | 1 |
| `V` | 5 |
| `X` | 10 |
| `L` | 50 |
| `C` | 100 |
| `D` | 500 |
| `M` | 1000 |

Roman numerals are formed by appending the conversion of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

- If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
- If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol: `4 (IV)`, `9 (IX)`, `40 (XL)`, `90 (XC)`, `400 (CD)`, and `900 (CM)`.

Given an integer `num`, convert it to a Roman numeral string.

---

## Examples

### Example 1
```text
Input: num = 3749
Output: "MMDCCXLIX"
Explanation:
3000 = MMM
 700 = DCC
  40 = XL
   9 = IX
3749 = MMDCCXLIX
```

### Example 2
```text
Input: num = 58
Output: "LVIII"
Explanation:
 50 = L
  8 = VIII
 58 = LVIII
```

### Example 3
```text
Input: num = 1994
Output: "MCMXCIV"
Explanation:
1000 = M
 900 = CM
  90 = XC
   4 = IV
1994 = MCMXCIV
```

---

## Constraints

- $1 \le \text{num} \le 3999$
