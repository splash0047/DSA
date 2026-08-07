# Squares of a Sorted Array

## Pattern Used

- **Pattern**: **Two Pointers (Outside-In Fill)**
- **Concept**: Since `nums` is sorted in non-decreasing order, the largest squared values can only come from the extreme ends of the array (most negative on the left or most positive on the right).

---

## Observation

1. For an array like `[-4, -1, 0, 3, 10]`:
   - `(-4)^2 = 16`, `(10)^2 = 100`.
   - The maximum squared value in the remaining array is always at either `abs(nums[left])` or `abs(nums[right])`.
2. By filling a new result vector backwards from index $N - 1$ down to `0`, we can compare absolute values at `left` and `right` pointers and place the larger square at the current position.

---

## Intuition

Place `left = 0` and `right = n - 1`:
- Compare `abs(nums[left])` and `abs(nums[right])`.
- Whichever absolute value is larger produces the next largest square.
- Insert its square into `result[pos--]` and advance that pointer inward.

This guarantees a sorted output in a single linear pass.

---

## Algorithm

1. `left = 0`, `right = n - 1`, `pos = n - 1`.
2. Create `result` vector of size $N$.
3. While `left <= right`:
   a. If `abs(nums[left]) > abs(nums[right])`:
      - `result[pos] = nums[left] * nums[left]`
      - `left++`
   b. Else:
      - `result[pos] = nums[right] * nums[right]`
      - `right--`
   c. `pos--`
4. Return `result`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <cmath>

class Solution {
public:
    std::vector<int> sortedSquares(const std::vector<int>& nums) {
        int n = nums.size();
        std::vector<int> result(n);
        
        int left = 0;
        int right = n - 1;
        int pos = n - 1;
        
        while (left <= right) {
            if (std::abs(nums[left]) > std::abs(nums[right])) {
                result[pos--] = nums[left] * nums[left];
                left++;
            } else {
                result[pos--] = nums[right] * nums[right];
                right--;
            }
        }
        
        return result;
    }
};
```

---

## Dry Run

### Input
- `nums = [-4, -1, 0, 3, 10]`

### Execution Trace

| Step | `left` (`nums[left]`) | `right` (`nums[right]`) | Compare `abs` | `pos` | Value Written | `result` State |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `0` (`-4`) | `4` (`10`) | `|-4| < |10|` | `4` | $10^2 = 100$, `right--` | `[_, _, _, _, 100]` |
| 2 | `0` (`-4`) | `3` (`3`) | `|-4| > |3|` | `3` | $(-4)^2 = 16$, `left++` | `[_, _, _, 16, 100]` |
| 3 | `1` (`-1`) | `3` (`3`) | `|-1| < |3|` | `2` | $3^2 = 9$, `right--` | `[_, _, 9, 16, 100]` |
| 4 | `1` (`-1`) | `2` (`0`) | `|-1| > |0|` | `1` | $(-1)^2 = 1$, `left++` | `[_, 1, 9, 16, 100]` |
| 5 | `2` (`0`) | `2` (`0`) | `|0| <= |0|` | `0` | $0^2 = 0$, `right--` | `[0, 1, 9, 16, 100]` |

### Result
- Output: `[0, 1, 9, 16, 100]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass through $N$ elements; each step places one element into `result`.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Allocates `result` vector of size $N$ to store output (required by function signature).

---

## Why This is Optimal

- Reading all input elements requires $\Omega(N)$ time.
- Single-pass filling achieves optimal $\mathcal{O}(N)$ linear time.

---

## Common Mistakes

1. **Filling Front-to-Back**: Filling `result` starting from index `0` instead of index `N-1`. The outside-in comparisons yield the *largest* squares first, so `result` must be filled from right to left.
2. **Squaring during comparison**: Comparing `nums[left] * nums[left]` vs `nums[right] * nums[right]` can cause integer overflow if numbers are large; comparing `std::abs()` first avoids premature multiplication.
