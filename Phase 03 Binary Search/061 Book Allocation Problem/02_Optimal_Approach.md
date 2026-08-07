# Book Allocation Problem

## Pattern Used

- **Pattern**: **Binary Search on Answer Space (Minimax Allocation)**
- **Concept**: Search for the minimum possible "maximum page allocation" $P \in [\max(\text{arr}), \sum \text{arr}]$. The predicate function `canAllocate(P, m)` checks if books can be allocated to $\le m$ students without any student receiving $> P$ pages.

---

## Observation

1. Search Space Boundaries:
   - `low = max(arr)` (no student can receive fewer pages than the largest single book).
   - `high = sum(arr)` (when $m = 1$, one student reads all books).
2. Monotonicity:
   - If page limit $P$ allows allocating books to $\le m$ students, any larger limit $> P$ is ALSO valid.
   - If page limit $P$ requires $> m$ students, limit $P$ is too small.
3. Base Guard: If $m > n$ (more students than books), it is impossible for each student to get at least 1 book. Return `-1`.

---

## Intuition

Set `low = max(arr)` and `high = sum(arr)`. Test midpoint limit `mid`:
- Simulate allocation: add books to student's stack. When adding `arr[i]` exceeds `mid`, allocate to next student.
- Count required students `count`.
- If `count <= m`: `mid` limit is valid! Record `ans = mid` and contract `high = mid - 1`.
- If `count > m`: `mid` limit is too small. Increase limit `low = mid + 1`.

---

## Algorithm

1. If `m > arr.size()`, return `-1`.
2. `low = max(arr)`, `high = sum(arr)`, `ans = high`.
3. While `low <= high`:
   a. `mid = low + (high - low) / 2`.
   b. `students = 1`, `current_pages = 0`.
   c. For each `p` in `arr`:
      - If `current_pages + p > mid`:
        - `students++`.
        - `current_pages = p`.
      - Else: `current_pages += p`.
   d. If `students <= m`:
      - `ans = mid`.
      - `high = mid - 1`.
   e. Else:
      - `low = mid + 1`.
4. Return `ans`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <numeric>
#include <algorithm>

class Solution {
private:
    bool canAllocate(const std::vector<int>& arr, int m, int max_pages) {
        int students = 1;
        int current_pages = 0;
        
        for (int p : arr) {
            if (current_pages + p > max_pages) {
                students++;
                current_pages = p;
            } else {
                current_pages += p;
            }
        }
        
        return students <= m;
    }
public:
    int findPages(const std::vector<int>& arr, int m) {
        int n = arr.size();
        if (m > n) return -1;
        
        int low = *std::max_element(arr.begin(), arr.end());
        int high = std::accumulate(arr.begin(), arr.end(), 0);
        int ans = high;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (canAllocate(arr, m, mid)) {
                ans = mid;
                high = mid - 1; // Try to minimize maximum pages
            } else {
                low = mid + 1;  // Page limit too small, increase limit
            }
        }
        
        return ans;
    }
};
```

---

## Dry Run

### Input
- `arr = [12, 34, 67, 90]`, `m = 2`
- `low = 90`, `high = 203`

### Execution Trace

| Step | `low` | `high` | `mid` (Page Limit) | Allocation Groups | Students Needed | `students <= 2`? | `ans` | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `90` | `203` | `146` | `{12, 34, 67} (113)`, `{90} (90)` | 2 | `2 <= 2` (**Yes**) | `146` | `high = mid - 1 = 145` |
| 2 | `90` | `145` | `117` | `{12, 34, 67} (113)`, `{90} (90)` | 2 | `2 <= 2` (**Yes**) | `117` | `high = mid - 1 = 116` |
| 3 | `90` | `116` | `103` | `{12, 34} (46)`, `{67} (67)`, `{90} (90)` | 3 | `3 <= 2` (No) | `117` | `low = mid + 1 = 104` |
| 4 | `104` | `116` | `110` | `{12, 34} (46)`, `{67} (67)`, `{90} (90)` | 3 | `3 <= 2` (No) | `117` | `low = mid + 1 = 111` |
| 5 | `111` | `116` | `113` | `{12, 34, 67} (113)`, `{90} (90)` | 2 | `2 <= 2` (**Yes**) | **`113`** | `high = mid - 1 = 112` |
| End | `113` | `112` | - | - | - | - | `low > high` (Stop) | Return `113` |

### Result
- Output: `113`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log(\sum \text{arr}))$
  - Binary search over page range takes $\mathcal{O}(\log(\sum \text{arr}))$ steps; simulation takes $\mathcal{O}(N)$ per step.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This is Optimal

- Solves classic Book Allocation in optimal $\mathcal{O}(N \log(\sum \text{arr}))$ time.
- Uses zero extra memory.

---

## Common Mistakes

1. **Missing `m > n` Check**: Forgetting to check if students $m$ exceeds books $n$, which causes invalid allocations.
2. **Incorrect Initial Bounds**: Sizing `low = 0` instead of `max(arr)`.
