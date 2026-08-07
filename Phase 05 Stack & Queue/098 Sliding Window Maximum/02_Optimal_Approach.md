# Sliding Window Maximum

## Pattern Used

- **Pattern**: **Monotonic Decreasing Deque (Double-Ended Queue)**
- **Concept**: Maintain a double-ended queue `std::deque<int> dq` storing indices in **monotonically decreasing order** of their corresponding values (`nums[dq.front()]` is always the maximum element of the current window!).
  - As index `i` moves from `0` to `n - 1`:
    1. **Evict Out-of-Bound Indices**: If `dq.front() <= i - k`, pop from front (`dq.pop_front()`).
    2. **Maintain Monotonic Decreasing Order**: While `!dq.empty()` and `nums[i] >= nums[dq.back()]`, pop smaller elements from back (`dq.pop_back()`).
    3. Push current index `i` to back (`dq.push_back(i)`).
    4. **Record Result**: When `i >= k - 1`, record `ans.push_back(nums[dq.front()])`.

---

## Observation

1. Any element `nums[j]` smaller than current element `nums[i]` (where $j < i$) will NEVER be the maximum in any future window, because `nums[i]` is both LARGER and LATER!
2. Thus, smaller elements at the back of `dq` can be discarded immediately.
3. The front of `dq` (`dq.front()`) will ALWAYS hold the index of the maximum element for the current window!

---

## Intuition

Keep candidates for window maximum ordered in a deque. Pop expired out-of-window indices from the front, and pop dominated smaller values from the back before pushing the current index.

---

## Algorithm

1. `n = nums.size()`, `std::deque<int> dq`, `std::vector<int> ans`.
2. Loop `i` from `0` to `n - 1`:
   a. If `!dq.empty()` and `dq.front() == i - k`: `dq.pop_front()`.
   b. While `!dq.empty()` and `nums[i] >= nums[dq.back()]`: `dq.pop_back()`.
   c. `dq.push_back(i)`.
   d. If `i >= k - 1`: `ans.push_back(nums[dq.front()])`.
3. Return `ans`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <deque>

class Solution {
public:
    std::vector<int> maxSlidingWindow(const std::vector<int>& nums, int k) {
        int n = nums.size();
        std::vector<int> ans;
        ans.reserve(n - k + 1);
        std::deque<int> dq; // Monotonic Decreasing Deque of indices
        
        for (int i = 0; i < n; ++i) {
            // Step 1: Remove out-of-bound indices
            if (!dq.empty() && dq.front() == i - k) {
                dq.pop_front();
            }
            
            // Step 2: Maintain monotonic decreasing property
            while (!dq.empty() && nums[i] >= nums[dq.back()]) {
                dq.pop_back();
            }
            
            // Step 3: Add current index
            dq.push_back(i);
            
            // Step 4: Record maximum for valid windows
            if (i >= k - 1) {
                ans.push_back(nums[dq.front()]);
            }
        }
        
        return ans;
    }
};
```

---

## Dry Run

### Input
- `nums = [1, 3, -1, -3, 5, 3, 6, 7]`, `k = 3`

### Execution Trace

- `i = 0` (val 1): `dq = [0]`
- `i = 1` (val 3): `3 >= 1` $\implies$ Pop `0`. `dq = [1]`
- `i = 2` (val -1): `dq = [1, 2]`. $i \ge 2 \implies$ Record `nums[dq.front()]` = `nums[1]` = **`3`**.
- `i = 3` (val -3): `dq = [1, 2, 3]`. Record `nums[1]` = **`3`**.
- `i = 4` (val 5):
  - Evict `dq.front()` if `== 4-3=1` $\implies$ Pop `1`.
  - `5 >= -3` & `5 >= -1` $\implies$ Pop `3`, `2`. `dq = [4]`.
  - Record `nums[4]` = **`5`**.
- `i = 5` (val 3): `dq = [4, 5]`. Record `nums[4]` = **`5`**.
- `i = 6` (val 6): Pops `5`, `4`. `dq = [6]`. Record `nums[6]` = **`6`**.
- `i = 7` (val 7): Pops `6`. `dq = [7]`. Record `nums[7]` = **`7`**.

### Result
- Output: `[3, 3, 5, 5, 6, 7]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Each index is pushed and popped from `dq` at most once across all iterations.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(K)$
  - Deque stores at most $K$ indices at any given moment.

---

## Why This is Optimal

- Solves sliding window maximum in linear $\mathcal{O}(N)$ time.
- Uses optimal $\mathcal{O}(K)$ auxiliary deque space.

---

## Common Mistakes

1. **Storing Values Instead of Indices in Deque**: Storing `nums[i]` makes it impossible to check if the maximum element is out of the current sliding window boundary (`dq.front() == i - k`).
2. **Using Strict `>` instead of `>=`**: Failing to pop duplicate equal values, which can leave obsolete indices in the deque.
