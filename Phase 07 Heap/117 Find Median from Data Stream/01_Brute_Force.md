# Find Median from Data Stream

- **Problem Number**: 295
- **Platform**: LeetCode #295
- **Difficulty**: Hard
- **Pattern**: Insertion Sort / Dynamic Vector Sorting

---

## Brute Force Intuition

Keep a `std::vector<int> nums` to store all numbers received so far.
- `addNum(num)`: Append `num` to `nums` and sort the entire vector using `std::sort`. Alternatively, use `std::lower_bound` to insert `num` into its sorted position (insertion sort style).
- `findMedian()`:
  - If size $N$ is odd, return `nums[N / 2]`.
  - If size $N$ is even, return `(nums[N / 2 - 1] + nums[N / 2]) / 2.0`.

---

## Algorithm

1. Class member `vector<int> nums`.
2. `addNum(num)`:
   - Insert `num` into `nums` using `std::lower_bound` to keep `nums` sorted in $\mathcal{O}(N)$ time per insertion.
3. `findMedian()`:
   - `n = nums.size()`.
   - If `n % 2 == 1`, return `nums[n / 2]`.
   - Else return `(nums[n / 2 - 1] + nums[n / 2]) / 2.0`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class MedianFinder {
private:
    std::vector<int> nums;

public:
    MedianFinder() {}
    
    void addNum(int num) {
        auto it = std::lower_bound(nums.begin(), nums.end(), num);
        nums.insert(it, num);
    }
    
    double findMedian() {
        int n = nums.size();
        if (n % 2 == 1) {
            return nums[n / 2];
        } else {
            return (nums[n / 2 - 1] + nums[n / 2]) / 2.0;
        }
    }
};
```

---

## Time Complexity

- **`addNum(num)`**: $\mathcal{O}(N)$
  - Binary search using `std::lower_bound` takes $\mathcal{O}(\log N)$, but array element shifting during `vector::insert` takes $\mathcal{O}(N)$ time.
- **`findMedian()`**: $\mathcal{O}(1)$
  - Direct index lookup.
- **Total Time for $M$ operations**: $\mathcal{O}(M \times N)$ or $\mathcal{O}(M^2)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Stores all $N$ elements in dynamic vector.

---

## Why This Approach Is Not Optimal

Shifting elements on every insertion requires linear $\mathcal{O}(N)$ time. With up to $50,000$ calls, $O(N^2)$ overall time causes **Time Limit Exceeded (TLE)**. Using **Two Heaps (Max-Heap + Min-Heap)**, we reduce `addNum` time to logarithmic $\mathcal{O}(\log N)$!
