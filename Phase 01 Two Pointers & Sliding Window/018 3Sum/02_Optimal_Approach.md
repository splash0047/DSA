# 3Sum

## Pattern Used

- **Pattern**: **Sort + Two Pointers (Fixed Outer Loop)**
- **Concept**: Sort the array first. Fix element `nums[i]` using an outer loop, then use Two Pointers (`left = i + 1`, `right = n - 1`) to find pairs adding up to `-nums[i]`.

---

## Observation

1. Sorting `nums` arranges duplicate elements contiguously.
2. If `nums[i] > 0`, since the array is sorted, no three positive numbers can add up to `0`. We can break early!
3. To avoid duplicate triplets without using a Hash Set:
   - Skip duplicate values for `nums[i]`: `if (i > 0 && nums[i] == nums[i-1]) continue;`
   - When a valid triplet is found, skip duplicate values for both `nums[left]` and `nums[right]` before advancing pointers.

---

## Intuition

1. Sort the input vector.
2. Iterate `i` from `0` to `n - 3`:
   - If `nums[i] > 0`, break loop immediately.
   - If `i > 0` and `nums[i] == nums[i-1]`, skip to avoid duplicate triplets.
   - Set `left = i + 1`, `right = n - 1`.
   - Run Two Sum II logic:
     - `sum = nums[i] + nums[left] + nums[right]`
     - If `sum == 0`: record triplet, advance `left` and `right`, skipping duplicates.
     - If `sum < 0`: `left++`.
     - If `sum > 0`: `right--`.

---

## Algorithm

1. Sort `nums`.
2. Initialize `std::vector<std::vector<int>> result`.
3. Loop `i` from `0` to `n - 3`:
   a. If `nums[i] > 0` break.
   b. If `i > 0 && nums[i] == nums[i - 1]` continue.
   c. `left = i + 1`, `right = n - 1`.
   d. While `left < right`:
      - `sum = nums[i] + nums[left] + nums[right]`.
      - If `sum == 0`:
        - `result.push_back({nums[i], nums[left], nums[right]})`.
        - While `left < right && nums[left] == nums[left + 1]`: `left++`.
        - While `left < right && nums[right] == nums[right - 1]`: `right--`.
        - `left++`, `right--`.
      - Else if `sum < 0`: `left++`.
      - Else: `right--`.
4. Return `result`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
        std::vector<std::vector<int>> result;
        int n = nums.size();
        if (n < 3) return result;
        
        std::sort(nums.begin(), nums.end());
        
        for (int i = 0; i < n - 2; ++i) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            int left = i + 1;
            int right = n - 1;
            
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                if (sum == 0) {
                    result.push_back({nums[i], nums[left], nums[right]});
                    
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    
                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        
        return result;
    }
};
```

---

## Dry Run

### Input
- `nums = [-1, 0, 1, 2, -1, -4]`
- Sorted `nums = [-4, -1, -1, 0, 1, 2]`

### Execution Trace

| `i` | `nums[i]` | `left` (`nums[left]`) | `right` (`nums[right]`) | `sum` | Match / Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | `-4` | 1 (`-1`) | 5 (`2`) | `-3 < 0` | `left++` -> no pair sums to 4 with -4 |
| 1 | `-1` | 2 (`-1`) | 5 (`2`) | `0 == 0` | **Found `[-1, -1, 2]`**, skip dups, `l=3, r=4` |
| 1 | `-1` | 3 (`0`) | 4 (`1`) | `0 == 0` | **Found `[-1, 0, 1]`**, `l=4, r=3` (ends inner loop) |
| 2 | `-1` | Skip (`nums[2] == nums[1]`) | - | - | Skip duplicate outer index |
| 3 | `0` | 4 (`1`) | 5 (`2`) | `3 > 0` | `right--` |
| 4 | `1` | `nums[4] > 0` | - | - | **Break outer loop** |

### Result
- Output: `[[-1, -1, 2], [-1, 0, 1]]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - Sorting takes $\mathcal{O}(N \log N)$ time.
  - Outer loop runs $N$ times; inner two-pointer search runs in $\mathcal{O}(N)$ time per step.
  - Total time: $\mathcal{O}(N \log N + N^2) = \mathcal{O}(N^2)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$ or $\mathcal{O}(\log N)$ auxiliary space (excluding result vector) for sorting memory.

---

## Why This is Optimal

- Under the 3SUM conjecture, 3Sum cannot be solved faster than $\mathcal{O}(N^2)$ time in the general case.
- In-place duplicate skipping eliminates the need for an expensive hash set.

---

## Common Mistakes

1. **Not Skipping Duplicates for `nums[i]`**: Forgetting `if (i > 0 && nums[i] == nums[i-1]) continue;` introduces duplicate triplets.
2. **Not Skipping Duplicates for `left` and `right`**: Forgetting inner `while` loops after finding a valid triplet.
3. **Out-of-Bounds in Duplicate Skips**: Forgetting `left < right` bounds check inside inner `while` loops.
