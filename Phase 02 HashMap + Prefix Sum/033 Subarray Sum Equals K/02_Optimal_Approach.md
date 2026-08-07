# Subarray Sum Equals K

## Pattern Used

- **Pattern**: **Prefix Sum + Hash Map Frequency Counting**
- **Concept**: Let $P[j]$ be the prefix sum up to index $j$. The sum of a subarray `nums[i ... j]` is $P[j] - P[i - 1]$.
  $$\text{SubarraySum}(i, j) = k \iff P[j] - P[i - 1] = k \iff P[i - 1] = P[j] - k$$

---

## Observation

1. As we iterate through `nums` maintaining running `prefix_sum`, any previous prefix sum equal to `prefix_sum - k` represents a valid subarray ending at current index with sum equal to `k`.
2. A hash map `prefix_counts` stores `{prefix_sum: frequency}`.
3. *Critical Base Case*: Initialize `prefix_counts[0] = 1`. This accounts for valid subarrays starting at index `0` whose sum is exactly `k` (since `prefix_sum - k = 0`).

---

## Intuition

1. Maintain running `prefix_sum = 0`.
2. Map `prefix_counts` tracks how many times each prefix sum has appeared so far.
3. At each element `x`:
   - `prefix_sum += x`.
   - Add `prefix_counts[prefix_sum - k]` to total count.
   - Increment `prefix_counts[prefix_sum]++`.

---

## Algorithm

1. `std::unordered_map<int, int> prefix_counts;`
2. `prefix_counts[0] = 1;`
3. `prefix_sum = 0`, `count = 0`.
4. For each `x` in `nums`:
   a. `prefix_sum += x`.
   b. `if (prefix_counts.count(prefix_sum - k))`:
      - `count += prefix_counts[prefix_sum - k]`.
   c. `prefix_counts[prefix_sum]++`.
5. Return `count`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <unordered_map>

class Solution {
public:
    int subarraySum(const std::vector<int>& nums, int k) {
        std::unordered_map<int, int> prefix_counts;
        prefix_counts[0] = 1; // Base case: prefix sum of 0 appears once before array starts
        
        int prefix_sum = 0;
        int count = 0;
        
        for (int num : nums) {
            prefix_sum += num;
            
            if (prefix_counts.find(prefix_sum - k) != prefix_counts.end()) {
                count += prefix_counts[prefix_sum - k];
            }
            
            prefix_counts[prefix_sum]++;
        }
        
        return count;
    }
};
```

---

## Dry Run

### Input
- `nums = [1, 1, 1]`, `k = 2`

### Execution Trace

| Step | `num` | `prefix_sum` | `prefix_sum - k` | `prefix_counts` Map State | Map Check (`p_sum - k`) | Total `count` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Init | - | `0` | - | `{0: 1}` | - | `0` |
| 1 | `1` | `1` | `1 - 2 = -1` | `{0: 1, 1: 1}` | Not found | `0` |
| 2 | `1` | `2` | `2 - 2 = 0` | `{0: 1, 1: 1, 2: 1}` | Found `0` (freq = 1) | `0 + 1 = 1` |
| 3 | `1` | `3` | `3 - 2 = 1` | `{0: 1, 1: 1, 2: 1, 3: 1}` | Found `1` (freq = 1) | `1 + 1 = 2` |

### Result
- Output: `2`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass through $N$ elements. Hash map lookups and inserts take average $\mathcal{O}(1)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Hash map stores up to $N + 1$ distinct prefix sums.

---

## Why This is Optimal

- Solves subarray sum search in a single pass ($\Omega(N)$ lower bound).
- Handles negative, zero, and positive numbers correctly.

---

## Common Mistakes

1. **Forgetting Base Case `prefix_counts[0] = 1`**: Missing `0: 1` causes subarrays starting at index `0` with sum equal to `k` to be missed!
2. **Updating Hash Map Before Querying**: Writing `prefix_counts[prefix_sum]++` *before* checking `prefix_counts[prefix_sum - k]` can lead to erroneous self-matching when $k = 0$.
