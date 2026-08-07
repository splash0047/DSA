# Product of Array Except Self

## Pattern Used

- **Pattern**: **Prefix & Suffix Accumulated Products**
- **Concept**: The product of all elements except `nums[i]` is equal to:
$$\text{answer}[i] = (\text{Prefix Product of elements to left of } i) \times (\text{Suffix Product of elements to right of } i)$$

---

## Observation

1. In a first forward pass from `0` to `n - 1`, compute the prefix products and store them directly inside `answer`:
   - `answer[i]` stores the product of all elements from `0` to `i - 1`.
   - `answer[0] = 1`.
2. In a second backward pass from `n - 1` down to `0`, maintain a running variable `suffix_prod`:
   - Multiply `answer[i]` by `suffix_prod`.
   - Update `suffix_prod *= nums[i]`.
3. This satisfies both constraints: **No Division Used** and **$\mathcal{O}(1)$ Auxiliary Space**!

---

## Intuition

- Pass 1 (Left-to-Right): Populate `answer[i]` with product of all elements to the left of `i`.
- Pass 2 (Right-to-Left): Accumulate running `suffix_prod` from the right and multiply into `answer[i]`.

---

## Algorithm

1. Allocate `answer` vector of size $N$.
2. `answer[0] = 1`.
3. Pass 1: Loop `i` from `1` to `n - 1`:
   - `answer[i] = answer[i - 1] * nums[i - 1]`.
4. `suffix_prod = 1`.
5. Pass 2: Loop `i` from `n - 1` down to `0`:
   - `answer[i] *= suffix_prod`.
   - `suffix_prod *= nums[i]`.
6. Return `answer`.

---

## Clean C++17 Solution

```cpp
#include <vector>

class Solution {
public:
    std::vector<int> productExceptSelf(const std::vector<int>& nums) {
        int n = nums.size();
        std::vector<int> answer(n, 1);
        
        // Pass 1: Accumulate Prefix Products (Left to Right)
        for (int i = 1; i < n; ++i) {
            answer[i] = answer[i - 1] * nums[i - 1];
        }
        
        // Pass 2: Accumulate Suffix Products (Right to Left)
        int suffix_prod = 1;
        for (int i = n - 1; i >= 0; --i) {
            answer[i] *= suffix_prod;
            suffix_prod *= nums[i];
        }
        
        return answer;
    }
};
```

---

## Dry Run

### Input
- `nums = [1, 2, 3, 4]`

### Execution Trace

#### Pass 1: Prefix Products
- `answer[0] = 1`
- `answer[1] = answer[0] * nums[0] = 1 * 1 = 1`
- `answer[2] = answer[1] * nums[1] = 1 * 2 = 2`
- `answer[3] = answer[2] * nums[2] = 2 * 3 = 6`
- State after Pass 1: `answer = [1, 1, 2, 6]`

#### Pass 2: Suffix Products Multiplication
- `i = 3`: `answer[3] *= 1` $\rightarrow$ `6`. `suffix_prod = 1 * 4 = 4`.
- `i = 2`: `answer[2] *= 4` $\rightarrow$ `8`. `suffix_prod = 4 * 3 = 12`.
- `i = 1`: `answer[1] *= 12` $\rightarrow$ `12`. `suffix_prod = 12 * 2 = 24`.
- `i = 0`: `answer[0] *= 24` $\rightarrow$ `24`. `suffix_prod = 24 * 1 = 24`.

### Result
- Output: `[24, 12, 8, 6]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Two linear passes through array of length $N$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses only 1 integer variable `suffix_prod` (output array `answer` is excluded from space complexity).

---

## Why This is Optimal

- Solves without division operator in $\mathcal{O}(N)$ time.
- Achieves $\mathcal{O}(1)$ auxiliary space.

---

## Common Mistakes

1. **Using Division Operator**: Using total product division (`total_prod / nums[i]`) breaks down when array contains `0`s (division by zero error!).
2. **Allocating Separate Prefix and Suffix Arrays**: Allocating two auxiliary vectors `prefix` and `suffix` of size $N$ takes $\mathcal{O}(N)$ extra space instead of optimal $\mathcal{O}(1)$ space.
