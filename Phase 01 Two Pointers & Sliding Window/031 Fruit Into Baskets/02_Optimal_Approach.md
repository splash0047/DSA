# Fruit Into Baskets

## Pattern Used

- **Pattern**: **Variable-Size Sliding Window (At Most K Distinct Elements)**
- **Concept**: Maintain a window `[left ... right]` and a hash map `basket` mapping `fruit_type -> frequency`. Keep `basket.size() <= 2`.

---

## Observation

1. We can pick from a continuous sequence of trees as long as the total number of distinct fruit types in our current range does not exceed `2`.
2. As `right` pointer expands the window:
   - Insert `fruits[right]` into `basket` and increment its count.
   - If `basket.size() > 2`: the window contains 3 distinct fruit types (invalid!).
   - Shrink `left` pointer: decrement `basket[fruits[left]]`. If its count reaches `0`, remove the key from `basket` using `basket.erase()`. Advance `left++`.
3. The valid window length is `right - left + 1`.

---

## Intuition

1. Expand `right` to collect fruits into `basket`.
2. Whenever you hold 3 different fruit types in your baskets, shrink `left` until one fruit type is completely discarded (`count == 0`).
3. Record `max_len = max(max_len, right - left + 1)`.

---

## Algorithm

1. `unordered_map<int, int> basket`.
2. `left = 0`, `max_len = 0`.
3. Loop `right` from `0` to `n - 1`:
   a. `basket[fruits[right]]++`.
   b. `while (basket.size() > 2)`:
      - `basket[fruits[left]]--`
      - If `basket[fruits[left]] == 0`: `basket.erase(fruits[left])`
      - `left++`
   c. `max_len = max(max_len, right - left + 1)`.
4. Return `max_len`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    int totalFruit(const std::vector<int>& fruits) {
        std::unordered_map<int, int> basket;
        int left = 0;
        int max_len = 0;
        int n = fruits.size();
        
        for (int right = 0; right < n; ++right) {
            basket[fruits[right]]++;
            
            while (basket.size() > 2) {
                basket[fruits[left]]--;
                if (basket[fruits[left]] == 0) {
                    basket.erase(fruits[left]);
                }
                left++;
            }
            
            max_len = std::max(max_len, right - left + 1);
        }
        
        return max_len;
    }
};
```

---

## Dry Run

### Input
- `fruits = [1, 2, 3, 2, 2]`

### Execution Trace

| `right` | `fruits[right]` | `basket` Map State | `basket.size()` | `left` | Window Subarray | `max_len` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | `1` | `{1: 1}` | 1 | 0 | `[1]` | 1 |
| 1 | `2` | `{1: 1, 2: 1}` | 2 | 0 | `[1, 2]` | 2 |
| 2 | `3` | `{1: 1, 2: 1, 3: 1}` | 3 ($> 2$) | Shrink `l=1` (`erase 1`) | `[2, 3]` | 2 |
| 3 | `2` | `{2: 2, 3: 1}` | 2 | 1 | `[2, 3, 2]` | 3 |
| 4 | `2` | `{2: 3, 3: 1}` | 2 | 1 | `[2, 3, 2, 2]` | **4** |

### Result
- Output: `4`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - `right` and `left` pointers advance at most $N$ times.
  - Map operations take average $\mathcal{O}(1)$ time (map size never exceeds 3).

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Hash map contains at most 3 distinct keys at any point.

---

## Why This is Optimal

- Inspecting every tree requires $\Omega(N)$ time.
- Single-pass sliding window achieves $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Common Mistakes

1. **Forgetting `basket.erase()`**: Decrementing `basket[fruit]--` to 0 without erasing the key leaves `basket.size()` equal to 3, causing infinite shrinking!
2. **Confusing Subarray with Subsequence**: Picking fruits out of order. Trees must be picked sequentially from left to right (contiguous subarray).
