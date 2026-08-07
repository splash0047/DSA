# Remove Duplicates from Sorted Array

## Pattern Used

- **Pattern**: **Two Pointers (Read / Write Pointers)**
- **Concept**: Leveraging array pre-sorting so that identical values are adjacent. We maintain a `write_index` pointer for placing unique elements and a `read_index` pointer for scanning the array.

---

## Observation

Since the input array `nums` is already sorted in non-decreasing order:
1. **All identical elements are strictly contiguous** (adjacent to each other).
2. The first element `nums[0]` is guaranteed to be unique and will always stay at index `0`.
3. An element `nums[j]` is a new unique value if and only if:
$$\text{nums}[j] \neq \text{nums}[i]$$
where `i` points to the last unique element placed so far.

---

## Intuition

Think of this as managing two pointers on a single conveyor belt:
- **`unique_ptr` (`i`)**: Keeps track of the end of our cleaned array containing only unique elements.
- **`scan_ptr` (`j`)**: Scans through the rest of the array searching for the next distinct number.

Whenever `scan_ptr` encounters a number that is different from `nums[unique_ptr]`, it means we have found a new unique number. We increment `unique_ptr` to move to the next available write slot, overwrite `nums[unique_ptr]` with `nums[scan_ptr]`, and continue.

---

## Algorithm

1. If the input array `nums` is empty, return `0`.
2. Initialize `write_index = 0` (pointing to the position of the first unique element).
3. Loop `read_index` from `1` to `n - 1`:
   a. Compare `nums[read_index]` with `nums[write_index]`.
   b. If `nums[read_index] != nums[write_index]`:
      - Increment `write_index` by 1.
      - Copy `nums[write_index] = nums[read_index]`.
4. Return `write_index + 1` as the count of unique elements ($k$).

---

## Clean C++17 Solution

```cpp
#include <vector>

class Solution {
public:
    int removeDuplicates(std::vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        
        int write_index = 0;
        int n = nums.size();
        
        for (int read_index = 1; read_index < n; ++read_index) {
            if (nums[read_index] != nums[write_index]) {
                ++write_index;
                nums[write_index] = nums[read_index];
            }
        }
        
        return write_index + 1;
    }
};
```

---

## Dry Run

### Input
- `nums = [0, 0, 1, 1, 1, 2]`

### Execution Trace

| Step | `read_index` | `nums[read_index]` | `write_index` | `nums[write_index]` | Condition (`!=`) | Array State (`nums`) | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Start| - | - | `0` | `0` | - | `[0, 0, 1, 1, 1, 2]` | Initialize `write_index = 0` |
| 1 | `1` | `0` | `0` | `0` | `0 != 0` (False) | `[0, 0, 1, 1, 1, 2]` | Duplicate, skip |
| 2 | `2` | `1` | `0` | `0` | `1 != 0` (**True**) | `[0, 1, 1, 1, 1, 2]` | `write_index++` (1), write `nums[1] = 1` |
| 3 | `3` | `1` | `1` | `1` | `1 != 1` (False) | `[0, 1, 1, 1, 1, 2]` | Duplicate, skip |
| 4 | `4` | `1` | `1` | `1` | `1 != 1` (False) | `[0, 1, 1, 1, 1, 2]` | Duplicate, skip |
| 5 | `5` | `2` | `1` | `1` | `2 != 1` (**True**) | `[0, 1, 2, 1, 1, 2]` | `write_index++` (2), write `nums[2] = 2` |

### Result
- Return `write_index + 1` = `2 + 1 = 3`.
- Modified prefix: `[0, 1, 2]`.

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - `read_index` moves from index `1` to `N - 1` exactly once.
  - Inside the loop, all operations (comparison, increment, assignment) take $\mathcal{O}(1)$ time.
  - Overall time complexity is strictly linear, $\mathcal{O}(N)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Modification is performed strictly **in-place**.
  - Only two integer variables (`write_index`, `read_index`) are used, requiring constant extra memory.

---

## Why This is Optimal

- **Time Optimality**: Any algorithm must inspect all $N$ elements at least once to determine if they are duplicates. Thus, $\Omega(N)$ time is a lower bound, and our $\mathcal{O}(N)$ time solution achieves this bound.
- **Space Optimality**: The problem requires overwriting the array in-place. Using $\mathcal{O}(1)$ additional memory is the theoretical minimum space possible.

---

## Common Mistakes

1. **Out-of-Bounds Error on Empty Array**: Accessing `nums[0]` without checking if `nums.empty()`.
2. **Incorrect Return Value**: Returning `write_index` instead of `write_index + 1`. Note that `write_index` is 0-indexed, so the count of elements is `write_index + 1`.
3. **Comparing with Previous Element Instead of `nums[write_index]`**: Comparing `nums[read_index] != nums[read_index - 1]` is valid logic, but writing logic must still correctly target `write_index`.
