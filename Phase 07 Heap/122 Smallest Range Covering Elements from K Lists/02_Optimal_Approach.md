# Smallest Range Covering Elements from K Lists

## Pattern Used

- **Pattern**: **Min-Heap (K-Pointer Range Tracking)**
- **Concept**:
  - Insert the 0th element of each of the $k$ lists into a **Min-Heap** `minHeap` of elements `{val, list_index, element_index}`.
  - Track `max_val` among all elements currently inside `minHeap`.
  - The current range covering at least one element from every list is `[minHeap.top().val, max_val]`.
  - While `minHeap.size() == k`:
    - Extract `curr = minHeap.top(); minHeap.pop();`
    - Update best range if `max_val - curr.val < range_len`.
    - If `curr` has a next element in its list `nums[curr.list_idx][curr.elem_idx + 1]`:
      - Advance to next element: push `{next_val, curr.list_idx, curr.elem_idx + 1}` into `minHeap`.
      - Update `max_val = max(max_val, next_val)`.
    - Else: Break loop (we can no longer form a valid range containing elements from all $k$ lists!).

---

## Observation

1. At any moment, if `minHeap` contains 1 element from each of the $k$ lists, the minimum element `min_val = minHeap.top()` and maximum element `max_val` define a valid covering range `[min_val, max_val]`.
2. To shrink the range greedily, we MUST advance the pointer of the smallest element `min_val`. Advancing any other pointer can only increase `max_val` without increasing `min_val`, which would worsen the range!

---

## Intuition

Start with a window holding the first number of every list. The range is `[smallest_number, largest_number]`. To shrink the range length `largest - smallest`, advance the smallest number's pointer to its next larger element in its list.

---

## Algorithm

1. Struct `Node { int val; int listIdx; int elemIdx; }`.
2. Custom comparator for Min-Heap: `a.val > b.val`.
3. Push `nums[i][0]` for all $0 \le i < k$ into `minHeap`. Keep track of `maxVal = max(nums[i][0])`.
4. Init `minRange = INF`, `ans = [0, 0]`.
5. Loop while true:
   a. `curr = minHeap.top(); minHeap.pop();`
   b. `minVal = curr.val`.
   c. If `maxVal - minVal < minRange`:
      - `minRange = maxVal - minVal;`
      - `ans = {minVal, maxVal};`
   d. If `curr.elemIdx + 1 < nums[curr.listIdx].size()`:
      - `nextVal = nums[curr.listIdx][curr.elemIdx + 1]`.
      - Push `Node{nextVal, curr.listIdx, curr.elemIdx + 1}` into `minHeap`.
      - `maxVal = max(maxVal, nextVal)`.
   e. Else: Break (one list has been fully exhausted).
6. Return `ans`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <queue>
#include <algorithm>

struct Element {
    int val;
    int listIdx;
    int elemIdx;
};

struct Compare {
    bool operator()(const Element& a, const Element& b) {
        return a.val > b.val; // Min-heap on value
    }
};

class Solution {
public:
    std::vector<int> smallestRange(std::vector<std::vector<int>>& nums) {
        int k = nums.size();
        std::priority_queue<Element, std::vector<Element>, Compare> minHeap;
        
        int maxVal = -1e9;
        
        // Push the first element of each list into minHeap
        for (int i = 0; i < k; ++i) {
            minHeap.push({nums[i][0], i, 0});
            maxVal = std::max(maxVal, nums[i][0]);
        }
        
        int minRange = 2e9;
        std::vector<int> ans = {0, 0};
        
        while (true) {
            Element curr = minHeap.top();
            minHeap.pop();
            
            int minVal = curr.val;
            
            // Check if current range [minVal, maxVal] is smaller
            if (maxVal - minVal < minRange) {
                minRange = maxVal - minVal;
                ans = {minVal, maxVal};
            }
            
            // If next element exists in the same list, push it to heap
            if (curr.elemIdx + 1 < nums[curr.listIdx].size()) {
                int nextVal = nums[curr.listIdx][curr.elemIdx + 1];
                minHeap.push({nextVal, curr.listIdx, curr.elemIdx + 1});
                maxVal = std::max(maxVal, nextVal);
            } else {
                // One list exhausted, cannot cover all k lists anymore
                break;
            }
        }
        
        return ans;
    }
};
```

---

## Dry Run

### Input
- `nums = [[4, 10, 15], [0, 9, 12], [5, 18, 22]]`

### Execution Trace

1. Push `4 (L0)`, `0 (L1)`, `5 (L2)`. `maxVal = 5`. Heap: `[0(L1), 4(L0), 5(L2)]`.
2. Range: `[0, 5]` (len 5). Pop `0(L1)`. Push `9(L1)`. `maxVal = 9`. Heap: `[4(L0), 5(L2), 9(L1)]`.
3. Range: `[4, 9]` (len 5). Pop `4(L0)`. Push `10(L0)`. `maxVal = 10`. Heap: `[5(L2), 9(L1), 10(L0)]`.
4. Range: `[5, 10]` (len 5). Pop `5(L2)`. Push `18(L2)`. `maxVal = 18`. Heap: `[9(L1), 10(L0), 18(L2)]`.
5. Range: `[9, 18]` (len 9). Pop `9(L1)`. Push `12(L1)`. `maxVal = 18`. Heap: `[10(L0), 12(L1), 18(L2)]`.
6. Range: `[10, 18]` (len 8). Pop `10(L0)`. Push `15(L0)`. `maxVal = 18`. Heap: `[12(L1), 15(L0), 18(L2)]`.
...
7. Eventually arrives at range `[20, 24]` (len 4).

### Result
- Output: `[20, 24]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log k)$
  - Where $N$ is total elements across all lists and $k$ is number of lists.
  - Heap operations take $\mathcal{O}(\log k)$ time per element.
  - Total time: $\mathcal{O}(N \log k)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(k)$
  - Min-Heap stores exactly $k$ elements.

---

## Why This is Optimal

- Reduces space complexity from $\mathcal{O}(N)$ to $\mathcal{O}(k)$ compared to full flattening.
- Operates in $\mathcal{O}(N \log k)$ optimal time.

---

## Common Mistakes

1. **Not Tracking `maxVal` Continuously**: Forgetting to update `maxVal = max(maxVal, nextVal)` whenever pushing a new element into `minHeap`.
2. **Continuing After List Exhaustion**: Attempting to continue after one list is exhausted leads to invalid ranges that fail to cover elements from all $k$ lists.
