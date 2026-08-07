# Sort Colors

## Pattern Used

- **Pattern**: **Dutch National Flag Algorithm (Three Pointers)**
- **Concept**: Maintain three pointers to partition the array into 4 zones in a single pass:
  - `[0 ... low-1]`: Region containing `0`s (Red)
  - `[low ... mid-1]`: Region containing `1`s (White)
  - `[mid ... high]`: Unexamined elements
  - `[high+1 ... n-1]`: Region containing `2`s (Blue)

---

## Observation

1. `mid` serves as the primary scanning pointer.
2. If `nums[mid] == 0`: It belongs in the `0`s region. Swap `nums[low]` and `nums[mid]`, then increment `low++` and `mid++`.
3. If `nums[mid] == 1`: It is already in the correct region. Simply increment `mid++`.
4. If `nums[mid] == 2`: It belongs in the `2`s region. Swap `nums[mid]` and `nums[high]`, then decrement `high--`. **Do NOT increment `mid`**, because the element swapped from `high` into `mid` has not yet been examined!

---

## Intuition

Think of partitioning three categories simultaneously:
- Push all `0`s to the left boundary (`low`).
- Push all `2`s to the right boundary (`high`).
- All `1`s automatically settle into the middle region (`low` to `mid`).

---

## Algorithm

1. `low = 0`, `mid = 0`, `high = nums.size() - 1`.
2. While `mid <= high`:
   a. If `nums[mid] == 0`:
      - `std::swap(nums[low], nums[mid])`
      - `low++`, `mid++`
   b. Else if `nums[mid] == 1`:
      - `mid++`
   c. Else (`nums[mid] == 2`):
      - `std::swap(nums[mid], nums[high])`
      - `high--`
3. Array is sorted in-place in a single pass.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    void sortColors(std::vector<int>& nums) {
        int low = 0;
        int mid = 0;
        int high = nums.size() - 1;
        
        while (mid <= high) {
            if (nums[mid] == 0) {
                std::swap(nums[low++], nums[mid++]);
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                std::swap(nums[mid], nums[high--]);
            }
        }
    }
};
```

---

## Dry Run

### Input
- `nums = [2, 0, 2, 1, 1, 0]`

### Execution Trace

| Step | `low` | `mid` | `high` | `nums[mid]` | Action | Array State (`nums`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Start| `0` | `0` | `5` | `2` | Swap `nums[0], nums[5]`, `high--` | `[0, 0, 2, 1, 1, 2]` |
| 1 | `0` | `0` | `4` | `0` | Swap `nums[0], nums[0]`, `low++`, `mid++` | `[0, 0, 2, 1, 1, 2]` |
| 2 | `1` | `1` | `4` | `0` | Swap `nums[1], nums[1]`, `low++`, `mid++` | `[0, 0, 2, 1, 1, 2]` |
| 3 | `2` | `2` | `4` | `2` | Swap `nums[2], nums[4]`, `high--` | `[0, 0, 1, 1, 2, 2]` |
| 4 | `2` | `2` | `3` | `1` | `mid++` | `[0, 0, 1, 1, 2, 2]` |
| 5 | `2` | `3` | `3` | `1` | `mid++` | `[0, 0, 1, 1, 2, 2]` |
| End | `2` | `4` | `3` | - | `mid > high`, Loop ends | `[0, 0, 1, 1, 2, 2]` |

### Result
- Output: `[0, 0, 1, 1, 2, 2]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass through $N$ elements. Each step advances either `mid` or decrements `high`.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Strictly in-place using 3 pointer variables.

---

## Why This is Optimal

- Single pass $\mathcal{O}(N)$ time lower bound.
- Zero extra memory allocation ($\mathcal{O}(1)$ space).

---

## Common Mistakes

1. **Incrementing `mid` when swapping with `high`**: Incrementing `mid` after swapping `nums[mid]` with `nums[high]` is wrong! The element coming from `high` is unexamined and could be `0` or `2`. It must be checked at the current `mid` index during the next iteration.
2. **Incorrect Loop Condition**: Using `while (mid < high)` instead of `while (mid <= high)` leaves the last element unexamined.
