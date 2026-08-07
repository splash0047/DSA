# Reverse String

- **Problem Number**: 344
- **Platform**: LeetCode #344
- **Difficulty**: Easy
- **Pattern**: Auxiliary Vector Copy

---

## Brute Force Intuition

To reverse a vector of characters, the simplest approach is to copy elements from `s` into a new vector in reverse order, and then assign the new vector back to `s`.

---

## Algorithm

1. Create an auxiliary vector `temp` of size $N$.
2. Loop `i` from `0` to $N - 1$:
   - `temp[i] = s[n - 1 - i]`.
3. Copy `temp` back into `s`.

---

## Code

```cpp
#include <vector>

class Solution {
public:
    void reverseString(std::vector<char>& s) {
        int n = s.size();
        std::vector<char> temp(n);
        
        for (int i = 0; i < n; ++i) {
            temp[i] = s[n - 1 - i];
        }
        
        s = temp;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Copies $N$ elements into `temp` and back to `s`.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Allocates an extra vector of size $N$.

---

## Why This Approach Is Not Optimal

This approach violates the strict in-place constraint requiring $\mathcal{O}(1)$ extra memory. Using **Two Pointers (In-Place Swap)** solves it using $\mathcal{O}(1)$ space.
