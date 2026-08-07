# Remove Duplicates from Sorted Array

- **Problem Number**: 26
- **Platform**: LeetCode #26
- **Difficulty**: Easy
- **Pattern**: Auxiliary Data Structure / Hash Set

---

## Brute Force Intuition

When asked to remove duplicates from a collection, a natural initial thought is to use a data structure that inherently enforces uniqueness, such as a Hash Set or an ordered Set (`std::set`).

We can iterate through the input array `nums`, inserting every element into a set. Because set structures automatically ignore duplicate insertions, the set will retain only the unique values. After collecting all unique values, we copy them back into the prefix of the original array `nums` and return the size of the set.

---

## Algorithm

1. Initialize an ordered set `std::set<int> unique_elements`.
2. Iterate through each element `x` in `nums` and insert `x` into `unique_elements`.
3. Initialize an index counter `k = 0`.
4. Iterate through each element in `unique_elements`, placing it at `nums[k]` and incrementing `k`.
5. Return `k` as the count of unique elements.

---

## Code

```cpp
#include <vector>
#include <set>

class Solution {
public:
    int removeDuplicates(std::vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        
        std::set<int> unique_elements;
        for (int num : nums) {
            unique_elements.insert(num);
        }
        
        int k = 0;
        for (int num : unique_elements) {
            nums[k++] = num;
        }
        
        return k;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log N)$
  - Inserting $N$ elements into an ordered `std::set` (implemented as a Red-Black Tree) takes $\mathcal{O}(\log N)$ time per insertion.
  - Total time for all insertions: $N \times \mathcal{O}(\log N) = \mathcal{O}(N \log N)$.
  - Writing back to `nums` takes $\mathcal{O}(K)$ time where $K \le N$.
  - Overall time complexity is $\mathcal{O}(N \log N)$. (If using `std::unordered_set`, insertion takes average $\mathcal{O}(N)$ total time, but re-sorting is required, still taking $\mathcal{O}(N \log N)$).

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - The set `unique_elements` stores up to $N$ unique elements in auxiliary memory.
  - This violates the strict $\mathcal{O}(1)$ extra memory constraint required by the problem statement.

---

## Why This Approach Is Not Optimal

1. **Violates In-Place Space Constraint**: The problem explicitly requires an **in-place** solution with $\mathcal{O}(1)$ extra memory. Allocating a set creates $\mathcal{O}(N)$ auxiliary memory.
2. **Ignores Sorted Property**: The input array is already sorted in non-decreasing order. By using a set, we completely ignore this crucial property. Because duplicates in a sorted array are always adjacent to each other, we can identify duplicates locally in $\mathcal{O}(1)$ space without extra data structures.
