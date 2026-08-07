# Last Stone Weight

- **Problem Number**: 1046
- **Platform**: LeetCode #1046
- **Difficulty**: Easy
- **Pattern**: Repeated Array Sorting

---

## Brute Force Intuition

At each step, sort the array in ascending order so that the two heaviest stones are positioned at the end of the array (indices `n - 1` and `n - 2`). Pop the two heaviest stones, compute the difference, and if non-zero, push the remaining weight back into the array. Repeat until at most 1 stone remains.

---

## Algorithm

1. While `stones.size() > 1`:
   a. `std::sort(stones.begin(), stones.end())`.
   b. `y = stones.back()`; `stones.pop_back()`.
   c. `x = stones.back()`; `stones.pop_back()`.
   d. If `x != y`: `stones.push_back(y - x)`.
2. Return `stones.empty() ? 0 : stones[0]`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int lastStoneWeight(std::vector<int>& stones) {
        while (stones.size() > 1) {
            std::sort(stones.begin(), stones.end());
            int y = stones.back();
            stones.pop_back();
            int x = stones.back();
            stones.pop_back();
            
            if (x != y) {
                stones.push_back(y - x);
            }
        }
        
        return stones.empty() ? 0 : stones[0];
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2 \log N)$
  - In worst case, $N - 1$ smashes take place. Sorting the array $N$ times takes $\mathcal{O}(N \times N \log N) = \mathcal{O}(N^2 \log N)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(\log N)$
  - Auxiliary call stack space for sorting.

---

## Why This Approach Is Not Optimal

Repeatedly sorting the entire array takes $\mathcal{O}(N^2 \log N)$ time. Using a **Max-Heap (Priority Queue)**, we can extract the two largest stones and insert the remainder in $\mathcal{O}(\log N)$ time per step, reducing total runtime to $\mathcal{O}(N \log N)$.
