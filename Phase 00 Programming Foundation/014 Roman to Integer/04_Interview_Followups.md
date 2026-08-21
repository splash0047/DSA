# 04 Interview Follow-ups & System Variations: Roman to Integer

The standard problem converts a valid Roman numeral string into an integer. The standard right-to-left or left-to-right subtraction logic runs in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In top-tier interviews, interviewers rarely stop at parsing valid input; they ask how to **validate strict grammatical rules of Roman Numerals**, optimize mapping lookups to avoid hash map allocations, and scale beyond standard bounds (1 to 3999).

---

## 1. What if the Roman Numeral String May Be Grammatically Invalid?

### 🛑 Why Simple Subtraction Fails on Invalid Input
A simple subtraction parser turns `"IL"` into $49$ and `"VX"` into $5$, even though both are strictly invalid in standard Roman numeral grammar (49 must be `"XLIX"`).

### 💡 Strict Grammatical Rules & Validation
1. **Subtractives Rule**:
   - `'I'` can only precede `'V'` ($5$) and `'X'` ($10$).
   - `'X'` can only precede `'L'` ($50$) and `'C'` ($100$).
   - `'C'` can only precede `'D'` ($500$) and `'M'` ($1000$).
   - `'V'`, `'L'`, `'D'` can **never** be subtracted.
2. **Repetition Limit**:
   - `'I'`, `'X'`, `'C'`, `'M'` can appear at most 3 consecutive times (e.g., `"IIII"` is invalid).
   - `'V'`, `'L'`, `'D'` can appear at most 1 time consecutively.
3. **Deterministic Finite Automaton (DFA) / Regex Validator**:
   - Valid Regex pattern:
     ```regex
     ^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$
     ```

---

## 2. Low-Level Optimization: Avoiding Hash Map Overhead

### 🛑 Hash Map Inefficiency
Using `std::unordered_map<char, int>` or Python `dict` introduces hashing overhead and heap allocations.

### 💡 Fixed 128-Byte Direct Array Lookup
```cpp
int romanToInt(const string& s) {
    int val[128] = {0};
    val['I'] = 1; val['V'] = 5; val['X'] = 10;
    val['L'] = 50; val['C'] = 100; val['D'] = 500; val['M'] = 1000;
    
    int total = 0, n = s.size();
    for (int i = 0; i < n; i++) {
        if (i + 1 < n && val[s[i]] < val[s[i + 1]]) {
            total -= val[s[i]];
        } else {
            total += val[s[i]];
        }
    }
    return total;
}
```
- Operates in **L1 CPU Cache** with zero dynamic memory allocation.

---

## 3. What if Numbers Exceed 3,999 (Vinculum / Overline Notation)?

### 💡 Extended Roman System
- In classical Roman notation, an overline (Vinculum) multiplies a numeral's value by 1,000:
  - $\overline{\text{V}} = 5,000$
  - $\overline{\text{X}} = 10,000$
  - $\overline{\text{L}} = 50,000$
  - $\overline{\text{C}} = 100,000$
  - $\overline{\text{D}} = 500,000$
  - $\overline{\text{M}} = 1,000,000$
- System parser adds an extra pass or token representation (e.g., `_V`, `_X`) to handle integers up to millions.

---

## Summary Matrix: Trade-offs at a Glance

| Goal | Strategy | Time | Space |
| :--- | :--- | :--- | :--- |
| **Standard Parser** | Left-to-right lookahead with Direct Array | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Strict Syntax Validation** | Regex / DFA State Machine | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Bidirectional Sanity Check** | Convert to Int $\to$ Convert back to Roman | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Extended Range ($> 4,000$)** | Vinculum / Token prefix multiplier | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
