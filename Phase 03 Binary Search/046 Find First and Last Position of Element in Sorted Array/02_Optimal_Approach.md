# Find First and Last Position of Element in Sorted Array

## Pattern Used

- **Pattern**: **Dual Binary Search (Lower Bound & Upper Bound)**
- **Concept**:
  - **First Occurrence**: Binary search for lower bound of `target` (first index `i` where `nums[i] >= target`).
  - **Last Occurrence**: Binary search for upper bound minus 1 (first index `i` where `nums[i] > target`, minus 1).

---

## Observation

1. **Find First Index**:
   - `if (nums[mid] >= target)`: record `first = mid`, search left half `high = mid - 1`.
   - `else`: search right half `low = mid + 1`.
   - Verify `first != -1 && nums[first] == target`. If invalid, target is not present, return `{-1, -1}`.
2. **Find Last Index**:
   - `if (nums[mid] <= target)`: record `last = mid`, search right half `low = mid + 1`.
   - `else`: search left half `high = mid - 1`.

---

## Intuition

Run binary search twice:
- Search 1: Bias search towards the **left** to find the starting index.
- Search 2: Bias search towards the **right** to find the ending index.

---

## Algorithm

### `findFirst(nums, target)`
1. `low = 0`, `high = n - 1`, `ans = -1`.
2. While `low <= high`:
   a. `mid = low + (high - low) / 2`.
   b. If `nums[mid] >= target`:
      - `if (nums[mid] == target) ans = mid;`
      - `high = mid - 1;`
   c. Else: `low = mid + 1;`
3. Return `ans`.

### `findLast(nums, target)`
1. `low = 0`, `high = n - 1`, `ans = -1`.
2. While `low <= high`:
   a. `mid = low + (high - low) / 2`.
   b. If `nums[mid] <= target`:
      - `if (nums[mid] == target) ans = mid;`
      - `low = mid + 1;`
   c. Else: `high = mid - 1;`
3. Return `ans`.

---

## Clean C++17 Solution

```cpp
#include <vector>

class Solution {
private:
    int findFirst(const std::vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        int ans = -1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (nums[mid] >= target) {
                if (nums[mid] == target) ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        
        return ans;
    }
    
    int findLast(const std::vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        int ans = -1;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (nums[mid] <= target) {
                if (nums[mid] == target) ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        
        return ans;
    }
public:
    std::vector<int> searchRange(const std::vector<int>& nums, int target) {
        int first = findFirst(nums, target);
        if (first == -1) return {-1, -1};
        int last = findLast(nums, target);
        return {first, last};
    }
};
```

---

## Dry Run

### Input
- `nums = [5, 7, 7, 8, 8, 10]`, `target = 8`

### Execution Trace

#### Search 1: `findFirst`
- `L=0, H=5` $\rightarrow$ `mid=2` (`nums[2]=7 < 8`) $\rightarrow$ `L=3`
- `L=3, H=5` $\rightarrow$ `mid=4` (`nums[4]=8 == 8`) $\rightarrow$ `ans=4`, `H=3`
- `L=3, H=3` $\rightarrow$ `mid=3` (`nums[3]=8 == 8`) $\rightarrow$ `ans=3`, `H=2`
- Loop ends. `first = 3`.

#### Search 2: `findLast`
- `L=0, H=5` $\rightarrow$ `mid=2` (`nums[2]=7 < 8`) $\rightarrow$ `L=3`
- `L=3, H=5` $\rightarrow$ `mid=4` (`nums[4]=8 == 8`) $\rightarrow$ `ans=4`, `L=5`
- `L=5, H=5` $\rightarrow$ `mid=5` (`nums[5]=10 > 8`) $\rightarrow$ `H=4`
- Loop ends. `last = 4`.

### Result
- Output: `[3, 4]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(\log N)$
  - Two independent binary searches, each taking $\mathcal{O}(\log N)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This is Optimal

- Solves range boundary queries in logarithmic $\mathcal{O}(\log N)$ time.
- Uses zero extra memory.

---

## Common Mistakes

1. **Early Return on First Match**: Stopping standard binary search as soon as `nums[mid] == target` returns an arbitrary index, which may be neither the first nor the last occurrence!
2. **Missing `first == -1` Short-Circuit**: Executing `findLast` when `findFirst` returns `-1` (unnecessary work).
