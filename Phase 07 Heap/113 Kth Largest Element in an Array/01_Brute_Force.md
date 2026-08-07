# Kth Largest Element in an Array

- **Problem Number**: 215
- **Platform**: LeetCode #215
- **Difficulty**: Medium
- **Pattern**: Full Array Sorting

---

## Brute Force Intuition

The most straightforward way to find the $k^{th}$ largest element in an array is to sort the array in non-decreasing order. Once sorted, the largest element is at index `n - 1`, the $2^{nd}$ largest is at index `n - 2`, and in general, the $k^{th}$ largest element is at index `n - k`.

Alternatively, sorting in descending order places the $k^{th}$ largest element at index `k - 1`.

---

## Algorithm

1. Sort the given `nums` array in non-decreasing order using `std::sort`.
2. Compute index `n - k`, where `n = nums.size()`.
3. Return `nums[n - k]`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int findKthLargest(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        return nums[nums.size() - k];
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log N)$
  - `std::sort` in C++ utilizes IntroSort (a hybrid of QuickSort, HeapSort, and InsertionSort), which takes $\mathcal{O}(N \log N)$ time for an array of size $N$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(\log N)$ to $\mathcal{O}(N)$
  - Call stack space used by `std::sort` for recursion depth.

---

## Why This Approach Is Not Optimal

Full sorting does unnecessary work by ordering all $N$ elements, even though we only care about the single element at rank $k$. Using a **Min-Heap (Priority Queue)** of size $k$ or **QuickSelect (Hoare's Selection Algorithm)**, we can find the $k^{th}$ largest element in $\mathcal{O}(N \log k)$ or average $\mathcal{O}(N)$ time.
