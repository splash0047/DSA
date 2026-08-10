# Find Pivot Index

## Pattern Used

- **Pattern**: **Total Sum & Running Prefix Sum**
- **Concept**: Calculate `total_sum` of the array first. At index `i`, if `left_sum` is known, the right sum is:
$$\text{right\_sum} = \text{total\_sum} - \text{left\_sum} - \text{nums}[i]$$

---

## Observation

1. Pivot index condition:
$$\text{left\_sum} = \text{right\_sum} \iff \text{left\_sum} = \text{total\_sum} - \text{left\_sum} - \text{nums}[i]$$
$$2 \times \text{left\_sum} + \text{nums}[i] = \text{total\_sum}$$
2. By computing `total_sum` in an initial pass, we only need to maintain a single running variable `left_sum` as we scan through `nums` from left to right.
3. Return the very first index `i` that satisfies this equation to guarantee returning the **leftmost pivot index**.

---

## Intuition

1. `total_sum = sum(nums)`.
2. `left_sum = 0`.
3. Loop `i` from `0` to `n - 1`:
   - If `left_sum == total_sum - left_sum - nums[i]`, return `i`.
   - `left_sum += nums[i]`.
4. Return `-1`.

---

## Algorithm

1. `total_sum = std::accumulate(nums.begin(), nums.end(), 0)`.
2. `left_sum = 0`.
3. Loop `i` from `0` to `nums.size() - 1`:
   a. `right_sum = total_sum - left_sum - nums[i]`.
   b. If `left_sum == right_sum`, return `i`.
   c. `left_sum += nums[i]`.
4. Return `-1`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <numeric>

class Solution {
public:
    int pivotIndex(std::vector<int>& nums) {
        int total = 0;

        for (int num : nums) {
            total += num;
        }

        int left = 0;

        for (int i = 0; i < nums.size(); i++) {
            int right = total - left - nums[i];

            if (left == right) {
                return i;
            }

            left += nums[i];
        }

        return -1;
    }
};
```

---

## Dry Run

### Input
- `nums = [1, 7, 3, 6, 5, 6]`
- `total_sum = 28`

### Execution Trace

| `i` | `nums[i]` | `left_sum` | `right_sum = 28 - left_sum - nums[i]` | `left_sum == right_sum`? | Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | `1` | `0` | `28 - 0 - 1 = 27` | `0 != 27` | `left_sum += 1` $\rightarrow$ `1` |
| 1 | `7` | `1` | `28 - 1 - 7 = 20` | `1 != 20` | `left_sum += 7` $\rightarrow$ `8` |
| 2 | `3` | `8` | `28 - 8 - 3 = 17` | `8 != 17` | `left_sum += 3` $\rightarrow$ `11` |
| 3 | `6` | `11` | `28 - 11 - 6 = 11` | **`11 == 11`** | **Return `3`** |

### Result
- Output: `3`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Pass 1: `std::accumulate` takes $N$ steps.
  - Pass 2: Single loop takes at most $N$ steps. Total: $\mathcal{O}(N)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses two integer variables (`total_sum` and `left_sum`).

---

## Why This is Optimal

- Requires reading elements to compute sums ($\Omega(N)$ time lower bound).
- Solves in two simple linear passes using constant $\mathcal{O}(1)$ space.

---

## Common Mistakes

1. **Updating `left_sum` BEFORE comparison**: Writing `left_sum += nums[i]` *before* checking `left_sum == right_sum` includes `nums[i]` in the left sum! `left_sum` must strictly exclude `nums[i]`.
2. **Not Returning Leftmost Index**: Returning rightmost pivot index instead of breaking on the first match.
