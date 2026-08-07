# Kth Largest Element in an Array

## Pattern Used

- **Pattern**: **Min-Heap (Fixed-Size Priority Queue)** & **QuickSelect**
- **Primary Optimal Approach**: Min-Heap of size $k$ maintaining the top $k$ largest elements seen so far.
- **Alternative Optimal Approach**: QuickSelect (Linear time average selection algorithm based on QuickSort partitioning).

---

## Observation

1. If we maintain a **Min-Heap** of size $k$, the heap top element will always be the **smallest** among the top $k$ largest elements processed so far.
2. After processing all elements in the array:
   - The heap contains exactly the $k$ largest elements of the entire array.
   - The root (`min_heap.top()`) is the $k^{th}$ largest element!

---

## Intuition

Think of the min-heap as a "VIP leaderboard" with space for only $k$ contestants:
- Iterate through each number in `nums`.
- Push the number into the min-heap.
- If the heap size exceeds $k$, evict the smallest candidate (`min_heap.pop()`).
- At the end, the person sitting at the door of the VIP lounge (the min element in the heap) is the $k^{th}$ largest!

---

## Algorithm (Min-Heap Approach)

1. Declare a min-priority queue `std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap`.
2. For each number `num` in `nums`:
   a. Push `num` into `minHeap`.
   b. If `minHeap.size() > k`, pop the top element.
3. Return `minHeap.top()`.

---

## Clean C++17 Solution

### Approach 1: Min-Heap ($\mathcal{O}(N \log k)$ Time, $\mathcal{O}(k)$ Space)

```cpp
#include <vector>
#include <queue>

class Solution {
public:
    int findKthLargest(std::vector<int>& nums, int k) {
        std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
        
        for (int num : nums) {
            minHeap.push(num);
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }
        
        return minHeap.top();
    }
};
```

### Approach 2: QuickSelect ($\mathcal{O}(N)$ Average Time, $\mathcal{O}(1)$ Auxiliary Space)

```cpp
#include <vector>
#include <algorithm>
#include <cstdlib>

class Solution {
private:
    int partition(std::vector<int>& nums, int left, int right) {
        int pivotIndex = left + rand() % (right - left + 1);
        int pivotValue = nums[pivotIndex];
        std::swap(nums[pivotIndex], nums[right]);
        int storeIndex = left;
        
        for (int i = left; i < right; ++i) {
            if (nums[i] > pivotValue) { // Descending order for Kth largest
                std::swap(nums[i], nums[storeIndex]);
                storeIndex++;
            }
        }
        std::swap(nums[storeIndex], nums[right]);
        return storeIndex;
    }

public:
    int findKthLargest(std::vector<int>& nums, int k) {
        int left = 0, right = nums.size() - 1;
        int targetIndex = k - 1; // 0-indexed position in descending sorted order
        
        while (left <= right) {
            int pivotIndex = partition(nums, left, right);
            if (pivotIndex == targetIndex) {
                return nums[pivotIndex];
            } else if (pivotIndex < targetIndex) {
                left = pivotIndex + 1;
            } else {
                right = pivotIndex - 1;
            }
        }
        return -1;
    }
};
```

---

## Dry Run

### Input
- `nums = [3, 2, 1, 5, 6, 4]`, `k = 2`

### Execution Trace (Min-Heap)

| Step | Element | Heap Contents (after push) | Heap Size | Action Taken |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 3 | `[3]` | 1 | Kept |
| 2 | 2 | `[2, 3]` | 2 | Kept |
| 3 | 1 | `[1, 3, 2]` | 3 (> 2) | Pop `1` $\implies$ Heap becomes `[2, 3]` |
| 4 | 5 | `[2, 3, 5]` | 3 (> 2) | Pop `2` $\implies$ Heap becomes `[3, 5]` |
| 5 | 6 | `[3, 5, 6]` | 3 (> 2) | Pop `3` $\implies$ Heap becomes `[5, 6]` |
| 6 | 4 | `[4, 6, 5]` | 3 (> 2) | Pop `4` $\implies$ Heap becomes `[5, 6]` |

- `minHeap.top()` returns `5`.

### Result
- Output: `5`

---

## Time Complexity

- **Min-Heap Approach**: $\mathcal{O}(N \log k)$
  - We process $N$ elements. Each push/pop operation on a min-heap of size $k$ takes $\mathcal{O}(\log k)$ time.
- **QuickSelect Approach**: $\mathcal{O}(N)$ Average, $\mathcal{O}(N^2)$ Worst Case.
  - Average time complexity is linear $\mathcal{O}(N + N/2 + N/4 + \dots) = \mathcal{O}(N)$.

---

## Space Complexity

- **Min-Heap Approach**: $\mathcal{O}(k)$
  - Stores at most $k + 1$ elements in the priority queue.
- **QuickSelect Approach**: $\mathcal{O}(1)$ auxiliary space if done iteratively.

---

## Why This is Optimal

- Min-Heap reduces complexity from $\mathcal{O}(N \log N)$ to $\mathcal{O}(N \log k)$, which is significantly faster when $k \ll N$.
- QuickSelect achieves average $\mathcal{O}(N)$ time, meeting the theoretical lower bound for selection.

---

## Common Mistakes

1. **Confusing Min-Heap vs Max-Heap**: Using Max-Heap of size $N$ requires building a full heap ($\mathcal{O}(N)$) and popping $k-1$ times ($\mathcal{O}(k \log N)$). Min-Heap of size $k$ is much more space efficient.
2. **Off-by-One in QuickSelect**: Forgetting to convert $k$ to 0-based index `k - 1`.
