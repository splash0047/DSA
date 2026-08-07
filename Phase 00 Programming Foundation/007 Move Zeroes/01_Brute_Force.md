# Move Zeroes

- **Problem Number**: 283
- **Platform**: LeetCode #283
- **Difficulty**: Easy
- **Pattern**: Auxiliary Memory Copy

---

## Brute Force Intuition

The most direct way to move all zeroes to the end while preserving relative order is to copy all non-zero elements into an auxiliary array, and then fill the remaining elements of the auxiliary array with `0`. Finally, copy the auxiliary array back to `nums`.

---

## Algorithm

1. Create a temporary vector `temp`.
2. Iterate through `nums` and append all non-zero elements to `temp`.
3. Fill the remaining slots of `temp` (up to size $N$) with `0`.
4. Copy `temp` back into `nums`.

---

## Code

```cpp
#include <vector>

class Solution {
public:
    void moveZeroes(std::vector<int>& nums) {
        std::vector<int> temp;
        
        for (int x : nums) {
            if (x != 0) {
                temp.push_back(x);
            }
        }
        
        while (temp.size() < nums.size()) {
            temp.push_back(0);
        }
        
        nums = temp;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass to filter non-zeroes and pad zeroes, plus copying back.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Allocates an extra vector of size $N$.

---

## Why This Approach Is Not Optimal

The problem explicitly forbids making a copy of the array and demands an **in-place** solution with $\mathcal{O}(1)$ extra memory. Using **Two Pointers** achieves in-place zero relocation with $\mathcal{O}(1)$ space.
