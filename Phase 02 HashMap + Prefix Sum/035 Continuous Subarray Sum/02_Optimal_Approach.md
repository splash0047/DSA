# Continuous Subarray Sum

## Pattern Used

- **Pattern**: **Prefix Sum Modulo Hash Map (Earliest Index Tracking)**
- **Concept**: Maintain a hash map `remainder_map` storing `{remainder: earliest_index}`. If a remainder appears at index `i` and was previously recorded at `prev_index`, the subarray `nums[prev_index + 1 ... i]` has a sum divisible by `k`.

---

## Observation

1. If $P[i] \pmod k = P[j] \pmod k$, then $(P[i] - P[j]) \pmod k = 0$.
2. To satisfy the length constraint (length $\ge 2$), the index difference must be:
   $$i - \text{prev\_index} \ge 2$$
3. Therefore, we store only the **earliest index** where a remainder first appears in the array (do NOT update the map if the remainder is already present).
4. *Base Case Initialization*: Initialize `remainder_map[0] = -1`. This allows a valid subarray starting at index `0` of length $i - (-1) = i + 1 \ge 2$ to be correctly validated.

---

## Intuition

1. `prefix_sum = 0`.
2. Seed `remainder_map[0] = -1`.
3. Loop through `i` from `0` to `n - 1`:
   - `prefix_sum += nums[i]`.
   - `rem = prefix_sum % k`.
   - If `rem` exists in `remainder_map`:
     - If `i - remainder_map[rem] >= 2`, return `true`!
   - Else:
     - Record `remainder_map[rem] = i`.
4. Return `false`.

---

## Algorithm

1. `std::unordered_map<int, int> remainder_map;`
2. `remainder_map[0] = -1;`
3. `prefix_sum = 0`.
4. Loop `i` from `0` to `nums.size() - 1`:
   a. `prefix_sum += nums[i]`.
   b. `rem = prefix_sum % k`.
   c. If `remainder_map.find(rem) != remainder_map.end()`:
      - If `i - remainder_map[rem] >= 2`: return `true`.
   d. Else:
      - `remainder_map[rem] = i`.
5. Return `false`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <unordered_map>

class Solution {
public:
    bool checkSubarraySum(const std::vector<int>& nums, int k) {
        std::unordered_map<int, int> remainder_map;
        remainder_map[0] = -1; // Base case: remainder 0 at index -1
        
        long long prefix_sum = 0;
        int n = nums.size();
        
        for (int i = 0; i < n; ++i) {
            prefix_sum += nums[i];
            int rem = prefix_sum % k;
            
            if (remainder_map.find(rem) != remainder_map.end()) {
                if (i - remainder_map[rem] >= 2) {
                    return true;
                }
            } else {
                remainder_map[rem] = i; // Store only earliest occurrence
            }
        }
        
        return false;
    }
};
```

---

## Dry Run

### Input
- `nums = [23, 2, 4, 6, 7]`, `k = 6`

### Execution Trace

| `i` | `nums[i]` | `prefix_sum` | `rem = prefix_sum % 6` | `remainder_map` State | Match Check | Result |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Init | - | `0` | - | `{0: -1}` | - | - |
| 0 | `23` | `23` | `5` | `{0: -1, 5: 0}` | New rem | `false` |
| 1 | `2` | `25` | `1` | `{0: -1, 5: 0, 1: 1}` | New rem | `false` |
| 2 | `4` | `29` | `5` | `{0: -1, 5: 0, 1: 1}` | Found `5` at index `0` | `2 - 0 = 2 >= 2` $\rightarrow$ **`true`** |

### Result
- Output: `true` (Subarray `[2, 4]` sums to 6)

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass over $N$ elements. Map operations take average $\mathcal{O}(1)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(\min(N, K))$
  - Map stores at most $\min(N, K)$ distinct remainders.

---

## Why This is Optimal

- Inspects each element in `nums` once ($\Omega(N)$ lower bound).
- Uses $\mathcal{O}(\min(N, K))$ auxiliary space.

---

## Common Mistakes

1. **Overwriting Earliest Index**: Writing `remainder_map[rem] = i` even when `rem` already exists in the map! Overwriting reduces the index distance $i - \text{prev\_index}$, causing valid subarrays of length $\ge 2$ to be missed.
2. **Missing `remainder_map[0] = -1` Base Case**: Missing `0: -1` fails to detect valid subarrays starting from index 0 (e.g. `nums = [23, 2, 4]`, `k = 6` where prefix sum 29 has remainder 5).
