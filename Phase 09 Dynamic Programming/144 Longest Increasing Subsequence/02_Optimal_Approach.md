# Longest Increasing Subsequence

## Pattern Used

- **Pattern**: **Patience Sorting / Binary Search (`std::lower_bound`)**
- **Concept**:
  - Maintain a dynamic vector `tails` where `tails[i]` stores the **smallest tail element** of all increasing subsequences of length `i + 1` found so far.
  - For each number `num` in `nums`:
    - Use binary search (`std::lower_bound`) to find the first element in `tails` that is $\ge \text{num}$.
    - If no such element exists (all elements in `tails` are $< \text{num}$), `num` extends the longest subsequence $\implies$ append `tails.push_back(num)`.
    - Else if an element $\ge \text{num}$ is found at index `it`, replace `*it = num` (greedily lower the tail value for subsequences of that length).
  - Return `tails.size()`.

---

## Observation

1. To maximize the likelihood of extending an increasing subsequence in the future, we should always prefer a **smaller tail element**.
2. Vector `tails` is strictly increasing at all times, making binary search (`std::lower_bound`) applicable for $\mathcal{O}(\log N)$ insertion.

---

## Intuition

Think of card solitaire (Patience Sorting):
- When a number comes in, try to place it on top of the first existing pile whose top card is $\ge \text{num}$.
- If `num` is larger than the top card of all piles, create a new pile at the end.
- The total number of piles created equals the length of the Longest Increasing Subsequence!

---

## Algorithm

1. `vector<int> tails`.
2. For each `num` in `nums`:
   - `auto it = lower_bound(tails.begin(), tails.end(), num)`.
   - If `it == tails.end()`:
     - `tails.push_back(num)`.
   - Else:
     - `*it = num`.
3. Return `tails.size()`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int lengthOfLIS(std::vector<int>& nums) {
        if (nums.empty()) return 0;
        
        std::vector<int> tails;
        tails.reserve(nums.size());
        
        for (int num : nums) {
            // Find first element in tails >= num using Binary Search
            auto it = std::lower_bound(tails.begin(), tails.end(), num);
            
            if (it == tails.end()) {
                tails.push_back(num); // Extend LIS
            } else {
                *it = num; // Replace with smaller tail element
            }
        }
        
        return tails.size();
    }
};
```

---

## Dry Run

### Input
- `nums = [10, 9, 2, 5, 3, 7, 101, 18]`

### Execution Trace

- `num = 10`: `tails = [10]`
- `num = 9`: replace 10 $\implies$ `tails = [9]`
- `num = 2`: replace 9 $\implies$ `tails = [2]`
- `num = 5`: append $\implies$ `tails = [2, 5]`
- `num = 3`: replace 5 $\implies$ `tails = [2, 3]`
- `num = 7`: append $\implies$ `tails = [2, 3, 7]`
- `num = 101`: append $\implies$ `tails = [2, 3, 7, 101]`
- `num = 18`: replace 101 $\implies$ `tails = [2, 3, 7, 18]`

### Result
- `tails.size()` returns `4`.

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log N)$
  - Processing $N$ numbers with binary search (`std::lower_bound`) taking $\mathcal{O}(\log N)$ per element.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - `tails` vector stores at most $N$ elements.

---

## Why This is Optimal

- Reduces time complexity from quadratic $\mathcal{O}(N^2)$ to optimal $\mathcal{O}(N \log N)$ using patience sorting binary search.

---

## Common Mistakes

1. **Confusing `std::lower_bound` with `std::upper_bound`**: For STRICLY increasing subsequence, use `lower_bound` ($\ge$). For non-decreasing subsequence, use `upper_bound` ($>$).
2. **Assuming `tails` Contains the Actual LIS Sequence**: `tails` array stores smallest tail elements for each length, not the actual elements of the LIS sequence!
