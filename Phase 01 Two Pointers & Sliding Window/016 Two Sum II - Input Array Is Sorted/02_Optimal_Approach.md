# Two Sum II - Input Array Is Sorted

## Pattern Used

- **Pattern**: **Two Pointers (Opposite Ends / Shrinking Window)**
- **Concept**: Place `left` pointer at index `0` and `right` pointer at index `n - 1`. Use the sorted property to adjust pointer bounds deterministically.

---

## Observation

1. If `numbers[left] + numbers[right] == target`, we found the answer!
2. If `sum < target`, the sum is too small. Because the array is sorted, incrementing `left++` is guaranteed to increase `numbers[left]` and increase the sum.
3. If `sum > target`, the sum is too large. Decrementing `right--` is guaranteed to decrease `numbers[right]` and decrease the sum.

---

## Intuition

Place two pointers at the boundaries:
- Sum too small? Move `left` pointer rightward to get a larger value.
- Sum too large? Move `right` pointer leftward to get a smaller value.
- Sum matches? Return 1-based indices `{left + 1, right + 1}`.

---

## Algorithm

1. `left = 0`, `right = numbers.size() - 1`.
2. While `left < right`:
   a. `current_sum = numbers[left] + numbers[right]`.
   b. If `current_sum == target`: return `{left + 1, right + 1}`.
   c. Else if `current_sum < target`: `left++`.
   d. Else: `right--`.
3. Return `{}` if not found.

---

## Clean C++17 Solution

```cpp
#include <vector>

class Solution {
public:
    std::vector<int> twoSum(const std::vector<int>& numbers, int target) {
        int left = 0;
        int right = numbers.size() - 1;
        
        while (left < right) {
            int current_sum = numbers[left] + numbers[right];
            
            if (current_sum == target) {
                return {left + 1, right + 1};
            } else if (current_sum < target) {
                left++;
            } else {
                right--;
            }
        }
        
        return {};
    }
};
```

---

## Dry Run

### Input
- `numbers = [2, 7, 11, 15]`, `target = 9`

### Execution Trace

| Step | `left` (`numbers[left]`) | `right` (`numbers[right]`) | `current_sum` | Target Comparison | Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `0` (`2`) | `3` (`15`) | `17` | `17 > 9` (Too large) | `right--` |
| 2 | `0` (`2`) | `2` (`11`) | `13` | `13 > 9` (Too large) | `right--` |
| 3 | `0` (`2`) | `1` (`7`) | `9` | `9 == 9` (**Exact Match!**) | Return `{1, 2}` |

### Result
- Output: `[1, 2]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - In each step, either `left` increments or `right` decrements.
  - The loop runs at most $N$ times.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses constant extra space.

---

## Why This is Optimal

- Requires examining elements at most once ($\Omega(N)$ time).
- Uses zero extra memory ($\mathcal{O}(1)$ space), fulfilling the strict problem constraint.

---

## Common Mistakes

1. **Returning 0-Based Indices**: Problem explicitly asks for 1-indexed output (`left + 1`, `right + 1`).
2. **Using Hash Map**: Using a Hash Map solves it in $\mathcal{O}(N)$ time, but uses $\mathcal{O}(N)$ extra space, violating the $\mathcal{O}(1)$ space constraint!
