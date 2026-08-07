# Find Median from Data Stream

## Pattern Used

- **Pattern**: **Two Heaps (Max-Heap + Min-Heap Balancing)**
- **Concept**:
  - Split the dataset into two halves:
    - **Left Half (Smaller numbers)**: Managed by a **Max-Heap** `maxHeap` (stores smaller half, top is max of small half).
    - **Right Half (Larger numbers)**: Managed by a **Min-Heap** `minHeap` (stores larger half, top is min of large half).
  - Maintain invariant: `maxHeap.size() == minHeap.size()` OR `maxHeap.size() == minHeap.size() + 1`.

---

## Observation

1. In a sorted list, the median is determined by the boundary between the smaller half and larger half.
2. `maxHeap.top()` gives the largest element in the smaller half.
3. `minHeap.top()` gives the smallest element in the larger half.
4. If sizes are equal $\implies$ Median $= (\text{maxHeap.top()} + \text{minHeap.top()}) / 2.0$.
5. If `maxHeap` has 1 more element $\implies$ Median $= \text{maxHeap.top()}$.

---

## Intuition

Imagine dividing the data stream into two equal-sized piles:
- Left pile (`maxHeap`): holds the smaller half of numbers. The largest number in this pile sits at the top.
- Right pile (`minHeap`): holds the larger half of numbers. The smallest number in this pile sits at the top.

When adding a number:
1. Always push into `maxHeap` first.
2. Balance values: If `maxHeap.top() > minHeap.top()`, move `maxHeap.top()` to `minHeap`.
3. Balance sizes: If `maxHeap.size() > minHeap.size() + 1`, pop from `maxHeap` and push to `minHeap`. If `minHeap.size() > maxHeap.size()`, pop from `minHeap` and push to `maxHeap`.

---

## Algorithm

### `addNum(num)`
1. Push `num` into `maxHeap`.
2. If `!minHeap.empty() && maxHeap.top() > minHeap.top()`:
   - Pop top from `maxHeap` and push into `minHeap`.
3. Rebalance sizes:
   - If `maxHeap.size() > minHeap.size() + 1`:
     - Pop top from `maxHeap` and push into `minHeap`.
   - If `minHeap.size() > maxHeap.size()`:
     - Pop top from `minHeap` and push into `maxHeap`.

### `findMedian()`
1. If `maxHeap.size() > minHeap.size()`, return `maxHeap.top()`.
2. Else return `(maxHeap.top() + minHeap.top()) / 2.0`.

---

## Clean C++17 Solution

```cpp
#include <queue>
#include <vector>

class MedianFinder {
private:
    std::priority_queue<int> maxHeap; // Lower half
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap; // Upper half

public:
    MedianFinder() {}
    
    void addNum(int num) {
        // Step 1: Push to maxHeap
        maxHeap.push(num);
        
        // Step 2: Ensure maxHeap elements <= minHeap elements
        if (!maxHeap.empty() && !minHeap.empty() && maxHeap.top() > minHeap.top()) {
            int val = maxHeap.top();
            maxHeap.pop();
            minHeap.push(val);
        }
        
        // Step 3: Maintain size invariant: maxHeap size == minHeap size OR minHeap size + 1
        if (maxHeap.size() > minHeap.size() + 1) {
            int val = maxHeap.top();
            maxHeap.pop();
            minHeap.push(val);
        } else if (minHeap.size() > maxHeap.size()) {
            int val = minHeap.top();
            minHeap.pop();
            maxHeap.push(val);
        }
    }
    
    double findMedian() {
        if (maxHeap.size() > minHeap.size()) {
            return maxHeap.top();
        }
        return (maxHeap.top() + minHeap.top()) / 2.0;
    }
};
```

---

## Dry Run

### Operations
`addNum(1)`, `addNum(2)`, `findMedian()`, `addNum(3)`, `findMedian()`

### Execution Trace

1. `addNum(1)`:
   - `maxHeap` = `[1]`, `minHeap` = `[]`. `maxHeap` size 1, `minHeap` size 0. OK.
2. `addNum(2)`:
   - Push `2` to `maxHeap` $\implies$ `maxHeap = [2, 1]`.
   - Rebalance value: `maxHeap.top() (2) > minHeap.top() (none)`.
   - Rebalance size: `maxHeap` size 2 > 1 $\implies$ Move `2` to `minHeap`.
   - `maxHeap` = `[1]`, `minHeap` = `[2]`.
3. `findMedian()`:
   - Sizes equal (1, 1) $\implies$ `(1 + 2) / 2.0 = 1.5`.
4. `addNum(3)`:
   - Push `3` to `maxHeap` $\implies$ `maxHeap = [3, 1]`.
   - Value balance: `maxHeap.top() (3) > minHeap.top() (2)` $\implies$ move `3` to `minHeap` $\implies$ `maxHeap = [1]`, `minHeap = [2, 3]`.
   - Size balance: `minHeap` size 2 > `maxHeap` size 1 $\implies$ move `2` to `maxHeap` $\implies$ `maxHeap = [2, 1]`, `minHeap = [3]`.
5. `findMedian()`:
   - `maxHeap` size 2 > `minHeap` size 1 $\implies$ Returns `maxHeap.top()` = `2.0`.

---

## Time Complexity

- **`addNum(num)`**: $\mathcal{O}(\log N)$
  - Priority queue push and pop operations take logarithmic $\mathcal{O}(\log N)$ time.
- **`findMedian()`**: $\mathcal{O}(1)$
  - Returns `top()` element in $\mathcal{O}(1)$ constant time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Storing all $N$ elements across two heaps.

---

## Why This is Optimal

- Reduces stream insertion time from linear $\mathcal{O}(N)$ to logarithmic $\mathcal{O}(\log N)$.
- Provides median queries in instantaneous constant $\mathcal{O}(1)$ time.

---

## Common Mistakes

1. **Integer Division Bug**: Writing `(maxHeap.top() + minHeap.top()) / 2` instead of `/ 2.0` (truncates decimal places).
2. **Size Imbalance**: Allowing size difference between heaps to exceed 1.
