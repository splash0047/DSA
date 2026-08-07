# Top K Frequent Elements

- **Problem Number**: 347
- **Platform**: LeetCode #347
- **Difficulty**: Medium
- **Pattern**: Frequency HashMap + Custom Sorting

---

## Brute Force Intuition

1. Count the frequency of each element in `nums` using a Hash Map (`std::unordered_map<int, int>`).
2. Transfer the key-value pairs from the hash map into a vector of pairs `std::vector<std::pair<int, int>>`.
3. Sort the vector in descending order of frequency.
4. Extract the elements corresponding to the first $k$ pairs in the sorted vector.

---

## Algorithm

1. Build frequency map `freq`: `freq[num]++` for each element in `nums`.
2. Convert `freq` to vector of pairs `vec` where each element is `{frequency, num}`.
3. Sort `vec` using `std::sort` in descending order of frequency (`std::greater`).
4. Extract the first $k$ element values into result vector `ans`.
5. Return `ans`.

---

## Code

```cpp
#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    std::vector<int> topKFrequent(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }
        
        std::vector<std::pair<int, int>> vec; // {frequency, num}
        for (const auto& [num, count] : freq) {
            vec.push_back({count, num});
        }
        
        std::sort(vec.rbegin(), vec.rend());
        
        std::vector<int> ans;
        for (int i = 0; i < k; ++i) {
            ans.push_back(vec[i].second);
        }
        
        return ans;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(U \log U)$
  - Where $U$ is the number of unique elements in `nums` ($U \le N$).
  - In worst case (all elements unique), $U = N$, giving $\mathcal{O}(N \log N)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(U)$
  - Hash map and vector of pairs store $U$ unique elements.

---

## Why This Approach Is Not Optimal

Sorting all unique elements takes $\mathcal{O}(U \log U)$ time. The problem requires a time complexity better than $\mathcal{O}(N \log N)$. Using a **Min-Heap of size $k$** achieves $\mathcal{O}(N \log k)$ time, while **Bucket Sort** achieves optimal linear $\mathcal{O}(N)$ time!
