# Next Greater Element II

- **Problem Number**: 503
- **Platform**: LeetCode #503
- **Difficulty**: Medium
- **Pattern**: Circular Array Double Loop

---

## Brute Force Intuition

For each element at index `i`, perform a circular scan of up to $N - 1$ steps:
- Inspect `nums[(i + j) % N]` for $j \in [1, N-1]$.
- The first element strictly greater than `nums[i]` is the Next Greater Element.
- If no such element exists, set `ans[i] = -1`.

---

## Algorithm

1. Initialize `ans` of size `n` with `-1`.
2. Loop `i` from `0` to `n - 1`:
   a. Loop `j` from `1` to `n - 1`:
      - `idx = (i + j) % n`.
      - If `nums[idx] > nums[i]`:
        - `ans[i] = nums[idx]`.
        - Break.
3. Return `ans`.

---

## Code

```cpp
#include <vector>

class Solution {
public:
    std::vector<int> nextGreaterElements(const std::vector<int>& nums) {
        int n = nums.size();
        std::vector<int> ans(n, -1);
        
        for (int i = 0; i < n; ++i) {
            for (int j = 1; j < n; ++j) {
                int idx = (i + j) % n;
                if (nums[idx] > nums[i]) {
                    ans[i] = nums[idx];
                    break;
                }
            }
        }
        
        return ans;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - Nested circular loop takes $\mathcal{O}(N^2)$ time in worst case.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space excluding output vector.

---

## Why This Approach Is Not Optimal

Nested circular search takes $\mathcal{O}(N^2)$ time. By simulating a **Virtual Doubled Array ($2N$ iterations) with a Monotonic Stack**, we can compute Next Greater Elements in a circular array in linear $\mathcal{O}(N)$ time.
