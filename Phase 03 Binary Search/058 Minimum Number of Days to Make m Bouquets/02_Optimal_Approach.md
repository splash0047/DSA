# Minimum Number of Days to Make m Bouquets

## Pattern Used

- **Pattern**: **Binary Search on Answer Space (Monotonic Predicate Function)**
- **Concept**: Search for the minimum day $D \in [\min(\text{bloomDay}), \max(\text{bloomDay})]$. The predicate function `canMake(day)` verifies if at least $m$ bouquets of $k$ adjacent bloomed flowers can be formed on `day`.

---

## Observation

1. **Initial Feasibility Guard**:
   - Total flowers required: $m \times k$.
   - Total flowers available: $n = \text{bloomDay.length}$.
   - If $1\text{LL} \times m \times k > n$, it is mathematically impossible to make $m$ bouquets! Return `-1` immediately.
2. Monotonicity:
   - If we can form $m$ bouquets on day $D$, we can ALSO form them on day $D + 1$.
   - Search space: `low = min(bloomDay)` and `high = max(bloomDay)`.
3. Adjacent Flower Counting:
   - Traverse `bloomDay`. Maintain a running counter `adjacent`.
   - If `bloomDay[i] <= day`: `adjacent++`. When `adjacent == k`, increment `bouquets++` and reset `adjacent = 0`.
   - If `bloomDay[i] > day`: reset `adjacent = 0`.

---

## Intuition

1. Set `low = min(bloomDay)` and `high = max(bloomDay)`.
2. Test midpoint day `mid`:
   - If `canMake(mid)` is `true`: `mid` is a valid day candidate. Record `ans = mid` and contract `high = mid - 1`.
   - If `canMake(mid)` is `false`: `mid` is too early. Increase days `low = mid + 1`.

---

## Algorithm

1. `n = bloomDay.size()`.
2. If `1LL * m * k > n`, return `-1`.
3. `low = min(bloomDay)`, `high = max(bloomDay)`, `ans = high`.
4. While `low <= high`:
   a. `mid = low + (high - low) / 2`.
   b. `bouquets = 0`, `adjacent = 0`.
   c. For each `bd` in `bloomDay`:
      - If `bd <= mid`:
        - `adjacent++`.
        - If `adjacent == k`: `bouquets++`, `adjacent = 0`.
      - Else: `adjacent = 0`.
   d. If `bouquets >= m`:
      - `ans = mid`.
      - `high = mid - 1`.
   e. Else:
      - `low = mid + 1`.
5. Return `ans`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>

class Solution {
private:
    bool canMake(const std::vector<int>& bloomDay, int m, int k, int day) {
        int bouquets = 0;
        int count = 0;
        
        for (int bd : bloomDay) {
            if (bd <= day) {
                count++;
                if (count == k) {
                    bouquets++;
                    count = 0;
                }
            } else {
                count = 0;
            }
        }
        
        return bouquets >= m;
    }
public:
    int minDays(const std::vector<int>& bloomDay, int m, int k) {
        int n = bloomDay.size();
        if (1LL * m * k > n) return -1;
        
        int low = *std::min_element(bloomDay.begin(), bloomDay.end());
        int high = *std::max_element(bloomDay.begin(), bloomDay.end());
        int ans = high;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (canMake(bloomDay, m, k, mid)) {
                ans = mid;
                high = mid - 1; // Try to find an earlier day
            } else {
                low = mid + 1;  // Not enough bouquets, wait longer
            }
        }
        
        return ans;
    }
};
```

---

## Dry Run

### Input
- `bloomDay = [1, 10, 3, 10, 2]`, `m = 3`, `k = 1`
- `low = 1`, `high = 10`

### Execution Trace

| Step | `low` | `high` | `mid` (Day) | Bloomed Array at `mid` | Bouquets Formed ($k=1$) | `bouquets >= 3`? | `ans` | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `1` | `10` | `5` | `[x, _, x, _, x]` | 3 | `3 >= 3` (**Yes**) | `5` | `high = mid - 1 = 4` |
| 2 | `1` | `4` | `2` | `[x, _, _, _, x]` | 2 | `2 >= 3` (No) | `5` | `low = mid + 1 = 3` |
| 3 | `3` | `4` | `3` | `[x, _, x, _, x]` | 3 | `3 >= 3` (**Yes**) | **`3`** | `high = mid - 1 = 2` |
| End | `3` | `2` | - | - | - | - | `low > high` (Stop) | Return `3` |

### Result
- Output: `3`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log(\max(\text{bloomDay})))$
  - Binary search over day range takes $\mathcal{O}(\log(\max(\text{bloomDay})))$ steps; counting takes $\mathcal{O}(N)$ per step.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This is Optimal

- Calculates minimum days in optimal $\mathcal{O}(N \log D)$ time.
- Uses zero extra memory.

---

## Common Mistakes

1. **Integer Overflow in Feasibility Guard**: Writing `m * k > n` with 32-bit integers. If $m = 10^6$ and $k = 10^5$, $m \times k = 10^{11}$, causing integer overflow. Use `1LL * m * k > n`.
2. **Not Resetting `adjacent` Counter**: Failing to reset `adjacent = 0` when encountering a non-bloomed flower (`bd > day`). Bouquets must contain **adjacent** bloomed flowers!
