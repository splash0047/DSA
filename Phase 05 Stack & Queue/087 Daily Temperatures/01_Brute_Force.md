# Daily Temperatures

- **Problem Number**: 739
- **Platform**: LeetCode #739
- **Difficulty**: Medium
- **Pattern**: Nested Loop Linear Search

---

## Brute Force Intuition

For each day `i`, scan all subsequent days `j` from `i + 1` to `n - 1`. The first day `j` where `temperatures[j] > temperatures[i]` is the next warmer day. The answer for index `i` is `j - i`. If no such day `j` exists, `answer[i] = 0`.

---

## Algorithm

1. Initialize `ans` of size `n` with `0`.
2. Loop `i` from `0` to `n - 1`:
   a. Loop `j` from `i + 1` to `n - 1`:
      - If `temperatures[j] > temperatures[i]`:
        - `ans[i] = j - i`.
        - Break inner loop.
3. Return `ans`.

---

## Code

```cpp
#include <vector>

class Solution {
public:
    std::vector<int> dailyTemperatures(const std::vector<int>& temperatures) {
        int n = temperatures.size();
        std::vector<int> ans(n, 0);
        
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (temperatures[j] > temperatures[i]) {
                    ans[i] = j - i;
                    break;
                }
            }
        }
        
        return ans;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - Nested loops take $\mathcal{O}(N^2)$ time in worst-case (e.g. monotonically decreasing temperatures like `[100, 90, 80, 70]`).

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space excluding output vector.

---

## Why This Approach Is Not Optimal

Nested linear search takes quadratic $\mathcal{O}(N^2)$ time. Using a **Monotonic Decreasing Stack**, we can find the Next Greater Element for all indices in a single pass in linear $\mathcal{O}(N)$ time.
