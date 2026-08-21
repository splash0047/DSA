# Longest Consecutive Sequence - Brute Force (Sorting)

- **Problem Number**: 128
- **Platform**: LeetCode #128
- **Difficulty**: Medium
- **Pattern**: Sorting + Linear Scan

---

## Algorithm

1. If array is empty, return 0.
2. Sort `nums` in ascending order.
3. Traverse sorted array, tracking `current_streak`:
   - If `nums[i] == nums[i-1]`, skip duplicate.
   - If `nums[i] == nums[i-1] + 1`, `current_streak++`.
   - Else, reset `current_streak = 1`.
4. Return `max_streak`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int longestConsecutive(std::vector<int>& nums) {
        if (nums.empty()) return 0;
        std::sort(nums.begin(), nums.end());

        int longest = 1, current = 1;
        for (size_t i = 1; i < nums.size(); i++) {
            if (nums[i] == nums[i - 1]) continue;
            if (nums[i] == nums[i - 1] + 1) {
                current++;
            } else {
                longest = std::max(longest, current);
                current = 1;
            }
        }
        return std::max(longest, current);
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(N \log N)$
- **Space Complexity**: $\mathcal{O}(1)$ or $\mathcal{O}(N)$ depending on sorting algorithm.
