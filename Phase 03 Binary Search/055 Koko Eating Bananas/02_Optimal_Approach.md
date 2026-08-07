# Koko Eating Bananas

## Pattern Used

- **Pattern**: **Binary Search on Answer Space (Monotonic Predicate Function)**
- **Concept**: Search for the minimum valid speed $k \in [1, \max(\text{piles})]$. The predicate function `canFinish(k)` returns `true` if $\sum \lceil \text{piles}[i] / k \rceil \le h$.

---

## Observation

1. Monotonic Predicate Property:
   - If speed $k$ is fast enough to finish within $h$ hours, any speed $> k$ will ALSO finish within $h$ hours.
   - If speed $k$ is too slow, any speed $< k$ will ALSO be too slow.
2. Binary Search bounds:
   - Minimum possible speed: `low = 1`.
   - Maximum possible speed: `high = max(piles)` (at this speed, Koko eats 1 pile per hour, requiring $N$ hours).
3. Integer Ceiling Division: To calculate $\lceil a / b \rceil$ using integer arithmetic:
   $$\lceil a / b \rceil = (a + b - 1) / b$$

---

## Intuition

Set search space `low = 1` and `high = max(piles)`. Test midpoint speed `mid`:
- If `canFinish(mid)` is `true`: `mid` is a valid speed candidate. Record `ans = mid` and contract `high = mid - 1` to check if a slower speed works.
- If `canFinish(mid)` is `false`: `mid` is too slow. Increase speed `low = mid + 1`.

---

## Algorithm

1. `low = 1`, `high = max(piles)`, `ans = high`.
2. While `low <= high`:
   a. `mid = low + (high - low) / 2`.
   b. Calculate `total_hours` for speed `mid`:
      - For each `p` in `piles`: `total_hours += (p + mid - 1LL) / mid`.
   c. If `total_hours <= h`:
      - `ans = mid`.
      - `high = mid - 1`.
   d. Else:
      - `low = mid + 1`.
3. Return `ans`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>

class Solution {
private:
    bool canFinish(const std::vector<int>& piles, int h, int k) {
        long long total_hours = 0;
        for (int pile : piles) {
            total_hours += (pile + k - 1LL) / k;
        }
        return total_hours <= h;
    }
public:
    int minEatingSpeed(const std::vector<int>& piles, int h) {
        int low = 1;
        int high = *std::max_element(piles.begin(), piles.end());
        int ans = high;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (canFinish(piles, h, mid)) {
                ans = mid;
                high = mid - 1; // Try to find a slower speed
            } else {
                low = mid + 1;  // Speed too slow, increase speed
            }
        }
        
        return ans;
    }
};
```

---

## Dry Run

### Input
- `piles = [3, 6, 7, 11]`, `h = 8`
- `low = 1`, `high = 11`

### Execution Trace

| Step | `low` | `high` | `mid` (Speed) | Total Hours Calculation | `total_hours <= 8`? | `ans` | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `1` | `11` | `6` | $\lceil 3/6 \rceil + \lceil 6/6 \rceil + \lceil 7/6 \rceil + \lceil 11/6 \rceil = 1+1+2+2 = 6$ | `6 <= 8` (**Yes**) | `6` | `high = mid - 1 = 5` |
| 2 | `1` | `5` | `3` | $\lceil 3/3 \rceil + \lceil 6/3 \rceil + \lceil 7/3 \rceil + \lceil 11/3 \rceil = 1+2+3+4 = 10$ | `10 <= 8` (No) | `6` | `low = mid + 1 = 4` |
| 3 | `4` | `5` | `4` | $\lceil 3/4 \rceil + \lceil 6/4 \rceil + \lceil 7/4 \rceil + \lceil 11/4 \rceil = 1+2+2+3 = 8$ | `8 <= 8` (**Yes**) | **`4`** | `high = mid - 1 = 3` |
| End | `4` | `3` | - | - | - | `low > high` (Stop) | Return `4` |

### Result
- Output: `4`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log(\max(\text{piles})))$
  - Binary search takes $\mathcal{O}(\log(\max(\text{piles})))$ steps; each step evaluates predicate function over $N$ piles in $\mathcal{O}(N)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This is Optimal

- Solves Binary Search on Answer Space in optimal $\mathcal{O}(N \log M)$ time.
- Uses zero extra memory.

---

## Common Mistakes

1. **Integer Overflow in Hours Accumulation**: Accumulating `total_hours` into a standard 32-bit `int` instead of `long long`. If $N = 10^4$ and piles are $10^9$ with speed 1, sum reaches $10^{13}$, causing integer overflow.
2. **Ceiling Division Error**: Using floating point `ceil((double)pile / k)` which suffers from precision loss on large integers. Use integer math `(pile + k - 1LL) / k`.
