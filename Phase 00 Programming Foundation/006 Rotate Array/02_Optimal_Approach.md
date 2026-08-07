# Rotate Array

## Pattern Used

- **Pattern**: **Array Reversal Trick**
- **Concept**: Cyclic right shifts can be performed in-place using three sequence reversal steps.

---

## Observation

Consider rotating `[1, 2, 3, 4, 5, 6, 7]` right by $k = 3$:
- The last $k$ elements `[5, 6, 7]` should move to the front.
- The first $N-k$ elements `[1, 2, 3, 4]` should move to the back.

Notice what happens when we reverse the entire array:
- Entire reverse: `[7, 6, 5, 4, 3, 2, 1]`
- Now, the last $k$ elements are in the first $k$ positions, but in reversed order (`[7, 6, 5]`).
- Reversing the first $k$ elements (`[0 ... k-1]`): `[5, 6, 7, 4, 3, 2, 1]`.
- Reversing the remaining $N-k$ elements (`[k ... N-1]`): `[5, 6, 7, 1, 2, 3, 4]`.

This yields the exact rotated array in $\mathcal{O}(1)$ space!

---

## Intuition

Think of splitting the array into two sections:
- Section A: First $N - k$ elements.
- Section B: Last $k$ elements.

Initial state: `[A B]`  
Target state: `[B A]`  

Using reverse:
1. Reverse whole array $\rightarrow$ `[B^R A^R]`
2. Reverse first $k$ elements ($B^R$) $\rightarrow$ `[B A^R]`
3. Reverse remaining elements ($A^R$) $\rightarrow$ `[B A]`

---

## Algorithm

1. Normalize $k = k \pmod N$.
2. Reverse the entire vector `nums[0 ... N-1]`.
3. Reverse the first $k$ elements `nums[0 ... k-1]`.
4. Reverse the remaining elements `nums[k ... N-1]`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    void rotate(std::vector<int>& nums, int k) {
        int n = nums.size();
        if (n == 0) return;
        
        k %= n;
        
        // Step 1: Reverse the entire array
        std::reverse(nums.begin(), nums.end());
        
        // Step 2: Reverse the first k elements
        std::reverse(nums.begin(), nums.begin() + k);
        
        // Step 3: Reverse the remaining n - k elements
        std::reverse(nums.begin() + k, nums.end());
    }
};
```

---

## Dry Run

### Input
- `nums = [1, 2, 3, 4, 5, 6, 7]`
- `k = 3`

### Execution Trace

| Step | Operation | Array State (`nums`) |
| :--- | :--- | :--- |
| Start | Initial Array | `[1, 2, 3, 4, 5, 6, 7]` |
| 1 | `reverse(0, 6)` (All) | `[7, 6, 5, 4, 3, 2, 1]` |
| 2 | `reverse(0, 2)` (First 3) | `[5, 6, 7, 4, 3, 2, 1]` |
| 3 | `reverse(3, 6)` (Rest) | `[5, 6, 7, 1, 2, 3, 4]` |

### Result
- Output: `[5, 6, 7, 1, 2, 3, 4]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Reversing the entire array takes $N/2$ swaps.
  - Reversing the two sub-arrays takes $k/2 + (N-k)/2 = N/2$ swaps.
  - Total swaps: $N$, resulting in linear $\mathcal{O}(N)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - All reversals are performed strictly **in-place**.

---

## Why This is Optimal

- Every element must move to its target position, requiring $\Omega(N)$ time.
- Performing the transformation using $\mathcal{O}(1)$ space meets the theoretical minimum.

---

## Common Mistakes

1. **Forgetting `k = k % n`**: If $k > N$ (e.g. $k = 10$, $N = 3$), calling `nums.begin() + k` results in out-of-bounds memory access.
2. **Off-by-One in Iterators**: `std::reverse(begin, end)` takes an exclusive end iterator. `nums.begin() + k` correctly points to index `k`.
