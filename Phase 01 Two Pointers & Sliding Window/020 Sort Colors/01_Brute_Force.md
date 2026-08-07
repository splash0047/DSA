# Sort Colors

- **Problem Number**: 75
- **Platform**: LeetCode #75
- **Difficulty**: Medium
- **Pattern**: Counting Sort (Two-Pass)

---

## Brute Force Intuition

Count the total occurrences of `0`s, `1`s, and `2`s in a first pass over the array. Then, in a second pass, overwrite `nums` with the counted number of `0`s, followed by `1`s, followed by `2`s.

---

## Algorithm

1. Initialize counters `count0 = 0`, `count1 = 0`, `count2 = 0`.
2. First pass: Loop through `nums` and increment `count0`, `count1`, or `count2` accordingly.
3. Second pass:
   - Fill first `count0` positions with `0`.
   - Fill next `count1` positions with `1`.
   - Fill remaining `count2` positions with `2`.

---

## Code

```cpp
#include <vector>

class Solution {
public:
    void sortColors(std::vector<int>& nums) {
        int count0 = 0, count1 = 0, count2 = 0;
        
        for (int num : nums) {
            if (num == 0) count0++;
            else if (num == 1) count1++;
            else if (num == 2) count2++;
        }
        
        int idx = 0;
        while (count0-- > 0) nums[idx++] = 0;
        while (count1-- > 0) nums[idx++] = 1;
        while (count2-- > 0) nums[idx++] = 2;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Performs two complete passes over the array ($2 \times N$ operations).

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses three integer variables.

---

## Why This Approach Is Not Optimal

While running in linear time and $\mathcal{O}(1)$ space, it requires **two passes** over the data. The follow-up challenge asks for a **single pass** algorithm using **Dutch National Flag (3 Pointers)**.
