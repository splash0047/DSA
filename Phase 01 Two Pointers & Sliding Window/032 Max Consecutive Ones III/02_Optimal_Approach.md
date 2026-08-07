# Max Consecutive Ones III

## Pattern Used

- **Pattern**: **Variable-Size Sliding Window (Zero Counter)**
- **Concept**: Maintain a window `[left ... right]` and track `zero_count` (the count of `0`s inside the current window). Window remains valid as long as `zero_count <= k`.

---

## Observation

1. Flipping at most $k$ zeroes to 1s is equivalent to finding the longest subarray containing at most $k$ zeroes.
2. Expand `right` pointer: if `nums[right] == 0`, increment `zero_count++`.
3. If `zero_count > k`: the window is invalid. Shrink `left` pointer: if `nums[left] == 0`, decrement `zero_count--`. Advance `left++`.
4. Update `max_len = max(max_len, right - left + 1)`.

---

## Intuition

Expand `right` to stretch your window. Keep track of how many 0s are inside. When the 0 count exceeds your budget of $k$, advance `left` to shrink the window until 0 count returns to $\le k$.

---

## Algorithm

1. `left = 0`, `zero_count = 0`, `max_len = 0`.
2. Loop `right` from `0` to `n - 1`:
   a. If `nums[right] == 0`: `zero_count++`.
   b. `while (zero_count > k)`:
      - If `nums[left] == 0`: `zero_count--`.
      - `left++`.
   c. `max_len = max(max_len, right - left + 1)`.
3. Return `max_len`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int longestOnes(const std::vector<int>& nums, int k) {
        int left = 0;
        int zero_count = 0;
        int max_len = 0;
        int n = nums.size();
        
        for (int right = 0; right < n; ++right) {
            if (nums[right] == 0) {
                zero_count++;
            }
            
            while (zero_count > k) {
                if (nums[left] == 0) {
                    zero_count--;
                }
                left++;
            }
            
            max_len = std::max(max_len, right - left + 1);
        }
        
        return max_len;
    }
};
```

---

## Dry Run

### Input
- `nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]`, `k = 2`

### Execution Trace

| `right` | `nums[right]` | `zero_count` | Window Subarray | `zero_count <= 2`? | `max_len` |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `0..2` | `1, 1, 1` | `0` | `[1, 1, 1]` | Yes | 3 |
| `3` | `0` | `1` | `[1, 1, 1, 0]` | Yes | 4 |
| `4` | `0` | `2` | `[1, 1, 1, 0, 0]` | Yes | 5 |
| `5` | `0` | `3` ($> 2$) | Shrink `left` past 1st zero $\rightarrow$ `l=4` (`zero_count=2`) | Yes | 5 |
| `6..9` | `1, 1, 1, 1` | `2` | `[0, 0, 1, 1, 1, 1]` | **Yes** | **6** |
| `10` | `0` | `3` ($> 2$) | Shrink `left` past 2nd zero $\rightarrow$ `l=5` (`zero_count=2`) | Yes | 6 |

### Result
- Output: `6`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass through $N$ elements. `right` and `left` pointers advance at most $N$ times.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses constant extra space (`left`, `zero_count`, `max_len`).

---

## Why This is Optimal

- Inspects each element in `nums` once ($\Omega(N)$ lower bound).
- Operates in $\mathcal{O}(1)$ space.

---

## Common Mistakes

1. **Thinking 0s Need to be Flipped in Array**: Modifying the array memory directly. (No actual flipping is needed; just count 0s in the window!).
2. **Incorrect Shrink Condition**: Decrementing `zero_count` unconditionally without checking `if (nums[left] == 0)`.
