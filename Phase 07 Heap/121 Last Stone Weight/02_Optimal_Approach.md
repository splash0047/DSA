# Last Stone Weight

## Pattern Used

- **Pattern**: **Max-Heap (Priority Queue)**
- **Concept**:
  - Insert all stone weights into a **Max-Heap** `maxHeap`.
  - While `maxHeap.size() > 1`:
    - Extract top stone `y = maxHeap.top(); maxHeap.pop();` (heaviest stone).
    - Extract top stone `x = maxHeap.top(); maxHeap.pop();` (second heaviest stone).
    - If `y > x`, push `y - x` back into `maxHeap`.
  - If `maxHeap` is empty, return `0`. Otherwise, return `maxHeap.top()`.

---

## Observation

1. Max-Heap allows extracting the maximum element in $\mathcal{O}(1)$ time and re-heapifying in $\mathcal{O}(\log N)$ time.
2. At most $N - 1$ smash operations take place before $\le 1$ stone remains.

---

## Intuition

Put all stones into a Max-Heap where the heaviest stone always floats to the top. At each step, pull out the two top stones, smash them, and if any leftover weight remains, drop it back into the heap.

---

## Algorithm

1. Initialize `priority_queue<int> maxHeap(stones.begin(), stones.end())`.
2. While `maxHeap.size() > 1`:
   a. `y = maxHeap.top(); maxHeap.pop();`
   b. `x = maxHeap.top(); maxHeap.pop();`
   c. If `y != x`: `maxHeap.push(y - x);`
3. Return `maxHeap.empty() ? 0 : maxHeap.top()`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <queue>

class Solution {
public:
    int lastStoneWeight(std::vector<int>& stones) {
        std::priority_queue<int> maxHeap(stones.begin(), stones.end());
        
        while (maxHeap.size() > 1) {
            int y = maxHeap.top();
            maxHeap.pop();
            int x = maxHeap.top();
            maxHeap.pop();
            
            if (y > x) {
                maxHeap.push(y - x);
            }
        }
        
        return maxHeap.empty() ? 0 : maxHeap.top();
    }
};
```

---

## Dry Run

### Input
- `stones = [2, 7, 4, 1, 8, 1]`

### Execution Trace

1. Init `maxHeap` = `[8, 7, 4, 2, 1, 1]`
2. Step 1: Pop `8` and `7`. `y = 8, x = 7`. `y - x = 1`. Push `1`.
   - `maxHeap` becomes `[4, 2, 1, 1, 1]`.
3. Step 2: Pop `4` and `2`. `y = 4, x = 2`. `y - x = 2`. Push `2`.
   - `maxHeap` becomes `[2, 1, 1, 1]`.
4. Step 3: Pop `2` and `1`. `y = 2, x = 1`. `y - x = 1`. Push `1`.
   - `maxHeap` becomes `[1, 1, 1]`.
5. Step 4: Pop `1` and `1`. `y = 1, x = 1`. `1 == 1` $\implies$ Both destroyed.
   - `maxHeap` becomes `[1]`.
6. Heap size 1 $\implies$ Loop ends. Return `maxHeap.top()` = `1`.

### Result
- Output: `1`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log N)$
  - Building max-heap takes $\mathcal{O}(N)$ time.
  - At most $N - 1$ smash steps, each performing logarithmic $\mathcal{O}(\log N)$ heap operations. Total time $= \mathcal{O}(N \log N)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Max-Heap stores up to $N$ elements.

---

## Why This is Optimal

- Reduces simulation step cost from $\mathcal{O}(N \log N)$ to $\mathcal{O}(\log N)$, yielding an optimal overall $\mathcal{O}(N \log N)$ solution.

---

## Common Mistakes

1. **Ordering of Pop Variables**: `x` is the second heaviest, `y` is the heaviest. `y >= x` must hold so `y - x >= 0`.
2. **Handling Empty Heap**: Returning `maxHeap.top()` directly without checking `maxHeap.empty()`.
