# Smallest Range Covering Elements from K Lists

- **Problem Number**: 632
- **Platform**: LeetCode #632
- **Difficulty**: Hard
- **Pattern**: Flatten + Sliding Window / Pairwise Cartesian Product

---

## Brute Force Intuition

Combine all elements from all $k$ lists into a single flat vector `vector<pair<int, int>> merged`, where each pair store `{val, list_index}`. Sort this merged vector by value. Then, find the shortest window `[merged[left], merged[right]]` in the flattened array that contains at least one element from each of the $k$ lists using a sliding window and frequency map.

---

## Algorithm

1. Merge all elements into `vector<pair<int, int>> merged`, storing `{val, list_idx}`.
2. Sort `merged` by `val`.
3. Use two pointers `left = 0` and `right = 0` with a hash map `freq` tracking count of items from each `list_idx`.
4. Expand `right`: Add `merged[right].list_idx` to `freq`.
5. When `freq.size() == k` (window covers elements from all $k$ lists):
   - Check if current range `merged[right].val - merged[left].val` is smaller than best range.
   - Shrink `left` to find minimal valid range.
6. Return `bestRange`.

---

## Code

```cpp
#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    std::vector<int> smallestRange(std::vector<std::vector<int>>& nums) {
        int k = nums.size();
        std::vector<std::pair<int, int>> merged;
        
        for (int i = 0; i < k; ++i) {
            for (int val : nums[i]) {
                merged.push_back({val, i});
            }
        }
        
        std::sort(merged.begin(), merged.end());
        
        std::unordered_map<int, int> count;
        int uniqueLists = 0;
        int minRange = 1e9;
        std::vector<int> ans = {0, 0};
        
        int left = 0;
        for (int right = 0; right < merged.size(); ++right) {
            int rightList = merged[right].second;
            if (count[rightList] == 0) {
                uniqueLists++;
            }
            count[rightList]++;
            
            while (uniqueLists == k) {
                int curRange = merged[right].first - merged[left].first;
                if (curRange < minRange) {
                    minRange = curRange;
                    ans = {merged[left].first, merged[right].first};
                }
                
                int leftList = merged[left].second;
                count[leftList]--;
                if (count[leftList] == 0) {
                    uniqueLists--;
                }
                left++;
            }
        }
        
        return ans;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log N)$
  - Where $N$ is total number of elements across all $k$ lists. Sorting all $N$ elements takes $\mathcal{O}(N \log N)$ time. Two-pointer sliding window takes $\mathcal{O}(N)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Merged array stores $N$ pairs.

---

## Why This Approach Is Not Optimal

While $\mathcal{O}(N \log N)$ with flattening works, using a **Min-Heap of size $k$** allows us to maintain dynamic range boundaries `[min_val, max_val]` directly without flattening or storing all $N$ pairs into a dynamic array, running in optimal $\mathcal{O}(N \log k)$ time and $\mathcal{O}(k)$ space!
