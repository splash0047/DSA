# Sort Array by Increasing Frequency

- **Problem Number**: 1636
- **Platform**: LeetCode #1636
- **Difficulty**: Easy
- **Pattern**: Custom Lambda Sorting

---

## Brute Force Intuition

1. Count the frequency of every element using a Hash Map `unordered_map<int, int> freq`.
2. Use `std::sort` directly on the input array `nums` with a custom lambda comparator.
3. The comparator compares elements `a` and `b`:
   - If `freq[a] != freq[b]`, return `freq[a] < freq[b]` (increasing frequency).
   - If `freq[a] == freq[b]`, return `a > b` (decreasing value).

---

## Algorithm

1. Build frequency map `freq`.
2. Sort `nums` using `std::sort` with custom comparator:
   - `freq[a] != freq[b] ? freq[a] < freq[b] : a > b`.
3. Return sorted `nums`.

---

## Code

```cpp
#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    std::vector<int> frequencySort(std::vector<int>& nums) {
        std::unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }
        
        std::sort(nums.begin(), nums.end(), [&](int a, int b) {
            if (freq[a] != freq[b]) {
                return freq[a] < freq[b]; // Increasing frequency
            }
            return a > b; // Decreasing value for tie-breaking
        });
        
        return nums;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log N)$
  - `std::sort` takes $\mathcal{O}(N \log N)$ time, where hash map lookups in the lambda comparator take $\mathcal{O}(1)$ average time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Hash map stores frequencies for up to $N$ unique elements.

---

## Why This Approach Is Not Optimal

While using standard sort with a custom comparator is extremely clean and practical, an explicit **Priority Queue (Min-Heap with custom ordering)** demonstrates the Heap pattern explicitly in an interview setting.
