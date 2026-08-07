# K Closest Points to Origin

## Pattern Used

- **Pattern**: **Max-Heap (Fixed-Size Bounded Priority Queue)**
- **Concept**:
  - Maintain a **Max-Heap** of size $k$ storing `{squared_distance, point}` pairs.
  - The top element of a max-heap is the **farthest** point among the current $k$ closest points.
  - When inserting a new point:
    - If heap size exceeds $k$, pop the top element (the farthest point among the current $k$).
  - At the end, the max-heap contains precisely the $k$ closest points to origin!

---

## Observation

1. Squared distance $x^2 + y^2$ preserves strict ordering of true Euclidean distance $\sqrt{x^2 + y^2}$ while eliminating floating-point rounding errors.
2. Holding a Max-Heap of size $k$ ensures that whenever we encounter a point closer than the farthest point in our top-$k$ set, the farthest point gets evicted (`maxHeap.pop()`).

---

## Intuition

Think of keeping a "Shortest Distance VIP List" of size $k$:
- We measure distance to origin for each point.
- We put points into a Max-Heap (where the farthest point sits at the top).
- If the heap has more than $k$ points, we kick out the farthest point at the top.
- The remaining $k$ points in the heap are the $k$ closest points!

---

## Algorithm

1. Define squared distance function `distSq(x, y) = x*x + y*y`.
2. Instantiate `std::priority_queue<pair<int, vector<int>>> maxHeap`.
3. For each point `p` in `points`:
   a. Compute `d = distSq(p[0], p[1])`.
   b. Push `{d, p}` into `maxHeap`.
   c. If `maxHeap.size() > k`, pop the top element.
4. Extract all points from `maxHeap` into `ans` vector.
5. Return `ans`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <queue>

class Solution {
public:
    std::vector<std::vector<int>> kClosest(std::vector<std::vector<int>>& points, int k) {
        // Max-heap storing pair<squared_distance, point>
        using Pair = std::pair<int, std::vector<int>>;
        std::priority_queue<Pair> maxHeap;
        
        for (const auto& p : points) {
            int dist = p[0] * p[0] + p[1] * p[1];
            maxHeap.push({dist, p});
            
            if (maxHeap.size() > k) {
                maxHeap.pop(); // Evict farthest point
            }
        }
        
        std::vector<std::vector<int>> ans;
        ans.reserve(k);
        
        while (!maxHeap.empty()) {
            ans.push_back(maxHeap.top().second);
            maxHeap.pop();
        }
        
        return ans;
    }
};
```

---

## Dry Run

### Input
- `points = [[1,3], [-2,2]]`, `k = 1`

### Execution Trace

1. Point `[1, 3]`: `dist = 1^2 + 3^2 = 10`. `maxHeap` = `[{10, [1,3]}]`. Size 1. OK.
2. Point `[-2, 2]`: `dist = (-2)^2 + 2^2 = 8`.
   - Push `{8, [-2,2]}` $\implies$ `maxHeap` = `[{10, [1,3]}, {8, [-2,2]}]`. Size 2.
   - Size > 1 $\implies$ `maxHeap.pop()` removes top `{10, [1,3]}`.
   - `maxHeap` becomes `[{8, [-2,2]}]`.
3. Extract result: `[[-2, 2]]`.

### Result
- Output: `[[-2, 2]]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log k)$
  - Processing $N$ points with a priority queue of size $k$ takes $\mathcal{O}(\log k)$ per push/pop.
  - Overall time complexity: $\mathcal{O}(N \log k)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(k)$
  - Priority queue stores at most $k + 1$ elements.

---

## Why This is Optimal

- Avoids $\mathcal{O}(N \log N)$ sorting time by capping priority queue size at $k$.
- Avoids square root floating-point operations by using squared integer distances.

---

## Common Mistakes

1. **Computing `sqrt()`**: Using `sqrt()` introduces potential floating point precision errors. Comparing squared distances $x^2 + y^2$ is exact and integer-safe.
2. **Min-Heap vs Max-Heap Confusion**: Using Min-Heap of size $N$ instead of Max-Heap of size $k$. Max-Heap of size $k$ is optimal for $k$ closest/smallest queries.
