# Kth Smallest Element in an Array

## Pattern Used

- **Pattern**: **Max-Heap (Fixed-Size Priority Queue)**
- **Concept**: Maintain a **Max-Heap** of size $k$ containing the $k$ smallest elements seen so far.
  - The top element of a max-heap is always the **largest** among its elements.
  - When maintaining $k$ smallest elements, the max-heap root `maxHeap.top()` represents the $k^{th}$ smallest element overall!

---

## Observation

1. If we hold a Max-Heap of size $k$, the top element is the **largest** of the $k$ smallest values encountered so far.
2. When a new element is smaller than `maxHeap.top()`, we pop the current max and insert the new element.
3. At the end of the array traversal, the root of the max-heap is guaranteed to be the $k^{th}$ smallest element.

---

## Intuition

To keep track of the $k$ smallest numbers:
- Keep a "room" (Max-Heap) with space for at most $k$ smallest items.
- Whenever a new number comes in, push it into the heap.
- If the room exceeds capacity $k$, kick out the largest item in the room (`maxHeap.pop()`).
- After visiting all numbers, the largest item left in the room is the $k^{th}$ smallest overall.

---

## Algorithm

1. Declare a Max-Heap `std::priority_queue<int> maxHeap`.
2. Iterate through each number `num` in `arr`:
   a. Push `num` into `maxHeap`.
   b. If `maxHeap.size() > k`, pop the top element.
3. Return `maxHeap.top()`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <queue>

class Solution {
public:
    int kthSmallest(std::vector<int>& arr, int k) {
        std::priority_queue<int> maxHeap;
        
        for (int num : arr) {
            maxHeap.push(num);
            if (maxHeap.size() > k) {
                maxHeap.pop();
            }
        }
        
        return maxHeap.top();
    }
};
```

---

## Dry Run

### Input
- `arr = [7, 10, 4, 3, 20, 15]`, `k = 3`

### Execution Trace

| Step | Element | Heap Contents (after push) | Heap Size | Action Taken |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 7 | `[7]` | 1 | Kept |
| 2 | 10 | `[10, 7]` | 2 | Kept |
| 3 | 4 | `[10, 7, 4]` | 3 | Kept |
| 4 | 3 | `[10, 7, 4, 3]` | 4 (> 3) | Pop `10` $\implies$ Heap becomes `[7, 4, 3]` |
| 5 | 20 | `[20, 7, 4, 3]` | 4 (> 3) | Pop `20` $\implies$ Heap becomes `[7, 4, 3]` |
| 6 | 15 | `[15, 7, 4, 3]` | 4 (> 3) | Pop `15` $\implies$ Heap becomes `[7, 4, 3]` |

- `maxHeap.top()` returns `7`.

### Result
- Output: `7` (3rd smallest element)

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log k)$
  - Processing $N$ elements with a priority queue of size $k$ takes $\mathcal{O}(\log k)$ time per insertion/deletion.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(k)$
  - Priority queue stores at most $k + 1$ elements.

---

## Why This is Optimal

- Reduces time from $\mathcal{O}(N \log N)$ to $\mathcal{O}(N \log k)$.
- Uses $\mathcal{O}(k)$ auxiliary space instead of $\mathcal{O}(N)$ for full array copies.

---

## Common Mistakes

1. **Using Min-Heap instead of Max-Heap**: For $k^{th}$ SMALLEST, we need a **MAX-heap** of size $k$ so the largest element gets popped out, preserving the $k$ smallest.
2. **Pushing After Size Check**: Pushing into heap first, then checking `size > k` and popping ensures correct bounded heap behavior.
