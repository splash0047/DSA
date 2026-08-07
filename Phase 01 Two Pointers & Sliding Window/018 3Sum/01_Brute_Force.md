# 3Sum

- **Problem Number**: 15
- **Platform**: LeetCode #15
- **Difficulty**: Medium
- **Pattern**: Triple Nested Loops + Hash Set Deduplication

---

## Brute Force Intuition

Check all possible triplets $(i, j, k)$ with $i < j < k$. For each triplet where `nums[i] + nums[j] + nums[k] == 0`, sort the triplet and insert it into a `std::set<std::vector<int>>` to avoid returning duplicate triplets.

---

## Algorithm

1. Initialize `std::set<std::vector<int>> unique_triplets`.
2. Loop `i` from `0` to `n - 3`.
3. Loop `j` from `i + 1` to `n - 2`.
4. Loop `k` from `j + 1` to `n - 1`.
5. If `nums[i] + nums[j] + nums[k] == 0`:
   - Sort triplet `[nums[i], nums[j], nums[k]]`.
   - Insert triplet into `unique_triplets`.
6. Convert set to vector and return.

---

## Code

```cpp
#include <vector>
#include <set>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
        std::set<std::vector<int>> unique_triplets;
        int n = nums.size();
        
        for (int i = 0; i < n - 2; ++i) {
            for (int j = i + 1; j < n - 1; ++j) {
                for (int k = j + 1; k < n; ++k) {
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        std::vector<int> triplet = {nums[i], nums[j], nums[k]};
                        std::sort(triplet.begin(), triplet.end());
                        unique_triplets.insert(triplet);
                    }
                }
            }
        }
        
        return std::vector<std::vector<int>>(unique_triplets.begin(), unique_triplets.end());
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^3 \log K)$
  - Triple nested loops take $\mathcal{O}(N^3)$ time.
  - Set insertion takes $\mathcal{O}(\log K)$ time where $K$ is the number of valid triplets.
  - For $N = 3000$, $N^3 = 2.7 \times 10^{10}$ operations, causing TLE.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(K)$
  - Extra memory to store unique triplets in set.

---

## Why This Approach Is Not Optimal

Cubic time $\mathcal{O}(N^3)$ is too slow. By **sorting the array first**, we can fix the outer loop index `i` and reduce the remaining two indices to a Two Pointers search in $\mathcal{O}(N^2)$ time.
