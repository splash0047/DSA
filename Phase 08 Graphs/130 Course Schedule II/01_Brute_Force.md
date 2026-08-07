# Course Schedule II

- **Problem Number**: 210
- **Platform**: LeetCode #210
- **Difficulty**: Medium
- **Pattern**: Permutations Permissibility Validation

---

## Brute Force Intuition

Generate all possible course ordering permutations ($N!$). For each ordering, check if it satisfies all prerequisite rules in `prerequisites`. Return the first valid ordering permutation found. If no valid ordering exists after checking all $N!$ permutations, return an empty vector `{}`.

---

## Algorithm

1. Create initial ordering `order = [0, 1, ..., numCourses - 1]`.
2. Map `pos[course]` to its index in `order`.
3. For each permutation of `order`:
   - Valid = true.
   - For each `[a, b]` in `prerequisites`:
     - If `pos[b] > pos[a]` (prerequisite `b` taken after `a`):
       - Valid = false; break.
   - If Valid: return `order`.
4. Return `{}`.

---

## Code

```cpp
#include <vector>
#include <numeric>
#include <algorithm>

class Solution {
public:
    std::vector<int> findOrder(int numCourses, std::vector<std::vector<int>>& prerequisites) {
        std::vector<int> order(numCourses);
        std::iota(order.begin(), order.end(), 0);
        
        do {
            std::vector<int> pos(numCourses);
            for (int i = 0; i < numCourses; ++i) {
                pos[order[i]] = i;
            }
            
            bool valid = true;
            for (const auto& req : prerequisites) {
                int a = req[0], b = req[1];
                if (pos[b] > pos[a]) {
                    valid = false;
                    break;
                }
            }
            
            if (valid) return order;
            
        } while (std::next_permutation(order.begin(), order.end()));
        
        return {};
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N! \times (N + E))$
  - Generating $N!$ permutations and testing $E$ constraints for each permutation takes factorial time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Vector storage for order and position map.

---

## Why This Approach Is Not Optimal

Testing all $N!$ ordering permutations is impossibly slow for $N = 2000$. Using **Kahn's Algorithm (BFS Topological Sort)**, we can construct the exact topological course order in linear $\mathcal{O}(V + E)$ time!
