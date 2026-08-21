# Longest Consecutive Sequence - Optimal Approach (Hash Set Streak Start)

- **Problem Number**: 128
- **Platform**: LeetCode #128
- **Difficulty**: Medium
- **Pattern**: Hash Set with Sequence Start Detection ($\mathcal{O}(N)$)

---

## Optimal Intuition

Insert all numbers into an `unordered_set`. A number `x` is the **start of a sequence** if and only if `x - 1` is NOT in the set. For each sequence start, count how many consecutive numbers exist (`x + 1, x + 2, ...`).

Every element is visited at most twice $\implies$ strictly $\mathcal{O}(N)$ time!

---

## Code

```cpp
#include <vector>
#include <unordered_set>
#include <algorithm>

class Solution {
public:
    int longestConsecutive(const std::vector<int>& nums) {
        std::unordered_set<int> num_set(nums.begin(), nums.end());
        int longest = 0;

        for (int num : num_set) {
            // Check if 'num' is the start of a sequence
            if (!num_set.count(num - 1)) {
                int current_num = num;
                int current_streak = 1;

                while (num_set.count(current_num + 1)) {
                    current_num++;
                    current_streak++;
                }
                longest = std::max(longest, current_streak);
            }
        }
        return longest;
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(N)$ average time (each number is evaluated at most twice).
- **Space Complexity**: $\mathcal{O}(N)$ auxiliary space for the Hash Set.
