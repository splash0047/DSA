# Maximum Average Subarray I

## Pattern Used

- **Pattern**: **Fixed-Size Sliding Window**
- **Concept**: Maintain a running sum of a window of fixed size $k$. As the window slides 1 position right, add the incoming element `nums[i]` and subtract the outgoing element `nums[i - k]`.

---

## Observation

1. To maximize average $\frac{\text{sum}}{k}$, we simply need to maximize the window sum $\text{sum}$.
2. Sum of window starting at index $i+1$:
$$\text{Sum}_{i+1} = \text{Sum}_i + \text{nums}[i + k] - \text{nums}[i]$$
3. This allows calculating the next window's sum in constant $\mathcal{O}(1)$ time instead of $\mathcal{O}(K)$ time.

---

## Intuition

1. Calculate sum of first $k$ elements (`nums[0 ... k-1]`). Initialize `max_sum = current_sum`.
2. Slide the window from index `k` to `n - 1`:
   - Add `nums[i]` (incoming element).
   - Subtract `nums[i - k]` (outgoing element).
   - Update `max_sum = max(max_sum, current_sum)`.
3. Return `(double)max_sum / k`.

---

## Algorithm

1. `current_sum = 0`.
2. Loop `i` from `0` to `k - 1`: `current_sum += nums[i]`.
3. `max_sum = current_sum`.
4. Loop `i` from `k` to `n - 1`:
   a. `current_sum += nums[i] - nums[i - k]`.
   b. `max_sum = max(max_sum, current_sum)`.
5. Return `(double)max_sum / k`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    double findMaxAverage(const std::vector<int>& nums, int k) {
        double current_sum = 0;
        
        // Step 1: Compute sum of first window of size k
        for (int i = 0; i < k; ++i) {
            current_sum += nums[i];
        }
        
        double max_sum = current_sum;
        int n = nums.size();
        
        // Step 2: Slide window across remaining array
        for (int i = k; i < n; ++i) {
            current_sum += nums[i] - nums[i - k];
            max_sum = std::max(max_sum, current_sum);
        }
        
        return max_sum / k;
    }
};
```

---

## Dry Run

### Input
- `nums = [1, 12, -5, -6, 50, 3]`, `k = 4`

### Execution Trace

| Window Range | Incoming `nums[i]` | Outgoing `nums[i-k]` | `current_sum` | `max_sum` | Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[0 ... 3]` | - | - | `1 + 12 - 5 - 6 = 2` | `2` | Initial Window sum |
| `[1 ... 4]` | `nums[4] = 50` | `nums[0] = 1` | `2 + 50 - 1 = 51` | `51` | Update `max_sum = 51` |
| `[2 ... 5]` | `nums[5] = 3` | `nums[1] = 12` | `51 + 3 - 12 = 42` | `51` | No change (`42 < 51`) |

### Result
- `max_sum / k = 51 / 4.0 = 12.75`
- Output: `12.75`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass through $N$ elements. Each element added and subtracted once.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space used.

---

## Why This is Optimal

- Inspects every array element once ($\Omega(N)$ time lower bound).
- Uses $\mathcal{O}(1)$ extra space.

---

## Common Mistakes

1. **Integer Division**: Returning `max_sum / k` with integer types, causing truncation. Use `double` for sum or cast before division.
2. **Initializing `max_sum` to `0`**: If array contains negative numbers (e.g. `[-5]`), initializing `max_sum = 0` produces incorrect results. Initialize `max_sum` to sum of first window.
