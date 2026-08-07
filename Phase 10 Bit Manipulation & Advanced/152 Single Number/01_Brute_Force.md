# Single Number

- **Problem Number**: 136
- **Platform**: LeetCode #136
- **Difficulty**: Easy
- **Pattern**: Frequency Counting / Hash Map

---

## Brute Force Intuition

Count the occurrence frequency of each number in `nums` using an `std::unordered_map<int, int>`. Iterate through the frequency map and return the element whose frequency is `1`.

---

## Algorithm

1. `unordered_map<int, int> freq`.
2. For `num` in `nums`:
   - `freq[num]++`.
3. For pair `[num, count]` in `freq`:
   - If `count == 1`, return `num`.
4. Return `-1`.

---

## Code

```cpp
#include <vector>
#include <unordered_map>

class Solution {
public:
    int singleNumber(std::vector<int>& nums) {
        std::unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }
        
        for (const auto& [num, count] : freq) {
            if (count == 1) {
                return num;
            }
        }
        
        return -1;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass to populate hash map and single pass to find frequency 1.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Hash map stores $\approx N/2$ unique elements.

---

## Why This Approach Is Not Optimal

The problem strictly requires **constant extra space $\mathcal{O}(1)$**. Using **Bitwise XOR Reduction**, we can find the single number in linear $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space!
