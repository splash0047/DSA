# Maximum Product Subarray

## Pattern Used

- **Pattern**: **Min & Max Product Kadane's Variant (Dynamic Programming)**
- **Concept**:
  - Unlike maximum sum subarray, a **negative number** flips a large positive product into a large negative product, AND flips a large negative product into a large positive product!
  - Therefore, at each element `nums[i]`, we MUST maintain two quantities:
    1. `curMax`: Max product ending at `nums[i]`.
    2. `curMin`: Min product ending at `nums[i]`.
  - When `nums[i]` is negative, `curMax` and `curMin` swap places!
  - State transitions at index `i`:
    - `tempMax = max({num, num * curMax, num * curMin})`
    - `curMin  = min({num, num * curMax, num * curMin})`
    - `curMax  = tempMax`
  - Track `result = max(result, curMax)`.

---

## Observation

1. Multiplying by a negative number swaps the maximum product and minimum product.
2. If `nums[i] < 0`, we can simply `swap(curMax, curMin)` before calculating the new products!

---

## Intuition

Think of negative numbers as sign flippers. A very negative number is a "dormant bomb" that could become the largest positive number if multiplied by another negative number! By tracking both the largest positive product AND the smallest negative product at each step, you're always prepared for sign flips.

---

## Algorithm

1. `curMax = nums[0]`, `curMin = nums[0]`, `ans = nums[0]`.
2. Loop `i` from `1` to `n - 1`:
   - `num = nums[i]`.
   - If `num < 0`, `swap(curMax, curMin)`.
   - `curMax = max(num, curMax * num)`.
   - `curMin = min(num, curMin * num)`.
   - `ans = max(ans, curMax)`.
3. Return `ans`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int maxProduct(std::vector<int>& nums) {
        if (nums.empty()) return 0;
        
        int curMax = nums[0];
        int curMin = nums[0];
        int ans = nums[0];
        
        for (int i = 1; i < nums.size(); ++i) {
            int num = nums[i];
            
            // Negative number flips min and max products
            if (num < 0) {
                std::swap(curMax, curMin);
            }
            
            curMax = std::max(num, curMax * num);
            curMin = std::min(num, curMin * num);
            
            ans = std::max(ans, curMax);
        }
        
        return ans;
    }
};
```

---

## Dry Run

### Input
- `nums = [2, 3, -2, 4]`

### Execution Trace

- Init: `curMax = 2`, `curMin = 2`, `ans = 2`.
- `i = 1 (num = 3)`:
  - `curMax = max(3, 2 * 3) = 6`.
  - `curMin = min(3, 2 * 3) = 3`.
  - `ans = max(2, 6) = 6`.
- `i = 2 (num = -2)`:
  - `num < 0` $\implies$ swap `curMax` (6) and `curMin` (3) $\implies$ `curMax = 3, curMin = 6`.
  - `curMax = max(-2, 3 * -2) = -2`.
  - `curMin = min(-2, 6 * -2) = -12`.
  - `ans = max(6, -2) = 6`.
- `i = 3 (num = 4)`:
  - `curMax = max(4, -2 * 4) = 4`.
  - `curMin = min(4, -12 * 4) = -48`.
  - `ans = max(6, 4) = 6`.

### Result
- Output: `6`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass through `nums` vector of size $N$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses constant extra space (`curMax`, `curMin`, `ans`).

---

## Why This is Optimal

- Computes maximum product subarray in linear $\mathcal{O}(N)$ time.
- Uses $\mathcal{O}(1)$ auxiliary space by tracking only current max and min product variables.

---

## Common Mistakes

1. **Only Tracking Max Product**: Failing to track `curMin`, which misses large positive products resulting from multiplying two negative numbers (e.g. `[-2, 3, -4]`).
2. **Forgetting Swap on Negative Numbers**: Not swapping `curMax` and `curMin` when `num < 0` before updating states.
