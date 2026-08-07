# Product of Array Except Self

- **Problem Number**: 238
- **Platform**: LeetCode #238
- **Difficulty**: Medium
- **Pattern**: Nested Loop Multiplication

---

## Brute Force Intuition

For each index `i`, compute the product of all elements in `nums` except `nums[i]` using an inner loop.

---

## Algorithm

1. Initialize `answer` vector of size $N$.
2. Outer loop `i` from `0` to `n - 1`.
3. `prod = 1`.
4. Inner loop `j` from `0` to `n - 1`:
   a. If `i != j`, `prod *= nums[j]`.
5. `answer[i] = prod`.
6. Return `answer`.

---

## Code

```cpp
#include <vector>

class Solution {
public:
    std::vector<int> productExceptSelf(const std::vector<int>& nums) {
        int n = nums.size();
        std::vector<int> answer(n, 1);
        
        for (int i = 0; i < n; ++i) {
            long long prod = 1;
            for (int j = 0; j < n; ++j) {
                if (i != j) {
                    prod *= nums[j];
                }
            }
            answer[i] = static_cast<int>(prod);
        }
        
        return answer;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - Double loop takes $\mathcal{O}(N^2)$ time.
  - For $N = 10^5$, causes TLE.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$ extra space (excluding output array).

---

## Why This Approach Is Not Optimal

Evaluating product of all other elements takes quadratic time. The problem explicitly forbids using division (which would be $\mathcal{O}(N)$ with zero handling). Using **Prefix & Suffix Products**, we can calculate the result for all indices in linear $\mathcal{O}(N)$ time.
