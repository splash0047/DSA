# Minimum Operations to Reduce X to Zero

## Pattern Used

- **Pattern**: **Problem Reframe $\rightarrow$ Longest Middle Subarray with Target Sum**
- **Concept**: Removing elements from the left and right ends to sum to $x$ is equivalent to finding a **contiguous middle subarray** whose sum equals $\text{target} = \text{total\_sum} - x$.
  $$\text{Minimum Operations} = N - \text{Maximum Length of Middle Subarray with sum } (\text{total\_sum} - x)$$

---

## Observation

1. Let $\text{total\_sum} = \sum \text{nums}[i]$.
2. If $\text{total\_sum} == x$, we must pick all $N$ elements, so return $N$.
3. If $\text{total\_sum} < x$, it is impossible to reach $x$, return $-1$.
4. Target sum for middle subarray: $\text{target} = \text{total\_sum} - x$.
5. Because all elements in `nums` are strictly **positive integers** ($\text{nums}[i] \ge 1$), we can find the maximum length of a subarray with sum equal to $\text{target}$ using a **Variable-Size Sliding Window** in linear $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space!

---

## Intuition

1. `target = total_sum - x`.
2. Maintain a sliding window `[left ... right]` with `current_sum`.
3. Expand `right`: `current_sum += nums[right]`.
4. While `current_sum > target` and `left <= right`:
   - `current_sum -= nums[left++]`.
5. If `current_sum == target`:
   - `max_len = max(max_len, right - left + 1)`.
6. Final answer: `max_len == -1 ? -1 : N - max_len`.

---

## Algorithm

1. Compute `total_sum = std::accumulate(nums.begin(), nums.end(), 0LL)`.
2. `target = total_sum - x`.
3. If `target == 0` return `nums.size()`.
4. If `target < 0` return `-1`.
5. `left = 0`, `current_sum = 0`, `max_len = -1`.
6. Loop `right` from `0` to `n - 1`:
   a. `current_sum += nums[right]`.
   b. `while (current_sum > target && left <= right)`:
      - `current_sum -= nums[left++]`.
   c. `if (current_sum == target)`:
      - `max_len = max(max_len, right - left + 1)`.
7. Return `max_len == -1 ? -1 : n - max_len`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <numeric>
#include <algorithm>

class Solution {
public:
    int minOperations(const std::vector<int>& nums, int x) {
        long long total_sum = 0;
        for (int num : nums) {
            total_sum += num;
        }
        
        long long target = total_sum - x;
        if (target == 0) return nums.size();
        if (target < 0) return -1;
        
        int left = 0;
        long long current_sum = 0;
        int max_len = -1;
        int n = nums.size();
        
        for (int right = 0; right < n; ++right) {
            current_sum += nums[right];
            
            while (current_sum > target && left <= right) {
                current_sum -= nums[left++];
            }
            
            if (current_sum == target) {
                max_len = std::max(max_len, right - left + 1);
            }
        }
        
        return max_len == -1 ? -1 : n - max_len;
    }
};
```

---

## Dry Run

### Input
- `nums = [1, 1, 4, 2, 3]`, `x = 5`
- `total_sum = 11`, `target = 11 - 5 = 6`

### Execution Trace

| `right` | `nums[right]` | `current_sum` | `current_sum > 6`? | `current_sum == 6`? | `max_len` |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | `1` | `1` | No | No | `-1` |
| 1 | `1` | `2` | No | No | `-1` |
| 2 | `4` | `6` | No | **Yes** (len = 3 `[1,1,4]`) | **`3`** |
| 3 | `2` | `8` | Yes $\rightarrow$ shrink `l=1` (`sum=7`), shrink `l=2` (`sum=6`) | **Yes** (len = 2 `[4,2]`) | `3` |
| 4 | `3` | `9` | Yes $\rightarrow$ shrink `l=3` (`sum=5`) | No | `3` |

### Result
- `max_len = 3`
- Return `N - max_len = 5 - 3 = 2`
- Output: `2` (Operations: pick last 2 elements `3` and `2`)

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass through $N$ elements. `right` and `left` pointers advance at most $N$ times.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses constant auxiliary space.

---

## Why This is Optimal

- Solves inverse problem in linear $\mathcal{O}(N)$ time.
- Uses $\mathcal{O}(1)$ space.

---

## Common Mistakes

1. **Trying Direct Left/Right Recursion**: Using memoization on 2 pointers `(left, right, current_x)` takes $\mathcal{O}(N^2)$ space/time. Reframing as Middle Subarray is far superior.
2. **Missing `target == 0` Guard**: Returning `-1` when `total_sum == x`. (If `total_sum == x`, removing all $N$ elements reduces $x$ to 0, so output should be $N$).
