# Range Sum Query - Immutable

## Pattern Used

- **Pattern**: **1D Prefix Sum Array Pre-computation**
- **Concept**: Pre-compute a prefix sum array `pref` of size $N + 1$ where `pref[i]` represents the sum of elements `nums[0 ... i-1]`.
  $$\text{RangeSum}(L, R) = \text{pref}[R + 1] - \text{pref}[L]$$

---

## Observation

1. Let `pref[i] = nums[0] + nums[1] + ... + nums[i-1]`, with `pref[0] = 0`.
2. Sum of subarray from index `left` to `right` (inclusive):
   $$\sum_{i=\text{left}}^{\text{right}} \text{nums}[i] = \text{pref}[\text{right} + 1] - \text{pref}[\text{left}]$$
3. By pre-building `pref` of length $N + 1$ in the constructor:
   - Constructor time: $\mathcal{O}(N)$
   - `sumRange` query time: $\mathcal{O}(1)$

---

## Intuition

1. Build `pref` vector of size $N + 1$.
2. For $i = 0$ to $N - 1$: `pref[i + 1] = pref[i] + nums[i]`.
3. For any query `(left, right)`: return `pref[right + 1] - pref[left]`.

---

## Algorithm

### Constructor
1. `n = nums.size()`.
2. Allocate `pref` vector of size $n + 1$ initialized to `0`.
3. For `i` from `0` to `n - 1`:
   - `pref[i + 1] = pref[i] + nums[i]`.

### `sumRange(left, right)`
1. Return `pref[right + 1] - pref[left]`.

---

## Clean C++17 Solution

```cpp
#include <vector>

class NumArray {
private:
    std::vector<int> pref;
public:
    NumArray(const std::vector<int>& nums) {
        int n = nums.size();
        pref.resize(n + 1, 0);
        
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i] + nums[i];
        }
    }
    
    int sumRange(int left, int right) {
        return pref[right + 1] - pref[left];
    }
};
```

---

## Dry Run

### Input
- `nums = [-2, 0, 3, -5, 2, -1]`

### Constructor Pre-computation Trace
- `pref[0] = 0`
- `pref[1] = 0 + (-2) = -2`
- `pref[2] = -2 + 0 = -2`
- `pref[3] = -2 + 3 = 1`
- `pref[4] = 1 + (-5) = -4`
- `pref[5] = -4 + 2 = -2`
- `pref[6] = -2 + (-1) = -3`
- `pref = [0, -2, -2, 1, -4, -2, -3]`

### Query Traces
1. `sumRange(0, 2)`: `pref[3] - pref[0] = 1 - 0 = 1`. (Correct!)
2. `sumRange(2, 5)`: `pref[6] - pref[2] = -3 - (-2) = -1`. (Correct!)
3. `sumRange(0, 5)`: `pref[6] - pref[0] = -3 - 0 = -3`. (Correct!)

---

## Time Complexity

- **Constructor**: $\mathcal{O}(N)$
  - Single pass to populate `pref` array.
- **`sumRange`**: $\mathcal{O}(1)$
  - Single subtraction lookup per query.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Allocates prefix sum vector of size $N + 1$.

---

## Why This is Optimal

- Answers each of the $Q$ queries in $\mathcal{O}(1)$ time.
- Standard optimal range query technique for static (immutable) arrays.

---

## Common Mistakes

1. **Size $N$ vs Size $N + 1$ Prefix Array**: Building prefix array of size $N$ requires an `if (left == 0)` branch for every query. Allocating size $N + 1$ with `pref[0] = 0` eliminates branches.
