# Maximum Size Subarray Sum Equals k

## Pattern Used

- **Pattern**: **Prefix Sum + Earliest Index Hash Map**
- **Concept**: If running prefix sum at index `j` is $P[j]$, we search for an earlier prefix sum $P[i] = P[j] - k$. The length of the valid subarray is $j - i$.

---

## Observation

1. To **maximize** the length $j - i$, we must minimize the start index $i$.
2. Therefore, when recording prefix sums in our map `first_seen`, we **only insert a prefix sum if it does not already exist in the map**.
3. *Base Case*: Seed `first_seen[0] = -1` to handle valid subarrays starting from index `0`.

---

## Intuition

1. Maintain running `prefix_sum = 0`.
2. Map `first_seen` stores `{prefix_sum : earliest_index}`.
3. At index `i`:
   - `prefix_sum += nums[i]`.
   - If `prefix_sum - k` is in `first_seen`:
     - Update `max_len = max(max_len, i - first_seen[prefix_sum - k])`.
   - If `prefix_sum` is NOT in `first_seen`:
     - Store `first_seen[prefix_sum] = i`.

---

## Algorithm

1. `std::unordered_map<long long, int> first_seen;`
2. `first_seen[0] = -1;`
3. `prefix_sum = 0`, `max_len = 0`.
4. Loop `i` from `0` to `n - 1`:
   a. `prefix_sum += nums[i]`.
   b. `if (first_seen.count(prefix_sum - k))`:
      - `max_len = max(max_len, i - first_seen[prefix_sum - k])`.
   c. `if (!first_seen.count(prefix_sum))`:
      - `first_seen[prefix_sum] = i`.
5. Return `max_len`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    int maxSubArrayLen(std::vector<int>& nums, int k) {
        std::unordered_map<long long, int> first;

        first[0] = -1;

        long long sum = 0;
        int maxLen = 0;

        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];

            if (first.find(sum - k) != first.end()) {
                maxLen = std::max(maxLen, i - first[sum - k]);
            }

            if (first.find(sum) == first.end()) {
                first[sum] = i;
            }
        }

        return maxLen;
    }
};
```

---

## Dry Run

### Input
- `nums = [1, -1, 5, -2, 3]`, `k = 3`

### Execution Trace

| `i` | `nums[i]` | `prefix_sum` | `target = p_sum - k` | `first_seen` Map State | Match Found? | Subarray Length | `max_len` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Init | - | `0` | - | `{0: -1}` | - | - | `0` |
| 0 | `1` | `1` | `1 - 3 = -2` | `{0: -1, 1: 0}` | No | - | `0` |
| 1 | `-1` | `0` | `0 - 3 = -3` | `{0: -1, 1: 0}` | No (0 already present!) | - | `0` |
| 2 | `5` | `5` | `5 - 3 = 2` | `{0: -1, 1: 0, 5: 2}` | No | - | `0` |
| 3 | `-2` | `3` | `3 - 3 = 0` | `{0: -1, 1: 0, 5: 2, 3: 3}` | Found `0` at `-1` | `3 - (-1) = 4` | **`4`** |
| 4 | `3` | `6` | `6 - 3 = 3` | `{0: -1, 1: 0, 5: 2, 3: 3, 6: 4}` | Found `3` at `3` | `4 - 3 = 1` | `4` |

### Result
- Output: `4` (Subarray `[1, -1, 5, -2]`)

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass over $N$ elements. Map operations take average $\mathcal{O}(1)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Hash map stores up to $N + 1$ distinct prefix sum values.

---

## Why This is Optimal

- Solves maximum length subarray sum search in a single pass ($\Omega(N)$ lower bound).
- Handles positive, negative, and zero values seamlessly.

---

## Common Mistakes

1. **Overwriting Earliest Index**: Writing `first_seen[prefix_sum] = i` without checking if it already exists! Overwriting increases the start index $i$, shrinking the resulting window length.
2. **Missing `first_seen[0] = -1`**: Forgetting base case causes maximum length subarrays starting at index 0 to be computed with incorrect lengths.
