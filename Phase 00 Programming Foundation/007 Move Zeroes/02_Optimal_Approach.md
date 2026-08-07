# Move Zeroes

## Pattern Used

- **Pattern**: **Two Pointers (Read / Write Pointers)**
- **Concept**: Maintain a `write_index` pointer for placing the next non-zero element, and a `read_index` pointer for exploring the array.

---

## Observation

1. All non-zero elements must retain their original relative order.
2. If we swap every non-zero element found at `read_index` with the element at `write_index`, all non-zero elements will naturally group at the prefix of the array, while zeroes are pushed towards the back.

---

## Intuition

Think of `write_index` as marking the boundary of non-zero elements placed so far:
- As `read_index` scans the array, whenever it encounters a non-zero element (`nums[read_index] != 0`), we swap `nums[write_index]` and `nums[read_index]`, then advance `write_index++`.
- If `nums[read_index] == 0`, we do nothing and advance `read_index`.

This guarantees that all non-zero elements are packed to the front in optimal time and $\mathcal{O}(1)$ space.

---

## Algorithm

1. Initialize `write_index = 0`.
2. Loop `read_index` from `0` to `n - 1`:
   a. If `nums[read_index] != 0`:
      - `swap(nums[write_index], nums[read_index])`
      - `write_index++`
3. Array `nums` is modified in-place.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    void moveZeroes(std::vector<int>& nums) {
        int write_index = 0;
        int n = nums.size();
        
        for (int read_index = 0; read_index < n; ++read_index) {
            if (nums[read_index] != 0) {
                std::swap(nums[write_index], nums[read_index]);
                write_index++;
            }
        }
    }
};
```

---

## Dry Run

### Input
- `nums = [0, 1, 0, 3, 12]`

### Execution Trace

| Step | `read_index` | `nums[read_index]` | `write_index` | `nums[write_index]` | Action | Array State (`nums`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Start| - | - | `0` | `0` | Initialize `write_index = 0` | `[0, 1, 0, 3, 12]` |
| 1 | `0` | `0` | `0` | `0` | Zero -> skip | `[0, 1, 0, 3, 12]` |
| 2 | `1` | `1` | `0` | `0` | Swap `nums[0], nums[1]`, `w++` | `[1, 0, 0, 3, 12]` |
| 3 | `2` | `0` | `1` | `0` | Zero -> skip | `[1, 0, 0, 3, 12]` |
| 4 | `3` | `3` | `1` | `0` | Swap `nums[1], nums[3]`, `w++` | `[1, 3, 0, 0, 12]` |
| 5 | `4` | `12` | `2` | `0` | Swap `nums[2], nums[4]`, `w++` | `[1, 3, 12, 0, 0]` |

### Result
- `nums = [1, 3, 12, 0, 0]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - `read_index` traverses $N$ elements once.
  - Each swap operation takes $\mathcal{O}(1)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - In-place modification without external data structures.

---

## Why This is Optimal

- Every element must be inspected at least once ($\Omega(N)$ lower bound).
- Minimizes writes by swapping only non-zero elements.
- Uses $\mathcal{O}(1)$ extra space.

---

## Common Mistakes

1. **Overwriting Without Swapping**: Copying non-zero values forward without swapping causes trailing non-zero elements to remain duplicate unless explicitly overwritten with `0`s at the end.
2. **Self-Swapping Overhead**: Swapping when `write_index == read_index`. (Harmless in logic, but adding `if (write_index != read_index)` can slightly optimize writes when no zeroes have been encountered yet).
