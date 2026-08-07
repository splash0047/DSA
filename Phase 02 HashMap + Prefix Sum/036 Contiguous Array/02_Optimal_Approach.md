# Contiguous Array

## Pattern Used

- **Pattern**: **Prefix Sum Transformation + Earliest Index Hash Map**
- **Concept**: Convert every `0` into `-1` (conceptually). An equal number of `0`s and `1`s means the sum of elements in that subarray is exactly `0`!

---

## Observation

1. If we add `+1` for `1` and `-1` for `0`, the running sum at index `i` is `prefix_sum`.
2. If `prefix_sum` at index `j` is equal to `prefix_sum` at index `i`, then the net sum of elements between `i + 1` and `j` is $0$ (equal number of `0`s and `1`s).
3. To maximize subarray length `j - i`, we store only the **earliest index** where each `prefix_sum` first appears.
4. *Base Case*: Initialize `first_seen[0] = -1`.

---

## Intuition

1. Maintain running `prefix_sum` (increment for `1`, decrement for `0`).
2. Map `first_seen` records `{prefix_sum : earliest_index}`.
3. At index `i`:
   - If `prefix_sum` is already in `first_seen`:
     - Calculate length `i - first_seen[prefix_sum]`.
     - Update `max_len = max(max_len, length)`.
   - Else:
     - Record `first_seen[prefix_sum] = i`.

---

## Algorithm

1. `std::unordered_map<int, int> first_seen;`
2. `first_seen[0] = -1;`
3. `prefix_sum = 0`, `max_len = 0`.
4. Loop `i` from `0` to `nums.size() - 1`:
   a. `prefix_sum += (nums[i] == 1 ? 1 : -1)`.
   b. If `first_seen.find(prefix_sum) != first_seen.end()`:
      - `max_len = max(max_len, i - first_seen[prefix_sum])`.
   c. Else:
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
    int findMaxLength(const std::vector<int>& nums) {
        std::unordered_map<int, int> first_seen;
        first_seen[0] = -1; // Base case: cumulative sum of 0 occurs at index -1
        
        int prefix_sum = 0;
        int max_len = 0;
        int n = nums.size();
        
        for (int i = 0; i < n; ++i) {
            prefix_sum += (nums[i] == 1 ? 1 : -1);
            
            if (first_seen.find(prefix_sum) != first_seen.end()) {
                max_len = std::max(max_len, i - first_seen[prefix_sum]);
            } else {
                first_seen[prefix_sum] = i; // Store only earliest occurrence
            }
        }
        
        return max_len;
    }
};
```

---

## Dry Run

### Input
- `nums = [0, 1, 0]`

### Execution Trace

| `i` | `nums[i]` | Value (`1/-1`) | `prefix_sum` | `first_seen` Map State | Match Found? | Window Length | `max_len` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Init | - | - | `0` | `{0: -1}` | - | - | `0` |
| 0 | `0` | `-1` | `-1` | `{0: -1, -1: 0}` | No | - | `0` |
| 1 | `1` | `+1` | `0` | `{0: -1, -1: 0}` | Found `0` at `-1` | `1 - (-1) = 2` | **`2`** |
| 2 | `0` | `-1` | `-1` | `{0: -1, -1: 0}` | Found `-1` at `0` | `2 - 0 = 2` | `2` |

### Result
- Output: `2` (Subarray `[0, 1]`)

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass through $N$ elements. Map operations take average $\mathcal{O}(1)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Map stores at most $2N + 1$ distinct prefix sum values.

---

## Why This is Optimal

- Solves continuous equal frequency search in a single pass ($\Omega(N)$ lower bound).
- Optimal $\mathcal{O}(N)$ space.

---

## Common Mistakes

1. **Overwriting Earliest Index**: Updating `first_seen[prefix_sum] = i` when `prefix_sum` already exists in map! Overwriting decreases subarray length $i - \text{first\_seen}[p\_sum]$.
2. **Missing `first_seen[0] = -1`**: Forgetting base case causes sub-arrays starting at index 0 (e.g. `[0, 1]`) to be computed incorrectly.
