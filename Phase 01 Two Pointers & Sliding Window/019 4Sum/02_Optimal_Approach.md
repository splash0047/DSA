# 4Sum

## Pattern Used

- **Pattern**: **Sort + Two Fixed Loops + Two Pointers (K-Sum Generalization)**
- **Concept**: Sort the array. Fix the first two elements using outer loops `i` and `j`, then use Two Pointers (`left = j + 1`, `right = n - 1`) for the remaining two elements.

---

## Observation

1. 4Sum extends 3Sum by adding one more outer loop.
2. In-place duplicate handling:
   - Outer loop `i`: Skip if `i > 0 && nums[i] == nums[i-1]`.
   - Second loop `j`: Skip if `j > i + 1 && nums[j] == nums[j-1]`.
   - Two pointers `left` and `right`: Skip duplicate values after finding a valid quadruplet.
3. **Integer Overflow Guard**: Sum of 4 large integers (e.g. $10^9 + 10^9 + 10^9 + 10^9$) can exceed standard 32-bit signed integer limits. Always cast intermediate sum to `long long`.

---

## Intuition

1. Sort array.
2. Loop `i` from `0` to `n - 4` (skip duplicate `nums[i]`).
3. Loop `j` from `i + 1` to `n - 3` (skip duplicate `nums[j]`).
4. Set `left = j + 1`, `right = n - 1`.
5. Use Two Pointers logic to adjust `sum = (long long)nums[i] + nums[j] + nums[left] + nums[right]` against `target`.

---

## Algorithm

1. If `nums.size() < 4`, return `{}`.
2. Sort `nums`.
3. Loop `i` from `0` to `n - 4`:
   a. If `i > 0 && nums[i] == nums[i - 1]` continue.
   b. Loop `j` from `i + 1` to `n - 3`:
      - If `j > i + 1 && nums[j] == nums[j - 1]` continue.
      - `left = j + 1`, `right = n - 1`.
      - While `left < right`:
        - `sum = (long long)nums[i] + nums[j] + nums[left] + nums[right]`.
        - If `sum == target`:
          - Record quadruplet `{nums[i], nums[j], nums[left], nums[right]}`.
          - Skip duplicate `left` and `right` values.
          - `left++`, `right--`.
        - Else if `sum < target`: `left++`.
        - Else: `right--`.
4. Return `result`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> fourSum(std::vector<int>& nums, int target) {
        std::vector<std::vector<int>> result;
        int n = nums.size();
        if (n < 4) return result;
        
        std::sort(nums.begin(), nums.end());
        
        for (int i = 0; i < n - 3; ++i) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            for (int j = i + 1; j < n - 2; ++j) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;
                
                int left = j + 1;
                int right = n - 1;
                
                while (left < right) {
                    long long sum = (long long)nums[i] + nums[j] + nums[left] + nums[right];
                    
                    if (sum == target) {
                        result.push_back({nums[i], nums[j], nums[left], nums[right]});
                        
                        while (left < right && nums[left] == nums[left + 1]) left++;
                        while (left < right && nums[right] == nums[right - 1]) right--;
                        
                        left++;
                        right--;
                    } else if (sum < target) {
                        left++;
                    } else {
                        right--;
                    }
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
- `nums = [1, 0, -1, 0, -2, 2]`, `target = 0`
- Sorted `nums = [-2, -1, 0, 0, 1, 2]`

### Execution Trace

| `i` (`nums[i]`) | `j` (`nums[j]`) | `left` (`nums[left]`) | `right` (`nums[right]`) | `sum` | Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0 (`-2`) | 1 (`-1`) | 2 (`0`) | 5 (`2`) | `-2+-1+0+2 = -1 < 0` | `left++` |
| 0 (`-2`) | 1 (`-1`) | 3 (`0`) | 5 (`2`) | `-2+-1+0+2 = -1 < 0` | `left++` |
| 0 (`-2`) | 1 (`-1`) | 4 (`1`) | 5 (`2`) | `-2+-1+1+2 = 0 == 0` | **Found `[-2, -1, 1, 2]`** |
| 0 (`-2`) | 2 (`0`) | 3 (`0`) | 5 (`2`) | `-2+0+0+2 = 0 == 0` | **Found `[-2, 0, 0, 2]`** |
| 1 (`-1`) | 2 (`0`) | 3 (`0`) | 4 (`1`) | `-1+0+0+1 = 0 == 0` | **Found `[-1, 0, 0, 1]`** |

### Result
- Output: `[[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^3)$
  - Sorting takes $\mathcal{O}(N \log N)$ time.
  - Two outer loops run $\mathcal{O}(N^2)$ times; inner two-pointer search runs in $\mathcal{O}(N)$ time per pair.
  - Total time: $\mathcal{O}(N^3)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$ (excluding output vector).

---

## Why This is Optimal

- Reduces 4Sum from $\mathcal{O}(N^4)$ to $\mathcal{O}(N^3)$ by replacing two nested loops with two pointers.
- Eliminates duplicate sets in-place without auxiliary set overhead.

---

## Common Mistakes

1. **Integer Overflow**: Adding 4 integers without casting `(long long)` causes overflow for large positive/negative values.
2. **Missing `j > i + 1` Guard**: Writing `if (j > 0 && nums[j] == nums[j-1])` instead of `if (j > i + 1 && nums[j] == nums[j-1])` skips valid first pairs for index `j`.
