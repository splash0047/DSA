# Find the Smallest Divisor Given a Threshold

## Pattern Used

- **Pattern**: **Binary Search on Answer Space (Monotonic Divisor Function)**
- **Concept**: Search for the minimum divisor $d \in [1, \max(\text{nums})]$. The predicate function `computeSum(d)` calculates $\sum \lceil \text{nums}[i] / d \rceil$ and verifies if it is $\le \text{threshold}$.

---

## Observation

1. Monotonic Property:
   - As divisor $d$ **increases**, the division sum $\sum \lceil \text{nums}[i] / d \rceil$ **decreases or stays the same**.
   - If divisor $d$ achieves a sum $\le \text{threshold}$, any larger divisor $> d$ will ALSO achieve a sum $\le \text{threshold}$.
2. Search Space Boundaries:
   - Minimum possible divisor: `low = 1`.
   - Maximum possible divisor: `high = max(nums)`.
3. Integer Ceiling Formula:
   $$\lceil x / d \rceil = (x + d - 1) / d$$

---

## Intuition

Set search space `low = 1` and `high = max(nums)`. Test midpoint divisor `mid`:
- If `computeSum(mid) <= threshold`: `mid` is a valid candidate. Record `ans = mid` and contract `high = mid - 1` to search for a smaller valid divisor.
- If `computeSum(mid) > threshold`: `mid` divisor is too small (sum is too big). Increase divisor `low = mid + 1`.

---

## Algorithm

1. `low = 1`, `high = max(nums)`, `ans = high`.
2. While `low <= high`:
   a. `mid = low + (high - low) / 2`.
   b. `current_sum = 0`.
   c. For each `x` in `nums`:
      - `current_sum += (x + mid - 1) / mid`.
   d. If `current_sum <= threshold`:
      - `ans = mid`.
      - `high = mid - 1`.
   e. Else:
      - `low = mid + 1`.
3. Return `ans`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>

class Solution {
private:
    bool isValid(const std::vector<int>& nums, int threshold, int divisor) {
        long long current_sum = 0;
        for (int x : nums) {
            current_sum += (x + divisor - 1) / divisor;
        }
        return current_sum <= threshold;
    }
public:
    int smallestDivisor(const std::vector<int>& nums, int threshold) {
        int low = 1;
        int high = *std::max_element(nums.begin(), nums.end());
        int ans = high;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (isValid(nums, threshold, mid)) {
                ans = mid;
                high = mid - 1; // Try to find a smaller divisor
            } else {
                low = mid + 1;  // Divisor too small, increase divisor
            }
        }
        
        return ans;
    }
};
```

---

## Dry Run

### Input
- `nums = [1, 2, 5, 9]`, `threshold = 6`
- `low = 1`, `high = 9`

### Execution Trace

| Step | `low` | `high` | `mid` (Divisor) | Division Sum Calculation | `sum <= 6`? | `ans` | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `1` | `9` | `5` | $\lceil 1/5 \rceil + \lceil 2/5 \rceil + \lceil 5/5 \rceil + \lceil 9/5 \rceil = 1+1+1+2 = 5$ | `5 <= 6` (**Yes**) | `5` | `high = mid - 1 = 4` |
| 2 | `1` | `4` | `2` | $\lceil 1/2 \rceil + \lceil 2/2 \rceil + \lceil 5/2 \rceil + \lceil 9/2 \rceil = 1+1+3+5 = 10$ | `10 <= 6` (No) | `5` | `low = mid + 1 = 3` |
| 3 | `3` | `4` | `3` | $\lceil 1/3 \rceil + \lceil 2/3 \rceil + \lceil 5/3 \rceil + \lceil 9/3 \rceil = 1+1+2+3 = 7$ | `7 <= 6` (No) | `5` | `low = mid + 1 = 4` |
| 4 | `4` | `4` | `4` | $\lceil 1/4 \rceil + \lceil 2/4 \rceil + \lceil 5/4 \rceil + \lceil 9/4 \rceil = 1+1+2+3 = 7$ | `7 <= 6` (No) | `5` | `low = mid + 1 = 5` |
| End | `5` | `4` | - | - | - | `low > high` (Stop) | **Return `5`** |

### Result
- Output: `5`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log(\max(\text{nums})))$
  - Binary search takes $\mathcal{O}(\log(\max(\text{nums})))$ steps; sum evaluation takes $\mathcal{O}(N)$ per step.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This is Optimal

- Solves smallest divisor search in optimal $\mathcal{O}(N \log M)$ time.
- Uses zero extra memory.

---

## Common Mistakes

1. **Integer Overflow in Sum**: Accumulating `current_sum` using standard 32-bit `int` instead of `long long`.
2. **Incorrect Ceiling Math**: Writing `x / divisor` instead of `(x + divisor - 1) / divisor`. Standard integer division truncates downwards!
