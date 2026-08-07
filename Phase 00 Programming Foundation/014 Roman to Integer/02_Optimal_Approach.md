# Roman to Integer

## Pattern Used

- **Pattern**: **Left-to-Right Single Pass (Lookahead Comparison)**
- **Concept**: If a Roman symbol value is strictly smaller than the value of the symbol immediately following it (e.g. `I` before `V`), it represents a subtractive combination (`value[next] - value[current]`). Otherwise, it is additive.

---

## Observation

1. Standard Roman numerals are written largest to smallest: `VI = 5 + 1 = 6`.
2. When a smaller value symbol appears **before** a larger value symbol, subtraction applies: `IV = -1 + 5 = 4`.
3. Therefore, for any position `i`:
   - If `value(s[i]) < value(s[i+1])`: Subtract `value(s[i])` from total.
   - Else: Add `value(s[i])` to total.

---

## Intuition

Scan string `s` from left to right. Look at current character `s[i]` and next character `s[i+1]`:
- If `s[i]` is smaller than `s[i+1]`, it subtracts from the total (e.g. `I` before `V` means $-1$).
- Otherwise, it adds to the total (e.g. `V` before `I` means $+5$).

This processes the Roman string cleanly in a single pass.

---

## Algorithm

1. Define helper `getValue(char c)` using a fast `switch` statement.
2. Initialize `total = 0`, `n = s.length()`.
3. Loop `i` from `0` to `n - 1`:
   a. `current = getValue(s[i])`.
   b. `next = (i + 1 < n) ? getValue(s[i+1]) : 0`.
   c. If `current < next`: `total -= current`.
   d. Else: `total += current`.
4. Return `total`.

---

## Clean C++17 Solution

```cpp
#include <string>

class Solution {
private:
    int getValue(char c) {
        switch (c) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: return 0;
        }
    }
public:
    int romanToInt(const std::string& s) {
        int total = 0;
        int n = s.length();
        
        for (int i = 0; i < n; ++i) {
            int current = getValue(s[i]);
            int next = (i + 1 < n) ? getValue(s[i + 1]) : 0;
            
            if (current < next) {
                total -= current;
            } else {
                total += current;
            }
        }
        
        return total;
    }
};
```

---

## Dry Run

### Input
- `s = "MCMXCIV"`

### Execution Trace

| Index `i` | `s[i]` | `current` | `s[i+1]` | `next` | `current < next`? | Action | `total` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | `'M'` | 1000 | `'C'` | 100 | No | `+ 1000` | 1000 |
| 1 | `'C'` | 100 | `'M'` | 1000 | **Yes** | `- 100` | 900 |
| 2 | `'M'` | 1000 | `'X'` | 10 | No | `+ 1000` | 1900 |
| 3 | `'X'` | 10 | `'C'` | 100 | **Yes** | `- 10` | 1890 |
| 4 | `'C'` | 100 | `'I'` | 1 | No | `+ 100` | 1990 |
| 5 | `'I'` | 1 | `'V'` | 5 | **Yes** | `- 1` | 1989 |
| 6 | `'V'` | 5 | - | 0 | No | `+ 5` | **1994** |

### Result
- Output: `1994`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Traverses string of length $N$ once. Since $N \le 15$, execution time is $\mathcal{O}(1)$ practically.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses `switch` statement without external heap or hash map allocations.

---

## Why This is Optimal

- Inspects each Roman character once ($\mathcal{O}(N)$ time).
- Uses $\mathcal{O}(1)$ extra space.

---

## Common Mistakes

1. **Out-of-Bounds on `s[i+1]`**: Accessing `s[i+1]` without checking `i + 1 < n`.
2. **Using `std::unordered_map` unnecessarily**: `std::unordered_map` adds hash table overhead. `switch` statement is zero-overhead and faster.
