# Reverse String

## Pattern Used

- **Pattern**: **Two Pointers (In-Place Swap)**
- **Concept**: Maintain `left` pointer at index `0` and `right` pointer at index `n - 1`. Swap `s[left]` and `s[right]` and move pointers towards center until `left >= right`.

---

## Observation

1. Reversing a sequence means element at index `0` swaps with element at index `N-1`, index `1` swaps with index `N-2`, and so forth.
2. In-place modification is achieved by performing symmetric swaps between front and back elements.

---

## Intuition

Place two fingers at the edges of the character array:
1. Swap the characters under your left and right fingers.
2. Move left finger rightward (`left++`) and right finger leftward (`right--`).
3. Stop when fingers cross (`left >= right`).

---

## Algorithm

1. `left = 0`, `right = s.size() - 1`.
2. While `left < right`:
   a. `std::swap(s[left], s[right])`.
   b. `left++`, `right--`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    void reverseString(std::vector<char>& s) {
        int left = 0;
        int right = s.size() - 1;
        
        while (left < right) {
            std::swap(s[left++], s[right--]);
        }
    }
};
```

---

## Dry Run

### Input
- `s = ["h", "e", "l", "l", "o"]`

### Execution Trace

| Step | `left` (`s[left]`) | `right` (`s[right]`) | Action | Array State (`s`) |
| :--- | :--- | :--- | :--- | :--- |
| Start | `0` (`'h'`) | `4` (`'o'`) | Swap `s[0], s[4]`, `l++`, `r--` | `['o', 'e', 'l', 'l', 'h']` |
| 1 | `1` (`'e'`) | `3` (`'l'`) | Swap `s[1], s[3]`, `l++`, `r--` | `['o', 'l', 'l', 'e', 'h']` |
| 2 | `2` (`'l'`) | `2` (`'l'`) | `left == right`, Loop ends | `['o', 'l', 'l', 'e', 'h']` |

### Result
- Output: `["o", "l", "l", "e", "h"]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Performs $N/2$ swaps.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Strictly in-place modification.

---

## Why This is Optimal

- Every character must be moved to its target index ($\Omega(N)$ time lower bound).
- Uses $\mathcal{O}(1)$ space.

---

## Common Mistakes

1. **Looping past Center**: Running loop up to `N - 1` without stopping at middle, which swaps elements twice and restores original string!
2. **C++ STL Alternative**: Using `std::reverse(s.begin(), s.end())` is standard C++ idiomatic style; ensure you can write explicit two-pointer swap logic when requested by interviewers.
