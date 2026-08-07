# Subarray Sums Divisible by K

## Pattern Used

- **Pattern**: **Prefix Sum Modulo Frequency Table**
- **Concept**: By Congruence Relation:
  $$(P[j] - P[i - 1]) \pmod k = 0 \iff P[j] \pmod k = P[i - 1] \pmod k$$

---

## Observation

1. If two prefix sums $P[j]$ and $P[i - 1]$ have the **same remainder** when divided by $k$, the subarray between them `nums[i ... j]` is divisible by $k$!
2. **Handling Negative Remainders in C++**: In C++, `-2 % 5` yields `-2`. To convert negative remainders to a positive range `[0, k - 1]`, use:
   $$\text{rem} = ((\text{prefix\_sum} \pmod k) + k) \pmod k$$
3. Use a frequency array `mod_counts[k]` initialized to `0`, with `mod_counts[0] = 1` as base case.

---

## Intuition

1. Maintain running `prefix_sum`.
2. Compute normalized `rem = ((prefix_sum % k) + k) % k`.
3. If this remainder has been seen `M` times previously, add `M` to `count` (since any of those previous positions forms a valid divisible subarray ending at current index).
4. Increment `mod_counts[rem]++`.

---

## Algorithm

1. Create array `mod_counts[k] = {0}`.
2. `mod_counts[0] = 1`.
3. `prefix_sum = 0`, `count = 0`.
4. Loop through each `num` in `nums`:
   a. `prefix_sum += num`.
   b. `rem = ((prefix_sum % k) + k) % k`.
   c. `count += mod_counts[rem]`.
   d. `mod_counts[rem]++`.
5. Return `count`.

---

## Clean C++17 Solution

```cpp
#include <vector>

class Solution {
public:
    int subarraysDivByK(const std::vector<int>& nums, int k) {
        std::vector<int> mod_counts(k, 0);
        mod_counts[0] = 1; // Base case for subarrays starting at index 0
        
        int prefix_sum = 0;
        int count = 0;
        
        for (int num : nums) {
            prefix_sum += num;
            
            // Normalize remainder to range [0, k - 1]
            int rem = ((prefix_sum % k) + k) % k;
            
            count += mod_counts[rem];
            mod_counts[rem]++;
        }
        
        return count;
    }
};
```

---

## Dry Run

### Input
- `nums = [4, 5, 0, -2, -3, 1]`, `k = 5`

### Execution Trace

| `num` | `prefix_sum` | `rem = ((p_sum % 5) + 5) % 5` | `count += mod_counts[rem]` | `mod_counts` State |
| :--- | :--- | :--- | :--- | :--- |
| Start| `0` | - | - | `[1, 0, 0, 0, 0]` |
| `4` | `4` | `4` | `count += 0` | `[1, 0, 0, 0, 1]` |
| `5` | `9` | `4` | `count += 1 = 1` | `[1, 0, 0, 0, 2]` |
| `0` | `9` | `4` | `count += 2 = 3` | `[1, 0, 0, 0, 3]` |
| `-2` | `7` | `2` | `count += 0` | `[1, 0, 2, 0, 3]` |
| `-3` | `4` | `4` | `count += 3 = 6` | `[1, 0, 2, 0, 4]` |
| `1` | `5` | `0` | `count += 1 = 7` | `[2, 0, 2, 0, 4]` |

### Result
- Output: `7`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass through $N$ elements. Vector array access takes $\mathcal{O}(1)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(K)$
  - Vector of size $K$ to hold remainder frequencies.

---

## Why This is Optimal

- Solves remainder matching in a single pass ($\Omega(N)$ lower bound).
- Uses $\mathcal{O}(K)$ auxiliary space.

---

## Common Mistakes

1. **Negative Remainder Bug**: Using `prefix_sum % k` directly without normalizing `((rem % k) + k) % k`. In C++, negative numbers produce negative remainders.
2. **Missing `mod_counts[0] = 1` Base Case**: Missing `0: 1` causes subarrays starting from index 0 whose sum is divisible by $k$ to be missed!
