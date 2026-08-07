# Minimum Size Subarray Sum

## Pattern Used

- **Pattern**: **Variable-Size Sliding Window (Dynamic Shrink)**
- **Concept**: Expand `right` pointer to add elements to current window sum until `sum >= target`. Then shrink `left` pointer to find the minimal valid subarray length.

---

## Observation

1. All elements in `nums` are strictly **positive integers** ($nums[i] \ge 1$).
2. Therefore:
   - Expanding `right` monotonically increases `current_sum`.
   - Shrinking `left` monotonically decreases `current_sum`.
3. Whenever `current_sum >= target`, the current window `[left ... right]` is valid. We record its length `right - left + 1`, and then try to make it even smaller by advancing `left++` until `current_sum < target`.

---

## Intuition

Think of a flexible rubber band window:
1. Stretch the right end until the window sum reaches at least `target`.
2. Once at or above `target`, record the window length, then contract the left end as much as possible while maintaining a sum $\ge \text{target}$.
3. Repeat until `right` reaches the end of the array.

---

## Algorithm

1. `left = 0`, `current_sum = 0`, `min_len = INF`.
2. Loop `right` from `0` to `n - 1`:
   a. `current_sum += nums[right]`.
   b. `while (current_sum >= target)`:
      - `min_len = min(min_len, right - left + 1)`
      - `current_sum -= nums[left++]`
3. Return `min_len == INF ? 0 : min_len`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int minSubArrayLen(int target, const std::vector<int>& nums) {
        int left = 0;
        long long current_sum = 0;
        int min_len = 1e9;
        int n = nums.size();
        
        for (int right = 0; right < n; ++right) {
            current_sum += nums[right];
            
            while (current_sum >= target) {
                min_len = std::min(min_len, right - left + 1);
                current_sum -= nums[left++];
            }
        }
        
        return min_len == 1e9 ? 0 : min_len;
    }
};
```

---

## Dry Run

### Input
- `target = 7`, `nums = [2, 3, 1, 2, 4, 3]`

### Execution Trace

| `right` | `nums[right]` | `current_sum` | Condition (`sum >= 7`) | `left` | Window Length | `min_len` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | `2` | `2` | No (`2 < 7`) | `0` | - | `INF` |
| 1 | `3` | `5` | No (`5 < 7`) | `0` | - | `INF` |
| 2 | `1` | `6` | No (`6 < 7`) | `0` | - | `INF` |
| 3 | `2` | `8` | **Yes** (`8 >= 7`) | `0` | `3 - 0 + 1 = 4` | `4` |
| - | Shrink `l=1` | `8 - 2 = 6` | No (`6 < 7`) | `1` | - | `4` |
| 4 | `4` | `6 + 4 = 10` | **Yes** (`10 >= 7`) | `1` | `4 - 1 + 1 = 4` | `4` |
| - | Shrink `l=2` | `10 - 3 = 7` | **Yes** (`7 >= 7`) | `2` | `4 - 2 + 1 = 3` | `3` |
| - | Shrink `l=3` | `7 - 1 = 6` | No (`6 < 7`) | `3` | - | `3` |
| 5 | `3` | `6 + 3 = 9` | **Yes** (`9 >= 7`) | `3` | `5 - 3 + 1 = 3` | `3` |
| - | Shrink `l=4` | `9 - 2 = 7` | **Yes** (`7 >= 7`) | `4` | `5 - 4 + 1 = 2` | **`2`** |
| - | Shrink `l=5` | `7 - 4 = 3` | No (`3 < 7`) | `5` | - | `2` |

### Result
- Output: `2` (Subarray `[4, 3]`)

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Each element is added to `current_sum` by `right` once and subtracted by `left` at most once. Both pointers move at most $N$ steps.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses constant extra space.

---

## Why This is Optimal

- Examining all elements takes $\Omega(N)$ time.
- Single-pass sliding window achieves $\mathcal{O}(N)$ linear time and $\mathcal{O}(1)$ space.

---

## Common Mistakes

1. **Returning Initial Large Value**: Returning `min_len` directly without checking if a valid subarray was found (`return min_len == INF ? 0 : min_len`).
2. **Forgetting Positive Constraint Requirement**: Assuming this sliding window approach works when negative numbers are present. (If array contains negative numbers, monotonic property breaks, requiring Prefix Sums + Monotonic Deque in $\mathcal{O}(N)$).
