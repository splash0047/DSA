# Range Sum Query - Immutable

- **Problem Number**: 303
- **Platform**: LeetCode #303
- **Difficulty**: Easy
- **Pattern**: Direct Sum Loop per Query

---

## Brute Force Intuition

For every call to `sumRange(left, right)`, iterate from index `left` to `right` and compute the sum of elements on the fly.

---

## Algorithm

1. Constructor: Store a copy of `nums`.
2. `sumRange(left, right)`:
   a. `sum = 0`.
   b. Loop `i` from `left` to `right`: `sum += nums[i]`.
   c. Return `sum`.

---

## Code

```cpp
#include <vector>

class NumArray {
private:
    std::vector<int> data;
public:
    NumArray(const std::vector<int>& nums) : data(nums) {}
    
    int sumRange(int left, int right) {
        int sum = 0;
        for (int i = left; i <= right; ++i) {
            sum += data[i];
        }
        return sum;
    }
};
```

---

## Time Complexity

- **Constructor**: $\mathcal{O}(N)$
- **`sumRange`**: $\mathcal{O}(N)$ per query.
- For $Q = 10^4$ queries on array of size $N = 10^4$, total time is $\mathcal{O}(Q \times N) = 10^8$ operations, leading to potential TLE.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Stores input vector copy.

---

## Why This Approach Is Not Optimal

Computing range sums from scratch for every query takes linear $\mathcal{O}(N)$ time per query. Using a **1D Prefix Sum Array**, pre-computations take $\mathcal{O}(N)$ time once, allowing every subsequent `sumRange` query to be answered in $\mathcal{O}(1)$ constant time.
