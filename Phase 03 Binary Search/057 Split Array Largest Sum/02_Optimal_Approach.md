# Split Array Largest Sum

## Pattern Used

- **Pattern**: **Binary Search on Answer Space (Minimax Partitioning)**
- **Concept**: Search for the minimum possible "maximum subarray sum" $S \in [\max(\text{nums}), \sum \text{nums}]$. The predicate function `canSplit(S, k)` checks if the array can be partitioned into $\le k$ contiguous subarrays where no subarray sum exceeds $S$.

---

## Observation

1. Search Space Boundaries:
   - Minimum possible largest sum: `low = max(nums)` (a subarray must contain at least 1 element, so max sum cannot be smaller than the largest element).
   - Maximum possible largest sum: `high = sum(nums)` (when $k = 1$, the single subarray contains all elements).
2. Monotonicity:
   - If maximum sum limit $S$ allows partitioning `nums` into $\le k$ subarrays, any larger sum limit $> S$ will ALSO be valid.
   - If maximum sum limit $S$ requires $> k$ subarrays, $S$ is too small.

---

## Intuition

1. Set `low = max(nums)` and `high = sum(nums)`.
2. Test midpoint limit `mid`:
   - Simulate greedy partition: accumulate elements into current subarray. When adding `nums[i]` exceeds `mid`, start a new subarray.
   - Count total required subarrays `count`.
   - If `count <= k`: `mid` is a valid sum limit candidate. Record `ans = mid` and contract `high = mid - 1`.
   - If `count > k`: `mid` limit is too restrictive. Increase limit `low = mid + 1`.

---

## Algorithm

1. `low = max(nums)`, `high = sum(nums)`, `ans = high`.
2. While `low <= high`:
   a. `mid = low + (high - low) / 2`.
   b. `count = 1`, `current_sum = 0`.
   c. For each `x` in `nums`:
      - If `current_sum + x > mid`:
        - `count++`.
        - `current_sum = x`.
      - Else: `current_sum += x`.
   d. If `count <= k`:
      - `ans = mid`.
      - `high = mid - 1`.
   e. Else:
      - `low = mid + 1`.
3. Return `ans`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <numeric>
#include <algorithm>

class Solution {
private:
    bool canSplit(const std::vector<int>& nums, int k, long long max_sum_limit) {
        int count = 1;
        long long current_sum = 0;
        
        for (int x : nums) {
            if (current_sum + x > max_sum_limit) {
                count++;
                current_sum = x;
            } else {
                current_sum += x;
            }
        }
        
        return count <= k;
    }
public:
    int splitArray(const std::vector<int>& nums, int k) {
        long long low = *std::max_element(nums.begin(), nums.end());
        long long high = std::accumulate(nums.begin(), nums.end(), 0LL);
        long long ans = high;
        
        while (low <= high) {
            long long mid = low + (high - low) / 2;
            
            if (canSplit(nums, k, mid)) {
                ans = mid;
                high = mid - 1; // Try to find a smaller maximum sum
            } else {
                low = mid + 1;  // Sum limit too small, increase limit
            }
        }
        
        return static_cast<int>(ans);
    }
};
```

---

## Dry Run

### Input
- `nums = [7, 2, 5, 10, 8]`, `k = 2`
- `low = 10` ($\max$), `high = 32` ($\sum$)

### Execution Trace

| Step | `low` | `high` | `mid` (Sum Limit) | Partitioning Subarrays | Subarrays Required | `count <= 2`? | `ans` | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `10` | `32` | `21` | `[7,2,5] (14)`, `[10,8] (18)` | 2 | `2 <= 2` (**Yes**) | `21` | `high = mid - 1 = 20` |
| 2 | `10` | `20` | `15` | `[7,2,5] (14)`, `[10] (10)`, `[8] (8)` | 3 | `3 <= 2` (No) | `21` | `low = mid + 1 = 16` |
| 3 | `16` | `20` | `18` | `[7,2,5] (14)`, `[10,8] (18)` | 2 | `2 <= 2` (**Yes**) | **`18`** | `high = mid - 1 = 17` |
| 4 | `16` | `17` | `16` | `[7,2,5] (14)`, `[10] (10)`, `[8] (8)` | 3 | `3 <= 2` (No) | `18` | `low = mid + 1 = 17` |
| 5 | `17` | `17` | `17` | `[7,2,5] (14)`, `[10] (10)`, `[8] (8)` | 3 | `3 <= 2` (No) | `18` | `low = mid + 1 = 18` |
| End | `18` | `17` | - | - | - | - | `low > high` (Stop) | Return `18` |

### Result
- Output: `18` (Partition: `[7,2,5]` sum 14, `[10,8]` sum 18)

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log(\sum \text{nums}))$
  - Binary search over range $[\max, \sum]$ takes $\mathcal{O}(\log(\sum \text{nums}))$ steps; simulation takes $\mathcal{O}(N)$ per step.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This is Optimal

- Reduces Hard DP problem from $\mathcal{O}(N^2 K)$ to $\mathcal{O}(N \log(\sum \text{nums}))$ time.
- Uses zero extra memory.

---

## Common Mistakes

1. **Confusing Subarray with Subsequence**: Partitioning must preserve contiguous subarrays (`[7,2,5]` and `[10,8]`).
2. **Incorrect `low` Bound**: Setting `low = 0` instead of `max(nums)`. If limit is smaller than `max(nums)`, a single element cannot fit into any subarray.
