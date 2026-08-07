# 4Sum

- **Problem Number**: 18
- **Platform**: LeetCode #18
- **Difficulty**: Medium
- **Pattern**: Quadruple Nested Loops + Hash Set Deduplication

---

## Brute Force Intuition

Check all combinations of 4 distinct indices $(i, j, k, l)$ with $i < j < k < l$. For each quadruplet where $\text{nums}[i] + \text{nums}[j] + \text{nums}[k] + \text{nums}[l] == \text{target}$, sort the quadruplet and insert it into a `std::set<std::vector<int>>` to eliminate duplicate outputs.

---

## Algorithm

1. Initialize `std::set<std::vector<int>> unique_quads`.
2. Four nested loops for indices $i, j, k, l$.
3. Compute `sum = (long long)nums[i] + nums[j] + nums[k] + nums[l]`.
4. If `sum == target`, sort quadruplet and insert into `unique_quads`.
5. Return vector from set.

---

## Code

```cpp
#include <vector>
#include <set>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> fourSum(std::vector<int>& nums, int target) {
        std::set<std::vector<int>> unique_quads;
        int n = nums.size();
        
        for (int i = 0; i < n - 3; ++i) {
            for (int j = i + 1; j < n - 2; ++j) {
                for (int k = j + 1; k < n - 1; ++k) {
                    for (int l = k + 1; l < n; ++l) {
                        long long sum = (long long)nums[i] + nums[j] + nums[k] + nums[l];
                        if (sum == target) {
                            std::vector<int> quad = {nums[i], nums[j], nums[k], nums[l]};
                            std::sort(quad.begin(), quad.end());
                            unique_quads.insert(quad);
                        }
                    }
                }
            }
        }
        
        return std::vector<std::vector<int>>(unique_quads.begin(), unique_quads.end());
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^4)$
  - Four nested loops run in $\mathcal{O}(N^4)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(K)$ for result set memory.

---

## Why This Approach Is Not Optimal

Quadruple nested loops take $\mathcal{O}(N^4)$ time. By **sorting the array first**, fixing the two outer loops $i$ and $j$, and applying Two Pointers to the inner pair, we can reduce the complexity to $\mathcal{O}(N^3)$.
