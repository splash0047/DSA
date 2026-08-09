# Permutation in String

## Pattern Used

- **Pattern**: **Fixed-Size Sliding Window (Character Frequency Vector)**
- **Concept**: Any permutation of `s1` must have length equal to `s1.length()` and character frequency count identical to `s1`.

---

## Observation

1. If `s1.length() > s2.length()`, `s2` cannot contain any permutation of `s1`.
2. Maintain a frequency difference array `count[26]` of size 26.
3. For the first window of size `len1` in `s2`:
   - Increment `count[s1[i] - 'a']++`.
   - Decrement `count[s2[i] - 'a']--`.
4. As the window of fixed size `len1` slides right through `s2`:
   - Add new incoming character: `count[s2[i] - 'a']--`.
   - Remove outgoing character: `count[s2[i - len1] - 'a']++`.
5. If at any step all 26 elements in `count` are `0`, `s2` contains a valid permutation of `s1`!

---

## Intuition

Slide a fixed window of size `len1` across `s2`. Maintain a tally ledger of character differences. When all 26 character differences reach 0, the current window in `s2` is an anagram (permutation) of `s1`.

---

## Algorithm

1. `len1 = s1.length()`, `len2 = s2.length()`.
2. If `len1 > len2`, return `false`.
3. `int count[26] = {0}`.
4. For `i` from `0` to `len1 - 1`:
   - `count[s1[i] - 'a']++`
   - `count[s2[i] - 'a']--`
5. If all 26 entries in `count` are `0`, return `true`.
6. For `i` from `len1` to `len2 - 1`:
   - `count[s2[i] - 'a']--` (incoming char)
   - `count[s2[i - len1] - 'a']++` (outgoing char)
   - If all 26 entries in `count` are `0`, return `true`.
7. Return `false`.

---

## Clean C++17 Solution

```cpp
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.length() > s2.length()) return false;

    vector<int> count1(26, 0); // frequency of chars in s1
    vector<int> count2(26, 0); // frequency of current window in s2

    // Count characters in s1 and first window of s2
    for (int i = 0; i < s1.length(); ++i) {
        count1[s1[i] - 'a']++;
        count2[s2[i] - 'a']++;
    }

    if (count1 == count2) return true;

    // Slide the window over s2
    for (int i = s1.length(); i < s2.length(); ++i) {
        count2[s2[i] - 'a']++;                      // Add new char to window
        count2[s2[i - s1.length()] - 'a']--;        // Remove old char from window

        if (count1 == count2) return true;
    }

    return false;
    }
};
```

---

## Dry Run

### Input
- `s1 = "ab"`, `s2 = "eidbaooo"`
- `len1 = 2`, `len2 = 8`

### Execution Trace

| Window Index `i` | Incoming Char | Outgoing Char | Active Substring in `s2` | `isZero(count)`? | Match Found? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Initial (`0..1`) | - | - | `"ei"` | No | False |
| `2` | `'d'` | `'e'` | `"id"` | No | False |
| `3` | `'b'` | `'i'` | `"db"` | No | False |
| `4` | `'a'` | `'d'` | `"ba"` | **Yes** (Matches `"ab"`) | **Return `true`** |

### Result
- Output: `true`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(L_2)$
  - Scanning `s2` takes $L_2$ steps.
  - Checking `isZero()` takes $26$ operations ($\mathcal{O}(1)$).
  - Total time: $26 \times L_2 = \mathcal{O}(L_2)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses fixed 26-element array.

---

## Why This is Optimal

- We must inspect characters of `s2` to find matches ($\Omega(L_2)$ time lower bound).
- Operates in $\mathcal{O}(1)$ extra space.

---

## Common Mistakes

1. **Forgetting `len1 > len2` Check**: If `s1` is longer than `s2`, accessing `s2[i]` during initial window setup causes out-of-bounds errors.
2. **Incorrect Sliding Window Bounds**: Writing `i - len1 - 1` instead of `i - len1` for the outgoing character.
