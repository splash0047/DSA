# K Closest Points to Origin

- **Problem Number**: 973
- **Platform**: LeetCode #973
- **Difficulty**: Medium
- **Pattern**: Full Array Sorting with Custom Comparator

---

## Brute Force Intuition

1. The Euclidean distance from point $(x, y)$ to $(0,0)$ is $\sqrt{x^2 + y^2}$.
2. To avoid floating point imprecision, compare squared distances: $dist^2 = x^2 + y^2$.
3. Sort all points in ascending order of their squared distances.
4. Return the first $k$ points from the sorted array.

---

## Algorithm

1. Define distance squared helper `distSq(p) = p[0]*p[0] + p[1]*p[1]`.
2. Sort `points` vector using `std::sort` with custom comparator: `distSq(a) < distSq(b)`.
3. Resize or copy the first $k$ points into `ans`.
4. Return `ans`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
private:
    int distSq(const std::vector<int>& p) {
        return p[0] * p[0] + p[1] * p[1];
    }

public:
    std::vector<std::vector<int>> kClosest(std::vector<std::vector<int>>& points, int k) {
        std::sort(points.begin(), points.end(), [&](const std::vector<int>& a, const std::vector<int>& b) {
            return distSq(a) < distSq(b);
        });
        
        return std::vector<std::vector<int>>(points.begin(), points.begin() + k);
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log N)$
  - Sorting $N$ points takes $\mathcal{O}(N \log N)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(\log N)$
  - Call stack memory used by IntroSort.

---

## Why This Approach Is Not Optimal

Full sorting orders all $N$ points when we only require the $k$ points closest to origin. Using a **Max-Heap of size $k$**, we can find the $k$ closest points in $\mathcal{O}(N \log k)$ time and $\mathcal{O}(k)$ space.
