# Rotate Array

- **Problem Number**: 189
- **Platform**: LeetCode #189
- **Difficulty**: Medium
- **Pattern**: Auxiliary Array Allocation / Index Mapping

---

## Brute Force Intuition

When rotating an array right by $k$ steps, each element at index `i` moves to index `(i + k) % n`. 

The simplest approach is to allocate a temporary auxiliary vector of size $N$, copy each element `nums[i]` into its new position `temp[(i + k) % n]`, and then copy `temp` back into `nums`.

---

## Algorithm

1. Let $N$ be the length of `nums`.
2. Normalize $k = k \pmod N$.
3. Create a vector `temp` of size $N$.
4. For each index `i` from `0` to $N - 1$:
   - Set `temp[(i + k) % N] = nums[i]`.
5. Copy `temp` back into `nums`.

---

## Code

```cpp
#include <vector>

class Solution {
public:
    void rotate(std::vector<int>& nums, int k) {
        int n = nums.size();
        if (n == 0) return;
        
        k %= n;
        std::vector<int> temp(n);
        
        for (int i = 0; i < n; ++i) {
            temp[(i + k) % n] = nums[i];
        }
        
        nums = temp;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Copying elements to `temp` and back to `nums` takes $2 \times N$ operations.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Allocates an extra vector of size $N$.

---

## Why This Approach Is Not Optimal

This approach allocates $\mathcal{O}(N)$ auxiliary memory. The follow-up challenge explicitly asks for an **in-place solution** using $\mathcal{O}(1)$ extra space. We can achieve this using the **Array Reversal Algorithm**.
