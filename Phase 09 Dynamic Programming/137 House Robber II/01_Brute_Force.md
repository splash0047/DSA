# House Robber II

- **Platform**: LeetCode #213
- **Difficulty**: Medium
- **Pattern**: Circular Array Case Decomposition + Linear DP Array Copies

---

## Brute Force Intuition

Because the houses are arranged in a **circle**, house `0` and house `n-1` are adjacent! Therefore:
- If we rob house `0`, we CANNOT rob house `n-1`. The problem reduces to standard House Robber I on subarray `nums[0 ... n-2]`.
- If we do NOT rob house `0`, we can consider house `n-1`. The problem reduces to standard House Robber I on subarray `nums[1 ... n-1]`.

The brute force intuition creates two separate subarray vectors (`subarray1` omitting last element, `subarray2` omitting first element) and runs standard House Robber I DP on both, returning `max(rob1, rob2)`.

---

## Algorithm

1. If `n == 1`, return `nums[0]`.
2. Construct `sub1 = nums[0 ... n-2]`.
3. Construct `sub2 = nums[1 ... n-1]`.
4. Return `max(robLinear(sub1), robLinear(sub2))`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
private:
    int robLinear(const std::vector<int>& nums) {
        int prev2 = 0, prev1 = 0;
        for (int num : nums) {
            int curr = std::max(num + prev2, prev1);
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    }

public:
    int rob(std::vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return nums[0];
        
        std::vector<int> sub1(nums.begin(), nums.end() - 1);
        std::vector<int> sub2(nums.begin() + 1, nums.end());
        
        return std::max(robLinear(sub1), robLinear(sub2));
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Vector slicing takes $\mathcal{O}(N)$ time. Linear DP runs twice in $\mathcal{O}(N)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Creates two auxiliary subarray vectors of size $N - 1$.

---

## Why This Approach Is Not Optimal

Creating explicit subarray vectors consumes extra $\mathcal{O}(N)$ auxiliary memory. Using **Index Range Parameterization**, we can run standard linear DP directly on pointer bounds `[start, end]` without allocating any subarray vectors, achieving $\mathcal{O}(1)$ auxiliary space!
