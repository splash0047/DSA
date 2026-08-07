# Majority Element

- **Problem Number**: 169
- **Platform**: LeetCode #169
- **Difficulty**: Easy
- **Pattern**: Hash Map Frequency Counting

---

## Brute Force Intuition

To find the element that appears more than $\lfloor n / 2 \rfloor$ times, the most direct approach is to count the occurrences of each element in the array using a Hash Map (`std::unordered_map`). As soon as an element's frequency count exceeds $\lfloor n / 2 \rfloor$, it is returned as the majority element.

---

## Algorithm

1. Create a hash map `counts` to store mapping `element_value -> frequency_count`.
2. Iterate through each element `num` in `nums`:
   a. Increment `counts[num]++`.
   b. If `counts[num] > n / 2`, return `num`.
3. Return `-1` if no majority element exists.

---

## Code

```cpp
#include <vector>
#include <unordered_map>

class Solution {
public:
    int majorityElement(const std::vector<int>& nums) {
        std::unordered_map<int, int> counts;
        int target = nums.size() / 2;
        
        for (int num : nums) {
            counts[num]++;
            if (counts[num] > target) {
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
  - Scanning $N$ elements and updating hash map counts takes average $\mathcal{O}(N)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - In the worst case, the hash map stores up to $N/2 + 1$ distinct elements, requiring $\mathcal{O}(N)$ auxiliary memory.

---

## Why This Approach Is Not Optimal

While this approach runs in linear time $\mathcal{O}(N)$, it uses $\mathcal{O}(N)$ extra space. By exploiting the mathematical property that the majority element appears more than $N/2$ times, we can eliminate the Hash Map and reduce space complexity to $\mathcal{O}(1)$ using the **Boyer-Moore Voting Algorithm**.
