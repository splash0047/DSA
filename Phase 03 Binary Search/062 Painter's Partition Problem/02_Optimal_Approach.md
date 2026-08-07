# Painter's Partition Problem

## Pattern Used

- **Pattern**: **Binary Search on Answer Space (Minimax Partitioning)**
- **Concept**: Search for the minimum possible maximum time limit $T \in [\max(\text{arr}), \sum \text{arr}]$. The predicate function `canPaint(T, k)` verifies if $k$ painters can complete all contiguous boards within time $T$.

---

## Observation

1. Search Space Boundaries:
   - `low = max(arr)` (a painter cannot spend less time than painting the largest single board).
   - `high = sum(arr)` (when $k = 1$, single painter paints all boards).
2. Monotonicity:
   - If time limit $T$ allows $k$ painters to finish, any larger time limit $> T$ will ALSO work.
   - If time limit $T$ requires $> k$ painters, limit $T$ is too small.

---

## Intuition

1. Set `low = max(arr)` and `high = sum(arr)`.
2. Test midpoint time limit `mid`:
   - Simulate board assignment: add board lengths to current painter's workload. When adding `arr[i]` exceeds `mid`, assign board to next painter.
   - Count required painters `painters`.
   - If `painters <= k`: `mid` time limit is valid! Record `ans = mid` and contract `high = mid - 1`.
   - If `painters > k`: `mid` limit is too small. Increase limit `low = mid + 1`.

---

## Algorithm

1. `low = max(arr)`, `high = sum(arr)`, `ans = high`.
2. While `low <= high`:
   a. `mid = low + (high - low) / 2`.
   b. `painters = 1`, `current_time = 0`.
   c. For each `b` in `arr`:
      - If `current_time + b > mid`:
        - `painters++`.
        - `current_time = b`.
      - Else: `current_time += b`.
   d. If `painters <= k`:
      - `ans = mid`.
      - `high = mid - 1`.
   e. Else:
      - `low = mid + 1`.
3. Return `ans`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <numeric>
#include <algorithm>

class Solution {
private:
    bool canPaint(const std::vector<int>& arr, int k, long long max_time) {
        int painters = 1;
        long long current_time = 0;
        
        for (int b : arr) {
            if (current_time + b > max_time) {
                painters++;
                current_time = b;
            } else {
                current_time += b;
            }
        }
        
        return painters <= k;
    }
public:
    long long minTime(const std::vector<int>& arr, int k) {
        long long low = *std::max_element(arr.begin(), arr.end());
        long long high = std::accumulate(arr.begin(), arr.end(), 0LL);
        long long ans = high;
        
        while (low <= high) {
            long long mid = low + (high - low) / 2;
            
            if (canPaint(arr, k, mid)) {
                ans = mid;
                high = mid - 1; // Try to minimize maximum time
            } else {
                low = mid + 1;  // Time limit too small, increase limit
            }
        }
        
        return ans;
    }
};
```

---

## Dry Run

### Input
- `arr = [5, 10, 30, 20, 15]`, `k = 3`
- `low = 30`, `high = 80`

### Execution Trace

| Step | `low` | `high` | `mid` (Time Limit) | Painter Assignments | Painters Needed | `painters <= 3`? | `ans` | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `30` | `80` | `55` | `[5,10,30] (45)`, `[20,15] (35)` | 2 | `2 <= 3` (**Yes**) | `55` | `high = mid - 1 = 54` |
| 2 | `30` | `54` | `42` | `[5,10] (15)`, `[30] (30)`, `[20,15] (35)` | 3 | `3 <= 3` (**Yes**) | `42` | `high = mid - 1 = 41` |
| 3 | `30` | `41` | `35` | `[5,10] (15)`, `[30] (30)`, `[20,15] (35)` | 3 | `3 <= 3` (**Yes**) | **`35`** | `high = mid - 1 = 34` |
| 4 | `30` | `34` | `32` | `[5,10] (15)`, `[30] (30)`, `[20] (20)`, `[15] (15)` | 4 | `4 <= 3` (No) | `35` | `low = mid + 1 = 33` |
| 5 | `33` | `34` | `33` | `[5,10] (15)`, `[30] (30)`, `[20] (20)`, `[15] (15)` | 4 | `4 <= 3` (No) | `35` | `low = mid + 1 = 34` |
| 6 | `34` | `34` | `34` | `[5,10] (15)`, `[30] (30)`, `[20] (20)`, `[15] (15)` | 4 | `4 <= 3` (No) | `35` | `low = mid + 1 = 35` |
| End | `35` | `34` | - | - | - | - | `low > high` (Stop) | Return `35` |

### Result
- Output: `35`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log(\sum \text{arr}))$
  - Binary search over time range takes $\mathcal{O}(\log(\sum \text{arr}))$ steps; simulation takes $\mathcal{O}(N)$ per step.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This is Optimal

- Solves Painter's Partition Problem in optimal $\mathcal{O}(N \log(\sum \text{arr}))$ time.
- Uses zero extra memory.

---

## Common Mistakes

1. **Integer Overflow**: Sizing `high` as `int` instead of `long long`. Accumulating board lengths up to $10^5 \times 10^5 = 10^{10}$ requires `long long`.
2. **Incorrect `low` Bound**: Setting `low = 0` instead of `max(arr)`.
