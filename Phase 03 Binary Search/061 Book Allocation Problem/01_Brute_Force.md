# Book Allocation Problem

- **Problem Number**: GFG Allocate Minimum Pages
- **Platform**: GeeksforGeeks
- **Difficulty**: Hard
- **Pattern**: Linear Search on Page Limits

---

## Brute Force Intuition

Test every possible maximum page limit $P$ starting from $\max(\text{arr})$ up to $\sum \text{arr}$. For each page limit $P$, simulate allocating books to students sequentially:
- Allocate contiguous books to current student until adding next book exceeds limit $P$.
- Move to next student.
- If total students needed $\le m$, return $P$.

---

## Algorithm

1. If `m > n`, return `-1`.
2. `low = max(arr)`, `high = sum(arr)`.
3. Loop page limit `pages` from `low` to `high`:
   a. `students = 1`, `current_pages = 0`.
   b. For each `p` in `arr`:
      - If `current_pages + p > pages`:
        - `students++`.
        - `current_pages = p`.
      - Else: `current_pages += p`.
   c. If `students <= m`, return `pages`.
4. Return `high`.

---

## Code

```cpp
#include <vector>
#include <numeric>
#include <algorithm>

class Solution {
public:
    int findPages(const std::vector<int>& arr, int m) {
        int n = arr.size();
        if (m > n) return -1;
        
        int low = *std::max_element(arr.begin(), arr.end());
        int high = std::accumulate(arr.begin(), arr.end(), 0);
        
        for (int pages = low; pages <= high; ++pages) {
            int students = 1;
            int current_pages = 0;
            
            for (int p : arr) {
                if (current_pages + p > pages) {
                    students++;
                    current_pages = p;
                } else {
                    current_pages += p;
                }
            }
            
            if (students <= m) {
                return pages;
            }
        }
        
        return high;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}((\sum \text{arr} - \max(\text{arr})) \times N)$
  - Testing each page limit takes $\mathcal{O}(N)$ simulation time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

Linear search takes $\mathcal{O}((\sum \text{arr} - \max(\text{arr})) \times N)$ time. Because the student allocation predicate `canAllocate(pages)` is **monotonic**, we can apply **Binary Search on Answer Space** in logarithmic $\mathcal{O}(N \log(\sum \text{arr}))$ time.
